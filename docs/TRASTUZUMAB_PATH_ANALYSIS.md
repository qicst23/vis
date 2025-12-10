# 🔬 Trastuzumab Path Analysis Report

*Generated: 2025-12-07 14:00:25*

## 1. Drug Profile

| Property | Value |
|----------|-------|
| **Drug ID** | DB00072 |
| **Drug Name** | Trastuzumab |
| **Type** | drug |

## 2. Path Statistics

| Metric | Value |
|--------|-------|
| **Total Paths** | 100 |
| **Unique Diseases** | 72 |
| **Mean Attention** | 0.5990 |
| **Std Attention** | 0.0600 |
| **Min Attention** | 0.4733 |
| **Max Attention** | 0.7458 |

### Paths by Hop Count

| Hops | Count |
|------|-------|
| 1 | 1 |
| 2 | 400 |
| 3 | 400 |
| 4 | 400 |
| 5 | 400 |

## 3. Path Type Summary

| Path Type | Count | Description |
|-----------|-------|-------------|
| Drug Similarity | 99 | Paths through similar drugs |
| Protein Target | 0 | Paths through protein targets |
| Pathway | 0 | Paths through biological pathways |
| Biological Process | 0 | Paths through biological processes |
| Other | 1 | Other connection types |

### Key Similar Drugs

| Similar Drug | Max Attention | # Diseases |
|--------------|---------------|------------|
| Dasatinib | 0.7630 | 22 |
| Estradiol | 0.6954 | 25 |
| Mestranol | 0.6941 | 4 |
| Chlorotrianisene | 0.6896 | 34 |
| Ibrutinib | 0.6848 | 2 |
| Ethinylestradiol | 0.6817 | 11 |
| Tibolone | 0.6573 | 1 |

## 4. Top 20 Paths (by Combined Score)

### Path #1: HER2 positive breast carcinoma

**Path:**
```
[Trastuzumab] --(0.496)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.4961 |
| Combined Score | 0.4961 |
| Confidence | ⭐⭐ Low |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Trastuzumab may treat HER2 positive breast carcinoma based on embedding similarity.

---

### Path #2: heart failure

**Path:**
```
[Trastuzumab] --(0.763)--> [Dasatinib] --(0.535)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6492 |
| Combined Score | 0.4591 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Trastuzumab is similar to Dasatinib, which is associated with heart failure. This suggests shared therapeutic mechanisms.

---

### Path #3: blast phase chronic myelogenous leukemia, BCR-ABL1 positive

**Path:**
```
[Trastuzumab] --(0.763)--> [Dasatinib] --(0.535)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6492 |
| Combined Score | 0.4591 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Trastuzumab is similar to Dasatinib, which is associated with blast phase chronic myelogenous leukemia, BCR-ABL1 positive. This suggests shared therapeutic mechanisms.

---

### Path #4: active peptic ulcer disease

**Path:**
```
[Trastuzumab] --(0.763)--> [Dasatinib] --(0.535)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6492 |
| Combined Score | 0.4590 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Trastuzumab is similar to Dasatinib, which is associated with active peptic ulcer disease. This suggests shared therapeutic mechanisms.

---

### Path #5: intracerebral hemorrhage

**Path:**
```
[Trastuzumab] --(0.763)--> [Dasatinib] --(0.529)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6462 |
| Combined Score | 0.4569 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Trastuzumab is similar to Dasatinib, which is associated with intracerebral hemorrhage. This suggests shared therapeutic mechanisms.

---

### Path #6: coronary thrombosis

**Path:**
```
[Trastuzumab] --(0.763)--> [Dasatinib] --(0.528)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6456 |
| Combined Score | 0.4565 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Trastuzumab is similar to Dasatinib, which is associated with coronary thrombosis. This suggests shared therapeutic mechanisms.

---

### Path #7: liver disease

**Path:**
```
[Trastuzumab] --(0.763)--> [Dasatinib] --(0.525)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6442 |
| Combined Score | 0.4555 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Trastuzumab is similar to Dasatinib, which is associated with liver disease. This suggests shared therapeutic mechanisms.

---

### Path #8: neutropenia

**Path:**
```
[Trastuzumab] --(0.763)--> [Dasatinib] --(0.525)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6438 |
| Combined Score | 0.4552 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Trastuzumab is similar to Dasatinib, which is associated with neutropenia. This suggests shared therapeutic mechanisms.

---

### Path #9: congestive heart failure

