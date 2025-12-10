# 🔬 Panitumumab Path Analysis Report

*Generated: 2025-12-07 14:00:25*

## 1. Drug Profile

| Property | Value |
|----------|-------|
| **Drug ID** | DB01269 |
| **Drug Name** | Panitumumab |
| **Type** | drug |

## 2. Path Statistics

| Metric | Value |
|--------|-------|
| **Total Paths** | 100 |
| **Unique Diseases** | 48 |
| **Mean Attention** | 0.5895 |
| **Std Attention** | 0.0634 |
| **Min Attention** | 0.4718 |
| **Max Attention** | 0.7307 |

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
| Chlorotrianisene | 0.6073 | 82 |
| Estradiol | 0.5975 | 13 |
| Conjugated estrogens | 0.5884 | 2 |
| Tibolone | 0.5872 | 2 |

## 4. Top 20 Paths (by Combined Score)

### Path #1: metastatic malignant neoplasm in the colon

**Path:**
```
[Panitumumab] --(0.487)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.4866 |
| Combined Score | 0.4866 |
| Confidence | ⭐⭐ Low |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Panitumumab may treat metastatic malignant neoplasm in the colon based on embedding similarity.

---

### Path #2: ovarian carcinosarcoma

**Path:**
```
[Panitumumab] --(0.607)--> [Chlorotrianisene] --(0.540)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.5738 |
| Combined Score | 0.4057 |
| Confidence | ⭐⭐⭐ Medium |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Panitumumab is similar to Chlorotrianisene, which is associated with ovarian carcinosarcoma. This suggests shared therapeutic mechanisms.

---

### Path #3: ovarian carcinosarcoma

**Path:**
```
[Panitumumab] --(0.607)--> [Chlorotrianisene] --(0.540)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.5738 |
| Combined Score | 0.4057 |
| Confidence | ⭐⭐⭐ Medium |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Panitumumab is similar to Chlorotrianisene, which is associated with ovarian carcinosarcoma. This suggests shared therapeutic mechanisms.

---

### Path #4: uterine corpus leiomyoma

**Path:**
```
[Panitumumab] --(0.607)--> [Chlorotrianisene] --(0.538)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.5727 |
| Combined Score | 0.4050 |
| Confidence | ⭐⭐⭐ Medium |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Panitumumab is similar to Chlorotrianisene, which is associated with uterine corpus leiomyoma. This suggests shared therapeutic mechanisms.

---

### Path #5: uterine corpus leiomyoma

**Path:**
```
[Panitumumab] --(0.607)--> [Chlorotrianisene] --(0.538)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.5727 |
| Combined Score | 0.4050 |
| Confidence | ⭐⭐⭐ Medium |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Panitumumab is similar to Chlorotrianisene, which is associated with uterine corpus leiomyoma. This suggests shared therapeutic mechanisms.

---

### Path #6: maligant granulosa cell tumor of ovary

**Path:**
```
[Panitumumab] --(0.607)--> [Chlorotrianisene] --(0.537)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.5723 |
| Combined Score | 0.4047 |
| Confidence | ⭐⭐⭐ Medium |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Panitumumab is similar to Chlorotrianisene, which is associated with maligant granulosa cell tumor of ovary. This suggests shared therapeutic mechanisms.

---

### Path #7: maligant granulosa cell tumor of ovary

**Path:**
```
[Panitumumab] --(0.607)--> [Chlorotrianisene] --(0.537)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.5723 |
| Combined Score | 0.4047 |
| Confidence | ⭐⭐⭐ Medium |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Panitumumab is similar to Chlorotrianisene, which is associated with maligant granulosa cell tumor of ovary. This suggests shared therapeutic mechanisms.

---

### Path #8: cerebral infarction

**Path:**
```
[Panitumumab] --(0.607)--> [Chlorotrianisene] --(0.537)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.5721 |
| Combined Score | 0.4045 |
| Confidence | ⭐⭐⭐ Medium |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Panitumumab is similar to Chlorotrianisene, which is associated with cerebral infarction. This suggests shared therapeutic mechanisms.

---

### Path #9: cerebral infarction

