# Feature-Level Fusion for Scene Text Detection

This project implements **feature-level fusion** as an ensemble technique using  
**EAST** and **CRAFT** text detection models to improve scene text detection performance.

## 🔹 Methodology
- EAST provides fast coarse text region scores
- CRAFT provides fine-grained character-level confidence maps
- Both feature maps are **aligned, normalized, and fused at feature level**
- Fusion is performed using weighted averaging before thresholding

## 🔹 Dataset
- ICDAR 2015 Scene Text Dataset
- Evaluation performed on **500 images**

## 🔹 Evaluation Metrics
- Precision
- Recall
- F1-score (ICDAR-style pixel-level evaluation)

# Results (500 Images)

| Metric    | Value |
| --------- | ----- |
| Precision | 0.63  |
| Recall    | 0.28  |
| F1-score  | 0.39  |

