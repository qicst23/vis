# 🔬 Romiplostim Path Analysis Report

*Generated: 2025-12-07 14:00:25*

## 1. Drug Profile

| Property | Value |
|----------|-------|
| **Drug ID** | DB05332 |
| **Drug Name** | Romiplostim |
| **Type** | drug |

## 2. Path Statistics

| Metric | Value |
|--------|-------|
| **Total Paths** | 100 |
| **Unique Diseases** | 41 |
| **Mean Attention** | 0.6196 |
| **Std Attention** | 0.0730 |
| **Min Attention** | 0.4536 |
| **Max Attention** | 0.7493 |

### Paths by Hop Count

| Hops | Count |
|------|-------|
| 1 | 6 |
| 2 | 400 |
| 3 | 400 |
| 4 | 400 |
| 5 | 400 |

## 3. Path Type Summary

| Path Type | Count | Description |
|-----------|-------|-------------|
| Drug Similarity | 94 | Paths through similar drugs |
| Protein Target | 0 | Paths through protein targets |
| Pathway | 0 | Paths through biological pathways |
| Biological Process | 0 | Paths through biological processes |
| Other | 6 | Other connection types |

### Key Similar Drugs

| Similar Drug | Max Attention | # Diseases |
|--------------|---------------|------------|
| Vinblastine | 0.8264 | 54 |
| Vincristine | 0.8205 | 40 |

## 4. Top 20 Paths (by Combined Score)

### Path #1: aplastic anemia

**Path:**
```
[Romiplostim] --(0.531)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.5314 |
| Combined Score | 0.5314 |
| Confidence | ⭐⭐⭐ Medium |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Romiplostim may treat aplastic anemia based on embedding similarity.

---

### Path #2: aplastic anemia

**Path:**
```
[Romiplostim] --(0.531)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.5314 |
| Combined Score | 0.5314 |
| Confidence | ⭐⭐⭐ Medium |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Romiplostim may treat aplastic anemia based on embedding similarity.

---

### Path #3: autoimmune thrombocytopenic

**Path:**
```
[Romiplostim] --(0.500)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.5000 |
| Combined Score | 0.5000 |
| Confidence | ⭐⭐⭐ Medium |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Romiplostim may treat autoimmune thrombocytopenic based on embedding similarity.

---

### Path #4: autoimmune thrombocytopenic

**Path:**
```
[Romiplostim] --(0.500)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.5000 |
| Combined Score | 0.5000 |
| Confidence | ⭐⭐⭐ Medium |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Romiplostim may treat autoimmune thrombocytopenic based on embedding similarity.

---

### Path #5: non-Hodgkin lymphoma

**Path:**
```
[Romiplostim] --(0.826)--> [Vinblastine] --(0.559)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6927 |
| Combined Score | 0.4898 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Romiplostim is similar to Vinblastine, which is associated with non-Hodgkin lymphoma. This suggests shared therapeutic mechanisms.

---

### Path #6: non-Hodgkin lymphoma

**Path:**
```
[Romiplostim] --(0.826)--> [Vinblastine] --(0.559)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6927 |
| Combined Score | 0.4898 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Romiplostim is similar to Vinblastine, which is associated with non-Hodgkin lymphoma. This suggests shared therapeutic mechanisms.

---

### Path #7: liver failure

**Path:**
```
[Romiplostim] --(0.826)--> [Vinblastine] --(0.557)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6915 |
| Combined Score | 0.4890 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Romiplostim is similar to Vinblastine, which is associated with liver failure. This suggests shared therapeutic mechanisms.

---

### Path #8: liver failure

**Path:**
```
[Romiplostim] --(0.826)--> [Vinblastine] --(0.557)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6915 |
| Combined Score | 0.4890 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Romiplostim is similar to Vinblastine, which is associated with liver failure. This suggests shared therapeutic mechanisms.

---

### Path #9: spermatocytic seminoma

**Path:**
```
[Romiplostim] --(0.826)--> [Vinblastine] --(0.557)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6915 |
| Combined Score | 0.4890 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Romiplostim is similar to Vinblastine, which is associated with spermatocytic seminoma. This suggests shared therapeutic mechanisms.

---

### Path #10: spermatocytic seminoma

**Path:**
```
[Romiplostim] --(0.826)--> [Vinblastine] --(0.557)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6915 |
| Combined Score | 0.4890 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Romiplostim is similar to Vinblastine, which is associated with spermatocytic seminoma. This suggests shared therapeutic mechanisms.

---

### Path #11: obsolete rare pulmonary disease

**Path:**
```
[Romiplostim] --(0.826)--> [Vinblastine] --(0.556)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6914 |
| Combined Score | 0.4889 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Romiplostim is similar to Vinblastine, which is associated with obsolete rare pulmonary disease. This suggests shared therapeutic mechanisms.

---

### Path #12: obsolete rare pulmonary disease

**Path:**
```
[Romiplostim] --(0.826)--> [Vinblastine] --(0.556)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6914 |
| Combined Score | 0.4889 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Romiplostim is similar to Vinblastine, which is associated with obsolete rare pulmonary disease. This suggests shared therapeutic mechanisms.

---

### Path #13: testicular teratoma

**Path:**
```
[Romiplostim] --(0.826)--> [Vinblastine] --(0.555)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6909 |
| Combined Score | 0.4886 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Romiplostim is similar to Vinblastine, which is associated with testicular teratoma. This suggests shared therapeutic mechanisms.

---

### Path #14: testicular teratoma

**Path:**
```
[Romiplostim] --(0.826)--> [Vinblastine] --(0.555)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6909 |
| Combined Score | 0.4886 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Romiplostim is similar to Vinblastine, which is associated with testicular teratoma. This suggests shared therapeutic mechanisms.

---

### Path #15: neurotic disorder

**Path:**
```
[Romiplostim] --(0.826)--> [Vinblastine] --(0.555)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6908 |
| Combined Score | 0.4885 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Romiplostim is similar to Vinblastine, which is associated with neurotic disorder. This suggests shared therapeutic mechanisms.

---

### Path #16: neurotic disorder

**Path:**
```
[Romiplostim] --(0.826)--> [Vinblastine] --(0.555)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6908 |
| Combined Score | 0.4885 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Romiplostim is similar to Vinblastine, which is associated with neurotic disorder. This suggests shared therapeutic mechanisms.

---

### Path #17: testicular seminoma

**Path:**
```
[Romiplostim] --(0.826)--> [Vinblastine] --(0.555)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6908 |
| Combined Score | 0.4885 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Romiplostim is similar to Vinblastine, which is associated with testicular seminoma. This suggests shared therapeutic mechanisms.

---

### Path #18: testicular seminoma

**Path:**
```
[Romiplostim] --(0.826)--> [Vinblastine] --(0.555)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6908 |
| Combined Score | 0.4885 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Romiplostim is similar to Vinblastine, which is associated with testicular seminoma. This suggests shared therapeutic mechanisms.

---

### Path #19: seminoma

**Path:**
```
[Romiplostim] --(0.826)--> [Vinblastine] --(0.555)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6908 |
| Combined Score | 0.4885 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Romiplostim is similar to Vinblastine, which is associated with seminoma. This suggests shared therapeutic mechanisms.

---

### Path #20: seminoma

**Path:**
```
[Romiplostim] --(0.826)--> [Vinblastine] --(0.555)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6908 |
| Combined Score | 0.4885 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Romiplostim is similar to Vinblastine, which is associated with seminoma. This suggests shared therapeutic mechanisms.

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