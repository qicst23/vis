# 🔬 Filgrastim Path Analysis Report

*Generated: 2025-12-07 14:00:25*

## 1. Drug Profile

| Property | Value |
|----------|-------|
| **Drug ID** | DB00099 |
| **Drug Name** | Filgrastim |
| **Type** | drug |

## 2. Path Statistics

| Metric | Value |
|--------|-------|
| **Total Paths** | 100 |
| **Unique Diseases** | 49 |
| **Mean Attention** | 0.5896 |
| **Std Attention** | 0.0737 |
| **Min Attention** | 0.4686 |
| **Max Attention** | 0.7437 |

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
| Vindesine | 0.7416 | 16 |
| Topotecan | 0.7012 | 56 |
| Bleomycin | 0.6709 | 20 |

## 4. Top 20 Paths (by Combined Score)

### Path #1: neutropenia, chronic familial

**Path:**
```
[Filgrastim] --(0.513)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.5132 |
| Combined Score | 0.5132 |
| Confidence | ⭐⭐⭐ Medium |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Filgrastim may treat neutropenia, chronic familial based on embedding similarity.

---

### Path #2: neutropenia, chronic familial

**Path:**
```
[Filgrastim] --(0.513)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.5132 |
| Combined Score | 0.5132 |
| Confidence | ⭐⭐⭐ Medium |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Filgrastim may treat neutropenia, chronic familial based on embedding similarity.

---

### Path #3: constitutional neutropenia

**Path:**
```
[Filgrastim] --(0.493)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.4931 |
| Combined Score | 0.4931 |
| Confidence | ⭐⭐ Low |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Filgrastim may treat constitutional neutropenia based on embedding similarity.

---

### Path #4: constitutional neutropenia

**Path:**
```
[Filgrastim] --(0.493)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.4931 |
| Combined Score | 0.4931 |
| Confidence | ⭐⭐ Low |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Filgrastim may treat constitutional neutropenia based on embedding similarity.

---

### Path #5: severe congenital neutropenia

**Path:**
```
[Filgrastim] --(0.486)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.4862 |
| Combined Score | 0.4862 |
| Confidence | ⭐⭐ Low |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Filgrastim may treat severe congenital neutropenia based on embedding similarity.

---

### Path #6: severe congenital neutropenia

**Path:**
```
[Filgrastim] --(0.486)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.4862 |
| Combined Score | 0.4862 |
| Confidence | ⭐⭐ Low |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Filgrastim may treat severe congenital neutropenia based on embedding similarity.

---

### Path #7: cyclic hematopoiesis

**Path:**
```
[Filgrastim] --(0.469)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.4686 |
| Combined Score | 0.4686 |
| Confidence | ⭐⭐ Low |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Filgrastim may treat cyclic hematopoiesis based on embedding similarity.

---

### Path #8: cyclic hematopoiesis

**Path:**
```
[Filgrastim] --(0.469)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.4686 |
| Combined Score | 0.4686 |
| Confidence | ⭐⭐ Low |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Filgrastim may treat cyclic hematopoiesis based on embedding similarity.

---

### Path #9: precursor T-cell acute lymphoblastic leukemia

**Path:**
```
[Filgrastim] --(0.742)--> [Vindesine] --(0.554)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6478 |
| Combined Score | 0.4580 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Filgrastim is similar to Vindesine, which is associated with precursor T-cell acute lymphoblastic leukemia. This suggests shared therapeutic mechanisms.

---

### Path #10: precursor T-cell acute lymphoblastic leukemia

**Path:**
```
[Filgrastim] --(0.742)--> [Vindesine] --(0.554)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6478 |
| Combined Score | 0.4580 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Filgrastim is similar to Vindesine, which is associated with precursor T-cell acute lymphoblastic leukemia. This suggests shared therapeutic mechanisms.

---

### Path #11: melanoma

**Path:**
```
[Filgrastim] --(0.742)--> [Vindesine] --(0.547)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6442 |
| Combined Score | 0.4555 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Filgrastim is similar to Vindesine, which is associated with melanoma. This suggests shared therapeutic mechanisms.

---

### Path #12: melanoma

**Path:**
```
[Filgrastim] --(0.742)--> [Vindesine] --(0.547)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6442 |
| Combined Score | 0.4555 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Filgrastim is similar to Vindesine, which is associated with melanoma. This suggests shared therapeutic mechanisms.

---

### Path #13: lung neoplasm

**Path:**
```
[Filgrastim] --(0.742)--> [Vindesine] --(0.541)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6416 |
| Combined Score | 0.4536 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Filgrastim is similar to Vindesine, which is associated with lung neoplasm. This suggests shared therapeutic mechanisms.

---

### Path #14: lung neoplasm

**Path:**
```
[Filgrastim] --(0.742)--> [Vindesine] --(0.541)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6416 |
| Combined Score | 0.4536 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Filgrastim is similar to Vindesine, which is associated with lung neoplasm. This suggests shared therapeutic mechanisms.

---

### Path #15: leukemia, lymphocytic, susceptibility to

**Path:**
```
[Filgrastim] --(0.742)--> [Vindesine] --(0.531)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6365 |
| Combined Score | 0.4501 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Filgrastim is similar to Vindesine, which is associated with leukemia, lymphocytic, susceptibility to. This suggests shared therapeutic mechanisms.

---

### Path #16: leukemia, lymphocytic, susceptibility to

**Path:**
```
[Filgrastim] --(0.742)--> [Vindesine] --(0.531)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6365 |
| Combined Score | 0.4501 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Filgrastim is similar to Vindesine, which is associated with leukemia, lymphocytic, susceptibility to. This suggests shared therapeutic mechanisms.

---

### Path #17: chronic myelogenous leukemia, BCR-ABL1 positive

**Path:**
```
[Filgrastim] --(0.742)--> [Vindesine] --(0.526)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6337 |
| Combined Score | 0.4481 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Filgrastim is similar to Vindesine, which is associated with chronic myelogenous leukemia, BCR-ABL1 positive. This suggests shared therapeutic mechanisms.

---

### Path #18: chronic myelogenous leukemia, BCR-ABL1 positive

**Path:**
```
[Filgrastim] --(0.742)--> [Vindesine] --(0.526)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6337 |
| Combined Score | 0.4481 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Filgrastim is similar to Vindesine, which is associated with chronic myelogenous leukemia, BCR-ABL1 positive. This suggests shared therapeutic mechanisms.

---

### Path #19: acute lymphoblastic/lymphocytic leukemia

**Path:**
```
[Filgrastim] --(0.742)--> [Vindesine] --(0.526)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6336 |
| Combined Score | 0.4480 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Filgrastim is similar to Vindesine, which is associated with acute lymphoblastic/lymphocytic leukemia. This suggests shared therapeutic mechanisms.

---

### Path #20: acute lymphoblastic/lymphocytic leukemia

**Path:**
```
[Filgrastim] --(0.742)--> [Vindesine] --(0.526)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6336 |
| Combined Score | 0.4480 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Filgrastim is similar to Vindesine, which is associated with acute lymphoblastic/lymphocytic leukemia. This suggests shared therapeutic mechanisms.

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