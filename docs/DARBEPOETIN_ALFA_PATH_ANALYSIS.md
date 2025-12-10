# 🔬 Darbepoetin alfa Path Analysis Report

*Generated: 2025-12-07 14:00:25*

## 1. Drug Profile

| Property | Value |
|----------|-------|
| **Drug ID** | DB00012 |
| **Drug Name** | Darbepoetin alfa |
| **Type** | drug |

## 2. Path Statistics

| Metric | Value |
|--------|-------|
| **Total Paths** | 100 |
| **Unique Diseases** | 60 |
| **Mean Attention** | 0.6000 |
| **Std Attention** | 0.0692 |
| **Min Attention** | 0.4642 |
| **Max Attention** | 0.7817 |

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
| Hydroxyprogesterone caproate | 0.8117 | 30 |
| Medroxyprogesterone acetate | 0.7516 | 29 |
| Chlorotrianisene | 0.7368 | 17 |
| Megestrol acetate | 0.7208 | 22 |

## 4. Top 20 Paths (by Combined Score)

### Path #1: hypertensive disorder

**Path:**
```
[Darbepoetin alfa] --(0.554)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.5537 |
| Combined Score | 0.5537 |
| Confidence | ⭐⭐⭐ Medium |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Darbepoetin alfa may treat hypertensive disorder based on embedding similarity.

---

### Path #2: hypertension

**Path:**
```
[Darbepoetin alfa] --(0.545)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.5452 |
| Combined Score | 0.5452 |
| Confidence | ⭐⭐⭐ Medium |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Darbepoetin alfa may treat hypertension based on embedding similarity.

---

### Path #3: mild pre-eclampsia

**Path:**
```
[Darbepoetin alfa] --(0.812)--> [Hydroxyprogesterone ca...] --(0.559)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6855 |
| Combined Score | 0.4847 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Darbepoetin alfa is similar to Hydroxyprogesterone caproate, which is associated with mild pre-eclampsia. This suggests shared therapeutic mechanisms.

---

### Path #4: intrinsic asthma

**Path:**
```
[Darbepoetin alfa] --(0.812)--> [Hydroxyprogesterone ca...] --(0.546)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6789 |
| Combined Score | 0.4801 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Darbepoetin alfa is similar to Hydroxyprogesterone caproate, which is associated with intrinsic asthma. This suggests shared therapeutic mechanisms.

---

### Path #5: endometrium neoplasm

**Path:**
```
[Darbepoetin alfa] --(0.812)--> [Hydroxyprogesterone ca...] --(0.546)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6787 |
| Combined Score | 0.4799 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Darbepoetin alfa is similar to Hydroxyprogesterone caproate, which is associated with endometrium neoplasm. This suggests shared therapeutic mechanisms.

---

### Path #6: migraine with or without aura, susceptibility to

**Path:**
```
[Darbepoetin alfa] --(0.812)--> [Hydroxyprogesterone ca...] --(0.545)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6784 |
| Combined Score | 0.4797 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Darbepoetin alfa is similar to Hydroxyprogesterone caproate, which is associated with migraine with or without aura, susceptibility to. This suggests shared therapeutic mechanisms.

---

### Path #7: glucose intolerance

**Path:**
```
[Darbepoetin alfa] --(0.812)--> [Hydroxyprogesterone ca...] --(0.542)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6769 |
| Combined Score | 0.4786 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Darbepoetin alfa is similar to Hydroxyprogesterone caproate, which is associated with glucose intolerance. This suggests shared therapeutic mechanisms.

---

### Path #8: gallbladder disease

**Path:**
```
[Darbepoetin alfa] --(0.812)--> [Hydroxyprogesterone ca...] --(0.541)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6765 |
| Combined Score | 0.4784 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Darbepoetin alfa is similar to Hydroxyprogesterone caproate, which is associated with gallbladder disease. This suggests shared therapeutic mechanisms.

---

### Path #9: neurotic disorder

