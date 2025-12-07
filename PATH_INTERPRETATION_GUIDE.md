# 🔬 Path Interpretation Guide

## How to Understand Drug-Disease Paths in TxGNN

This guide explains how to interpret the paths shown in the "All Paths (2-5 hop)" visualization tab.

---

## What Are Paths?

Each path shows a **mechanistic explanation** for why a drug might treat a disease. The path traces connections through the Knowledge Graph (KG) that explain the drug-disease relationship through intermediate biological entities.

---

## Path Components

### 1. Start Node (Drug)
- Always the query drug (e.g., Inebilizumab)
- This is the drug we're analyzing for repurposing opportunities

### 2. Intermediate Nodes (The "Bridge")
These explain the connection between drug and disease:

| Node Type | Meaning | Example |
|-----------|---------|---------|
| **drug** | A similar drug that treats the target disease | Rituximab |
| **gene/protein** | A protein target shared between drug and disease | CD19, PAX5 |
| **biological_process** | A biological function connecting them | B cell activation |
| **pathway** | A metabolic/signaling pathway involved | NF-κB signaling |
| **anatomy** | A tissue/organ connecting drug effect to disease | Bone marrow |

### 3. End Node (Disease)
- The candidate disease that the drug might treat
- This is the repurposing prediction target

---

## Path Types & Interpretations

### Type 1: Drug → Protein → Disease (Target-Based)

```
Inebilizumab ──(0.50)──> CD19 ──(0.50)──> Agammaglobulinemia
    [drug]              [protein]            [disease]
```

**How to Read:**
1. **Inebilizumab targets CD19** - This is its known mechanism of action
2. **CD19 is implicated in agammaglobulinemia** - CD19 mutations cause this antibody deficiency disease
3. **Inference:** By modulating CD19, Inebilizumab may affect agammaglobulinemia

**Biological Meaning:**
- This is the most mechanistically meaningful path type
- Shows direct biological connection through protein targets
- High confidence predictions

---

### Type 2: Drug → Drug → Disease (Drug Similarity)

```
Inebilizumab ──(0.83)──> Rituximab ──(0.48)──> Non-Hodgkin Lymphoma
    [drug]                [drug]                   [disease]
```

**How to Read:**
1. **Inebilizumab is similar to Rituximab** (attention: 0.83 = very similar)
   - Both are monoclonal antibodies targeting B cells
   - Inebilizumab targets CD19, Rituximab targets CD20
2. **Rituximab treats Non-Hodgkin Lymphoma** (known FDA indication)
3. **Inference:** Since both drugs work through similar mechanisms, Inebilizumab might also be effective

**Biological Meaning:**
- Based on drug class similarity
- "Guilt by association" - similar drugs may have similar effects
- The higher the first attention score, the more similar the drugs

---

### Type 3: Drug → Protein → Protein → Disease (Pathway-Based)

```
Inebilizumab ──> CD19 ──> PAX5 ──> B-cell Leukemia
    [drug]      [protein] [protein]   [disease]
```

**How to Read:**
1. **Inebilizumab targets CD19** on B cells
2. **CD19 interacts with PAX5** (B-cell transcription factor)
3. **PAX5 is involved in B-cell leukemia** pathogenesis
4. **Inference:** Drug effects propagate through protein-protein interaction network

**Biological Meaning:**
- Shows indirect mechanism through protein networks
- Based on protein-protein interactions (PPIs)
- Explains how drug effects can reach diseases not directly linked to the target

---

### Type 4: Drug → Drug → Protein → Disease (Combined)

```
Inebilizumab ──> Cladribine ──> POLA1 ──> Colorectal Cancer
    [drug]        [drug]       [protein]    [disease]
```

**How to Read:**
1. **Inebilizumab is related to Cladribine** (both affect lymphocytes)
2. **Cladribine targets POLA1** (DNA polymerase)
3. **POLA1 is implicated in Colorectal Cancer**
4. **Inference:** Multi-step mechanistic connection

---

## Understanding Attention Scores

The attention score measures **semantic similarity** between connected nodes, derived from TxGNN embeddings.

| Score Range | Interpretation | Confidence |
|-------------|----------------|------------|
| **0.80 - 1.00** | Very strong relationship | ⭐⭐⭐⭐⭐ High |
| **0.65 - 0.80** | Strong relationship | ⭐⭐⭐⭐ Good |
| **0.50 - 0.65** | Moderate relationship | ⭐⭐⭐ Medium |
| **0.35 - 0.50** | Weak relationship | ⭐⭐ Low |
| **< 0.35** | Very weak relationship | ⭐ Speculative |

### What Attention Scores Represent:
- **High score (>0.7):** Nodes are semantically very similar in the TxGNN embedding space
  - Example: Two drugs with same mechanism of action
  - Example: Protein and disease it directly causes
  
