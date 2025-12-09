# 🔬 Teprotumumab Path Analysis Report

*Generated: 2025-12-07 14:00:25*

## 1. Drug Profile

| Property | Value |
|----------|-------|
| **Drug ID** | DB06343 |
| **Drug Name** | Teprotumumab |
| **Type** | drug |

## 2. Path Statistics

| Metric | Value |
|--------|-------|
| **Total Paths** | 100 |
| **Unique Diseases** | 79 |
| **Mean Attention** | 0.5873 |
| **Std Attention** | 0.0621 |
| **Min Attention** | 0.4743 |
| **Max Attention** | 0.7504 |

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
| Tibolone | 0.8928 | 2 |
| Mestranol | 0.8541 | 47 |
| Ethinylestradiol | 0.8109 | 38 |
| Chlorotrianisene | 0.7929 | 12 |

## 4. Top 20 Paths (by Combined Score)

### Path #1: endocrine exophthalmos

**Path:**
```
[Teprotumumab] --(0.529)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.5289 |
| Combined Score | 0.5289 |
| Confidence | ⭐⭐⭐ Medium |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Teprotumumab may treat endocrine exophthalmos based on embedding similarity.

---

### Path #2: postmenopausal osteoporosis

**Path:**
```
[Teprotumumab] --(0.893)--> [Tibolone] --(0.555)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.7238 |
| Combined Score | 0.5118 |
| Confidence | ⭐⭐⭐⭐⭐ Very High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Teprotumumab is similar to Tibolone, which is associated with postmenopausal osteoporosis. This suggests shared therapeutic mechanisms.

---

### Path #3: osteoporosis

**Path:**
```
[Teprotumumab] --(0.893)--> [Tibolone] --(0.535)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.7137 |
| Combined Score | 0.5047 |
| Confidence | ⭐⭐⭐⭐⭐ Very High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Teprotumumab is similar to Tibolone, which is associated with osteoporosis. This suggests shared therapeutic mechanisms.

---

### Path #4: benign mammary dysplasia

**Path:**
```
[Teprotumumab] --(0.854)--> [Mestranol] --(0.539)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6967 |
| Combined Score | 0.4926 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Teprotumumab is similar to Mestranol, which is associated with benign mammary dysplasia. This suggests shared therapeutic mechanisms.

---

### Path #5: neurotic disorder

**Path:**
```
[Teprotumumab] --(0.854)--> [Mestranol] --(0.538)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6963 |
| Combined Score | 0.4924 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Teprotumumab is similar to Mestranol, which is associated with neurotic disorder. This suggests shared therapeutic mechanisms.

---

### Path #6: obsolete susceptibility to ischemic stroke

**Path:**
```
[Teprotumumab] --(0.854)--> [Mestranol] --(0.539)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6964 |
| Combined Score | 0.4924 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Teprotumumab is similar to Mestranol, which is associated with obsolete susceptibility to ischemic stroke. This suggests shared therapeutic mechanisms.

---

### Path #7: cervical carcinosarcoma

**Path:**
```
[Teprotumumab] --(0.854)--> [Mestranol] --(0.538)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6963 |
| Combined Score | 0.4923 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Teprotumumab is similar to Mestranol, which is associated with cervical carcinosarcoma. This suggests shared therapeutic mechanisms.

---

### Path #8: migraine with or without aura, susceptibility to

**Path:**
```
[Teprotumumab] --(0.854)--> [Mestranol] --(0.538)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6959 |
| Combined Score | 0.4921 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Teprotumumab is similar to Mestranol, which is associated with migraine with or without aura, susceptibility to. This suggests shared therapeutic mechanisms.

---

### Path #9: cerebral infarction

**Path:**
```
[Teprotumumab] --(0.854)--> [Mestranol] --(0.537)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6957 |
| Combined Score | 0.4920 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Teprotumumab is similar to Mestranol, which is associated with cerebral infarction. This suggests shared therapeutic mechanisms.

---

### Path #10: biliary tract disease

**Path:**
```
[Teprotumumab] --(0.854)--> [Mestranol] --(0.537)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6953 |
| Combined Score | 0.4917 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Teprotumumab is similar to Mestranol, which is associated with biliary tract disease. This suggests shared therapeutic mechanisms.

---

### Path #11: obstructive jaundice

**Path:**
```
[Teprotumumab] --(0.854)--> [Mestranol] --(0.536)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6949 |
| Combined Score | 0.4914 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Teprotumumab is similar to Mestranol, which is associated with obstructive jaundice. This suggests shared therapeutic mechanisms.

---

### Path #12: endometrium neoplasm

**Path:**
```
[Teprotumumab] --(0.854)--> [Mestranol] --(0.535)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6946 |
| Combined Score | 0.4912 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Teprotumumab is similar to Mestranol, which is associated with endometrium neoplasm. This suggests shared therapeutic mechanisms.

---

### Path #13: stroke disorder

**Path:**
```
[Teprotumumab] --(0.854)--> [Mestranol] --(0.535)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6946 |
| Combined Score | 0.4912 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Teprotumumab is similar to Mestranol, which is associated with stroke disorder. This suggests shared therapeutic mechanisms.

---

### Path #14: coronary artery disease

**Path:**
```
[Teprotumumab] --(0.854)--> [Mestranol] --(0.533)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6938 |
| Combined Score | 0.4906 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Teprotumumab is similar to Mestranol, which is associated with coronary artery disease. This suggests shared therapeutic mechanisms.

---

### Path #15: hypertensive disorder

**Path:**
```
[Teprotumumab] --(0.854)--> [Mestranol] --(0.523)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6884 |
| Combined Score | 0.4868 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Teprotumumab is similar to Mestranol, which is associated with hypertensive disorder. This suggests shared therapeutic mechanisms.

---

### Path #16: cholestasis, intrahepatic, of pregnancy

**Path:**
```
[Teprotumumab] --(0.854)--> [Mestranol] --(0.518)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6862 |
| Combined Score | 0.4852 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Teprotumumab is similar to Mestranol, which is associated with cholestasis, intrahepatic, of pregnancy. This suggests shared therapeutic mechanisms.

---

### Path #17: endometriosis of uterus

**Path:**
```
[Teprotumumab] --(0.854)--> [Mestranol] --(0.518)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6861 |
| Combined Score | 0.4851 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Teprotumumab is similar to Mestranol, which is associated with endometriosis of uterus. This suggests shared therapeutic mechanisms.

---

### Path #18: diabetes mellitus (disease)

**Path:**
```
[Teprotumumab] --(0.854)--> [Mestranol] --(0.517)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6853 |
| Combined Score | 0.4846 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Teprotumumab is similar to Mestranol, which is associated with diabetes mellitus (disease). This suggests shared therapeutic mechanisms.

---

### Path #19: inherited porphyria

**Path:**
```
[Teprotumumab] --(0.854)--> [Mestranol] --(0.516)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6851 |
| Combined Score | 0.4844 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Teprotumumab is similar to Mestranol, which is associated with inherited porphyria. This suggests shared therapeutic mechanisms.

---

### Path #20: hyperlipidemia

**Path:**
```
[Teprotumumab] --(0.854)--> [Mestranol] --(0.515)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6847 |
| Combined Score | 0.4842 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Teprotumumab is similar to Mestranol, which is associated with hyperlipidemia. This suggests shared therapeutic mechanisms.

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