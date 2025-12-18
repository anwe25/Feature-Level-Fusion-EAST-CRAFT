# Feature-Level Fusion for Scene Text Detection

This project implements **feature-level fusion** as an ensemble technique using  
**EAST** and **CRAFT** text detection models to improve scene text detection performance
on natural scene images.

---

## 🔹 Overview
- **EAST** provides fast, coarse text region proposals  
- **CRAFT** provides fine-grained character-level confidence maps  
- Both feature maps are **aligned, normalised, and fused at feature level**
- The fused map is post-processed to generate final text bounding boxes

---

## 🔹 Methodology
1. Input images are passed independently through EAST and CRAFT
2. Feature maps are resized to a common spatial resolution
3. Normalisation is applied to both feature maps
4. Feature-level fusion is performed using weighted averaging
5. Thresholding and morphological operations are applied
6. Final text regions are obtained using contour-based bounding boxes

---

## 🔹 Dataset
- **ICDAR 2015 Scene Text Dataset**
- Evaluation performed on **500 images**

---

## 🔹 Evaluation Metrics
The performance is evaluated using ICDAR-style pixel-level metrics:
- Precision  
- Recall  
- F1-score  

### Results (500 Images)

| Metric    | Value |
|---------- |------ |
| Precision | 0.63  |
| Recall    | 0.28  |
| F1-score  | 0.39  |

---

## 🔹 Qualitative Results (Sample Outputs)

Below are sample detection results showing **prominent red bounding boxes**
obtained after feature-level fusion of EAST and CRAFT:

### Image 1
![Fusion Result 1](images/fusion_image1.png)

### Image 2
![Fusion Result 2](images/fusion_image2.png)

### Image 3
![Fusion Result 3](images/fusion_image3.png)

### Image 4
![Fusion Result 4](images/fusion_image4.png)

### Image 5
![Fusion Result 5](images/fusion_image5.png)


## 🔹 Key Highlights
- Feature-level fusion improves robustness compared to individual models
- Better localisation of scene text under complex backgrounds
- Demonstrates practical ensemble learning for computer vision tasks

---

## 🔹 Tools & Technologies
- Python
- OpenCV
- PyTorch
- EAST Text Detector
- CRAFT Text Detector

---

## 🔹 Author
**Anwesha Guha**  
B.Tech (AIML)  
Netaji Subhash Engineering College, Kolkata
