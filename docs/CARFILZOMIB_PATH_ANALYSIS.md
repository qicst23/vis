# 🔬 Carfilzomib Path Analysis Report

*Generated: 2025-12-07 14:00:25*

## 1. Drug Profile

| Property | Value |
|----------|-------|
| **Drug ID** | DB08889 |
| **Drug Name** | Carfilzomib |
| **Type** | drug |

## 2. Path Statistics

| Metric | Value |
|--------|-------|
| **Total Paths** | 100 |
| **Unique Diseases** | 90 |
| **Mean Attention** | 0.5722 |
| **Std Attention** | 0.0556 |
| **Min Attention** | 0.4628 |
| **Max Attention** | 0.7304 |

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
| Obinutuzumab | 0.7975 | 2 |
| Indomethacin | 0.7765 | 65 |
| Quinine | 0.7117 | 22 |
| Pentosan polysulfate | 0.7024 | 3 |
| Rivaroxaban | 0.6619 | 6 |
| Tipranavir | 0.6188 | 1 |

## 4. Top 20 Paths (by Combined Score)

### Path #1: plasma cell myeloma

**Path:**
```
[Carfilzomib] --(0.478)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.4780 |
| Combined Score | 0.4780 |
| Confidence | ⭐⭐ Low |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Carfilzomib may treat plasma cell myeloma based on embedding similarity.

---

### Path #2: tenosynovitis

**Path:**
```
[Carfilzomib] --(0.776)--> [Indomethacin] --(0.511)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6438 |
| Combined Score | 0.4552 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Carfilzomib is similar to Indomethacin, which is associated with tenosynovitis. This suggests shared therapeutic mechanisms.

---

### Path #3: infectious disease

**Path:**
```
[Carfilzomib] --(0.776)--> [Indomethacin] --(0.500)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6384 |
| Combined Score | 0.4515 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Carfilzomib is similar to Indomethacin, which is associated with infectious disease. This suggests shared therapeutic mechanisms.

---

### Path #4: squamous cell carcinoma of colon

**Path:**
```
[Carfilzomib] --(0.776)--> [Indomethacin] --(0.498)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6371 |
| Combined Score | 0.4505 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Carfilzomib is similar to Indomethacin, which is associated with squamous cell carcinoma of colon. This suggests shared therapeutic mechanisms.

---

### Path #5: acute lymphoblastic/lymphocytic leukemia

**Path:**
```
[Carfilzomib] --(0.797)--> [Obinutuzumab] --(0.472)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6349 |
| Combined Score | 0.4489 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Carfilzomib is similar to Obinutuzumab, which is associated with acute lymphoblastic/lymphocytic leukemia. This suggests shared therapeutic mechanisms.

---

### Path #6: Richter syndrome

**Path:**
```
[Carfilzomib] --(0.797)--> [Obinutuzumab] --(0.469)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6333 |
| Combined Score | 0.4478 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Carfilzomib is similar to Obinutuzumab, which is associated with Richter syndrome. This suggests shared therapeutic mechanisms.

---

### Path #7: myocardial infarction (disease)

**Path:**
```
[Carfilzomib] --(0.776)--> [Indomethacin] --(0.487)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6318 |
| Combined Score | 0.4468 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Carfilzomib is similar to Indomethacin, which is associated with myocardial infarction (disease). This suggests shared therapeutic mechanisms.

---

### Path #8: tendinitis

**Path:**
```
[Carfilzomib] --(0.776)--> [Indomethacin] --(0.484)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6303 |
| Combined Score | 0.4457 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Carfilzomib is similar to Indomethacin, which is associated with tendinitis. This suggests shared therapeutic mechanisms.

---

### Path #9: coronary thrombosis

**Path:**
```
[Carfilzomib] --(0.776)--> [Indomethacin] --(0.484)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6301 |
| Combined Score | 0.4455 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Carfilzomib is similar to Indomethacin, which is associated with coronary thrombosis. This suggests shared therapeutic mechanisms.

---

### Path #10: dyskinesia of esophagus

**Path:**
```
[Carfilzomib] --(0.776)--> [Indomethacin] --(0.483)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6298 |
| Combined Score | 0.4453 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Carfilzomib is similar to Indomethacin, which is associated with dyskinesia of esophagus. This suggests shared therapeutic mechanisms.

---

### Path #11: colonic neoplasm

**Path:**
```
[Carfilzomib] --(0.776)--> [Indomethacin] --(0.480)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6281 |
| Combined Score | 0.4442 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Carfilzomib is similar to Indomethacin, which is associated with colonic neoplasm. This suggests shared therapeutic mechanisms.

---

### Path #12: parkinsonian disorder

**Path:**
```
[Carfilzomib] --(0.776)--> [Indomethacin] --(0.479)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6278 |
| Combined Score | 0.4439 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Carfilzomib is similar to Indomethacin, which is associated with parkinsonian disorder. This suggests shared therapeutic mechanisms.

---

### Path #13: babesiosis

**Path:**
```
[Carfilzomib] --(0.712)--> [Quinine] --(0.543)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6271 |
| Combined Score | 0.4435 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Carfilzomib is similar to Quinine, which is associated with babesiosis. This suggests shared therapeutic mechanisms.

---

### Path #14: liver disease

**Path:**
```
[Carfilzomib] --(0.776)--> [Indomethacin] --(0.476)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6265 |
| Combined Score | 0.4430 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Carfilzomib is similar to Indomethacin, which is associated with liver disease. This suggests shared therapeutic mechanisms.

---

### Path #15: myasthenia gravis

**Path:**
```
[Carfilzomib] --(0.712)--> [Quinine] --(0.540)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6261 |
| Combined Score | 0.4427 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Carfilzomib is similar to Quinine, which is associated with myasthenia gravis. This suggests shared therapeutic mechanisms.

---

### Path #16: pyoureter

**Path:**
```
[Carfilzomib] --(0.776)--> [Indomethacin] --(0.475)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6259 |
| Combined Score | 0.4425 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Carfilzomib is similar to Indomethacin, which is associated with pyoureter. This suggests shared therapeutic mechanisms.

---

### Path #17: hyperaldosteronism

**Path:**
```
[Carfilzomib] --(0.776)--> [Indomethacin] --(0.474)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6255 |
| Combined Score | 0.4423 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Carfilzomib is similar to Indomethacin, which is associated with hyperaldosteronism. This suggests shared therapeutic mechanisms.

---

### Path #18: neuromuscular junction disease

**Path:**
```
[Carfilzomib] --(0.712)--> [Quinine] --(0.539)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6254 |
| Combined Score | 0.4422 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Carfilzomib is similar to Quinine, which is associated with neuromuscular junction disease. This suggests shared therapeutic mechanisms.

---

### Path #19: corneal deposit

**Path:**
```
[Carfilzomib] --(0.776)--> [Indomethacin] --(0.473)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6250 |
| Combined Score | 0.4419 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Carfilzomib is similar to Indomethacin, which is associated with corneal deposit. This suggests shared therapeutic mechanisms.

---

### Path #20: atrial flutter (disease)

**Path:**
```
[Carfilzomib] --(0.712)--> [Quinine] --(0.538)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6247 |
| Combined Score | 0.4417 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Carfilzomib is similar to Quinine, which is associated with atrial flutter (disease). This suggests shared therapeutic mechanisms.

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