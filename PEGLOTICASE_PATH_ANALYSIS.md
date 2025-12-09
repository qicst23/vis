# 🔬 Pegloticase Path Analysis Report

*Generated: 2025-12-07 14:00:25*

## 1. Drug Profile

| Property | Value |
|----------|-------|
| **Drug ID** | DB09208 |
| **Drug Name** | Pegloticase |
| **Type** | drug |

## 2. Path Statistics

| Metric | Value |
|--------|-------|
| **Total Paths** | 100 |
| **Unique Diseases** | 41 |
| **Mean Attention** | 0.6555 |
| **Std Attention** | 0.0615 |
| **Min Attention** | 0.5261 |
| **Max Attention** | 0.7645 |

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
| Azapropazone | 0.8750 | 14 |
| Peginterferon beta-1a | 0.8306 | 2 |
| Sulfinpyrazone | 0.8081 | 12 |
| Hydroflumethiazide | 0.8050 | 34 |
| Bendroflumethiazide | 0.7983 | 27 |
| Peginterferon alfa-2b | 0.7876 | 4 |
| Peginterferon alfa-2a | 0.7779 | 6 |

## 4. Top 20 Paths (by Combined Score)

### Path #1: gout

**Path:**
```
[Pegloticase] --(0.526)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.5261 |
| Combined Score | 0.5261 |
| Confidence | ⭐⭐⭐ Medium |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Pegloticase may treat gout based on embedding similarity.

---

### Path #2: osteoarthritis susceptibility

**Path:**
```
[Pegloticase] --(0.875)--> [Azapropazone] --(0.551)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.7132 |
| Combined Score | 0.5043 |
| Confidence | ⭐⭐⭐⭐⭐ Very High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Pegloticase is similar to Azapropazone, which is associated with osteoarthritis susceptibility. This suggests shared therapeutic mechanisms.

---

### Path #3: osteoarthritis susceptibility

**Path:**
```
[Pegloticase] --(0.875)--> [Azapropazone] --(0.551)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.7132 |
| Combined Score | 0.5043 |
| Confidence | ⭐⭐⭐⭐⭐ Very High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Pegloticase is similar to Azapropazone, which is associated with osteoarthritis susceptibility. This suggests shared therapeutic mechanisms.

---

### Path #4: gout

**Path:**
```
[Pegloticase] --(0.875)--> [Azapropazone] --(0.547)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.7110 |
| Combined Score | 0.5028 |
| Confidence | ⭐⭐⭐⭐⭐ Very High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Pegloticase is similar to Azapropazone, which is associated with gout. This suggests shared therapeutic mechanisms.

---

### Path #5: gout

**Path:**
```
[Pegloticase] --(0.875)--> [Azapropazone] --(0.547)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.7110 |
| Combined Score | 0.5028 |
| Confidence | ⭐⭐⭐⭐⭐ Very High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Pegloticase is similar to Azapropazone, which is associated with gout. This suggests shared therapeutic mechanisms.

---

### Path #6: ankylosing spondylitis

**Path:**
```
[Pegloticase] --(0.875)--> [Azapropazone] --(0.541)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.7078 |
| Combined Score | 0.5005 |
| Confidence | ⭐⭐⭐⭐⭐ Very High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Pegloticase is similar to Azapropazone, which is associated with ankylosing spondylitis. This suggests shared therapeutic mechanisms.

---

### Path #7: ankylosing spondylitis

**Path:**
```
[Pegloticase] --(0.875)--> [Azapropazone] --(0.541)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.7078 |
| Combined Score | 0.5005 |
| Confidence | ⭐⭐⭐⭐⭐ Very High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Pegloticase is similar to Azapropazone, which is associated with ankylosing spondylitis. This suggests shared therapeutic mechanisms.

---

### Path #8: rheumatoid arthritis

**Path:**
```
[Pegloticase] --(0.875)--> [Azapropazone] --(0.511)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6930 |
| Combined Score | 0.4901 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Pegloticase is similar to Azapropazone, which is associated with rheumatoid arthritis. This suggests shared therapeutic mechanisms.

