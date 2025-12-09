# 🔬 Evolocumab Path Analysis Report

*Generated: 2025-12-07 14:00:25*

## 1. Drug Profile

| Property | Value |
|----------|-------|
| **Drug ID** | DB09303 |
| **Drug Name** | Evolocumab |
| **Type** | drug |

## 2. Path Statistics

| Metric | Value |
|--------|-------|
| **Total Paths** | 100 |
| **Unique Diseases** | 84 |
| **Mean Attention** | 0.5646 |
| **Std Attention** | 0.0513 |
| **Min Attention** | 0.4589 |
| **Max Attention** | 0.7042 |

### Paths by Hop Count

| Hops | Count |
|------|-------|
| 1 | 2 |
| 2 | 400 |
| 3 | 400 |
| 4 | 400 |
| 5 | 400 |

## 3. Path Type Summary

| Path Type | Count | Description |
|-----------|-------|-------------|
| Drug Similarity | 98 | Paths through similar drugs |
| Protein Target | 0 | Paths through protein targets |
| Pathway | 0 | Paths through biological pathways |
| Biological Process | 0 | Paths through biological processes |
| Other | 2 | Other connection types |

### Key Similar Drugs

| Similar Drug | Max Attention | # Diseases |
|--------------|---------------|------------|
| Obinutuzumab | 0.7268 | 2 |
| Estradiol | 0.6932 | 51 |
| Chlorotrianisene | 0.6777 | 45 |

## 4. Top 20 Paths (by Combined Score)

### Path #1: homozygous familial hypercholesterolemia

**Path:**
```
[Evolocumab] --(0.465)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.4654 |
| Combined Score | 0.4654 |
| Confidence | ⭐⭐ Low |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Evolocumab may treat homozygous familial hypercholesterolemia based on embedding similarity.

---

### Path #2: syndromic dyslipidemia

**Path:**
```
[Evolocumab] --(0.459)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.4589 |
| Combined Score | 0.4589 |
| Confidence | ⭐⭐ Low |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Evolocumab may treat syndromic dyslipidemia based on embedding similarity.

---

### Path #3: inherited porphyria

**Path:**
```
[Evolocumab] --(0.693)--> [Estradiol] --(0.529)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6109 |
| Combined Score | 0.4320 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Evolocumab is similar to Estradiol, which is associated with inherited porphyria. This suggests shared therapeutic mechanisms.

---

### Path #4: myxedema

**Path:**
```
[Evolocumab] --(0.693)--> [Estradiol] --(0.526)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6098 |
| Combined Score | 0.4312 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Evolocumab is similar to Estradiol, which is associated with myxedema. This suggests shared therapeutic mechanisms.

---

### Path #5: intrinsic asthma

**Path:**
```
[Evolocumab] --(0.693)--> [Estradiol] --(0.526)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6096 |
| Combined Score | 0.4310 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Evolocumab is similar to Estradiol, which is associated with intrinsic asthma. This suggests shared therapeutic mechanisms.

---

### Path #6: liver failure

**Path:**
```
[Evolocumab] --(0.693)--> [Estradiol] --(0.525)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6094 |
| Combined Score | 0.4309 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Evolocumab is similar to Estradiol, which is associated with liver failure. This suggests shared therapeutic mechanisms.

---

### Path #7: anxiety disorder

**Path:**
```
[Evolocumab] --(0.693)--> [Estradiol] --(0.526)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6094 |
| Combined Score | 0.4309 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Evolocumab is similar to Estradiol, which is associated with anxiety disorder. This suggests shared therapeutic mechanisms.

---

### Path #8: hypothyroidism

**Path:**
```
[Evolocumab] --(0.693)--> [Estradiol] --(0.525)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6093 |
| Combined Score | 0.4308 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Evolocumab is similar to Estradiol, which is associated with hypothyroidism. This suggests shared therapeutic mechanisms.

---

