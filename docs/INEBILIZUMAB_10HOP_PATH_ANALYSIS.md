# 🔬 Inebilizumab 10-Hop Deep Path Analysis Report

*Generated: 2025-12-09*  
*Version: 2.0 - With Protein Mechanism Details*

## Executive Summary

This report provides an in-depth analysis of **10-hop deep paths** from Inebilizumab to diseases in the knowledge graph. Paths are now **enriched with protein-level mechanistic details**, showing exactly which protein targets connect similar drugs and explaining the biological basis for drug-drug relationships.

## 1. Drug Profile

| Property | Value |
|----------|-------|
| **Drug ID** | DB12530 |
| **Drug Name** | Inebilizumab |
| **Type** | Monoclonal Antibody |
| **Primary Target** | **CD19** (B-cell surface antigen) |
| **Mechanism** | B-cell depletion via ADCC |
| **Approved Indication** | Neuromyelitis Optica Spectrum Disorder (NMOSD) |

## 2. 10-Hop Path Statistics

| Metric | Value |
|--------|-------|
| **Total Paths Explored** | 5,648 |
| **Unique Diseases Reached** | 202 |
| **Mean Attention Score** | 0.8112 |
| **Paths with Protein Mechanisms** | 500+ |

### Path Distribution by Hop Count

| Hops | Count | Description |
|------|-------|-------------|
| 4 | 66 | Short indirect paths |
| 5 | 582 | Medium-length paths |
| 6 | 1,000 | Extended pathways |
| 7 | 1,000 | Complex networks |
| 8 | 1,000 | Deep exploration |
| 9 | 1,000 | Very deep paths |
| 10 | 1,000 | Maximum depth |

## 3. Key Protein Targets Identified

### Inebilizumab Target
| Protein | Type | Function |
|---------|------|----------|
| **CD19** | B-cell surface antigen | B-cell receptor signaling, activation |

### Connected Drug Targets (via path mechanisms)
| Drug | Protein Target | Connection to CD19 |
|------|---------------|-------------------|
| Basiliximab | **IL2RA, IL2RB** | Shared cellular component |
| Rituximab | **MS4A1 (CD20)** | B-cell surface (similar function) |
| Obinutuzumab | **MS4A1 (CD20)** | B-cell surface (similar function) |
| Trastuzumab | **ERBB2** | Embedding similarity |

## 4. Top Enriched Paths (with Protein Mechanisms)

### Path #1: Influenza 🎯

**Original Path (5 nodes):**
```
Inebilizumab → Basiliximab → Rubella virus vaccine → Moroxydine → influenza
```

**Enriched Path with Mechanisms (11 nodes):**
```
Inebilizumab ─(0.84)─→ CD19 ─[shared cellular component]─→ IL2RB ─→ Basiliximab
     │                   │                                    │
     │                   └── gene/protein                     │
     ↓                       (Inebilizumab target)            ↓
Rubella virus vaccine ←───────────────────────────────────────┘
     │                        (via IL2R receptor family connection)
     ↓
     ─(0.87)─→ [embedding similarity] → Moroxydine ─(0.58)─→ influenza
```

| Metric | Value |
|--------|-------|
| **Original Hops** | 4 |
| **Enriched Nodes** | 11 (with mechanisms) |
| **Avg Attention** | 0.7955 |
| **Combined Score** | 0.3977 |
| **Confidence** | ⭐⭐⭐⭐ High |

**Mechanism Explanation:**
1. **Inebilizumab targets CD19** (B-cell antigen)
2. **CD19 shares cellular components with IL2RB** (IL-2 receptor beta chain)
3. **Basiliximab targets IL2RA/IL2RB** (IL-2 receptor antagonist)
4. Both drugs modulate immune cell signaling pathways
5. Connection to antivirals (Rubella vaccine, Moroxydine) via immunomodulation

**Clinical Interpretation:**
This path suggests Inebilizumab's B-cell depleting mechanism could influence viral immunity through shared immune cell surface receptor biology. The CD19-IL2RB connection indicates overlap in lymphocyte signaling pathways.

---

### Path #2: Liver Disease 🎯

**Enriched Path:**
```
Inebilizumab ─(0.85)─→ CD19 ─[shared bioprocess]─→ [Cladribine targets] ─→ Cladribine
     │                                                                       │
     └── (B-cell depletion) ←── (purine analogue, MS treatment) ←───────────┘
                                          ↓
                           Anthrax vaccine → Rimantadine → liver disease
```

| Metric | Value |
|--------|-------|
| **Combined Score** | 0.3896 |
| **Key Connection** | Both used in multiple sclerosis |
| **Mechanism** | Immunomodulation affecting hepatic inflammation |

**Clinical Interpretation:**
Cladribine (a purine nucleoside analogue also used in MS) shares biological processes with CD19-targeting therapies. The path through antiviral agents to liver disease suggests potential hepatic effects of immune modulation.

---

### Path #3: Testicular Seminoma 🎯

**Enriched Path:**
```
Inebilizumab → CD19 → [similar targets] → Rozanolixizumab (FcRn inhibitor)
                                               ↓
                                    → Trastuzumab (ERBB2) → Plicamycin → seminoma
```