**Path:**
```
[Trastuzumab] --(0.763)--> [Dasatinib] --(0.524)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6434 |
| Combined Score | 0.4550 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Trastuzumab is similar to Dasatinib, which is associated with congestive heart failure. This suggests shared therapeutic mechanisms.

---

### Path #10: macrocytic anemia (disease)

**Path:**
```
[Trastuzumab] --(0.763)--> [Dasatinib] --(0.517)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6401 |
| Combined Score | 0.4526 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Trastuzumab is similar to Dasatinib, which is associated with macrocytic anemia (disease). This suggests shared therapeutic mechanisms.

---

### Path #11: myocardial infarction (disease)

**Path:**
```
[Trastuzumab] --(0.763)--> [Dasatinib] --(0.515)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6391 |
| Combined Score | 0.4519 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Trastuzumab is similar to Dasatinib, which is associated with myocardial infarction (disease). This suggests shared therapeutic mechanisms.

---

### Path #12: myocardial infarction

**Path:**
```
[Trastuzumab] --(0.763)--> [Dasatinib] --(0.515)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6388 |
| Combined Score | 0.4517 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Trastuzumab is similar to Dasatinib, which is associated with myocardial infarction. This suggests shared therapeutic mechanisms.

---

### Path #13: pericardial effusion (disease)

**Path:**
```
[Trastuzumab] --(0.763)--> [Dasatinib] --(0.508)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6357 |
| Combined Score | 0.4495 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Trastuzumab is similar to Dasatinib, which is associated with pericardial effusion (disease). This suggests shared therapeutic mechanisms.

---

### Path #14: familial long QT syndrome

**Path:**
```
[Trastuzumab] --(0.763)--> [Dasatinib] --(0.507)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6350 |
| Combined Score | 0.4490 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Trastuzumab is similar to Dasatinib, which is associated with familial long QT syndrome. This suggests shared therapeutic mechanisms.

---

### Path #15: long QT syndrome

**Path:**
```
[Trastuzumab] --(0.763)--> [Dasatinib] --(0.506)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6347 |
| Combined Score | 0.4488 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Trastuzumab is similar to Dasatinib, which is associated with long QT syndrome. This suggests shared therapeutic mechanisms.

---

### Path #16: gallbladder disease

**Path:**
```
[Trastuzumab] --(0.763)--> [Dasatinib] --(0.505)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6341 |
| Combined Score | 0.4484 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Trastuzumab is similar to Dasatinib, which is associated with gallbladder disease. This suggests shared therapeutic mechanisms.

---

### Path #17: thrombocytopenia

**Path:**
```
[Trastuzumab] --(0.763)--> [Dasatinib] --(0.505)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6340 |
| Combined Score | 0.4483 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Trastuzumab is similar to Dasatinib, which is associated with thrombocytopenia. This suggests shared therapeutic mechanisms.

---

### Path #18: torsades de pointes

**Path:**
```
[Trastuzumab] --(0.763)--> [Dasatinib] --(0.501)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6321 |
| Combined Score | 0.4469 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Trastuzumab is similar to Dasatinib, which is associated with torsades de pointes. This suggests shared therapeutic mechanisms.

---

### Path #19: hemoglobinopathy

**Path:**
```
[Trastuzumab] --(0.763)--> [Dasatinib] --(0.501)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6320 |
| Combined Score | 0.4469 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Trastuzumab is similar to Dasatinib, which is associated with hemoglobinopathy. This suggests shared therapeutic mechanisms.

---

### Path #20: chronic myelogenous leukemia, BCR-ABL1 positive

**Path:**
```
[Trastuzumab] --(0.763)--> [Dasatinib] --(0.500)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6316 |
| Combined Score | 0.4466 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Trastuzumab is similar to Dasatinib, which is associated with chronic myelogenous leukemia, BCR-ABL1 positive. This suggests shared therapeutic mechanisms.

---

## 5. Interpretation Guidelines

### Attention Score Scale

| Score Range | Confidence | Interpretation |
|-------------|------------|----------------|
| ≥ 0.70 | ⭐⭐⭐⭐⭐ Very High | Strong biological relationship |
| 0.60 - 0.70 | ⭐⭐⭐⭐ High | Good evidence for connection |
| 0.50 - 0.60 | ⭐⭐⭐ Medium | Moderate support |
| 0.40 - 0.50 | ⭐⭐ Low | Weak connection |
| < 0.40 | ⭐ Very Low | Speculative |

### How to Use This Report

1. **Prioritize high-scoring paths**: Focus on paths with combined scores > 0.45
2. **Validate intermediate nodes**: Cross-reference proteins/drugs with literature
3. **Consider path length**: Shorter paths (2-3 hops) are generally more reliable
4. **Check for known associations**: Some paths may represent known indications

---

*Report generated by TxGNN Path Analysis Pipeline*