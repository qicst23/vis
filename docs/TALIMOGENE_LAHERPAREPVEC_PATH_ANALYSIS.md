# 🔬 Talimogene laherparepvec Path Analysis Report

*Generated: 2025-12-07 14:00:25*

## 1. Drug Profile

| Property | Value |
|----------|-------|
| **Drug ID** | DB13896 |
| **Drug Name** | Talimogene laherparepvec |
| **Type** | drug |

## 2. Path Statistics

| Metric | Value |
|--------|-------|
| **Total Paths** | 100 |
| **Unique Diseases** | 47 |
| **Mean Attention** | 0.6338 |
| **Std Attention** | 0.0644 |
| **Min Attention** | 0.4796 |
| **Max Attention** | 0.7390 |

### Paths by Hop Count

| Hops | Count |
|------|-------|
| 1 | 2 |
| 2 | 4 |
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
| Darbepoetin alfa | 0.7265 | 98 |

## 4. Top 20 Paths (by Combined Score)

### Path #1: melanoma

**Path:**
```
[Talimogene laherparepvec] --(0.514)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.5139 |
| Combined Score | 0.5139 |
| Confidence | ⭐⭐⭐ Medium |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Talimogene laherparepvec may treat melanoma based on embedding similarity.

---

### Path #2: melanoma

**Path:**
```
[Talimogene laherparepvec] --(0.514)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.5139 |
| Combined Score | 0.5139 |
| Confidence | ⭐⭐⭐ Medium |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Talimogene laherparepvec may treat melanoma based on embedding similarity.

---

### Path #3: hypertensive disorder

**Path:**
```
[Talimogene laherparepvec] --(0.727)--> [Darbepoetin alfa] --(0.554)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6401 |
| Combined Score | 0.4526 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Talimogene laherparepvec is similar to Darbepoetin alfa, which is associated with hypertensive disorder. This suggests shared therapeutic mechanisms.

---

### Path #4: hypertensive disorder

**Path:**
```
[Talimogene laherparepvec] --(0.727)--> [Darbepoetin alfa] --(0.554)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6401 |
| Combined Score | 0.4526 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Talimogene laherparepvec is similar to Darbepoetin alfa, which is associated with hypertensive disorder. This suggests shared therapeutic mechanisms.

---

### Path #5: hypertension

**Path:**
```
[Talimogene laherparepvec] --(0.727)--> [Darbepoetin alfa] --(0.545)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6359 |
| Combined Score | 0.4496 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Talimogene laherparepvec is similar to Darbepoetin alfa, which is associated with hypertension. This suggests shared therapeutic mechanisms.

---

### Path #6: hypertension

**Path:**
```
[Talimogene laherparepvec] --(0.727)--> [Darbepoetin alfa] --(0.545)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6359 |
| Combined Score | 0.4496 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Talimogene laherparepvec is similar to Darbepoetin alfa, which is associated with hypertension. This suggests shared therapeutic mechanisms.

---

### Path #7: myxedema

**Path:**
```
[Talimogene laherparepvec] --(0.727)--> [Darbepoetin alfa] --(0.737)--> [Chlorotrianisene] --(0.534)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 3 |
| Avg Attention | 0.6657 |
| Combined Score | 0.3843 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `drug` → `disease`

**Interpretation:**

**Multi-hop path**: Talimogene laherparepvec connects to myxedema through 2 intermediate nodes: Darbepoetin alfa → Chlorotrianisene. This represents a complex biological relationship requiring further validation.

---

### Path #8: myxedema

**Path:**
```
[Talimogene laherparepvec] --(0.727)--> [Darbepoetin alfa] --(0.737)--> [Chlorotrianisene] --(0.534)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 3 |
| Avg Attention | 0.6657 |
| Combined Score | 0.3843 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `drug` → `disease`

**Interpretation:**

**Multi-hop path**: Talimogene laherparepvec connects to myxedema through 2 intermediate nodes: Darbepoetin alfa → Chlorotrianisene. This represents a complex biological relationship requiring further validation.

---

### Path #9: systemic lupus erythematosus (disease)

**Path:**
```
[Talimogene laherparepvec] --(0.727)--> [Darbepoetin alfa] --(0.737)--> [Chlorotrianisene] --(0.532)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 3 |
| Avg Attention | 0.6653 |
| Combined Score | 0.3841 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `drug` → `disease`

**Interpretation:**

**Multi-hop path**: Talimogene laherparepvec connects to systemic lupus erythematosus (disease) through 2 intermediate nodes: Darbepoetin alfa → Chlorotrianisene. This represents a complex biological relationship requiring further validation.

---

### Path #10: active peptic ulcer disease

**Path:**
```
[Talimogene laherparepvec] --(0.727)--> [Darbepoetin alfa] --(0.727)--> [Dasatinib] --(0.535)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 3 |
| Avg Attention | 0.6628 |
| Combined Score | 0.3827 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `drug` → `disease`

**Interpretation:**

**Multi-hop path**: Talimogene laherparepvec connects to active peptic ulcer disease through 2 intermediate nodes: Darbepoetin alfa → Dasatinib. This represents a complex biological relationship requiring further validation.

---

### Path #11: active peptic ulcer disease

