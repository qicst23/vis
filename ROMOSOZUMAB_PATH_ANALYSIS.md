# 🔬 Romosozumab Path Analysis Report

*Generated: 2025-12-07 14:00:25*

## 1. Drug Profile

| Property | Value |
|----------|-------|
| **Drug ID** | DB11866 |
| **Drug Name** | Romosozumab |
| **Type** | drug |

## 2. Path Statistics

| Metric | Value |
|--------|-------|
| **Total Paths** | 100 |
| **Unique Diseases** | 86 |
| **Mean Attention** | 0.5889 |
| **Std Attention** | 0.0541 |
| **Min Attention** | 0.4813 |
| **Max Attention** | 0.7311 |

### Paths by Hop Count

| Hops | Count |
|------|-------|
| 1 | 5 |
| 2 | 400 |
| 3 | 400 |
| 4 | 400 |
| 5 | 400 |

## 3. Path Type Summary

| Path Type | Count | Description |
|-----------|-------|-------------|
| Drug Similarity | 95 | Paths through similar drugs |
| Protein Target | 0 | Paths through protein targets |
| Pathway | 0 | Paths through biological pathways |
| Biological Process | 0 | Paths through biological processes |
| Other | 5 | Other connection types |

### Key Similar Drugs

| Similar Drug | Max Attention | # Diseases |
|--------------|---------------|------------|
| Tibolone | 0.8347 | 2 |
| Diethylstilbestrol | 0.8210 | 79 |
| Ethinylestradiol | 0.7638 | 5 |
| Mestranol | 0.7573 | 7 |
| Chlorotrianisene | 0.7544 | 1 |
| Conjugated estrogens | 0.7401 | 1 |

## 4. Top 20 Paths (by Combined Score)

### Path #1: phosphorus metabolism disease

**Path:**
```
[Romosozumab] --(0.571)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.5705 |
| Combined Score | 0.5705 |
| Confidence | ⭐⭐⭐ Medium |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Romosozumab may treat phosphorus metabolism disease based on embedding similarity.

---

### Path #2: postmenopausal osteoporosis

**Path:**
```
[Romosozumab] --(0.568)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.5675 |
| Combined Score | 0.5675 |
| Confidence | ⭐⭐⭐ Medium |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Romosozumab may treat postmenopausal osteoporosis based on embedding similarity.

---

### Path #3: nephrocalcinosis

**Path:**
```
[Romosozumab] --(0.556)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.5559 |
| Combined Score | 0.5559 |
| Confidence | ⭐⭐⭐ Medium |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Romosozumab may treat nephrocalcinosis based on embedding similarity.

---

### Path #4: osteoporosis

**Path:**
```
[Romosozumab] --(0.555)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.5546 |
| Combined Score | 0.5546 |
| Confidence | ⭐⭐⭐ Medium |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Romosozumab may treat osteoporosis based on embedding similarity.

---

### Path #5: hypercalcemia disease

**Path:**
```
[Romosozumab] --(0.541)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.5412 |
| Combined Score | 0.5412 |
| Confidence | ⭐⭐⭐ Medium |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Romosozumab may treat hypercalcemia disease based on embedding similarity.

---

### Path #6: ovarian carcinosarcoma

**Path:**
```
[Romosozumab] --(0.821)--> [Diethylstilbestrol] --(0.577)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6988 |
| Combined Score | 0.4942 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Romosozumab is similar to Diethylstilbestrol, which is associated with ovarian carcinosarcoma. This suggests shared therapeutic mechanisms.

---

### Path #7: coronary artery disease

**Path:**
```
[Romosozumab] --(0.821)--> [Diethylstilbestrol] --(0.577)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6988 |
| Combined Score | 0.4941 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Romosozumab is similar to Diethylstilbestrol, which is associated with coronary artery disease. This suggests shared therapeutic mechanisms.

---

### Path #8: stroke disorder

**Path:**
```
[Romosozumab] --(0.821)--> [Diethylstilbestrol] --(0.575)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6978 |
| Combined Score | 0.4934 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Romosozumab is similar to Diethylstilbestrol, which is associated with stroke disorder. This suggests shared therapeutic mechanisms.

