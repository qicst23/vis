# 🔬 Rituximab Path Analysis Report

*Generated: 2025-12-07 14:00:25*

## 1. Drug Profile

| Property | Value |
|----------|-------|
| **Drug ID** | DB00073 |
| **Drug Name** | Rituximab |
| **Type** | drug |

## 2. Path Statistics

| Metric | Value |
|--------|-------|
| **Total Paths** | 100 |
| **Unique Diseases** | 86 |
| **Mean Attention** | 0.5959 |
| **Std Attention** | 0.0763 |
| **Min Attention** | 0.4425 |
| **Max Attention** | 0.7466 |

### Paths by Hop Count

| Hops | Count |
|------|-------|
| 1 | 10 |
| 2 | 400 |
| 3 | 400 |
| 4 | 400 |
| 5 | 400 |

## 3. Path Type Summary

| Path Type | Count | Description |
|-----------|-------|-------------|
| Drug Similarity | 90 | Paths through similar drugs |
| Protein Target | 0 | Paths through protein targets |
| Pathway | 0 | Paths through biological pathways |
| Biological Process | 0 | Paths through biological processes |
| Other | 10 | Other connection types |

### Key Similar Drugs

| Similar Drug | Max Attention | # Diseases |
|--------------|---------------|------------|
| Pentosan polysulfate | 0.7925 | 7 |
| Vorapaxar | 0.7876 | 7 |
| Obinutuzumab | 0.7623 | 2 |
| Chlorotrianisene | 0.7222 | 58 |
| Mestranol | 0.7068 | 4 |
| Dasatinib | 0.7014 | 8 |
| Tibolone | 0.6912 | 2 |
| Conjugated estrogens | 0.6785 | 1 |
| Dabigatran etexilate | 0.6724 | 1 |

## 4. Top 20 Paths (by Combined Score)

### Path #1: non-Hodgkin lymphoma

**Path:**
```
[Rituximab] --(0.485)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.4848 |
| Combined Score | 0.4848 |
| Confidence | ⭐⭐ Low |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Rituximab may treat non-Hodgkin lymphoma based on embedding similarity.

---

### Path #2: Langerhans cell histiocytosis

**Path:**
```
[Rituximab] --(0.483)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.4831 |
| Combined Score | 0.4831 |
| Confidence | ⭐⭐ Low |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Rituximab may treat Langerhans cell histiocytosis based on embedding similarity.

---

### Path #3: lymphoma

**Path:**
```
[Rituximab] --(0.478)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.4781 |
| Combined Score | 0.4781 |
| Confidence | ⭐⭐ Low |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Rituximab may treat lymphoma based on embedding similarity.

---

### Path #4: lymphosarcoma

**Path:**
```
[Rituximab] --(0.473)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.4727 |
| Combined Score | 0.4727 |
| Confidence | ⭐⭐ Low |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Rituximab may treat lymphosarcoma based on embedding similarity.

---

### Path #5: B-cell neoplasm

**Path:**
```
[Rituximab] --(0.467)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.4673 |
| Combined Score | 0.4673 |
| Confidence | ⭐⭐ Low |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Rituximab may treat B-cell neoplasm based on embedding similarity.

---

### Path #6: acute lymphoblastic/lymphocytic leukemia

**Path:**
```
[Rituximab] --(0.458)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.4576 |
| Combined Score | 0.4576 |
| Confidence | ⭐⭐ Low |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Rituximab may treat acute lymphoblastic/lymphocytic leukemia based on embedding similarity.

---

### Path #7: lymphoma, non-Hodgkin, familial

**Path:**
```
[Rituximab] --(0.457)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.4572 |
| Combined Score | 0.4572 |
| Confidence | ⭐⭐ Low |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Rituximab may treat lymphoma, non-Hodgkin, familial based on embedding similarity.

---

### Path #8: Richter syndrome

**Path:**
```
[Rituximab] --(0.456)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.4561 |
| Combined Score | 0.4561 |
| Confidence | ⭐⭐ Low |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Rituximab may treat Richter syndrome based on embedding similarity.

