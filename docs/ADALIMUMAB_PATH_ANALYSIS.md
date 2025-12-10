# 🔬 Adalimumab Path Analysis Report

*Generated: 2025-12-07 14:00:25*

## 1. Drug Profile

| Property | Value |
|----------|-------|
| **Drug ID** | DB00051 |
| **Drug Name** | Adalimumab |
| **Type** | drug |

## 2. Path Statistics

| Metric | Value |
|--------|-------|
| **Total Paths** | 100 |
| **Unique Diseases** | 74 |
| **Mean Attention** | 0.5807 |
| **Std Attention** | 0.0635 |
| **Min Attention** | 0.4470 |
| **Max Attention** | 0.7577 |

### Paths by Hop Count

| Hops | Count |
|------|-------|
| 1 | 15 |
| 2 | 400 |
| 3 | 400 |
| 4 | 400 |
| 5 | 400 |

## 3. Path Type Summary

| Path Type | Count | Description |
|-----------|-------|-------------|
| Drug Similarity | 85 | Paths through similar drugs |
| Protein Target | 0 | Paths through protein targets |
| Pathway | 0 | Paths through biological pathways |
| Biological Process | 0 | Paths through biological processes |
| Other | 15 | Other connection types |

### Key Similar Drugs

| Similar Drug | Max Attention | # Diseases |
|--------------|---------------|------------|
| Obinutuzumab | 0.9584 | 2 |
| Conjugated estrogens | 0.7334 | 1 |
| Estradiol | 0.7247 | 39 |
| Chlorotrianisene | 0.6965 | 15 |
| Rivaroxaban | 0.6678 | 1 |
| Diethylstilbestrol | 0.6643 | 27 |

## 4. Top 20 Paths (by Combined Score)

### Path #1: acute lymphoblastic/lymphocytic leukemia

**Path:**
```
[Adalimumab] --(0.958)--> [Obinutuzumab] --(0.472)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.7153 |
| Combined Score | 0.5058 |
| Confidence | ⭐⭐⭐⭐⭐ Very High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Adalimumab is similar to Obinutuzumab, which is associated with acute lymphoblastic/lymphocytic leukemia. This suggests shared therapeutic mechanisms.

---

### Path #2: Richter syndrome

**Path:**
```
[Adalimumab] --(0.958)--> [Obinutuzumab] --(0.469)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.7137 |
| Combined Score | 0.5047 |
| Confidence | ⭐⭐⭐⭐⭐ Very High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Adalimumab is similar to Obinutuzumab, which is associated with Richter syndrome. This suggests shared therapeutic mechanisms.

---

### Path #3: non-infectious uveitis

**Path:**
```
[Adalimumab] --(0.485)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.4851 |
| Combined Score | 0.4851 |
| Confidence | ⭐⭐ Low |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Adalimumab may treat non-infectious uveitis based on embedding similarity.

---

### Path #4: inflammatory bowel disease

**Path:**
```
[Adalimumab] --(0.472)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.4721 |
| Combined Score | 0.4721 |
| Confidence | ⭐⭐ Low |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Adalimumab may treat inflammatory bowel disease based on embedding similarity.

---

### Path #5: Crohn disease

**Path:**
```
[Adalimumab] --(0.472)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.4720 |
| Combined Score | 0.4720 |
| Confidence | ⭐⭐ Low |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Adalimumab may treat Crohn disease based on embedding similarity.

---

### Path #6: dyshidrosis

**Path:**
```
[Adalimumab] --(0.472)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.4720 |
| Combined Score | 0.4720 |
| Confidence | ⭐⭐ Low |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Adalimumab may treat dyshidrosis based on embedding similarity.

---

### Path #7: hidradenitis suppurativa

**Path:**
```
[Adalimumab] --(0.471)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.4712 |
| Combined Score | 0.4712 |
| Confidence | ⭐⭐ Low |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Adalimumab may treat hidradenitis suppurativa based on embedding similarity.

---

### Path #8: psoriatic arthritis

**Path:**
```
[Adalimumab] --(0.469)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.4690 |
| Combined Score | 0.4690 |
| Confidence | ⭐⭐ Low |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Adalimumab may treat psoriatic arthritis based on embedding similarity.

---

### Path #9: juvenile arthritis due to defect in LACC1

**Path:**
```
[Adalimumab] --(0.469)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.4690 |
| Combined Score | 0.4690 |
| Confidence | ⭐⭐ Low |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Adalimumab may treat juvenile arthritis due to defect in LACC1 based on embedding similarity.

---

### Path #10: ankylosing spondylitis

**Path:**
```
[Adalimumab] --(0.468)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.4676 |
| Combined Score | 0.4676 |
| Confidence | ⭐⭐ Low |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Adalimumab may treat ankylosing spondylitis based on embedding similarity.

---

### Path #11: ulcerative colitis (disease)

**Path:**
```
[Adalimumab] --(0.468)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.4675 |
| Combined Score | 0.4675 |
| Confidence | ⭐⭐ Low |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Adalimumab may treat ulcerative colitis (disease) based on embedding similarity.

---

### Path #12: spondyloarthropathy, susceptibility to

**Path:**
```
[Adalimumab] --(0.466)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.4656 |
| Combined Score | 0.4656 |
| Confidence | ⭐⭐ Low |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Adalimumab may treat spondyloarthropathy, susceptibility to based on embedding similarity.

---

### Path #13: Crohn's colitis

**Path:**
```
[Adalimumab] --(0.465)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.4647 |
| Combined Score | 0.4647 |
| Confidence | ⭐⭐ Low |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Adalimumab may treat Crohn's colitis based on embedding similarity.

---

### Path #14: spondyloarthropathy

**Path:**
```
[Adalimumab] --(0.464)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.4641 |
| Combined Score | 0.4641 |
| Confidence | ⭐⭐ Low |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Adalimumab may treat spondyloarthropathy based on embedding similarity.

---

### Path #15: juvenile idiopathic arthritis

**Path:**
```
[Adalimumab] --(0.463)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.4627 |
| Combined Score | 0.4627 |
| Confidence | ⭐⭐ Low |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Adalimumab may treat juvenile idiopathic arthritis based on embedding similarity.

---

### Path #16: rheumatoid arthritis

**Path:**
```
[Adalimumab] --(0.457)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.4571 |
| Combined Score | 0.4571 |
| Confidence | ⭐⭐ Low |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Adalimumab may treat rheumatoid arthritis based on embedding similarity.

---

### Path #17: psychologic dyspareunia

**Path:**
```
[Adalimumab] --(0.733)--> [Conjugated estrogens] --(0.554)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6439 |
| Combined Score | 0.4553 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Adalimumab is similar to Conjugated estrogens, which is associated with psychologic dyspareunia. This suggests shared therapeutic mechanisms.

---

### Path #18: hidradenitis

**Path:**
```
[Adalimumab] --(0.447)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.4470 |
| Combined Score | 0.4470 |
| Confidence | ⭐⭐ Low |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Adalimumab may treat hidradenitis based on embedding similarity.

---

### Path #19: inherited porphyria

**Path:**
```
[Adalimumab] --(0.725)--> [Estradiol] --(0.529)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6267 |
| Combined Score | 0.4431 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Adalimumab is similar to Estradiol, which is associated with inherited porphyria. This suggests shared therapeutic mechanisms.

---

### Path #20: myxedema

**Path:**
```
[Adalimumab] --(0.725)--> [Estradiol] --(0.526)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6255 |
| Combined Score | 0.4423 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Adalimumab is similar to Estradiol, which is associated with myxedema. This suggests shared therapeutic mechanisms.

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