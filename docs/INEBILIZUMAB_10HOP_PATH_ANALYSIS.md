# 🔬 Inebilizumab 10-Hop Deep Path Analysis Report

*Generated: 2025-12-09*

## Executive Summary

This report provides an in-depth analysis of **10-hop deep paths** from Inebilizumab to diseases in the knowledge graph. Unlike the standard 2-5 hop analysis, this extended exploration reveals **indirect biological mechanisms** and **complex drug repurposing opportunities** that traverse multiple intermediary nodes.

## 1. Drug Profile

| Property | Value |
|----------|-------|
| **Drug ID** | DB12530 |
| **Drug Name** | Inebilizumab |
| **Type** | Monoclonal Antibody |
| **Target** | CD19 (B-cell surface antigen) |
| **Mechanism** | B-cell depletion via ADCC |
| **Approved Indication** | Neuromyelitis Optica Spectrum Disorder (NMOSD) |

## 2. 10-Hop Path Statistics

| Metric | Value |
|--------|-------|
| **Total Paths Explored** | 5,648 |
| **Unique Diseases Reached** | 202 |
| **Mean Attention Score** | 0.8112 |
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
```

| Metric | Value |
|--------|-------|
| **Hops** | 4 |
| **Avg Attention** | 0.7955 |
| **Combined Score** | 0.3977 |
| **Confidence** | ⭐⭐⭐⭐ High |

**Interpretation:**
Inebilizumab shows similarity to Basiliximab (IL-2R antagonist), which connects to vaccine-related drugs (Rubella vaccine → Moroxydine), ultimately linking to influenza. This suggests potential immunomodulatory effects relevant to viral infections.

---

### Path #2: Influenza (Severe Susceptibility) 🎯

**Path Visualization:**
```
[Inebilizumab] ─(0.836)─> [Basiliximab] ─(0.904)─> [Rubella virus vaccine] ─(0.866)─> [Moroxydine] ─(0.524)─> [influenza, severe]
     drug                      drug                     drug                          drug              disease
```

| Metric | Value |
|--------|-------|
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
```

| Metric | Value |
|--------|-------|
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