**Path:**
```
[Talimogene laherparepvec] --(0.727)--> [Darbepoetin alfa] --(0.727)--> [Dasatinib] --(0.535)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 3 |
| Avg Attention | 0.6628 |
| Combined Score | 0.3827 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `drug` → `disease`

**Interpretation:**

**Multi-hop path**: Talimogene laherparepvec connects to active peptic ulcer disease through 2 intermediate nodes: Darbepoetin alfa → Dasatinib. This represents a complex biological relationship requiring further validation.

---

### Path #12: heart failure

**Path:**
```
[Talimogene laherparepvec] --(0.727)--> [Darbepoetin alfa] --(0.727)--> [Dasatinib] --(0.535)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 3 |
| Avg Attention | 0.6629 |
| Combined Score | 0.3827 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `drug` → `disease`

**Interpretation:**

**Multi-hop path**: Talimogene laherparepvec connects to heart failure through 2 intermediate nodes: Darbepoetin alfa → Dasatinib. This represents a complex biological relationship requiring further validation.

---

### Path #13: heart failure

**Path:**
```
[Talimogene laherparepvec] --(0.727)--> [Darbepoetin alfa] --(0.727)--> [Dasatinib] --(0.535)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 3 |
| Avg Attention | 0.6629 |
| Combined Score | 0.3827 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `drug` → `disease`

**Interpretation:**

**Multi-hop path**: Talimogene laherparepvec connects to heart failure through 2 intermediate nodes: Darbepoetin alfa → Dasatinib. This represents a complex biological relationship requiring further validation.

---

### Path #14: blast phase chronic myelogenous leukemia, BCR-ABL1 positive

**Path:**
```
[Talimogene laherparepvec] --(0.727)--> [Darbepoetin alfa] --(0.727)--> [Dasatinib] --(0.535)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 3 |
| Avg Attention | 0.6629 |
| Combined Score | 0.3827 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `drug` → `disease`

**Interpretation:**

**Multi-hop path**: Talimogene laherparepvec connects to blast phase chronic myelogenous leukemia, BCR-ABL1 positive through 2 intermediate nodes: Darbepoetin alfa → Dasatinib. This represents a complex biological relationship requiring further validation.

---

### Path #15: blast phase chronic myelogenous leukemia, BCR-ABL1 positive

**Path:**
```
[Talimogene laherparepvec] --(0.727)--> [Darbepoetin alfa] --(0.727)--> [Dasatinib] --(0.535)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 3 |
| Avg Attention | 0.6629 |
| Combined Score | 0.3827 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `drug` → `disease`

**Interpretation:**

**Multi-hop path**: Talimogene laherparepvec connects to blast phase chronic myelogenous leukemia, BCR-ABL1 positive through 2 intermediate nodes: Darbepoetin alfa → Dasatinib. This represents a complex biological relationship requiring further validation.

---

### Path #16: hypothyroidism

**Path:**
```
[Talimogene laherparepvec] --(0.727)--> [Darbepoetin alfa] --(0.737)--> [Chlorotrianisene] --(0.521)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 3 |
| Avg Attention | 0.6616 |
| Combined Score | 0.3820 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `drug` → `disease`

**Interpretation:**

**Multi-hop path**: Talimogene laherparepvec connects to hypothyroidism through 2 intermediate nodes: Darbepoetin alfa → Chlorotrianisene. This represents a complex biological relationship requiring further validation.

---

### Path #17: hypothyroidism

**Path:**
```
[Talimogene laherparepvec] --(0.727)--> [Darbepoetin alfa] --(0.737)--> [Chlorotrianisene] --(0.521)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 3 |
| Avg Attention | 0.6616 |
| Combined Score | 0.3820 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `drug` → `disease`

**Interpretation:**

**Multi-hop path**: Talimogene laherparepvec connects to hypothyroidism through 2 intermediate nodes: Darbepoetin alfa → Chlorotrianisene. This represents a complex biological relationship requiring further validation.

---

### Path #18: hypertensive disorder

**Path:**
```
[Talimogene laherparepvec] --(0.727)--> [Darbepoetin alfa] --(0.737)--> [Chlorotrianisene] --(0.521)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 3 |
| Avg Attention | 0.6613 |
| Combined Score | 0.3818 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `drug` → `disease`

**Interpretation:**

**Multi-hop path**: Talimogene laherparepvec connects to hypertensive disorder through 2 intermediate nodes: Darbepoetin alfa → Chlorotrianisene. This represents a complex biological relationship requiring further validation.

---

### Path #19: hypertensive disorder

**Path:**
```
[Talimogene laherparepvec] --(0.727)--> [Darbepoetin alfa] --(0.737)--> [Chlorotrianisene] --(0.521)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 3 |
| Avg Attention | 0.6613 |
| Combined Score | 0.3818 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `drug` → `disease`

**Interpretation:**

**Multi-hop path**: Talimogene laherparepvec connects to hypertensive disorder through 2 intermediate nodes: Darbepoetin alfa → Chlorotrianisene. This represents a complex biological relationship requiring further validation.

---

### Path #20: intracerebral hemorrhage

**Path:**
```
[Talimogene laherparepvec] --(0.727)--> [Darbepoetin alfa] --(0.727)--> [Dasatinib] --(0.529)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 3 |
| Avg Attention | 0.6608 |
| Combined Score | 0.3815 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `drug` → `disease`

**Interpretation:**

**Multi-hop path**: Talimogene laherparepvec connects to intracerebral hemorrhage through 2 intermediate nodes: Darbepoetin alfa → Dasatinib. This represents a complex biological relationship requiring further validation.

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