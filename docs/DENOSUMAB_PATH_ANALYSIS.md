# 🔬 Denosumab Path Analysis Report

*Generated: 2025-12-07 14:00:25*

## 1. Drug Profile

| Property | Value |
|----------|-------|
| **Drug ID** | DB06643 |
| **Drug Name** | Denosumab |
| **Type** | drug |

## 2. Path Statistics

| Metric | Value |
|--------|-------|
| **Total Paths** | 100 |
| **Unique Diseases** | 78 |
| **Mean Attention** | 0.6262 |
| **Std Attention** | 0.0527 |
| **Min Attention** | 0.4792 |
| **Max Attention** | 0.7706 |

### Paths by Hop Count

| Hops | Count |
|------|-------|
| 1 | 3 |
| 2 | 400 |
| 3 | 400 |
| 4 | 400 |
| 5 | 400 |

## 3. Path Type Summary

| Path Type | Count | Description |
|-----------|-------|-------------|
| Drug Similarity | 97 | Paths through similar drugs |
| Protein Target | 0 | Paths through protein targets |
| Pathway | 0 | Paths through biological pathways |
| Biological Process | 0 | Paths through biological processes |
| Other | 3 | Other connection types |

### Key Similar Drugs

| Similar Drug | Max Attention | # Diseases |
|--------------|---------------|------------|
| Tibolone | 0.9354 | 2 |
| Mestranol | 0.8867 | 32 |
| Dasatinib | 0.8816 | 21 |
| Ibrutinib | 0.8546 | 3 |
| Ethinylestradiol | 0.8458 | 15 |
| Chlorotrianisene | 0.8456 | 24 |

## 4. Top 20 Paths (by Combined Score)

### Path #1: drug-induced osteoporosis

**Path:**
```
[Denosumab] --(0.532)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.5319 |
| Combined Score | 0.5319 |
| Confidence | ⭐⭐⭐ Medium |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Denosumab may treat drug-induced osteoporosis based on embedding similarity.

---

### Path #2: postmenopausal osteoporosis

**Path:**
```
[Denosumab] --(0.935)--> [Tibolone] --(0.555)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.7451 |
| Combined Score | 0.5269 |
| Confidence | ⭐⭐⭐⭐⭐ Very High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Denosumab is similar to Tibolone, which is associated with postmenopausal osteoporosis. This suggests shared therapeutic mechanisms.

---

### Path #3: postmenopausal osteoporosis

**Path:**
```
[Denosumab] --(0.525)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.5251 |
| Combined Score | 0.5251 |
| Confidence | ⭐⭐⭐ Medium |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Denosumab may treat postmenopausal osteoporosis based on embedding similarity.

---

### Path #4: osteoporosis

**Path:**
```
[Denosumab] --(0.935)--> [Tibolone] --(0.535)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.7350 |
| Combined Score | 0.5198 |
| Confidence | ⭐⭐⭐⭐⭐ Very High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Denosumab is similar to Tibolone, which is associated with osteoporosis. This suggests shared therapeutic mechanisms.

---

### Path #5: osteoporosis

**Path:**
```
[Denosumab] --(0.511)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.5114 |
| Combined Score | 0.5114 |
| Confidence | ⭐⭐⭐ Medium |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Denosumab may treat osteoporosis based on embedding similarity.

---

### Path #6: obsolete susceptibility to ischemic stroke

**Path:**
```
[Denosumab] --(0.887)--> [Mestranol] --(0.539)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.7127 |
| Combined Score | 0.5040 |
| Confidence | ⭐⭐⭐⭐⭐ Very High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Denosumab is similar to Mestranol, which is associated with obsolete susceptibility to ischemic stroke. This suggests shared therapeutic mechanisms.

---

### Path #7: neurotic disorder

**Path:**
```
[Denosumab] --(0.887)--> [Mestranol] --(0.538)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.7126 |
| Combined Score | 0.5039 |
| Confidence | ⭐⭐⭐⭐⭐ Very High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Denosumab is similar to Mestranol, which is associated with neurotic disorder. This suggests shared therapeutic mechanisms.

---

### Path #8: migraine with or without aura, susceptibility to

**Path:**
```
[Denosumab] --(0.887)--> [Mestranol] --(0.538)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.7123 |
| Combined Score | 0.5036 |
| Confidence | ⭐⭐⭐⭐⭐ Very High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Denosumab is similar to Mestranol, which is associated with migraine with or without aura, susceptibility to. This suggests shared therapeutic mechanisms.

---

### Path #9: cerebral infarction

