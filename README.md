# Feature-Level Fusion using EAST and CRAFT

# Overview
This project implements feature-level fusion, an ensemble learning technique, for scene text detection by combining two pretrained models:

EAST for global text region detection
CRAFT for character-level text detection
The goal is to improve robustness by fusing intermediate feature maps instead of relying on a single model.

# Dataset
~ ICDAR 2015 Scene Text Dataset
~ Evaluation performed on 500 images

# Method
-Extract text confidence map from EAST
-Extract character region map from CRAFT
-Align and normalize both feature maps
-Fuse features using weighted summation
-Generate final text mask by thresholding

# Evaluation Metrics

Precision
Recall
F1-score

# Results (500 Images)

| Metric    | Value |
| --------- | ----- |
| Precision | 0.63  |
| Recall    | 0.28  |
| F1-score  | 0.39  |

