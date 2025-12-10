# 🔬 Apremilast Path Analysis Report

*Generated: 2025-12-07 14:00:25*

## 1. Drug Profile

| Property | Value |
|----------|-------|
| **Drug ID** | DB05676 |
| **Drug Name** | Apremilast |
| **Type** | drug |

## 2. Path Statistics

| Metric | Value |
|--------|-------|
| **Total Paths** | 100 |
| **Unique Diseases** | 97 |
| **Mean Attention** | 0.5953 |
| **Std Attention** | 0.0693 |
| **Min Attention** | 0.4604 |
| **Max Attention** | 0.7362 |

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
| Diethylstilbestrol | 0.8231 | 79 |
| Edoxaban | 0.8032 | 1 |
| Conjugated estrogens | 0.7732 | 1 |
| Dabigatran etexilate | 0.7617 | 2 |
| Pentoxifylline | 0.7430 | 2 |
| Quinidine | 0.7357 | 11 |
| Rivaroxaban | 0.7255 | 3 |

## 4. Top 20 Paths (by Combined Score)

### Path #1: psoriatic arthritis

**Path:**
```
[Apremilast] --(0.561)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.5615 |
| Combined Score | 0.5615 |
| Confidence | ⭐⭐⭐ Medium |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Apremilast may treat psoriatic arthritis based on embedding similarity.

---

### Path #2: coronary artery disease

**Path:**
```
[Apremilast] --(0.823)--> [Diethylstilbestrol] --(0.577)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6999 |
| Combined Score | 0.4949 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Apremilast is similar to Diethylstilbestrol, which is associated with coronary artery disease. This suggests shared therapeutic mechanisms.

---

### Path #3: ovarian carcinosarcoma

**Path:**
```
[Apremilast] --(0.823)--> [Diethylstilbestrol] --(0.577)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6999 |
| Combined Score | 0.4949 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Apremilast is similar to Diethylstilbestrol, which is associated with ovarian carcinosarcoma. This suggests shared therapeutic mechanisms.

---

### Path #4: stroke disorder

**Path:**
```
[Apremilast] --(0.823)--> [Diethylstilbestrol] --(0.575)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6988 |
| Combined Score | 0.4942 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Apremilast is similar to Diethylstilbestrol, which is associated with stroke disorder. This suggests shared therapeutic mechanisms.

---

### Path #5: malignant dysgerminomatous germ cell tumor of ovary

**Path:**
```
[Apremilast] --(0.823)--> [Diethylstilbestrol] --(0.574)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6986 |
| Combined Score | 0.4940 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Apremilast is similar to Diethylstilbestrol, which is associated with malignant dysgerminomatous germ cell tumor of ovary. This suggests shared therapeutic mechanisms.

---

### Path #6: gallbladder disease

**Path:**
```
[Apremilast] --(0.823)--> [Diethylstilbestrol] --(0.574)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6986 |
| Combined Score | 0.4939 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Apremilast is similar to Diethylstilbestrol, which is associated with gallbladder disease. This suggests shared therapeutic mechanisms.

---

### Path #7: intrinsic asthma

**Path:**
```
[Apremilast] --(0.823)--> [Diethylstilbestrol] --(0.574)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6984 |
| Combined Score | 0.4938 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Apremilast is similar to Diethylstilbestrol, which is associated with intrinsic asthma. This suggests shared therapeutic mechanisms.

---

### Path #8: hypertriglyceridemia (disease)

**Path:**
```
[Apremilast] --(0.823)--> [Diethylstilbestrol] --(0.574)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6984 |
| Combined Score | 0.4938 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Apremilast is similar to Diethylstilbestrol, which is associated with hypertriglyceridemia (disease). This suggests shared therapeutic mechanisms.

---

### Path #9: myofibroma