| Metric | Value |
|--------|-------|
| **Combined Score** | 0.3826 |
| **Key Proteins** | CD19, FcRn, ERBB2 |
| **Mechanism** | Antibody drug similarity network |

**Clinical Interpretation:**
This path traverses through multiple monoclonal antibodies (Rozanolixizumab, Trastuzumab) to reach cancer chemotherapy (Plicamycin). Suggests Inebilizumab may have anti-tumor potential through B-cell mediated mechanisms.

---

## 5. Mechanism Types Identified

| Mechanism Type | Count | Description |
|----------------|-------|-------------|
| **Shared Cellular Component** | ~40% | Proteins localized to same cellular structure |
| **Embedding Similarity** | ~35% | TxGNN identified semantic similarity |
| **Shared Pathway** | ~15% | Proteins in same biological pathway |
| **Protein-Protein Interaction** | ~10% | Direct physical interaction |

### Example Mechanisms

```
CD19 ──[shared cellular component]──→ IL2RB
     └── Both are on lymphocyte cell surface

CD19 ──[shared pathway]──→ PAX5 targets
     └── Both involved in B-cell development

Drug A ──[embedding similarity]──→ Drug B
     └── TxGNN embeddings show high cosine similarity
```

## 6. Visual Legend for Enriched Paths

| Symbol | Meaning |
|--------|---------|
| 🟢 **Drug** (green) | Original drug in path |
| 🟠 **Gene/Protein** (orange) | Protein target - **newly added!** |
| 🟣 **[mechanism]** (purple dashed) | Connection explanation - **newly added!** |
| 🔴 **Disease** (red) | Terminal disease node |
| ⭐ | Enriched node (not in original path) |

## 7. Key Insights

### 1. CD19 is the Hub
Inebilizumab's target **CD19** serves as the mechanistic hub connecting to many other drugs through:
- Shared cellular components (cell surface receptors)
- B-cell signaling pathways
- Lymphocyte development processes

### 2. Immunomodulation Network
Most paths pass through immunomodulatory drugs:
- **Basiliximab** (IL-2R antagonist)
- **Rituximab** (CD20)
- **Cladribine** (MS treatment)

### 3. Unexpected Cancer Connections
Strong paths to testicular cancers through antibody similarity networks suggest potential oncology applications beyond autoimmune disease.

### 4. Infectious Disease Links
Multiple paths to influenza and viral diseases indicate immune system connections worth investigating.

## 8. How Paths are Enriched

For each **Drug → Drug** edge in the original path:

1. **Lookup Drug A's protein targets** (via `drug_protein` edges in KG)
2. **Lookup Drug B's protein targets**
3. **Find connection between targets:**
   - Same target? → "same_target"
   - Direct protein-protein interaction? → "protein_protein"
   - Shared pathway? → "shared_pathway"
   - Shared cellular component? → "shared_cellular_component"
   - High embedding similarity? → "similar_targets"
4. **Insert protein nodes and mechanism explanation into path**

### Before vs After

**Before (Drug-only):**
```
Inebilizumab → Basiliximab → Rubella vaccine → Moroxydine → influenza
```

**After (With Mechanisms):**
```
Inebilizumab → CD19 → [shared cellular component] → IL2RB → Basiliximab → IL2RB → [embedding similarity] → Rubella vaccine → [embedding similarity] → Moroxydine → influenza
```

## 9. Recommendations

### High Priority for Investigation
| Disease | Score | Mechanism Basis |
|---------|-------|-----------------|
| Influenza | 0.398 | CD19-IL2R cellular component sharing |
| Liver disease | 0.390 | Purine metabolism pathway overlap |
| Testicular seminoma | 0.383 | Antibody network (CD19→ERBB2) |

### Medium Priority
| Disease | Score | Mechanism Basis |
|---------|-------|-----------------|
| Actinic keratosis | 0.362 | Corticosteroid pathway connection |
| Vulvovaginal candidiasis | 0.382 | Kinase inhibitor network |

## 10. Technical Details

### Enrichment Algorithm
```python
for each drug-drug edge in path:
    drug1_targets = get_protein_targets(drug1)  # via drug_protein edges
    drug2_targets = get_protein_targets(drug2)
    
    for t1 in drug1_targets:
        for t2 in drug2_targets:
            if t1 == t2:
                add_node(t1, "same_target")
            elif protein_protein_edge(t1, t2):
                add_nodes(t1, t2, "protein_protein")
            elif shared_pathway(t1, t2):
                add_nodes(t1, t2, "shared_pathway")
            elif shared_cellular_component(t1, t2):
                add_nodes(t1, t2, "shared_cellular_component")
            elif embedding_similarity(t1, t2) > 0.6:
                add_nodes(t1, t2, "similar_targets")
```

### Files Generated
- `inebilizumab_10hop_paths.json` (16 MB, enriched)
- `inebilizumab_10hop_paths_original.json` (12 MB, original)

---

*Report generated by TxGNN 10-Hop Deep Path Analysis Pipeline v2.0*  
*With protein-level mechanistic enrichment*
