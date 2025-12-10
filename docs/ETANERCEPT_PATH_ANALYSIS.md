# 🔬 Etanercept Path Analysis Report

*Generated: 2025-12-07 14:00:25*

## 1. Drug Profile

| Property | Value |
|----------|-------|
| **Drug ID** | DB00005 |
| **Drug Name** | Etanercept |
| **Type** | drug |

## 2. Path Statistics

| Metric | Value |
|--------|-------|
| **Total Paths** | 100 |
| **Unique Diseases** | 85 |
| **Mean Attention** | 0.5746 |
| **Std Attention** | 0.0710 |
| **Min Attention** | 0.4544 |
| **Max Attention** | 0.7733 |

### Paths by Hop Count

| Hops | Count |
|------|-------|
| 1 | 7 |
| 2 | 400 |
| 3 | 400 |
| 4 | 400 |
| 5 | 400 |

## 3. Path Type Summary

| Path Type | Count | Description |
|-----------|-------|-------------|
| Drug Similarity | 93 | Paths through similar drugs |
| Protein Target | 0 | Paths through protein targets |
| Pathway | 0 | Paths through biological pathways |
| Biological Process | 0 | Paths through biological processes |
| Other | 7 | Other connection types |

### Key Similar Drugs

| Similar Drug | Max Attention | # Diseases |
|--------------|---------------|------------|
| Vorapaxar | 0.7271 | 6 |
| Dasatinib | 0.7034 | 21 |
| Ibrutinib | 0.6994 | 6 |
| Estradiol | 0.6967 | 33 |
| Pentoxifylline | 0.6787 | 3 |
| Tipranavir | 0.6595 | 12 |
| Conjugated estrogens | 0.6476 | 1 |
| Diethylstilbestrol | 0.6256 | 11 |

## 4. Top 20 Paths (by Combined Score)

### Path #1: juvenile idiopathic arthritis

**Path:**
```
[Etanercept] --(0.508)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.5083 |
| Combined Score | 0.5083 |
| Confidence | ⭐⭐⭐ Medium |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Etanercept may treat juvenile idiopathic arthritis based on embedding similarity.

---

### Path #2: psoriatic arthritis

**Path:**
```
[Etanercept] --(0.497)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.4974 |
| Combined Score | 0.4974 |
| Confidence | ⭐⭐ Low |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Etanercept may treat psoriatic arthritis based on embedding similarity.

---

### Path #3: spondyloarthropathy

**Path:**
```
[Etanercept] --(0.496)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.4962 |
| Combined Score | 0.4962 |
| Confidence | ⭐⭐ Low |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Etanercept may treat spondyloarthropathy based on embedding similarity.

---

### Path #4: ankylosing spondylitis

**Path:**
```
[Etanercept] --(0.493)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.4933 |
| Combined Score | 0.4933 |
| Confidence | ⭐⭐ Low |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Etanercept may treat ankylosing spondylitis based on embedding similarity.

---

### Path #5: rheumatoid arthritis

**Path:**
```
[Etanercept] --(0.487)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.4868 |
| Combined Score | 0.4868 |
| Confidence | ⭐⭐ Low |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Etanercept may treat rheumatoid arthritis based on embedding similarity.

---

### Path #6: spondyloarthropathy, susceptibility to

**Path:**
```
[Etanercept] --(0.483)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.4830 |
| Combined Score | 0.4830 |
| Confidence | ⭐⭐ Low |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Etanercept may treat spondyloarthropathy, susceptibility to based on embedding similarity.

---

### Path #7: juvenile arthritis due to defect in LACC1

**Path:**
```
[Etanercept] --(0.454)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.4544 |
| Combined Score | 0.4544 |
| Confidence | ⭐⭐ Low |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Etanercept may treat juvenile arthritis due to defect in LACC1 based on embedding similarity.

---

### Path #8: macroglobulinemia

**Path:**
```
[Etanercept] --(0.699)--> [Ibrutinib] --(0.551)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6254 |
| Combined Score | 0.4422 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Etanercept is similar to Ibrutinib, which is associated with macroglobulinemia. This suggests shared therapeutic mechanisms.

