# 🔬 Erenumab Path Analysis Report

*Generated: 2025-12-07 14:00:25*

## 1. Drug Profile

| Property | Value |
|----------|-------|
| **Drug ID** | DB14039 |
| **Drug Name** | Erenumab |
| **Type** | drug |

## 2. Path Statistics

| Metric | Value |
|--------|-------|
| **Total Paths** | 100 |
| **Unique Diseases** | 85 |
| **Mean Attention** | 0.5529 |
| **Std Attention** | 0.0583 |
| **Min Attention** | 0.4502 |
| **Max Attention** | 0.7149 |

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
| Mestranol | 0.7314 | 51 |
| Tibolone | 0.6903 | 2 |
| Ethinylestradiol | 0.6823 | 45 |

## 4. Top 20 Paths (by Combined Score)

### Path #1: migraine with or without aura, susceptibility to

**Path:**
```
[Erenumab] --(0.482)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.4818 |
| Combined Score | 0.4818 |
| Confidence | ⭐⭐ Low |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Erenumab may treat migraine with or without aura, susceptibility to based on embedding similarity.

---

### Path #2: migraine disorder

**Path:**
```
[Erenumab] --(0.465)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 1 |
| Avg Attention | 0.4654 |
| Combined Score | 0.4654 |
| Confidence | ⭐⭐ Low |

**Node Types:** `drug` → `disease`

**Interpretation:**

**Direct prediction**: TxGNN predicts Erenumab may treat migraine disorder based on embedding similarity.

---

### Path #3: benign mammary dysplasia

**Path:**
```
[Erenumab] --(0.731)--> [Mestranol] --(0.539)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6354 |
| Combined Score | 0.4493 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Erenumab is similar to Mestranol, which is associated with benign mammary dysplasia. This suggests shared therapeutic mechanisms.

---

### Path #4: neurotic disorder

**Path:**
```
[Erenumab] --(0.731)--> [Mestranol] --(0.538)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6350 |
| Combined Score | 0.4490 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Erenumab is similar to Mestranol, which is associated with neurotic disorder. This suggests shared therapeutic mechanisms.

---

### Path #5: obsolete susceptibility to ischemic stroke

**Path:**
```
[Erenumab] --(0.731)--> [Mestranol] --(0.539)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6351 |
| Combined Score | 0.4490 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Erenumab is similar to Mestranol, which is associated with obsolete susceptibility to ischemic stroke. This suggests shared therapeutic mechanisms.

---

### Path #6: cervical carcinosarcoma

**Path:**
```
[Erenumab] --(0.731)--> [Mestranol] --(0.538)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6349 |
| Combined Score | 0.4489 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Erenumab is similar to Mestranol, which is associated with cervical carcinosarcoma. This suggests shared therapeutic mechanisms.

---

### Path #7: migraine with or without aura, susceptibility to

**Path:**
```
[Erenumab] --(0.731)--> [Mestranol] --(0.538)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6346 |
| Combined Score | 0.4487 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Erenumab is similar to Mestranol, which is associated with migraine with or without aura, susceptibility to. This suggests shared therapeutic mechanisms.

---

### Path #8: cerebral infarction

**Path:**
```
[Erenumab] --(0.731)--> [Mestranol] --(0.537)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6344 |
| Combined Score | 0.4486 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Erenumab is similar to Mestranol, which is associated with cerebral infarction. This suggests shared therapeutic mechanisms.

---

### Path #9: biliary tract disease

**Path:**
```
[Erenumab] --(0.731)--> [Mestranol] --(0.537)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6340 |
| Combined Score | 0.4483 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Erenumab is similar to Mestranol, which is associated with biliary tract disease. This suggests shared therapeutic mechanisms.

---

### Path #10: obstructive jaundice

**Path:**
```
[Erenumab] --(0.731)--> [Mestranol] --(0.536)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6336 |
| Combined Score | 0.4480 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Erenumab is similar to Mestranol, which is associated with obstructive jaundice. This suggests shared therapeutic mechanisms.

---

### Path #11: endometrium neoplasm

**Path:**
```
[Erenumab] --(0.731)--> [Mestranol] --(0.535)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6333 |
| Combined Score | 0.4478 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Erenumab is similar to Mestranol, which is associated with endometrium neoplasm. This suggests shared therapeutic mechanisms.

---

### Path #12: stroke disorder

**Path:**
```
[Erenumab] --(0.731)--> [Mestranol] --(0.535)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6333 |
| Combined Score | 0.4478 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Erenumab is similar to Mestranol, which is associated with stroke disorder. This suggests shared therapeutic mechanisms.

---

### Path #13: coronary artery disease

**Path:**
```
[Erenumab] --(0.731)--> [Mestranol] --(0.533)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6324 |
| Combined Score | 0.4472 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Erenumab is similar to Mestranol, which is associated with coronary artery disease. This suggests shared therapeutic mechanisms.

---

### Path #14: hypertensive disorder

**Path:**
```
[Erenumab] --(0.731)--> [Mestranol] --(0.523)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6271 |
| Combined Score | 0.4434 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Erenumab is similar to Mestranol, which is associated with hypertensive disorder. This suggests shared therapeutic mechanisms.

---

### Path #15: endometriosis of uterus

**Path:**
```
[Erenumab] --(0.731)--> [Mestranol] --(0.518)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6248 |
| Combined Score | 0.4418 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Erenumab is similar to Mestranol, which is associated with endometriosis of uterus. This suggests shared therapeutic mechanisms.

---

### Path #16: cholestasis, intrahepatic, of pregnancy

**Path:**
```
[Erenumab] --(0.731)--> [Mestranol] --(0.518)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6248 |
| Combined Score | 0.4418 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Erenumab is similar to Mestranol, which is associated with cholestasis, intrahepatic, of pregnancy. This suggests shared therapeutic mechanisms.

---

### Path #17: diabetes mellitus (disease)

**Path:**
```
[Erenumab] --(0.731)--> [Mestranol] --(0.517)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6240 |
| Combined Score | 0.4412 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Erenumab is similar to Mestranol, which is associated with diabetes mellitus (disease). This suggests shared therapeutic mechanisms.

---

### Path #18: inherited porphyria

**Path:**
```
[Erenumab] --(0.731)--> [Mestranol] --(0.516)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6238 |
| Combined Score | 0.4411 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Erenumab is similar to Mestranol, which is associated with inherited porphyria. This suggests shared therapeutic mechanisms.

---

### Path #19: hyperlipidemia

**Path:**
```
[Erenumab] --(0.731)--> [Mestranol] --(0.515)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6234 |
| Combined Score | 0.4408 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Erenumab is similar to Mestranol, which is associated with hyperlipidemia. This suggests shared therapeutic mechanisms.

---

### Path #20: hypertriglyceridemia (disease)

**Path:**
```
[Erenumab] --(0.731)--> [Mestranol] --(0.515)--> 
```

| Metric | Value |
|--------|-------|
| Hops | 2 |
| Avg Attention | 0.6233 |
| Combined Score | 0.4407 |
| Confidence | ⭐⭐⭐⭐ High |

**Node Types:** `drug` → `drug` → `disease`

**Interpretation:**

**Drug similarity path**: Erenumab is similar to Mestranol, which is associated with hypertriglyceridemia (disease). This suggests shared therapeutic mechanisms.

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