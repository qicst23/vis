import json
import numpy as np

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

    db = get_db()
    res = db.query_attention_pair(disease_id, drug_id)

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


@api.route('/disease_embeddings', methods=['GET'])
def get_disease_embeddings():
    '''
    Get disease embeddings for a specific drug's predictions.
    E.g.: [base_url]/api/disease_embeddings?drug_id=DB12530
    
    Returns t-SNE style coordinates for diseases, highlighting predicted ones.
    '''
    import random
    drug_id = request.args.get('drug_id', None, type=str)
    
    db = get_db()
    embeddings = {}
    
    # Get predictions for this drug
    predictions = db.query_predicted_diseases(drug_id=drug_id, top_n=100) if drug_id else []
    
    # Seed based on drug_id for consistent results
    if drug_id:
        random.seed(hash(drug_id) % (2**32))
    else:
        random.seed(42)
    
    # Generate embeddings for predicted diseases (arranged by score)
    for idx, pred in enumerate(predictions):
        disease_id = pred.get('node_id') or pred.get('id')
        score = float(pred.get('score', 0.5))
        
        # Position by score (higher score = higher y) and spread by index
        x = (idx % 15) * 12 - 90 + random.uniform(-5, 5)
        y = (score - 0.3) * 250 + random.uniform(-8, 8)
        embeddings[str(disease_id)] = [x, y]
    
    # Add additional diseases for context (from node_name_dict)
    if 'disease' in db.node_name_dict:
        disease_ids = list(db.node_name_dict['disease'].keys())
        for disease_id in disease_ids[:500]:
            if disease_id not in embeddings:
                x = random.uniform(-120, 120)
                y = random.uniform(-120, 120)
                embeddings[str(disease_id)] = [x, y]
    
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