---

### Path #9: cerebral infarction

**Path:**
```
[Rituximab] --(0.788)--> [Vorapaxar] --(0.501)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6445 |
| Combined Score | 0.4558 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Rituximab is similar to Vorapaxar, which is associated with cerebral infarction. This suggests shared therapeutic mechanisms.

---

### Path #10: mantle cell lymphoma

**Path:**
```
[Rituximab] --(0.456)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.4556 |
| Combined Score | 0.4556 |
| Confidence | ⭐⭐ Low |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Rituximab may treat mantle cell lymphoma based on embedding similarity.

---

### Path #11: intracerebral hemorrhage

**Path:**
```
[Rituximab] --(0.788)--> [Vorapaxar] --(0.500)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6441 |
| Combined Score | 0.4554 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Rituximab is similar to Vorapaxar, which is associated with intracerebral hemorrhage. This suggests shared therapeutic mechanisms.

---

### Path #12: transient ischemic attack (disease)

**Path:**
```
[Rituximab] --(0.788)--> [Vorapaxar] --(0.499)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6431 |
| Combined Score | 0.4548 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Rituximab is similar to Vorapaxar, which is associated with transient ischemic attack (disease). This suggests shared therapeutic mechanisms.

---

### Path #13: interstitial cystitis

**Path:**
```
[Rituximab] --(0.792)--> [Pentosan polysulfate] --(0.491)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6420 |
| Combined Score | 0.4539 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Rituximab is similar to Pentosan polysulfate, which is associated with interstitial cystitis. This suggests shared therapeutic mechanisms.

---

### Path #14: obsolete susceptibility to ischemic stroke

**Path:**
```
[Rituximab] --(0.788)--> [Vorapaxar] --(0.495)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6414 |
| Combined Score | 0.4535 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Rituximab is similar to Vorapaxar, which is associated with obsolete susceptibility to ischemic stroke. This suggests shared therapeutic mechanisms.

---

### Path #15: vertebrobasilar insufficiency

**Path:**
```
[Rituximab] --(0.788)--> [Vorapaxar] --(0.494)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6411 |
| Combined Score | 0.4533 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Rituximab is similar to Vorapaxar, which is associated with vertebrobasilar insufficiency. This suggests shared therapeutic mechanisms.

---

### Path #16: stroke disorder

**Path:**
```
[Rituximab] --(0.788)--> [Vorapaxar] --(0.493)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6405 |
| Combined Score | 0.4529 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Rituximab is similar to Vorapaxar, which is associated with stroke disorder. This suggests shared therapeutic mechanisms.

---

### Path #17: heparin-induced thrombocytopenia (disease)

**Path:**
```
[Rituximab] --(0.792)--> [Pentosan polysulfate] --(0.483)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6379 |
| Combined Score | 0.4511 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Rituximab is similar to Pentosan polysulfate, which is associated with heparin-induced thrombocytopenia (disease). This suggests shared therapeutic mechanisms.

---

### Path #18: gallbladder disease

**Path:**
```
[Rituximab] --(0.792)--> [Pentosan polysulfate] --(0.479)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6359 |
| Combined Score | 0.4496 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Rituximab is similar to Pentosan polysulfate, which is associated with gallbladder disease. This suggests shared therapeutic mechanisms.

---

### Path #19: liver disease

**Path:**
```
[Rituximab] --(0.792)--> [Pentosan polysulfate] --(0.475)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6339 |
| Combined Score | 0.4482 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Rituximab is similar to Pentosan polysulfate, which is associated with liver disease. This suggests shared therapeutic mechanisms.

---

### Path #20: ovarian carcinosarcoma

**Path:**
```
[Rituximab] --(0.722)--> [Chlorotrianisene] --(0.540)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6312 |
| Combined Score | 0.4464 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Rituximab is similar to Chlorotrianisene, which is associated with ovarian carcinosarcoma. This suggests shared therapeutic mechanisms.

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