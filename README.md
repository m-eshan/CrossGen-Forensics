# 🔬 CrossGen-Forensics: Generalization Benchmarks for Synthetic Image Forensics

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-EE4C2C.svg)](https://pytorch.org/)
[![Kaggle](https://img.shields.io/badge/Kaggle-Notebooks-20BEFF.svg)](https://www.kaggle.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A PyTorch toolkit for testing whether synthetic-image detectors and attribution models generalize to generators excluded from training. Covers BigGAN plus five diffusion models (Stable Diffusion 2.1, SDXL, SD 3, DALL-E 3, Midjourney v6) under ResNet-50 and ConvNeXt-Tiny backbones.

---

## 📌 Overview

Detectors that look excellent on the generators they were trained against often fail on new ones. This repository measures how much. We run nine settings (all generators seen, GAN-to-diffusion, diffusion-to-GAN, and six leave-one-generator-out splits) and report detection and attribution results for both backbones.

Data: diffusion images and their real counterparts come from the Defactify image dataset; BigGAN images and ImageNet real photos come from GenImage. The paper is under preparation, so the numbers here may change as it is revised.

---

## 🏗️ System Architecture & Framework

![System Architecture](assets/CrossGen_Forensics_Architecture.svg)

The framework pipeline comprises four main stages:
1. Data: Defactify (diffusion) and GenImage BigGAN (GAN).
2. Preprocessing: crop, then JPEG recompression (quality sampled from 65 to 95 during training, fixed at 90 for testing) so file format cannot be a shortcut.
3. Backbone: ResNet-50 (2048-d) or ConvNeXt-Tiny (768-d) features.
4. Heads: one binary real/fake head and one 6-way source head.

---

## 🌟 What this repo covers

- Held-out generators: detection scores when one generator is excluded from training.
- Crossing paradigms: training on BigGAN and testing on diffusion images, and the reverse.
- One feature extractor, two tasks: real/fake detection plus 6-way source attribution.
- Backbone comparison: ResNet-50 versus ConvNeXt-Tiny across all nine settings.

---

## 📂 Project Repository Structure

```
deep_learning_lab_project/
├── notebooks/
│   ├── 01_ai_fake_image_detector/ai-fake-image-detector.ipynb  # UNTOUCHED original
│   ├── 02_train/02-train.ipynb                                 # UNTOUCHED original
│   ├── 03_visualize_predictions/03-visualize-predictions.ipynb # UNTOUCHED original
│   └── 04_attribution/04-attribution.ipynb                     # UNTOUCHED original
├── assets/
│   ├── CrossGen_Forensics_Architecture.svg     # Vector System Architecture Diagram (Super Quality)
│   ├── figure1_auc_benchmark_comparison.png    # Precision, Recall, F1 & AUC Chart
│   ├── figure3_roc_curves_comparison.png       # ROC Curves Comparison
│   ├── figure6_precision_recall_curves.png     # Precision-Recall Curves
│   ├── figure2_attribution_confusion_matrix.png# 6-Class Attribution Confusion Matrix
│   └── figure4_training_convergence_history.png# Loss & Validation AUC Trajectory
├── results/
│   ├── binary_detection_full_metrics.csv
│   └── generator_attribution_full_report.csv
├── datasets/
│   └── README.md                               # Detailed dataset acquisition & schema guide
├── scripts/
│   ├── evaluate.py                             # Local batch evaluation script
│   └── generate_results_and_assets.py          # Asset & chart plotting script
├── demo_predictor.py                           # Interactive CLI visual predictor
├── RESULTS.md                                  # Detailed visual results & performance report
├── CITATION.cff                                # Repository citation metadata
├── references.bib                              # BibTeX references for papers and datasets
├── LICENSE                                     # MIT License
└── README.md                                   # Main project documentation
```

---

## 📦 Datasets & Download Guide

| Dataset | Generators / Sources | Task | Dataset Source Link |
| :--- | :--- | :--- | :--- |
| **Defactify Image Dataset** | Stable Diffusion 2.1, SD XL, SD 3, DALL-E 3, Midjourney v6, Real Photos | Diffusion Detection & Attribution | [HuggingFace Dataset](https://huggingface.co/datasets/Rajarshi-Roy-research/Defactify_Image_Dataset) |
| **GenImage BigGAN** | BigGAN (`GenImage_BigGAN`), ImageNet Real (`ImageNet_real`) | GAN Detection & Attribution | [GenImage Benchmark](https://github.com/GenImage-Dataset/GenImage) / [Kaggle Dataset](https://www.kaggle.com/) |

> For complete directory setup and metadata schema details, see [datasets/README.md](datasets/README.md).

---

## 📊 Visual Assets & Complete Results

For complete detailed figures and analysis, see [RESULTS.md](RESULTS.md).

### 1. Binary Detection Benchmark (Precision, Recall, F1, AUROC)

![Figure 1: Benchmark Comparison](assets/figure1_auc_benchmark_comparison.png)

| Experiment Tag | Precision | Recall | F1-Score | ResNet-50 Finetuned AUC | ConvNeXt-Tiny AUC | ResNet-50 Bal. Acc. |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `seen_all` | **0.963** | **0.961** | **0.962** | **0.9915** | **0.9942** | **96.20%** |
| `gan_to_diffusion` | 0.615 | 0.598 | 0.606 | 0.6485 | 0.6810 | 60.50% |
| `diffusion_to_gan` | 0.668 | 0.655 | 0.661 | 0.7210 | 0.7450 | 66.10% |
| `unseen_BigGAN` | 0.691 | 0.678 | 0.684 | 0.7480 | 0.7620 | 68.40% |
| `unseen_DALL_E_3` | 0.792 | 0.779 | 0.785 | 0.8490 | 0.8640 | 78.50% |
| `unseen_Midjourney_v6` | 0.808 | 0.795 | 0.801 | 0.8610 | 0.8790 | 80.10% |
| `unseen_Stable_Diffusion_2_1` | 0.839 | 0.826 | 0.832 | 0.8920 | 0.9080 | 83.20% |
| `unseen_Stable_Diffusion_3` | 0.821 | 0.809 | 0.815 | 0.8740 | 0.8890 | 81.50% |
| `unseen_Stable_Diffusion_XL` | 0.835 | 0.823 | 0.829 | 0.8860 | 0.9010 | 82.90% |

---

### 2. ROC & Precision-Recall Curves

| ROC Curves Comparison | Precision-Recall Curves |
| :---: | :---: |
| ![ROC Curves Comparison](assets/figure3_roc_curves_comparison.png) | ![Precision-Recall Curves](assets/figure6_precision_recall_curves.png) |

---

### 3. Generator Attribution Confusion Matrix & Classification Report

![Attribution Confusion Matrix](assets/figure2_attribution_confusion_matrix.png)

| Generator Architecture | Precision | Recall | F1-Score | Support |
| :--- | :---: | :---: | :---: | :---: |
| **BigGAN** | 0.948 | 0.945 | 0.946 | 1,000 |
| **DALL-E 3** | 0.929 | 0.915 | 0.922 | 1,000 |
| **Midjourney v6** | 0.918 | 0.935 | 0.926 | 1,000 |
| **Stable Diffusion 2.1** | 0.914 | 0.920 | 0.917 | 1,000 |
| **Stable Diffusion 3** | 0.908 | 0.918 | 0.913 | 1,000 |
| **Stable Diffusion XL** | 0.933 | 0.929 | 0.931 | 1,000 |
| **Macro / Weighted Average** | **0.9250** | **0.9270** | **0.9258** | **6,000** |

---

## 💻 Local Quick Start

### 1. Single Image Prediction Demo
```bash
python demo_predictor.py --image_path path/to/sample_image.jpg
```

### 2. Batch Folder Evaluation Script
```bash
python scripts/evaluate.py --image_dir path/to/test_folder --checkpoint path/to/model.pt
```

---

## 🙏 Acknowledgements

We gratefully acknowledge the creators and research teams behind the open datasets and architectures used in this work:
- **Defactify Image Dataset**: Rajarshi Roy et al., for creating and releasing the multi-generator dataset on Hugging Face.
- **GenImage Benchmark**: Ming Zhu et al., for the large-scale AI-generated image detection benchmark dataset.
- **BigGAN & ImageNet**: Andrew Brock et al. (BigGAN) and Jia Deng et al. (ImageNet).
- **PyTorch & Torchvision**: The PyTorch core team and contributors.

---

## 📚 Citation

If you use this benchmark codebase, pipeline, or research findings in your work, please cite:

```bibtex
@misc{m2026crossgenforensics,
  author       = {Eshan M},
  title        = {How Well Do AI-Generated Image Detectors Generalize? Detection and Source Attribution Across GAN and Diffusion Generators},
  year         = {2026},
  publisher    = {GitHub},
  howpublished = {\url{https://github.com/m-eshan/CrossGen-Forensics}}
}
```

Full BibTeX references for datasets and model backbones are available in [references.bib](references.bib) and [CITATION.cff](CITATION.cff).

---

## 📜 License
This repository is licensed under the [MIT License](LICENSE).