**Path:**
```
[Darbepoetin alfa] --(0.812)--> [Hydroxyprogesterone ca...] --(0.541)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6762 |
| Combined Score | 0.4781 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Darbepoetin alfa is similar to Hydroxyprogesterone caproate, which is associated with neurotic disorder. This suggests shared therapeutic mechanisms.

---

### Path #10: anxiety disorder

**Path:**
```
[Darbepoetin alfa] --(0.812)--> [Hydroxyprogesterone ca...] --(0.537)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6745 |
| Combined Score | 0.4770 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Darbepoetin alfa is similar to Hydroxyprogesterone caproate, which is associated with anxiety disorder. This suggests shared therapeutic mechanisms.

---

### Path #11: hyperglycemia

**Path:**
```
[Darbepoetin alfa] --(0.812)--> [Hydroxyprogesterone ca...] --(0.538)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6746 |
| Combined Score | 0.4770 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Darbepoetin alfa is similar to Hydroxyprogesterone caproate, which is associated with hyperglycemia. This suggests shared therapeutic mechanisms.

---

### Path #12: hypertensive disorder

**Path:**
```
[Darbepoetin alfa] --(0.812)--> [Hydroxyprogesterone ca...] --(0.537)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6744 |
| Combined Score | 0.4769 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Darbepoetin alfa is similar to Hydroxyprogesterone caproate, which is associated with hypertensive disorder. This suggests shared therapeutic mechanisms.

---

### Path #13: dysthymic disorder

**Path:**
```
[Darbepoetin alfa] --(0.812)--> [Hydroxyprogesterone ca...] --(0.534)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6727 |
| Combined Score | 0.4757 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Darbepoetin alfa is similar to Hydroxyprogesterone caproate, which is associated with dysthymic disorder. This suggests shared therapeutic mechanisms.

---

### Path #14: prediabetes syndrome

**Path:**
```
[Darbepoetin alfa] --(0.812)--> [Hydroxyprogesterone ca...] --(0.530)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6708 |
| Combined Score | 0.4744 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Darbepoetin alfa is similar to Hydroxyprogesterone caproate, which is associated with prediabetes syndrome. This suggests shared therapeutic mechanisms.

---

### Path #15: liver disease

**Path:**
```
[Darbepoetin alfa] --(0.812)--> [Hydroxyprogesterone ca...] --(0.526)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6688 |
| Combined Score | 0.4729 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Darbepoetin alfa is similar to Hydroxyprogesterone caproate, which is associated with liver disease. This suggests shared therapeutic mechanisms.

---

### Path #16: allergic asthma

**Path:**
```
[Darbepoetin alfa] --(0.812)--> [Hydroxyprogesterone ca...] --(0.524)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6681 |
| Combined Score | 0.4724 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Darbepoetin alfa is similar to Hydroxyprogesterone caproate, which is associated with allergic asthma. This suggests shared therapeutic mechanisms.

---

### Path #17: liver neoplasm

**Path:**
```
[Darbepoetin alfa] --(0.812)--> [Hydroxyprogesterone ca...] --(0.519)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6656 |
| Combined Score | 0.4707 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Darbepoetin alfa is similar to Hydroxyprogesterone caproate, which is associated with liver neoplasm. This suggests shared therapeutic mechanisms.

---

### Path #18: diabetes mellitus (disease)

**Path:**
```
[Darbepoetin alfa] --(0.812)--> [Hydroxyprogesterone ca...] --(0.519)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6655 |
| Combined Score | 0.4706 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Darbepoetin alfa is similar to Hydroxyprogesterone caproate, which is associated with diabetes mellitus (disease). This suggests shared therapeutic mechanisms.

---

### Path #19: endometrial cancer

**Path:**
```
[Darbepoetin alfa] --(0.812)--> [Hydroxyprogesterone ca...] --(0.517)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6644 |
| Combined Score | 0.4698 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Darbepoetin alfa is similar to Hydroxyprogesterone caproate, which is associated with endometrial cancer. This suggests shared therapeutic mechanisms.

---

### Path #20: female breast carcinoma

**Path:**
```
[Darbepoetin alfa] --(0.812)--> [Hydroxyprogesterone ca...] --(0.513)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6624 |
| Combined Score | 0.4684 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Darbepoetin alfa is similar to Hydroxyprogesterone caproate, which is associated with female breast carcinoma. This suggests shared therapeutic mechanisms.

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