---

### Path #9: heart failure

**Path:**
```
[Etanercept] --(0.703)--> [Dasatinib] --(0.535)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6194 |
| Combined Score | 0.4380 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Etanercept is similar to Dasatinib, which is associated with heart failure. This suggests shared therapeutic mechanisms.

---

### Path #10: blast phase chronic myelogenous leukemia, BCR-ABL1 positive

**Path:**
```
[Etanercept] --(0.703)--> [Dasatinib] --(0.535)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6194 |
| Combined Score | 0.4380 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Etanercept is similar to Dasatinib, which is associated with blast phase chronic myelogenous leukemia, BCR-ABL1 positive. This suggests shared therapeutic mechanisms.

---

### Path #11: lymphoplasmacytic lymphoma

**Path:**
```
[Etanercept] --(0.699)--> [Ibrutinib] --(0.539)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6194 |
| Combined Score | 0.4380 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Etanercept is similar to Ibrutinib, which is associated with lymphoplasmacytic lymphoma. This suggests shared therapeutic mechanisms.

---

### Path #12: active peptic ulcer disease

**Path:**
```
[Etanercept] --(0.703)--> [Dasatinib] --(0.535)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6194 |
| Combined Score | 0.4379 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Etanercept is similar to Dasatinib, which is associated with active peptic ulcer disease. This suggests shared therapeutic mechanisms.

---

### Path #13: intracerebral hemorrhage

**Path:**
```
[Etanercept] --(0.703)--> [Dasatinib] --(0.529)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6163 |
| Combined Score | 0.4358 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Etanercept is similar to Dasatinib, which is associated with intracerebral hemorrhage. This suggests shared therapeutic mechanisms.

---

### Path #14: coronary thrombosis

**Path:**
```
[Etanercept] --(0.703)--> [Dasatinib] --(0.528)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6158 |
| Combined Score | 0.4354 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Etanercept is similar to Dasatinib, which is associated with coronary thrombosis. This suggests shared therapeutic mechanisms.

---

### Path #15: liver disease

**Path:**
```
[Etanercept] --(0.703)--> [Dasatinib] --(0.525)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6144 |
| Combined Score | 0.4344 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Etanercept is similar to Dasatinib, which is associated with liver disease. This suggests shared therapeutic mechanisms.

---

### Path #16: cerebral infarction

**Path:**
```
[Etanercept] --(0.727)--> [Vorapaxar] --(0.501)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6143 |
| Combined Score | 0.4344 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Etanercept is similar to Vorapaxar, which is associated with cerebral infarction. This suggests shared therapeutic mechanisms.

---

### Path #17: neutropenia

**Path:**
```
[Etanercept] --(0.703)--> [Dasatinib] --(0.525)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6140 |
| Combined Score | 0.4342 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Etanercept is similar to Dasatinib, which is associated with neutropenia. This suggests shared therapeutic mechanisms.

---

### Path #18: intracerebral hemorrhage

**Path:**
```
[Etanercept] --(0.727)--> [Vorapaxar] --(0.500)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6138 |
| Combined Score | 0.4340 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Etanercept is similar to Vorapaxar, which is associated with intracerebral hemorrhage. This suggests shared therapeutic mechanisms.

---

### Path #19: congestive heart failure

**Path:**
```
[Etanercept] --(0.703)--> [Dasatinib] --(0.524)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6136 |
| Combined Score | 0.4339 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Etanercept is similar to Dasatinib, which is associated with congestive heart failure. This suggests shared therapeutic mechanisms.

---

### Path #20: transient ischemic attack (disease)

**Path:**
```
[Etanercept] --(0.727)--> [Vorapaxar] --(0.499)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6129 |
| Combined Score | 0.4334 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Etanercept is similar to Vorapaxar, which is associated with transient ischemic attack (disease). This suggests shared therapeutic mechanisms.

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