# 🔬 Infliximab Path Analysis Report

*Generated: 2025-12-07 14:00:25*

## 1. Drug Profile

| Property | Value |
|----------|-------|
| **Drug ID** | DB00065 |
| **Drug Name** | Infliximab |
| **Type** | drug |

## 2. Path Statistics

| Metric | Value |
|--------|-------|
| **Total Paths** | 100 |
| **Unique Diseases** | 87 |
| **Mean Attention** | 0.5987 |
| **Std Attention** | 0.0721 |
| **Min Attention** | 0.4568 |
| **Max Attention** | 0.7362 |

### Paths by Hop Count

| Hops | Count |
|------|-------|
| 1 | 8 |
| 2 | 400 |
| 3 | 400 |
| 4 | 400 |
| 5 | 400 |

## 3. Path Type Summary

| Path Type | Count | Description |
|-----------|-------|-------------|
| Drug Similarity | 92 | Paths through similar drugs |
| Protein Target | 0 | Paths through protein targets |
| Pathway | 0 | Paths through biological pathways |
| Biological Process | 0 | Paths through biological processes |
| Other | 8 | Other connection types |

### Key Similar Drugs

| Similar Drug | Max Attention | # Diseases |
|--------------|---------------|------------|
| Quinine | 0.8552 | 22 |
| Tipranavir | 0.8258 | 23 |
| Tamoxifen | 0.7967 | 25 |
| Quinidine | 0.7914 | 11 |
| Chlorotrianisene | 0.7903 | 7 |
| Ibrutinib | 0.7836 | 1 |
| Tibolone | 0.7756 | 1 |
| Rivaroxaban | 0.7632 | 1 |
| Diethylstilbestrol | 0.7483 | 1 |

## 4. Top 20 Paths (by Combined Score)

### Path #1: Crohn disease

**Path:**
```
[Infliximab] --(0.538)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.5382 |
| Combined Score | 0.5382 |
| Confidence | ⭐⭐⭐ Medium |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Infliximab may treat Crohn disease based on embedding similarity.

---

### Path #2: inflammatory bowel disease

**Path:**
```
[Infliximab] --(0.538)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.5378 |
| Combined Score | 0.5378 |
| Confidence | ⭐⭐⭐ Medium |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Infliximab may treat inflammatory bowel disease based on embedding similarity.

---

### Path #3: Crohn's colitis

**Path:**
```
[Infliximab] --(0.533)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.5335 |
| Combined Score | 0.5335 |
| Confidence | ⭐⭐⭐ Medium |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Infliximab may treat Crohn's colitis based on embedding similarity.

---

### Path #4: ulcerative colitis (disease)

**Path:**
```
[Infliximab] --(0.531)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.5311 |
| Combined Score | 0.5311 |
| Confidence | ⭐⭐⭐ Medium |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Infliximab may treat ulcerative colitis (disease) based on embedding similarity.

---

### Path #5: psoriatic arthritis

**Path:**
```
[Infliximab] --(0.530)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.5299 |
| Combined Score | 0.5299 |
| Confidence | ⭐⭐⭐ Medium |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Infliximab may treat psoriatic arthritis based on embedding similarity.

---

### Path #6: ankylosing spondylitis

**Path:**
```
[Infliximab] --(0.525)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.5253 |
| Combined Score | 0.5253 |
| Confidence | ⭐⭐⭐ Medium |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Infliximab may treat ankylosing spondylitis based on embedding similarity.

---

### Path #7: spondyloarthropathy, susceptibility to

**Path:**
```
[Infliximab] --(0.512)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.5121 |
| Combined Score | 0.5121 |
| Confidence | ⭐⭐⭐ Medium |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Infliximab may treat spondyloarthropathy, susceptibility to based on embedding similarity.

---

### Path #8: rheumatoid arthritis

**Path:**
```
[Infliximab] --(0.503)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.5027 |
| Combined Score | 0.5027 |
| Confidence | ⭐⭐⭐ Medium |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Infliximab may treat rheumatoid arthritis based on embedding similarity.

---

### Path #9: babesiosis

**Path:**
```
[Infliximab] --(0.855)--> [Quinine] --(0.543)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6989 |
| Combined Score | 0.4942 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Infliximab is similar to Quinine, which is associated with babesiosis. This suggests shared therapeutic mechanisms.

---

### Path #10: myasthenia gravis

**Path:**
```
[Infliximab] --(0.855)--> [Quinine] --(0.540)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6978 |
| Combined Score | 0.4935 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Infliximab is similar to Quinine, which is associated with myasthenia gravis. This suggests shared therapeutic mechanisms.

---

### Path #11: neuromuscular junction disease

**Path:**
```
[Infliximab] --(0.855)--> [Quinine] --(0.539)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6971 |
| Combined Score | 0.4929 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Infliximab is similar to Quinine, which is associated with neuromuscular junction disease. This suggests shared therapeutic mechanisms.

---

### Path #12: atrial flutter (disease)

**Path:**
```
[Infliximab] --(0.855)--> [Quinine] --(0.538)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6965 |
| Combined Score | 0.4925 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Infliximab is similar to Quinine, which is associated with atrial flutter (disease). This suggests shared therapeutic mechanisms.

---

### Path #13: end stage renal failure

**Path:**
```
[Infliximab] --(0.855)--> [Quinine] --(0.537)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6961 |
| Combined Score | 0.4922 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Infliximab is similar to Quinine, which is associated with end stage renal failure. This suggests shared therapeutic mechanisms.

---

### Path #14: atrial fibrillation (disease)

**Path:**
```
[Infliximab] --(0.855)--> [Quinine] --(0.535)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6952 |
| Combined Score | 0.4916 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Infliximab is similar to Quinine, which is associated with atrial fibrillation (disease). This suggests shared therapeutic mechanisms.

---

### Path #15: chronic kidney disease

**Path:**
```
[Infliximab] --(0.855)--> [Quinine] --(0.535)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6951 |
| Combined Score | 0.4915 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Infliximab is similar to Quinine, which is associated with chronic kidney disease. This suggests shared therapeutic mechanisms.

---

### Path #16: adult-onset myasthenia gravis

**Path:**
```
[Infliximab] --(0.855)--> [Quinine] --(0.535)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6949 |
| Combined Score | 0.4914 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Infliximab is similar to Quinine, which is associated with adult-onset myasthenia gravis. This suggests shared therapeutic mechanisms.

---

### Path #17: liver failure

**Path:**
```
[Infliximab] --(0.826)--> [Tipranavir] --(0.564)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6947 |
| Combined Score | 0.4912 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Infliximab is similar to Tipranavir, which is associated with liver failure. This suggests shared therapeutic mechanisms.

---

### Path #18: chronic hepatitis C virus infection

**Path:**
```
[Infliximab] --(0.826)--> [Tipranavir] --(0.562)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6941 |
| Combined Score | 0.4908 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Infliximab is similar to Tipranavir, which is associated with chronic hepatitis C virus infection. This suggests shared therapeutic mechanisms.

---

### Path #19: gallbladder disease

**Path:**
```
[Infliximab] --(0.855)--> [Quinine] --(0.531)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6933 |
| Combined Score | 0.4902 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Infliximab is similar to Quinine, which is associated with gallbladder disease. This suggests shared therapeutic mechanisms.

---

### Path #20: malaria

**Path:**
```
[Infliximab] --(0.855)--> [Quinine] --(0.531)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6933 |
| Combined Score | 0.4902 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Infliximab is similar to Quinine, which is associated with malaria. This suggests shared therapeutic mechanisms.

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