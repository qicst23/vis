# 🔬 Inebilizumab 10-Hop Deep Path Analysis Report

<<<<<<< HEAD
*Generated: 2025-12-09*  
*Version: 2.0 - With Protein Mechanism Details*

## Executive Summary

This report provides an in-depth analysis of **10-hop deep paths** from Inebilizumab to diseases in the knowledge graph. Paths are now **enriched with protein-level mechanistic details**, showing exactly which protein targets connect similar drugs and explaining the biological basis for drug-drug relationships.
=======
*Generated: 2025-12-09*

## Executive Summary

This report provides an in-depth analysis of **10-hop deep paths** from Inebilizumab to diseases in the knowledge graph. Unlike the standard 2-5 hop analysis, this extended exploration reveals **indirect biological mechanisms** and **complex drug repurposing opportunities** that traverse multiple intermediary nodes.
>>>>>>> 6377db4836d60d8731e5bdd079bb5187fa9ae7e9

## 1. Drug Profile

| Property | Value |
|----------|-------|
| **Drug ID** | DB12530 |
| **Drug Name** | Inebilizumab |
| **Type** | Monoclonal Antibody |
<<<<<<< HEAD
| **Primary Target** | **CD19** (B-cell surface antigen) |
=======
| **Target** | CD19 (B-cell surface antigen) |
>>>>>>> 6377db4836d60d8731e5bdd079bb5187fa9ae7e9
| **Mechanism** | B-cell depletion via ADCC |
| **Approved Indication** | Neuromyelitis Optica Spectrum Disorder (NMOSD) |

## 2. 10-Hop Path Statistics

| Metric | Value |
|--------|-------|
| **Total Paths Explored** | 5,648 |
| **Unique Diseases Reached** | 202 |
| **Mean Attention Score** | 0.8112 |
<<<<<<< HEAD
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
=======
| **Std Attention** | 0.0515 |
| **Min Attention** | 0.6929 |
| **Max Attention** | 0.9186 |

### Path Distribution by Hop Count

| Hops | Count | Percentage | Description |
|------|-------|------------|-------------|
| 4 | 66 | 1.2% | Short indirect paths |
| 5 | 582 | 10.3% | Medium-length paths |
| 6 | 1,000 | 17.7% | Extended pathways |
| 7 | 1,000 | 17.7% | Complex networks |
| 8 | 1,000 | 17.7% | Deep exploration |
| 9 | 1,000 | 17.7% | Very deep paths |
| 10 | 1,000 | 17.7% | Maximum depth |

### Visual Distribution

```
Paths by Hop Count:

4-hop:  ██ (66)
5-hop:  ██████████ (582)
6-hop:  █████████████████ (1,000)
7-hop:  █████████████████ (1,000)
8-hop:  █████████████████ (1,000)
9-hop:  █████████████████ (1,000)
10-hop: █████████████████ (1,000)
```

## 3. Intermediate Node Analysis

The paths predominantly traverse through **drug nodes**, indicating that Inebilizumab's repurposing potential is largely discovered through drug similarity networks rather than direct protein-disease connections.

| Node Type | Count in Top 500 Paths |
|-----------|------------------------|
| drug | 2,224 |

This suggests that the knowledge graph connects Inebilizumab to diseases via chains of similar or related drugs.

## 4. Top 20 Unique Paths (Ranked by Combined Score)

### Path #1: Influenza 🎯

**Path Visualization:**
```
[Inebilizumab] ─(0.836)─> [Basiliximab] ─(0.904)─> [Rubella virus vaccine] ─(0.866)─> [Moroxydine] ─(0.577)─> [influenza]
     drug                      drug                     drug                          drug              disease
>>>>>>> 6377db4836d60d8731e5bdd079bb5187fa9ae7e9
```

| Metric | Value |
|--------|-------|
<<<<<<< HEAD
| **Original Hops** | 4 |
| **Enriched Nodes** | 11 (with mechanisms) |
=======
| **Hops** | 4 |
>>>>>>> 6377db4836d60d8731e5bdd079bb5187fa9ae7e9
| **Avg Attention** | 0.7955 |
| **Combined Score** | 0.3977 |
| **Confidence** | ⭐⭐⭐⭐ High |

<<<<<<< HEAD
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
=======
**Interpretation:**
Inebilizumab shows similarity to Basiliximab (IL-2R antagonist), which connects to vaccine-related drugs (Rubella vaccine → Moroxydine), ultimately linking to influenza. This suggests potential immunomodulatory effects relevant to viral infections.