**Path:**
```
[Denosumab] --(0.887)--> [Mestranol] --(0.537)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.7121 |
| Combined Score | 0.5035 |
| Confidence | ⭐⭐⭐⭐⭐ Very High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Denosumab is similar to Mestranol, which is associated with cerebral infarction. This suggests shared therapeutic mechanisms.

---

### Path #10: endometrium neoplasm

**Path:**
```
[Denosumab] --(0.887)--> [Mestranol] --(0.535)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.7109 |
| Combined Score | 0.5027 |
| Confidence | ⭐⭐⭐⭐⭐ Very High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Denosumab is similar to Mestranol, which is associated with endometrium neoplasm. This suggests shared therapeutic mechanisms.

---

### Path #11: stroke disorder

**Path:**
```
[Denosumab] --(0.887)--> [Mestranol] --(0.535)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.7109 |
| Combined Score | 0.5027 |
| Confidence | ⭐⭐⭐⭐⭐ Very High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Denosumab is similar to Mestranol, which is associated with stroke disorder. This suggests shared therapeutic mechanisms.

---

### Path #12: coronary artery disease

**Path:**
```
[Denosumab] --(0.887)--> [Mestranol] --(0.533)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.7101 |
| Combined Score | 0.5021 |
| Confidence | ⭐⭐⭐⭐⭐ Very High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Denosumab is similar to Mestranol, which is associated with coronary artery disease. This suggests shared therapeutic mechanisms.

---

### Path #13: heart failure

**Path:**
```
[Denosumab] --(0.882)--> [Dasatinib] --(0.535)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.7085 |
| Combined Score | 0.5010 |
| Confidence | ⭐⭐⭐⭐⭐ Very High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Denosumab is similar to Dasatinib, which is associated with heart failure. This suggests shared therapeutic mechanisms.

---

### Path #14: blast phase chronic myelogenous leukemia, BCR-ABL1 positive

**Path:**
```
[Denosumab] --(0.882)--> [Dasatinib] --(0.535)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.7085 |
| Combined Score | 0.5010 |
| Confidence | ⭐⭐⭐⭐⭐ Very High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Denosumab is similar to Dasatinib, which is associated with blast phase chronic myelogenous leukemia, BCR-ABL1 positive. This suggests shared therapeutic mechanisms.

---

### Path #15: active peptic ulcer disease

**Path:**
```
[Denosumab] --(0.882)--> [Dasatinib] --(0.535)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.7085 |
| Combined Score | 0.5009 |
| Confidence | ⭐⭐⭐⭐⭐ Very High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Denosumab is similar to Dasatinib, which is associated with active peptic ulcer disease. This suggests shared therapeutic mechanisms.

---

### Path #16: intracerebral hemorrhage

**Path:**
```
[Denosumab] --(0.882)--> [Dasatinib] --(0.529)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.7055 |
| Combined Score | 0.4988 |
| Confidence | ⭐⭐⭐⭐⭐ Very High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Denosumab is similar to Dasatinib, which is associated with intracerebral hemorrhage. This suggests shared therapeutic mechanisms.

---

### Path #17: coronary thrombosis

**Path:**
```
[Denosumab] --(0.882)--> [Dasatinib] --(0.528)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.7048 |
| Combined Score | 0.4984 |
| Confidence | ⭐⭐⭐⭐⭐ Very High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Denosumab is similar to Dasatinib, which is associated with coronary thrombosis. This suggests shared therapeutic mechanisms.

---

### Path #18: hypertensive disorder

**Path:**
```
[Denosumab] --(0.887)--> [Mestranol] --(0.523)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.7047 |
| Combined Score | 0.4983 |
| Confidence | ⭐⭐⭐⭐⭐ Very High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Denosumab is similar to Mestranol, which is associated with hypertensive disorder. This suggests shared therapeutic mechanisms.

---

### Path #19: liver disease

**Path:**
```
[Denosumab] --(0.882)--> [Dasatinib] --(0.525)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.7035 |
| Combined Score | 0.4974 |
| Confidence | ⭐⭐⭐⭐⭐ Very High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Denosumab is similar to Dasatinib, which is associated with liver disease. This suggests shared therapeutic mechanisms.

---

### Path #20: neutropenia

**Path:**
```
[Denosumab] --(0.882)--> [Dasatinib] --(0.525)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.7031 |
| Combined Score | 0.4972 |
| Confidence | ⭐⭐⭐⭐⭐ Very High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Denosumab is similar to Dasatinib, which is associated with neutropenia. This suggests shared therapeutic mechanisms.

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