---

### Path #9: malignant dysgerminomatous germ cell tumor of ovary

**Path:**
```
[Romosozumab] --(0.821)--> [Diethylstilbestrol] --(0.574)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6976 |
| Combined Score | 0.4933 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Romosozumab is similar to Diethylstilbestrol, which is associated with malignant dysgerminomatous germ cell tumor of ovary. This suggests shared therapeutic mechanisms.

---

### Path #10: gallbladder disease

**Path:**
```
[Romosozumab] --(0.821)--> [Diethylstilbestrol] --(0.574)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6975 |
| Combined Score | 0.4932 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Romosozumab is similar to Diethylstilbestrol, which is associated with gallbladder disease. This suggests shared therapeutic mechanisms.

---

### Path #11: intrinsic asthma

**Path:**
```
[Romosozumab] --(0.821)--> [Diethylstilbestrol] --(0.574)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6973 |
| Combined Score | 0.4931 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Romosozumab is similar to Diethylstilbestrol, which is associated with intrinsic asthma. This suggests shared therapeutic mechanisms.

---

### Path #12: hypertriglyceridemia (disease)

**Path:**
```
[Romosozumab] --(0.821)--> [Diethylstilbestrol] --(0.574)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6973 |
| Combined Score | 0.4931 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Romosozumab is similar to Diethylstilbestrol, which is associated with hypertriglyceridemia (disease). This suggests shared therapeutic mechanisms.

---

### Path #13: myofibroma

**Path:**
```
[Romosozumab] --(0.821)--> [Diethylstilbestrol] --(0.574)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6972 |
| Combined Score | 0.4930 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Romosozumab is similar to Diethylstilbestrol, which is associated with myofibroma. This suggests shared therapeutic mechanisms.

---

### Path #14: uterine corpus leiomyoma

**Path:**
```
[Romosozumab] --(0.821)--> [Diethylstilbestrol] --(0.573)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6970 |
| Combined Score | 0.4929 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Romosozumab is similar to Diethylstilbestrol, which is associated with uterine corpus leiomyoma. This suggests shared therapeutic mechanisms.

---

### Path #15: hypothyroidism

**Path:**
```
[Romosozumab] --(0.821)--> [Diethylstilbestrol] --(0.572)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6963 |
| Combined Score | 0.4924 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Romosozumab is similar to Diethylstilbestrol, which is associated with hypothyroidism. This suggests shared therapeutic mechanisms.

---

### Path #16: obsolete susceptibility to ischemic stroke

**Path:**
```
[Romosozumab] --(0.821)--> [Diethylstilbestrol] --(0.572)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6964 |
| Combined Score | 0.4924 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Romosozumab is similar to Diethylstilbestrol, which is associated with obsolete susceptibility to ischemic stroke. This suggests shared therapeutic mechanisms.

---

### Path #17: endometrium neoplasm

**Path:**
```
[Romosozumab] --(0.821)--> [Diethylstilbestrol] --(0.571)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6961 |
| Combined Score | 0.4922 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Romosozumab is similar to Diethylstilbestrol, which is associated with endometrium neoplasm. This suggests shared therapeutic mechanisms.

---

### Path #18: myxedema

**Path:**
```
[Romosozumab] --(0.821)--> [Diethylstilbestrol] --(0.571)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6958 |
| Combined Score | 0.4920 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Romosozumab is similar to Diethylstilbestrol, which is associated with myxedema. This suggests shared therapeutic mechanisms.

---

### Path #19: ovarian small cell carcinoma

**Path:**
```
[Romosozumab] --(0.821)--> [Diethylstilbestrol] --(0.571)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6958 |
| Combined Score | 0.4920 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Romosozumab is similar to Diethylstilbestrol, which is associated with ovarian small cell carcinoma. This suggests shared therapeutic mechanisms.

---

### Path #20: dementia (disease)

**Path:**
```
[Romosozumab] --(0.821)--> [Diethylstilbestrol] --(0.571)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6958 |
| Combined Score | 0.4920 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Romosozumab is similar to Diethylstilbestrol, which is associated with dementia (disease). This suggests shared therapeutic mechanisms.

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