---

### Path #2: Influenza (Severe Susceptibility) 🎯

**Path Visualization:**
```
[Inebilizumab] ─(0.836)─> [Basiliximab] ─(0.904)─> [Rubella virus vaccine] ─(0.866)─> [Moroxydine] ─(0.524)─> [influenza, severe]
     drug                      drug                     drug                          drug              disease
>>>>>>> 6377db4836d60d8731e5bdd079bb5187fa9ae7e9
```

| Metric | Value |
|--------|-------|
<<<<<<< HEAD
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
=======
| **Hops** | 4 |
| **Avg Attention** | 0.7825 |
| **Combined Score** | 0.3912 |
| **Confidence** | ⭐⭐⭐⭐ High |

**Interpretation:**
Similar to Path #1, but specifically linked to severe influenza susceptibility, indicating potential use in high-risk patient populations.

---

### Path #3: Liver Disease 🎯

**Path Visualization:**
```
[Inebilizumab] ─(0.848)─> [Cladribine] ─(0.870)─> [Anthrax vaccine] ─(0.912)─> [Rimantadine] ─(0.487)─> [liver disease]
     drug                      drug                  drug                        drug              disease
```

| Metric | Value |
|--------|-------|
| **Hops** | 4 |
| **Avg Attention** | 0.7791 |
| **Combined Score** | 0.3896 |
| **Confidence** | ⭐⭐⭐⭐ High |

**Interpretation:**
Connection through Cladribine (purine nucleoside analogue used in MS) and antiviral/vaccine pathways suggests potential hepatoprotective or liver-modulating effects.

---

### Path #4: Testicular Seminoma 🎯

**Path Visualization:**
```
[Inebilizumab] ─(0.875)─> [Rozanolixizumab] ─(0.864)─> [Trastuzumab] ─(0.830)─> [Plicamycin] ─(0.492)─> [testicular seminoma]
     drug                      drug                      drug                    drug              disease
>>>>>>> 6377db4836d60d8731e5bdd079bb5187fa9ae7e9
```

| Metric | Value |
|--------|-------|
<<<<<<< HEAD
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
=======
| **Hops** | 4 |
| **Avg Attention** | 0.7653 |
| **Combined Score** | 0.3826 |
| **Confidence** | ⭐⭐⭐⭐ High |

**Interpretation:**
Path through antibody drugs (Rozanolixizumab - FcRn inhibitor, Trastuzumab - HER2) to chemotherapy (Plicamycin) suggests potential anti-cancer mechanisms beyond immunomodulation.

---

### Path #5: Vulvovaginal Candidiasis 🎯

**Path Visualization:**
```
[Inebilizumab] ─(0.865)─> [AVE9633] ─(0.863)─> [Entrectinib] ─(0.862)─> [Tioconazole] ─(0.470)─> [vulvovaginal candidiasis]
     drug                    drug                 drug                    drug              disease
```

| Metric | Value |
|--------|-------|
| **Hops** | 4 |
| **Avg Attention** | 0.7648 |
| **Combined Score** | 0.3824 |
| **Confidence** | ⭐⭐⭐⭐ High |

**Interpretation:**
Connection through kinase inhibitors to antifungal agents suggests B-cell depletion may have implications for fungal infection susceptibility or treatment.

---

### Path #6: Actinic Keratosis 🎯

**Path Visualization:**
```
[Inebilizumab] ─(0.879)─> [Fluprednisolone] ─(0.873)─> [Cyclothiazide] ─(0.892)─> [Peginesatide] ─(0.902)─> [Aminolevulinic acid] ─(0.500)─> [actinic keratosis]
     drug                      drug                       drug                      drug                      drug                       disease
```

| Metric | Value |
|--------|-------|
| **Hops** | 5 |
| **Avg Attention** | 0.8092 |
| **Combined Score** | 0.3619 |
| **Confidence** | ⭐⭐⭐⭐ High |

**Interpretation:**
Path through corticosteroids and various drug classes to photodynamic therapy agent suggests potential dermatological applications.

---

### Path #7: Keratoacanthoma 🎯

**Path Visualization:**
```
[Inebilizumab] ─(0.879)─> [Fluprednisolone] ─(0.873)─> [Cyclothiazide] ─(0.892)─> [Peginesatide] ─(0.902)─> [Aminolevulinic acid] ─(0.499)─> [keratoacanthoma]
     drug                      drug                       drug                      drug                      drug                       disease
```

