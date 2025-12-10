# 🔬 Cinacalcet Path Analysis Report

*Generated: 2025-12-07 14:00:25*

## 1. Drug Profile

| Property | Value |
|----------|-------|
| **Drug ID** | DB01012 |
| **Drug Name** | Cinacalcet |
| **Type** | drug |

## 2. Path Statistics

| Metric | Value |
|--------|-------|
| **Total Paths** | 100 |
| **Unique Diseases** | 79 |
| **Mean Attention** | 0.5758 |
| **Std Attention** | 0.0715 |
| **Min Attention** | 0.4610 |
| **Max Attention** | 0.7448 |

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
| Dasatinib | 0.8432 | 21 |
| Ethinylestradiol | 0.8301 | 45 |
| Estradiol cypionate | 0.8215 | 23 |
| Ibrutinib | 0.8144 | 2 |
| Pentoxifylline | 0.8053 | 1 |

## 4. Top 20 Paths (by Combined Score)

### Path #1: phosphorus metabolism disease

**Path:**
```
[Cinacalcet] --(0.566)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.5656 |
| Combined Score | 0.5656 |
| Confidence | ⭐⭐⭐ Medium |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Cinacalcet may treat phosphorus metabolism disease based on embedding similarity.

---

### Path #2: liver disease

**Path:**
```
[Cinacalcet] --(0.538)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.5377 |
| Combined Score | 0.5377 |
| Confidence | ⭐⭐⭐ Medium |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Cinacalcet may treat liver disease based on embedding similarity.

---

### Path #3: nephrocalcinosis

**Path:**
```
[Cinacalcet] --(0.529)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.5294 |
| Combined Score | 0.5294 |
| Confidence | ⭐⭐⭐ Medium |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Cinacalcet may treat nephrocalcinosis based on embedding similarity.

---

### Path #4: hypercalcemia disease

**Path:**
```
[Cinacalcet] --(0.517)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.5167 |
| Combined Score | 0.5167 |
| Confidence | ⭐⭐⭐ Medium |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Cinacalcet may treat hypercalcemia disease based on embedding similarity.

---

### Path #5: gallbladder disease

**Path:**
```
[Cinacalcet] --(0.515)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.5147 |
| Combined Score | 0.5147 |
| Confidence | ⭐⭐⭐ Medium |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Cinacalcet may treat gallbladder disease based on embedding similarity.

---

### Path #6: hypophosphatemia (disease)

**Path:**
```
[Cinacalcet] --(0.501)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.5013 |
| Combined Score | 0.5013 |
| Confidence | ⭐⭐⭐ Medium |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Cinacalcet may treat hypophosphatemia (disease) based on embedding similarity.

---

### Path #7: epilepsy

**Path:**
```
[Cinacalcet] --(0.499)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.4991 |
| Combined Score | 0.4991 |
| Confidence | ⭐⭐ Low |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Cinacalcet may treat epilepsy based on embedding similarity.

---

### Path #8: hypotensive disorder

**Path:**
```
[Cinacalcet] --(0.499)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.4988 |
| Combined Score | 0.4988 |
| Confidence | ⭐⭐ Low |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Cinacalcet may treat hypotensive disorder based on embedding similarity.

---

### Path #9: active peptic ulcer disease

**Path:**
```
[Cinacalcet] --(0.843)--> [Dasatinib] --(0.535)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6892 |
| Combined Score | 0.4874 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Cinacalcet is similar to Dasatinib, which is associated with active peptic ulcer disease. This suggests shared therapeutic mechanisms.

---

### Path #10: heart failure

**Path:**
```
[Cinacalcet] --(0.843)--> [Dasatinib] --(0.535)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6893 |
| Combined Score | 0.4874 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Cinacalcet is similar to Dasatinib, which is associated with heart failure. This suggests shared therapeutic mechanisms.

---

### Path #11: blast phase chronic myelogenous leukemia, BCR-ABL1 positive

**Path:**
```
[Cinacalcet] --(0.843)--> [Dasatinib] --(0.535)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6893 |
| Combined Score | 0.4874 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Cinacalcet is similar to Dasatinib, which is associated with blast phase chronic myelogenous leukemia, BCR-ABL1 positive. This suggests shared therapeutic mechanisms.

---

### Path #12: intracerebral hemorrhage

**Path:**
```
[Cinacalcet] --(0.843)--> [Dasatinib] --(0.529)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6863 |
| Combined Score | 0.4853 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Cinacalcet is similar to Dasatinib, which is associated with intracerebral hemorrhage. This suggests shared therapeutic mechanisms.

---

### Path #13: coronary thrombosis

**Path:**
```
[Cinacalcet] --(0.843)--> [Dasatinib] --(0.528)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6856 |
| Combined Score | 0.4848 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Cinacalcet is similar to Dasatinib, which is associated with coronary thrombosis. This suggests shared therapeutic mechanisms.

---

### Path #14: phosphorus metabolism disease

**Path:**
```
[Cinacalcet] --(0.822)--> [Estradiol cypionate] --(0.550)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6856 |
| Combined Score | 0.4848 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Cinacalcet is similar to Estradiol cypionate, which is associated with phosphorus metabolism disease. This suggests shared therapeutic mechanisms.

---

### Path #15: liver disease

**Path:**
```
[Cinacalcet] --(0.843)--> [Dasatinib] --(0.525)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6843 |
| Combined Score | 0.4839 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Cinacalcet is similar to Dasatinib, which is associated with liver disease. This suggests shared therapeutic mechanisms.

---

### Path #16: liver failure

**Path:**
```
[Cinacalcet] --(0.822)--> [Estradiol cypionate] --(0.547)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6844 |
| Combined Score | 0.4839 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Cinacalcet is similar to Estradiol cypionate, which is associated with liver failure. This suggests shared therapeutic mechanisms.

---

### Path #17: neutropenia

**Path:**
```
[Cinacalcet] --(0.843)--> [Dasatinib] --(0.525)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6839 |
| Combined Score | 0.4836 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Cinacalcet is similar to Dasatinib, which is associated with neutropenia. This suggests shared therapeutic mechanisms.

---

### Path #18: neurotic disorder

**Path:**
```
[Cinacalcet] --(0.822)--> [Estradiol cypionate] --(0.546)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6836 |
| Combined Score | 0.4834 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Cinacalcet is similar to Estradiol cypionate, which is associated with neurotic disorder. This suggests shared therapeutic mechanisms.

---

### Path #19: congestive heart failure

**Path:**
```
[Cinacalcet] --(0.843)--> [Dasatinib] --(0.524)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6835 |
| Combined Score | 0.4833 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Cinacalcet is similar to Dasatinib, which is associated with congestive heart failure. This suggests shared therapeutic mechanisms.

---

### Path #20: uterine corpus leiomyoma

**Path:**
```
[Cinacalcet] --(0.822)--> [Estradiol cypionate] --(0.545)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6832 |
| Combined Score | 0.4831 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Cinacalcet is similar to Estradiol cypionate, which is associated with uterine corpus leiomyoma. This suggests shared therapeutic mechanisms.

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