**Path:**
```
[Apremilast] --(0.823)--> [Diethylstilbestrol] --(0.574)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6983 |
| Combined Score | 0.4938 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Apremilast is similar to Diethylstilbestrol, which is associated with myofibroma. This suggests shared therapeutic mechanisms.

---

### Path #10: uterine corpus leiomyoma

**Path:**
```
[Apremilast] --(0.823)--> [Diethylstilbestrol] --(0.573)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6981 |
| Combined Score | 0.4936 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Apremilast is similar to Diethylstilbestrol, which is associated with uterine corpus leiomyoma. This suggests shared therapeutic mechanisms.

---

### Path #11: obsolete susceptibility to ischemic stroke

**Path:**
```
[Apremilast] --(0.823)--> [Diethylstilbestrol] --(0.572)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6975 |
| Combined Score | 0.4932 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Apremilast is similar to Diethylstilbestrol, which is associated with obsolete susceptibility to ischemic stroke. This suggests shared therapeutic mechanisms.

---

### Path #12: hypothyroidism

**Path:**
```
[Apremilast] --(0.823)--> [Diethylstilbestrol] --(0.572)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6974 |
| Combined Score | 0.4931 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Apremilast is similar to Diethylstilbestrol, which is associated with hypothyroidism. This suggests shared therapeutic mechanisms.

---

### Path #13: endometrium neoplasm

**Path:**
```
[Apremilast] --(0.823)--> [Diethylstilbestrol] --(0.571)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6972 |
| Combined Score | 0.4930 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Apremilast is similar to Diethylstilbestrol, which is associated with endometrium neoplasm. This suggests shared therapeutic mechanisms.

---

### Path #14: myxedema

**Path:**
```
[Apremilast] --(0.823)--> [Diethylstilbestrol] --(0.571)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6969 |
| Combined Score | 0.4928 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Apremilast is similar to Diethylstilbestrol, which is associated with myxedema. This suggests shared therapeutic mechanisms.

---

### Path #15: ovarian small cell carcinoma

**Path:**
```
[Apremilast] --(0.823)--> [Diethylstilbestrol] --(0.571)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6968 |
| Combined Score | 0.4927 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Apremilast is similar to Diethylstilbestrol, which is associated with ovarian small cell carcinoma. This suggests shared therapeutic mechanisms.

---

### Path #16: dementia (disease)

**Path:**
```
[Apremilast] --(0.823)--> [Diethylstilbestrol] --(0.571)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6968 |
| Combined Score | 0.4927 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Apremilast is similar to Diethylstilbestrol, which is associated with dementia (disease). This suggests shared therapeutic mechanisms.

---

### Path #17: congestive heart failure

**Path:**
```
[Apremilast] --(0.823)--> [Diethylstilbestrol] --(0.570)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6966 |
| Combined Score | 0.4926 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Apremilast is similar to Diethylstilbestrol, which is associated with congestive heart failure. This suggests shared therapeutic mechanisms.

---

### Path #18: theca steroid-producing cell malignant tumor of ovary, not further specified

**Path:**
```
[Apremilast] --(0.823)--> [Diethylstilbestrol] --(0.570)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6963 |
| Combined Score | 0.4924 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Apremilast is similar to Diethylstilbestrol, which is associated with theca steroid-producing cell malignant tumor of ovary, not further specified. This suggests shared therapeutic mechanisms.

---

### Path #19: migraine with or without aura, susceptibility to

**Path:**
```
[Apremilast] --(0.823)--> [Diethylstilbestrol] --(0.569)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6962 |
| Combined Score | 0.4923 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Apremilast is similar to Diethylstilbestrol, which is associated with migraine with or without aura, susceptibility to. This suggests shared therapeutic mechanisms.

---

### Path #20: prostate cancer

**Path:**
```
[Apremilast] --(0.823)--> [Diethylstilbestrol] --(0.568)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6958 |
| Combined Score | 0.4920 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Apremilast is similar to Diethylstilbestrol, which is associated with prostate cancer. This suggests shared therapeutic mechanisms.

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