| Metric | Value |
|--------|-------|
| **Hops** | 5 |
| **Avg Attention** | 0.8089 |
| **Combined Score** | 0.3618 |
| **Confidence** | ⭐⭐⭐⭐ High |

**Interpretation:**
Similar path to actinic keratosis, suggesting potential for treating other skin neoplasms.

---

### Path #8: Perinatal Necrotizing Enterocolitis 🎯

**Path Visualization:**
```
[Inebilizumab] ─(0.879)─> [Fluprednisolone] ─(0.944)─> [Elvitegravir] ─(0.856)─> [BCG vaccine] ─(0.859)─> [Fidaxomicin] ─(0.498)─> [perinatal NEC]
     drug                      drug                      drug                    drug                     drug                   disease
```

| Metric | Value |
|--------|-------|
| **Hops** | 5 |
| **Avg Attention** | 0.8072 |
| **Combined Score** | 0.3610 |
| **Confidence** | ⭐⭐⭐⭐ High |

**Interpretation:**
Path through anti-inflammatory and antimicrobial agents suggests potential gut-related immunomodulatory effects.

---

## 5. Extended Deep Paths (8-10 Hops)

### Best 8-Hop Path: Influenza

**Path:**
```
Inebilizumab → Basiliximab → Belatacept → Typhoid Vi vaccine → Daclizumab → Fluocortin → 
Varicella Zoster Vaccine → Moroxydine → influenza
```

| Metric | Value |
|--------|-------|
| **Combined Score** | 0.3176 |
| **Path Length** | 8 hops |
| **Confidence** | ⭐⭐⭐ Medium |

---

### Best 9-Hop Path: Influenza

**Path:**
```
Inebilizumab → Basiliximab → Belatacept → Typhoid Vi vaccine → Daclizumab → 
Influenza A H1N1 hemagglutinin antigen → Aloxiprin → Varicella Zoster Vaccine → Moroxydine → influenza
```

| Metric | Value |
|--------|-------|
| **Combined Score** | 0.3032 |
| **Path Length** | 9 hops |
| **Confidence** | ⭐⭐⭐ Medium |

---

### Best 10-Hop Path: Influenza

**Path:**
```
Inebilizumab → Basiliximab → Belatacept → Typhoid Vi vaccine → Fluocortin → Daclizumab → 
Influenza A H1N1 antigen → Aloxiprin → Varicella Zoster Vaccine → Moroxydine → influenza
```

| Metric | Value |
|--------|-------|
| **Combined Score** | 0.2905 |
| **Path Length** | 10 hops |
| **Confidence** | ⭐⭐ Low-Medium |

---

## 6. Disease Categories Reached

### Top 20 Unique Diseases

| # | Disease | Category |
|---|---------|----------|
| 1 | influenza | Infectious |
| 2 | influenza, severe, susceptibility to | Infectious |
| 3 | liver disease | Gastrointestinal |
| 4 | testicular seminoma | Cancer |
| 5 | seminoma | Cancer |
| 6 | spermatocytic seminoma | Cancer |
| 7 | testicular teratoma | Cancer |
| 8 | vulvovaginal candidiasis | Infectious |
| 9 | testicular cancer | Cancer |
| 10 | testicular germ cell tumor | Cancer |
| 11 | yolk sac tumor | Cancer |
| 12 | actinic keratosis | Dermatological |
| 13 | actinic cheilitis | Dermatological |
| 14 | keratoacanthoma | Dermatological |
| 15 | inverted follicular keratosis | Dermatological |
| 16 | photoparoxysmal response | Neurological |
| 17 | photosensitivity disease | Dermatological |
| 18 | perinatal necrotizing enterocolitis | Gastrointestinal |
| 19 | Clostridium infectious disease | Infectious |
| 20 | Clostridium difficile colitis | Gastrointestinal |

### Disease Category Distribution

| Category | Count | Notable Examples |
|----------|-------|------------------|
| **Cancer** | ~35% | Testicular cancers, seminomas, germ cell tumors |
| **Infectious** | ~25% | Influenza, candidiasis, C. difficile |
| **Dermatological** | ~20% | Actinic keratosis, photosensitivity |
| **Gastrointestinal** | ~15% | Liver disease, NEC |
| **Other** | ~5% | Various conditions |