**Path:**
```
[Panitumumab] --(0.607)--> [Chlorotrianisene] --(0.537)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.5721 |
| Combined Score | 0.4045 |
| Confidence | ⭐⭐⭐ Medium |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Panitumumab is similar to Chlorotrianisene, which is associated with cerebral infarction. This suggests shared therapeutic mechanisms.

---

### Path #10: intrinsic asthma

**Path:**
```
[Panitumumab] --(0.607)--> [Chlorotrianisene] --(0.536)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.5715 |
| Combined Score | 0.4041 |
| Confidence | ⭐⭐⭐ Medium |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Panitumumab is similar to Chlorotrianisene, which is associated with intrinsic asthma. This suggests shared therapeutic mechanisms.

---

### Path #11: intrinsic asthma

**Path:**
```
[Panitumumab] --(0.607)--> [Chlorotrianisene] --(0.536)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.5715 |
| Combined Score | 0.4041 |
| Confidence | ⭐⭐⭐ Medium |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Panitumumab is similar to Chlorotrianisene, which is associated with intrinsic asthma. This suggests shared therapeutic mechanisms.

---

### Path #12: psychologic dyspareunia

**Path:**
```
[Panitumumab] --(0.588)--> [Conjugated estrogens] --(0.554)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.5714 |
| Combined Score | 0.4040 |
| Confidence | ⭐⭐⭐ Medium |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Panitumumab is similar to Conjugated estrogens, which is associated with psychologic dyspareunia. This suggests shared therapeutic mechanisms.

---

### Path #13: psychologic dyspareunia

**Path:**
```
[Panitumumab] --(0.588)--> [Conjugated estrogens] --(0.554)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.5714 |
| Combined Score | 0.4040 |
| Confidence | ⭐⭐⭐ Medium |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Panitumumab is similar to Conjugated estrogens, which is associated with psychologic dyspareunia. This suggests shared therapeutic mechanisms.

---

### Path #14: migraine with or without aura, susceptibility to

**Path:**
```
[Panitumumab] --(0.607)--> [Chlorotrianisene] --(0.535)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.5712 |
| Combined Score | 0.4039 |
| Confidence | ⭐⭐⭐ Medium |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Panitumumab is similar to Chlorotrianisene, which is associated with migraine with or without aura, susceptibility to. This suggests shared therapeutic mechanisms.

---

### Path #15: migraine with or without aura, susceptibility to

**Path:**
```
[Panitumumab] --(0.607)--> [Chlorotrianisene] --(0.535)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.5712 |
| Combined Score | 0.4039 |
| Confidence | ⭐⭐⭐ Medium |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Panitumumab is similar to Chlorotrianisene, which is associated with migraine with or without aura, susceptibility to. This suggests shared therapeutic mechanisms.

---

### Path #16: endometrium neoplasm

**Path:**
```
[Panitumumab] --(0.607)--> [Chlorotrianisene] --(0.535)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.5713 |
| Combined Score | 0.4039 |
| Confidence | ⭐⭐⭐ Medium |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Panitumumab is similar to Chlorotrianisene, which is associated with endometrium neoplasm. This suggests shared therapeutic mechanisms.

---

### Path #17: endometrium neoplasm

**Path:**
```
[Panitumumab] --(0.607)--> [Chlorotrianisene] --(0.535)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.5713 |
| Combined Score | 0.4039 |
| Confidence | ⭐⭐⭐ Medium |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Panitumumab is similar to Chlorotrianisene, which is associated with endometrium neoplasm. This suggests shared therapeutic mechanisms.

---

### Path #18: postmenopausal osteoporosis

**Path:**
```
[Panitumumab] --(0.587)--> [Tibolone] --(0.555)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.5710 |
| Combined Score | 0.4038 |
| Confidence | ⭐⭐⭐ Medium |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Panitumumab is similar to Tibolone, which is associated with postmenopausal osteoporosis. This suggests shared therapeutic mechanisms.

---

### Path #19: obsolete susceptibility to ischemic stroke

**Path:**
```
[Panitumumab] --(0.607)--> [Chlorotrianisene] --(0.534)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.5708 |
| Combined Score | 0.4037 |
| Confidence | ⭐⭐⭐ Medium |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Panitumumab is similar to Chlorotrianisene, which is associated with obsolete susceptibility to ischemic stroke. This suggests shared therapeutic mechanisms.

---

### Path #20: obsolete susceptibility to ischemic stroke

**Path:**
```
[Panitumumab] --(0.607)--> [Chlorotrianisene] --(0.534)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.5708 |
| Combined Score | 0.4037 |
| Confidence | ⭐⭐⭐ Medium |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Panitumumab is similar to Chlorotrianisene, which is associated with obsolete susceptibility to ischemic stroke. This suggests shared therapeutic mechanisms.

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