- **Medium score (0.5-0.7):** Nodes have meaningful biological relationship
  - Example: Drugs in related therapeutic classes
  - Example: Protein in pathway related to disease
  
- **Low score (<0.5):** Weak or indirect relationship
  - May still be valid but requires more validation
  - Often seen in longer paths (3-5 hops)

---

## Combined Score Formula

The **Combined Score** balances attention strength with path length:

```
Combined Score = Average Attention × (1 / √hops)
```

| Hops | Length Penalty | Effect |
|------|----------------|--------|
| 2 | 0.71 | Slight penalty |
| 3 | 0.58 | Moderate penalty |
| 4 | 0.50 | Significant penalty |
| 5 | 0.45 | Heavy penalty |

**Why penalize longer paths?**
- Shorter paths = more direct biological connection
- Longer paths = more assumptions/uncertainty
- But longer paths can reveal novel mechanisms!

---

## Example: Inebilizumab Analysis

### About Inebilizumab
| Property | Value |
|----------|-------|
| **Trade Name** | Uplizna |
| **Type** | Humanized monoclonal antibody |
| **Target** | CD19 (B-cell surface marker) |
| **Mechanism** | Depletes CD19+ B cells |
| **FDA Approved** | Neuromyelitis optica spectrum disorder (NMOSD) |

### Top Predicted Paths

#### 1. Inebilizumab → CD19 → Agammaglobulinemia
- **Attention:** 0.50 → 0.50
- **Why it makes sense:** CD19 deficiency causes agammaglobulinemia. Inebilizumab depletes CD19+ cells.
- **Clinical relevance:** Inebilizumab might worsen this condition (caution) or provide insights into B-cell biology.

#### 2. Inebilizumab → Rituximab → B-cell Lymphoma
- **Attention:** 0.83 → 0.48
- **Why it makes sense:** Both target B cells (CD19 vs CD20). Rituximab is approved for lymphoma.
- **Clinical relevance:** Strong candidate for clinical investigation.

#### 3. Inebilizumab → Cladribine → Multiple Sclerosis
- **Attention:** 0.85 → 0.47
- **Why it makes sense:** Both deplete lymphocytes. Cladribine is approved for MS.
- **Clinical relevance:** Inebilizumab already approved for NMOSD (related to MS).

---

## Visual Path Diagram

```
                    ┌─────────────────────────────────────────┐
                    │         PATH INTERPRETATION             │
                    └─────────────────────────────────────────┘
                    
Drug Similarity Path:              Target-Based Path:
                    
Inebilizumab ──0.83──> Rituximab      Inebilizumab ──0.50──> CD19
                           │                                  │
     "Similar antibody     │                "Targets this     │
      targeting B cells"   │                 protein"         │
                           ▼                                  ▼
              Non-Hodgkin Lymphoma              Agammaglobulinemia
                           
     "Rituximab treats     │                "CD19 mutations   │
      this cancer"         │                 cause this"      │
                           ▼                                  ▼
                           
     PREDICTION: Inebilizumab        PREDICTION: Inebilizumab's
     may also treat B-cell           B-cell depletion is
     malignancies                    mechanistically relevant
```

---

## Data Sources

The paths are derived from:

1. **PrimeKG Knowledge Graph**
   - 129,375 biomedical entities
   - 10 node types (drugs, diseases, proteins, etc.)
   - 8+ million edges (biological relationships)

2. **TxGNN Model**
   - Graph neural network trained on drug-disease associations
   - 512-dimensional node embeddings
   - Attention scores from embedding similarity

3. **Known Associations**
   - FDA-approved drug indications
   - Clinical trial data
   - Literature-derived relationships

---

## How to Use This Information

### For Drug Repurposing:
1. **Short paths (2-hop) with high attention** → Best candidates for follow-up
2. **Protein-mediated paths** → Mechanistically explainable predictions
3. **Drug-similarity paths** → Class-effect predictions

### For Understanding Mechanisms:
1. Look at the intermediate nodes to understand WHY the prediction was made
2. Higher attention = stronger biological relationship
3. Multiple paths to same disease = more confident prediction

### For Validation:
1. Check if intermediate proteins are known drug targets
2. Verify disease-gene associations in literature
3. Look for clinical evidence supporting the connection

---

## Glossary

| Term | Definition |
|------|------------|
| **Attention Score** | Cosine similarity between node embeddings (0-1) |
| **Hop** | One edge traversal in the knowledge graph |
| **Path** | Sequence of nodes and edges from drug to disease |
| **Combined Score** | Attention weighted by path length |
| **KG** | Knowledge Graph - structured biological database |
| **Embedding** | Vector representation of a node learned by TxGNN |

---

*Generated by TxGNN Drug Explorer*