### Path #9: migraine with or without aura, susceptibility to

**Path:**
```
[Evolocumab] --(0.693)--> [Estradiol] --(0.525)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6091 |
| Combined Score | 0.4307 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Evolocumab is similar to Estradiol, which is associated with migraine with or without aura, susceptibility to. This suggests shared therapeutic mechanisms.

---

### Path #10: ovarian carcinosarcoma

**Path:**
```
[Evolocumab] --(0.678)--> [Chlorotrianisene] --(0.540)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6090 |
| Combined Score | 0.4306 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Evolocumab is similar to Chlorotrianisene, which is associated with ovarian carcinosarcoma. This suggests shared therapeutic mechanisms.

---

### Path #11: uterine corpus leiomyoma

**Path:**
```
[Evolocumab] --(0.693)--> [Estradiol] --(0.524)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6087 |
| Combined Score | 0.4304 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Evolocumab is similar to Estradiol, which is associated with uterine corpus leiomyoma. This suggests shared therapeutic mechanisms.

---

### Path #12: dysthymic disorder

**Path:**
```
[Evolocumab] --(0.693)--> [Estradiol] --(0.524)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6084 |
| Combined Score | 0.4302 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Evolocumab is similar to Estradiol, which is associated with dysthymic disorder. This suggests shared therapeutic mechanisms.

---

### Path #13: congestive heart failure

**Path:**
```
[Evolocumab] --(0.693)--> [Estradiol] --(0.523)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6081 |
| Combined Score | 0.4300 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Evolocumab is similar to Estradiol, which is associated with congestive heart failure. This suggests shared therapeutic mechanisms.

---

### Path #14: uterine corpus leiomyoma

**Path:**
```
[Evolocumab] --(0.678)--> [Chlorotrianisene] --(0.538)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6079 |
| Combined Score | 0.4299 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Evolocumab is similar to Chlorotrianisene, which is associated with uterine corpus leiomyoma. This suggests shared therapeutic mechanisms.

---

### Path #15: phosphorus metabolism disease

**Path:**
```
[Evolocumab] --(0.693)--> [Estradiol] --(0.522)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6078 |
| Combined Score | 0.4297 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Evolocumab is similar to Estradiol, which is associated with phosphorus metabolism disease. This suggests shared therapeutic mechanisms.

---

### Path #16: maligant granulosa cell tumor of ovary

**Path:**
```
[Evolocumab] --(0.678)--> [Chlorotrianisene] --(0.537)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6075 |
| Combined Score | 0.4296 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Evolocumab is similar to Chlorotrianisene, which is associated with maligant granulosa cell tumor of ovary. This suggests shared therapeutic mechanisms.

---

### Path #17: hypertrophy of breast

**Path:**
```
[Evolocumab] --(0.693)--> [Estradiol] --(0.522)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6076 |
| Combined Score | 0.4296 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Evolocumab is similar to Estradiol, which is associated with hypertrophy of breast. This suggests shared therapeutic mechanisms.

---

### Path #18: cerebral infarction

**Path:**
```
[Evolocumab] --(0.678)--> [Chlorotrianisene] --(0.537)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6073 |
| Combined Score | 0.4294 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Evolocumab is similar to Chlorotrianisene, which is associated with cerebral infarction. This suggests shared therapeutic mechanisms.

---

### Path #19: neurotic disorder

**Path:**
```
[Evolocumab] --(0.693)--> [Estradiol] --(0.520)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6069 |
| Combined Score | 0.4291 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Evolocumab is similar to Estradiol, which is associated with neurotic disorder. This suggests shared therapeutic mechanisms.

---

### Path #20: intrinsic asthma

**Path:**
```
[Evolocumab] --(0.678)--> [Chlorotrianisene] --(0.536)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6066 |
| Combined Score | 0.4290 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Evolocumab is similar to Chlorotrianisene, which is associated with intrinsic asthma. This suggests shared therapeutic mechanisms.

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