---

### Path #9: rheumatoid arthritis

**Path:**
```
[Pegloticase] --(0.875)--> [Azapropazone] --(0.511)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6930 |
| Combined Score | 0.4901 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Pegloticase is similar to Azapropazone, which is associated with rheumatoid arthritis. This suggests shared therapeutic mechanisms.

---

### Path #10: spondyloarthropathy, susceptibility to

**Path:**
```
[Pegloticase] --(0.875)--> [Azapropazone] --(0.508)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6913 |
| Combined Score | 0.4888 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Pegloticase is similar to Azapropazone, which is associated with spondyloarthropathy, susceptibility to. This suggests shared therapeutic mechanisms.

---

### Path #11: spondyloarthropathy, susceptibility to

**Path:**
```
[Pegloticase] --(0.875)--> [Azapropazone] --(0.508)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6913 |
| Combined Score | 0.4888 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Pegloticase is similar to Azapropazone, which is associated with spondyloarthropathy, susceptibility to. This suggests shared therapeutic mechanisms.

---

### Path #12: arthropathy

**Path:**
```
[Pegloticase] --(0.875)--> [Azapropazone] --(0.507)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6909 |
| Combined Score | 0.4886 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Pegloticase is similar to Azapropazone, which is associated with arthropathy. This suggests shared therapeutic mechanisms.

---

### Path #13: arthropathy

**Path:**
```
[Pegloticase] --(0.875)--> [Azapropazone] --(0.507)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6909 |
| Combined Score | 0.4886 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Pegloticase is similar to Azapropazone, which is associated with arthropathy. This suggests shared therapeutic mechanisms.

---

### Path #14: osteoarthritis

**Path:**
```
[Pegloticase] --(0.875)--> [Azapropazone] --(0.497)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6860 |
| Combined Score | 0.4850 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Pegloticase is similar to Azapropazone, which is associated with osteoarthritis. This suggests shared therapeutic mechanisms.

---

### Path #15: osteoarthritis

**Path:**
```
[Pegloticase] --(0.875)--> [Azapropazone] --(0.497)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6860 |
| Combined Score | 0.4850 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Pegloticase is similar to Azapropazone, which is associated with osteoarthritis. This suggests shared therapeutic mechanisms.

---

### Path #16: inflammatory bowel disease

**Path:**
```
[Pegloticase] --(0.808)--> [Sulfinpyrazone] --(0.553)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6804 |
| Combined Score | 0.4812 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Pegloticase is similar to Sulfinpyrazone, which is associated with inflammatory bowel disease. This suggests shared therapeutic mechanisms.

---

### Path #17: inflammatory bowel disease

**Path:**
```
[Pegloticase] --(0.808)--> [Sulfinpyrazone] --(0.553)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6804 |
| Combined Score | 0.4812 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Pegloticase is similar to Sulfinpyrazone, which is associated with inflammatory bowel disease. This suggests shared therapeutic mechanisms.

---

### Path #18: urolithiasis

**Path:**
```
[Pegloticase] --(0.808)--> [Sulfinpyrazone] --(0.553)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6804 |
| Combined Score | 0.4811 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Pegloticase is similar to Sulfinpyrazone, which is associated with urolithiasis. This suggests shared therapeutic mechanisms.

---

### Path #19: urolithiasis

**Path:**
```
[Pegloticase] --(0.808)--> [Sulfinpyrazone] --(0.553)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6804 |
| Combined Score | 0.4811 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Pegloticase is similar to Sulfinpyrazone, which is associated with urolithiasis. This suggests shared therapeutic mechanisms.

---

### Path #20: relapsing-remitting multiple sclerosis

**Path:**
```
[Pegloticase] --(0.831)--> [Peginterferon beta-1a] --(0.530)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6802 |
| Combined Score | 0.4809 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Pegloticase is similar to Peginterferon beta-1a, which is associated with relapsing-remitting multiple sclerosis. This suggests shared therapeutic mechanisms.

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