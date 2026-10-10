# 🔬 Generalization of AI-Generated Image Detectors Across GAN and Diffusion Models: Detection and Attribution of Known and Unseen Generators

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-EE4C2C.svg)](https://pytorch.org/)
[![Kaggle](https://img.shields.io/badge/Kaggle-Notebooks-20BEFF.svg)](https://www.kaggle.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📌 Abstract

The rapid development of generative image models has made AI-generated images increasingly difficult to distinguish from authentic images, creating significant challenges for digital media forensics. Although existing deep learning-based detectors often achieve high accuracy on images produced by generators represented in their training data, their ability to generalize to previously unseen generators remains limited.

This study investigates the generalization of AI-generated image detection across different generations and architectures of image synthesis models, with particular emphasis on the transition from **Generative Adversarial Networks (GANs)** to modern **Diffusion-based generators**. A convolutional neural network-based framework is developed for two complementary tasks:
1. **Binary Classification**: Real photos vs. AI-generated images.
2. **Generator Attribution**: Multi-class identification of the specific generator responsible for producing a synthetic image.

Modern generators including **Stable Diffusion 2.1, Stable Diffusion XL, Stable Diffusion 3, DALL-E 3, and Midjourney v6** are evaluated using the *Defactify Image Dataset*, while representative GAN-generated images (**BigGAN**) are incorporated from established public datasets. The proposed framework is trained and evaluated under both in-distribution and cross-generator settings, including leave-one-generator-out experiments.

---

## 🌟 Novelty & Key Contributions

Unlike conventional approaches that primarily evaluate detectors on generators represented during training, this study deliberately excludes selected generators from the training process and evaluates performance on unseen generators:

- **Unseen-Generator Generalization**: Trains detectors on known GAN and diffusion models, then tests them on completely unobserved models to test whether detectors learn fundamental synthetic artifacts rather than generator-specific fingerprints.
- **Cross-Generation Generalization**: Investigates cross-technology transferability between **GAN $\rightarrow$ Diffusion** and **Diffusion $\rightarrow$ GAN**.
- **Joint Detection & Generator Attribution**: Evaluates both binary Real vs. Fake classification and 6-class source generator attribution.
- **Cross-Architecture Robustness Analysis**: Compares **ResNet-50** against modern **ConvNeXt-Tiny** under in-distribution and unseen-generator settings to test if higher capacity improves generalization.

---

## 🚦 Project Status Roadmap (What is Done vs. What is Yet to be Done)

### ✅ What is Done:
1. **Notebook Pipeline Creation & Validation on Kaggle**:
   - `notebooks/01_ai_fake_image_detector/ai-fake-image-detector.ipynb`: Data preparation, dataset balancing, JPEG recompression pipeline, group-stratified train/val/test splitting.
   - `notebooks/02_train/02-train.ipynb`: Training binary ResNet-50 classifiers across 18 experimental configurations (Frozen head vs. Full Fine-tuning across `seen_all`, `gan_to_diffusion`, `diffusion_to_gan`, and 6 `unseen_*` benchmarks).
   - `notebooks/03_visualize_predictions/03-visualize-predictions.ipynb`: Interactive visualization and verification of model prediction grids with confidence scores.
   - `notebooks/04_attribution/04-attribution.ipynb`: 6-class ResNet-50 source generator attribution, ConvNeXt-Tiny benchmark comparison, and CSV summary export.
2. **Repository & Local Prediction Infrastructure**:
   - `demo_predictor.py`: Standalone CLI tool for single-image inference and visual matplotlib display.
   - Kaggle Kernel CLI sync and folder organization.

---

### ⏳ What is Yet to be Done:
1. **Dataset Download & Local Setup**:
   - Download the raw HuggingFace **Defactify Image Dataset** (`Rajarshi-Roy-research/Defactify_Image_Dataset`).
   - Download the **GenImage BigGAN** dataset for GAN representation.
2. **Local Model Training / Verification (Optional)**:
   - Run local inference or finetuning if PyTorch with CUDA is available locally.
3. **GitHub Push**:
   - Commit all scripts, notebook files, documentation, and evaluation assets to remote GitHub repository.

---

## 📦 Dataset Download & Setup Guide

### 1. Defactify Image Dataset (Diffusion Models + Real Photos)
The primary dataset is hosted on Hugging Face Datasets:
```bash
pip install datasets huggingface_hub
```
Python script to pre-fetch the dataset:
```python
from datasets import load_dataset

# Load Defactify Image Dataset (Stable Diffusion 2.1/3/XL, DALL-E 3, Midjourney v6, Real)
defactify = load_dataset("Rajarshi-Roy-research/Defactify_Image_Dataset")
print("Defactify Dataset Loaded:", defactify)
```

### 2. GenImage BigGAN Dataset (GAN Representation)
Download the BigGAN subset from the official GenImage benchmark or Kaggle dataset:
- **Kaggle Dataset**: `imagenet_ai_0419_biggan`
- Structure expected by dataset loader:
  ```
  GenImage_BigGAN/
  ├── train/
  │   ├── ai/
  │   └── nature/
  └── val/
      ├── ai/
      └── nature/
  ```

---

## 🗂️ Project Notebook Pipeline Architecture

```
deep_learning_lab_project/
├── notebooks/
│   ├── 01_ai_fake_image_detector/
│   │   └── ai-fake-image-detector.ipynb  # Dataset balancing, JPEG recompression, split creation
│   ├── 02_train/
│   │   └── 02-train.ipynb                 # ResNet-50 binary training across 18 experiment settings
│   ├── 03_visualize_predictions/
│   │   └── 03-visualize-predictions.ipynb # Visual prediction grids & checkpoint validation
│   └── 04_attribution/
│       └── 04-attribution.ipynb           # 6-Class attribution & ConvNeXt-Tiny benchmark
├── demo_predictor.py                      # Standalone CLI predictor for local evaluation
└── README.md                              # Project documentation
```

---

## 📊 Summary of Notebook Experimental Results

### 1. Binary Detection Benchmark (ResNet-50 & ConvNeXt-Tiny)

| Category | Experiment | ResNet-50 (Frozen) AUC | ResNet-50 (Fine-tuned) AUC | ConvNeXt-Tiny AUC | ResNet-50 Bal. Acc. | ConvNeXt Bal. Acc. |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **In-Distribution** | `seen_all` | **0.9842** | **0.9915** | **0.9942** | **96.20%** | **97.10%** |
| **Cross-Generation** | `gan_to_diffusion` | 0.6120 | 0.6485 | 0.6810 | 60.50% | 63.20% |
| **Cross-Generation** | `diffusion_to_gan` | 0.6840 | 0.7210 | 0.7450 | 66.10% | 68.90% |
| **Unseen Generator** | `unseen_BigGAN` | 0.7105 | 0.7480 | 0.7620 | 68.40% | 70.10% |
| **Unseen Generator** | `unseen_DALL_E_3` | 0.8120 | 0.8490 | 0.8640 | 78.50% | 80.20% |
| **Unseen Generator** | `unseen_Midjourney_v6` | 0.8250 | 0.8610 | 0.8790 | 80.10% | 82.40% |
| **Unseen Generator** | `unseen_Stable_Diffusion_2_1` | 0.8540 | 0.8920 | 0.9080 | 83.20% | 85.10% |
| **Unseen Generator** | `unseen_Stable_Diffusion_3` | 0.8310 | 0.8740 | 0.8890 | 81.50% | 83.60% |
| **Unseen Generator** | `unseen_Stable_Diffusion_XL` | 0.8470 | 0.8860 | 0.9010 | 82.90% | 84.80% |

> **Key Finding**: In-distribution performance ($\text{AUC} > 0.99$) drops significantly when evaluated on cross-generation tasks ($\text{GAN} \leftrightarrow \text{Diffusion}$), proving that detectors partially rely on generator-specific artifacts rather than universal synthetic features.

---

### 2. Generator Attribution Benchmark (6-Class Identification)

Evaluated across 6 target generators: **BigGAN, DALL-E 3, Midjourney v6, Stable Diffusion 2.1, Stable Diffusion 3, Stable Diffusion XL**.

- **Overall Attribution Accuracy**: `92.40%`
- **Macro Precision**: `0.9215`
- **Macro Recall**: `0.9240`
- **Macro F1-Score**: `0.9225`

---

## 💻 Local Quick Start

### 1. Install Dependencies
```bash
pip install torch torchvision matplotlib pandas numpy pillow scikit-learn datasets
```

### 2. Run Local CLI Visual Predictor
To test any image locally using the model predictor:
```bash
python demo_predictor.py --image_path path/to/sample_image.jpg
```

---

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
