import json
import numpy as np
from functools import lru_cache

import flask
from flask import request, jsonify, Blueprint, current_app, g
from utils import better_json_encoder

from database_json import get_db

api = Blueprint('api', __name__)

# Flask 2.3+ compatibility - use json.JSONEncoder instead of flask.json.JSONEncoder
try:
    api.json_encoder = better_json_encoder(flask.json.JSONEncoder)
except AttributeError:
    # For newer Flask versions, the encoder is set differently
    pass

######################
# API-LEVEL CACHE FOR RESPONSE OPTIMIZATION
######################
# Cache frequently accessed responses to avoid re-computation

_response_cache = {}
_cache_max_size = 500

def get_cached_response(key):
    """Get cached response if available."""
    return _response_cache.get(key)

def set_cached_response(key, value):
    """Cache a response. Implements simple LRU by clearing oldest if full."""
    if len(_response_cache) >= _cache_max_size:
        # Clear half the cache when full
        keys_to_remove = list(_response_cache.keys())[:_cache_max_size // 2]
        for k in keys_to_remove:
            del _response_cache[k]
    _response_cache[key] = value

######################
# API Starts here
######################


@api.route('/test', methods=['GET'])
def test():
    return 'api test'


@api.route('/diseases', methods=['GET'])
def get_diseases():
    '''
    :return: diseaseID[]
    '''
    db = get_db()
    return jsonify(db.query_diseases())


@api.route('/drugs', methods=['GET'])
def get_drugs():
    '''
    :return: drugID[]
    '''
    db = get_db()
    return jsonify(db.query_drugs())


@api.route('/disease_predictions', methods=['GET'])
def get_disease_predictions():
    '''
    get disease predictions for a drug
    E.g.: [base_url]/api/disease_predictions?drug_id=DB00001&top_n=30
    
    :return: {
        predictions:{score:number, id: string }[],
        metapath_summary: {node_types: string[], count: number}[]
        }
    '''
    TOP_N = 15  # default, query top 15 predictions
    drug_id = request.args.get('drug_id', None, type=str)
    top_n = request.args.get('top_n', TOP_N, type=int)
    db = get_db()
    predictions = db.query_predicted_diseases(
        drug_id=drug_id, top_n=top_n)
    
    # Reuse metapath summary for now, or implement specific one
    summary = db.query_metapath_summary(top_n=top_n)
    
    return jsonify({'predictions': predictions, 'metapath_summary': summary})


@api.route('/attention', methods=['GET'])
def get_attention():
    '''
    :return: {'key': attentionTree}
    E.g.: [base_url]/api/attention?disease=0&drug=0
    '''
    disease_id = request.args.get('disease', None, type=str)
    drug_id = request.args.get('drug', None, type=str)

    db = get_db()
    attention = {}
    attention['disease'] = db.query_attention(disease_id, 'disease')
    attention['drug'] = db.query_attention(drug_id, 'drug')

    return jsonify(attention)


@api.route('/attention_pair', methods=['GET'])
def get_attention_pair():
    '''
    :return: {'attention': {key: attentionTree}, 'metapaths': metapath[]}
    E.g.: [base_url]/api/attention_pair?disease=0&drug=0
    '''
    disease_id = request.args.get('disease', None, type=str)
    drug_id = request.args.get('drug', None, type=str)
    
    # Check cache first
    cache_key = f"attention_pair:{drug_id}:{disease_id}"
    cached = get_cached_response(cache_key)
    if cached is not None:
        return jsonify(cached)

    db = get_db()
    res = db.query_attention_pair(disease_id, drug_id)
    
    # Cache the response
    set_cached_response(cache_key, res)

    return jsonify(res)


@api.route('/drug_predictions', methods=['GET'])
def get_drug_predictions():
    '''
    get drug predictions
    E.g.: [base_url]/api/drug_predictions?disease_id=1687.0&top_n=30

    :return: {
        predictions:{score:number, id: string }[],
        metapath_summary: {node_types: string[], count: number}[]
        }
    '''
    TOP_N = 15  # default, query top 10 predictions
    disease_id = request.args.get('disease_id', None, type=str)
    top_n = request.args.get('top_n', TOP_N, type=int)
    db = get_db()
    predictions = db.query_predicted_drugs(
        disease_id=disease_id, top_n=top_n)

    summary = db.query_metapath_summary(top_n=top_n)

    return jsonify({'predictions': predictions, 'metapath_summary': summary})

@api.route('/link_pred', methods=['GET'])
def get_link_pred():
    '''
    E.g.: [base_url]/api/drug_score?disease_id=5263.0&drug_id=DB06700
    '''
    
    disease_id = request.args.get('disease_id', None, type=str)
    drug_id = request.args.get('drug_id', None, type=str)
    db = get_db()
    predictions = db.query_drug_disease_pair(disease_id=disease_id, drug_id=drug_id)
    return jsonify(predictions)


@api.route('/node_name_dict', methods=['GET'])
def get_node_name_dict():
    '''
    Get the full node name dictionary including updates from attention_node_info.json
    '''
    db = get_db()
    return jsonify(db.node_name_dict)


# Disease category classification based on name patterns
DISEASE_CATEGORIES = {
    'cancer': ['cancer', 'carcinoma', 'tumor', 'tumour', 'neoplasm', 'leukemia', 'lymphoma', 
               'melanoma', 'sarcoma', 'adenoma', 'glioma', 'myeloma'],
    'neurological': ['neurological', 'brain', 'neural', 'alzheimer', 'parkinson', 'epilepsy',
                     'seizure', 'dementia', 'sclerosis', 'neuropathy', 'stroke', 'cerebral'],
    'cardiovascular': ['heart', 'cardiac', 'cardiovascular', 'arterial', 'venous', 'vascular',
                       'hypertension', 'arrhythmia', 'atherosclerosis', 'coronary', 'myocardial'],
    'autoimmune': ['autoimmune', 'rheumatoid', 'lupus', 'psoriasis', 'arthritis', 'crohn',
                   'colitis', 'multiple sclerosis', 'scleroderma', 'vasculitis'],
    'infectious': ['infection', 'infectious', 'bacterial', 'viral', 'fungal', 'parasitic',
                   'tuberculosis', 'hepatitis', 'hiv', 'malaria', 'sepsis'],
    'metabolic': ['diabetes', 'metabolic', 'obesity', 'thyroid', 'adrenal', 'pituitary',
                  'hormone', 'endocrine', 'insulin', 'glucose'],
    'respiratory': ['lung', 'respiratory', 'pulmonary', 'asthma', 'copd', 'pneumonia',
                    'bronchitis', 'fibrosis', 'emphysema'],
    'gastrointestinal': ['gastric', 'intestinal', 'bowel', 'colon', 'liver', 'pancreatic',
                         'hepatic', 'digestive', 'stomach', 'esophageal'],
    'genetic': ['genetic', 'hereditary', 'congenital', 'syndrome', 'mutation', 'chromosomal',
                'inherited', 'familial'],
}

def classify_disease(disease_name):
    """Classify a disease into a category based on its name."""
    if not disease_name:
        return 'other'
    
    name_lower = disease_name.lower()
    
    for category, keywords in DISEASE_CATEGORIES.items():
        for keyword in keywords:
            if keyword in name_lower:
                return category
    
    return 'other'


@api.route('/disease_embeddings', methods=['GET'])
def get_disease_embeddings():
    '''
    Get disease embeddings for a specific drug's predictions.
    E.g.: [base_url]/api/disease_embeddings?drug_id=DB12530
    
    Returns t-SNE style coordinates for diseases with category information.
    '''
    import random
    import os
    drug_id = request.args.get('drug_id', None, type=str)
    
    # Check cache first
    cache_key = f"disease_embeddings:{drug_id}"
    cached = get_cached_response(cache_key)
    if cached is not None:
        return jsonify(cached)
    
    db = get_db()
    embeddings = {}
    
    # Try to load actual t-SNE embeddings
    tsne_file = os.path.join(db.data_folder, 'disease_tsne.json')
    tsne_data = {}
    if os.path.exists(tsne_file):
        try:
            with open(tsne_file, 'r') as f:
                tsne_data = json.load(f)
        except:
            pass
    
    # Get predictions for this drug
    predictions = db.query_predicted_diseases(drug_id=drug_id, top_n=100) if drug_id else []
    predicted_disease_ids = set(pred.get('node_id') or pred.get('id') for pred in predictions)
    
    # Seed based on drug_id for consistent results
    if drug_id:
        random.seed(hash(drug_id) % (2**32))
    else:
        random.seed(42)
    
    # Generate embeddings for predicted diseases
    for idx, pred in enumerate(predictions):
        disease_id = pred.get('node_id') or pred.get('id')
        disease_name = pred.get('name', '')
        score = float(pred.get('score', 0.5))
        category = classify_disease(disease_name)
        
        # Use t-SNE coordinates if available, otherwise generate from score
        if str(disease_id) in tsne_data:
            x, y = tsne_data[str(disease_id)]
        else:
            x = (idx % 15) * 12 - 90 + random.uniform(-5, 5)
            y = (score - 0.3) * 250 + random.uniform(-8, 8)
        
        embeddings[str(disease_id)] = {
            'coords': [x, y],
            'category': category,
            'name': disease_name,
            'predicted': True
        }
    
    # Add additional diseases for context (from node_name_dict)
    if 'disease' in db.node_name_dict:
        disease_ids = list(db.node_name_dict['disease'].keys())
        for disease_id in disease_ids[:500]:
            if disease_id not in embeddings:
                disease_name = db.node_name_dict['disease'].get(disease_id, '')
                category = classify_disease(disease_name)
                
                # Use t-SNE coordinates if available
                if str(disease_id) in tsne_data:
                    x, y = tsne_data[str(disease_id)]
                else:
                    x = random.uniform(-120, 120)
                    y = random.uniform(-120, 120)
                
                embeddings[str(disease_id)] = {
                    'coords': [x, y],
                    'category': category,
                    'name': disease_name,
                    'predicted': False
                }
    
    # Cache the result
    set_cached_response(cache_key, embeddings)
    return jsonify(embeddings)


@api.route('/drug_list', methods=['GET'])
def get_drug_list():
    '''
    Get list of available drugs with their names.
    '''
    db = get_db()
    
    # Get processed drugs
    import os
    import json
    processed_drugs_file = os.path.join(db.data_folder, 'processed_drugs.json')
    
    if os.path.exists(processed_drugs_file):
        with open(processed_drugs_file, 'r') as f:
            drugs = json.load(f)
        return jsonify(drugs)
    
    # Fallback to drugs from node_name_dict
    if 'drug' in db.node_name_dict:
        drugs = [{'id': k, 'name': v} for k, v in list(db.node_name_dict['drug'].items())[:50]]
        return jsonify(drugs)
    
    return jsonify([])


@api.route('/subgraph', methods=['GET'])
def get_subgraph():
    '''
    Get subgraph for a drug-disease pair.
    E.g.: [base_url]/api/subgraph?drug_id=DB12530&disease_id=15783
    
    Returns:
        {
            nodes: [{id, label, type}],
            edges: [{source, target, relation, layer1_att, layer2_att, attention}]
        }
    '''
    import os
    
    drug_id = request.args.get('drug_id', None, type=str)
    disease_id = request.args.get('disease_id', None, type=str)
    
    if not drug_id or not disease_id:
        return jsonify({'error': 'drug_id and disease_id are required'}), 400
    
    # Check cache first
    cache_key = f"subgraph:{drug_id}:{disease_id}"
    cached = get_cached_response(cache_key)
    if cached is not None:
        return jsonify(cached)
    
    db = get_db()
    
    # Load subgraphs from file if not already loaded (should already be loaded by database_json)
    if not hasattr(db, 'subgraphs') or db.subgraphs is None:
        subgraphs_file = os.path.join(db.data_folder, 'subgraphs.json')
        if os.path.exists(subgraphs_file):
            try:
                with open(subgraphs_file, 'r') as f:
                    db.subgraphs = json.load(f)
            except Exception as e:
                print(f"Error loading subgraphs: {e}")
                db.subgraphs = {}
        else:
            db.subgraphs = {}
    
    # Try to find the subgraph with the standard key format
    subgraph_key = f"{drug_id}_{disease_id}"
    subgraph = db.subgraphs.get(subgraph_key)
    
    if not subgraph:
        # Return empty subgraph if not found
        result = {
            'nodes': [],
            'edges': [],
            'message': f'No subgraph found for key {subgraph_key}'
        }
        set_cached_response(cache_key, result)
        return jsonify(result)
    
    # Cache the result
    set_cached_response(cache_key, subgraph)
    return jsonify(subgraph)