---

## 7. Interpretation Guidelines

### Understanding 10-Hop Paths

Unlike shorter paths (2-3 hops) that represent direct mechanisms, 10-hop paths reveal:

1. **Drug Class Relationships**: Similarity between drug mechanisms across multiple generations
2. **Therapeutic Area Overlap**: Unexpected connections between different disease domains
3. **Exploratory Hypotheses**: Potential repurposing opportunities requiring further validation

### Confidence Scale for 10-Hop Paths

| Combined Score | Confidence | Recommendation |
|----------------|------------|----------------|
| > 0.35 | ⭐⭐⭐⭐ High | Strong candidate for further investigation |
| 0.30 - 0.35 | ⭐⭐⭐ Medium | Moderate support, requires validation |
| 0.25 - 0.30 | ⭐⭐ Low | Exploratory hypothesis only |
| < 0.25 | ⭐ Very Low | Weak connection, low priority |

### Key Insights from 10-Hop Analysis

1. **Immunotherapy Network**: Inebilizumab shows strong connectivity to other immunomodulatory antibodies (Basiliximab, Belatacept, Daclizumab)

2. **Vaccine Pathways**: Multiple paths traverse through vaccine nodes, suggesting interactions with immune response pathways

3. **Cancer Potential**: Unexpected connections to testicular cancers through antibody similarity networks

4. **Infectious Disease Links**: Strong paths to influenza and other infectious diseases via immunomodulation

5. **Dermatological Connections**: Paths through photodynamic therapy agents to skin conditions

---

## 8. Recommendations for Drug Repurposing

### High Priority Candidates (Score > 0.35)

| Disease | Score | Rationale |
|---------|-------|-----------|
| Influenza | 0.398 | Strong immunomodulatory pathway |
| Liver Disease | 0.390 | Through MS drug (Cladribine) pathway |
| Testicular Seminoma | 0.383 | Antibody network similarity |

### Medium Priority Candidates (0.30-0.35)

| Disease | Score | Rationale |
|---------|-------|-----------|
| Actinic Keratosis | 0.362 | Dermatological immunomodulation |
| Keratoacanthoma | 0.362 | Similar pathway to actinic keratosis |
| Perinatal NEC | 0.361 | Gut immunomodulation potential |

### Exploratory Candidates (0.25-0.30)

| Disease | Score | Rationale |
|---------|-------|-----------|
| Various 8-10 hop diseases | 0.25-0.32 | Require extensive validation |

---

## 9. Limitations

1. **Path Length Penalty**: Longer paths have inherently lower combined scores due to length penalty
2. **Drug-Only Intermediates**: Most paths traverse only drug nodes, missing potential protein/pathway mechanisms
3. **Knowledge Graph Completeness**: Some connections may be missing from the underlying PrimeKG
4. **Attention Score Interpretation**: High attention doesn't guarantee biological relevance

---

## 10. Technical Details

### Scoring Formula

```
Combined Score = Avg_Attention × (1 / √hops)

Where:
- Avg_Attention = Mean cosine similarity of TxGNN embeddings along path
- hops = Number of edges in path
```

### Exploration Parameters

| Parameter | Value |
|-----------|-------|
| Max Depth | 10 hops |
| Max Frontier Size | 100,000 nodes |
| Max Neighbors per Node | 50 |
| Max Paths per Node | 3 |
| Total Max Paths | 10,000 |

---

## Appendix: All 202 Unique Diseases Reached

<details>
<summary>Click to expand full disease list</summary>

1. influenza
2. influenza, severe, susceptibility to
3. liver disease
4. testicular seminoma
5. seminoma
6. spermatocytic seminoma
7. testicular teratoma
8. vulvovaginal candidiasis
9. testicular cancer
10. testicular germ cell tumor
11. yolk sac tumor
12. actinic keratosis (disease)
13. actinic cheilitis
14. keratoacanthoma
15. inverted follicular keratosis
16. photoparoxysmal response
17. photosensitivity disease
18. perinatal necrotizing enterocolitis
19. Clostridium infectious disease
20. Clostridium difficile colitis
... (and 182 more diseases)

</details>

---

*Report generated by TxGNN 10-Hop Deep Path Analysis Pipeline*

*For questions or additional analysis, contact the TxGNN team.*

>>>>>>> 6377db4836d60d8731e5bdd079bb5187fa9ae7e9
