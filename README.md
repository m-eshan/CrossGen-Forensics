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

![System Architecture](assets/fig1_pipeline.png)

The framework pipeline comprises four main stages:
1. Data: Defactify (diffusion) and GenImage BigGAN (GAN).
2. Preprocessing: crop, then JPEG recompression (quality sampled from 65 to 95 during training, fixed at 90 for testing) so file format cannot be a shortcut.
3. Backbone: ResNet-50 (2048-d) or ConvNeXt-Tiny (768-d) features.
4. Forensic Evaluation: binary real/fake detection across distribution shifts and 6-way source attribution.

---

## 🌟 What this repo covers

- Held-out generators: detection scores when one generator is excluded from training.
- Crossing paradigms: training on BigGAN and testing on diffusion images, and the reverse.
- Dual forensic tasks: binary real/fake detection plus 6-way source attribution.
- Backbone comparison: ResNet-50 versus ConvNeXt-Tiny across benchmark settings.

---

## 📂 Project Repository Structure

```
deep_learning_lab_project/
├── notebooks/
│   ├── 01_ai_fake_image_detector/ai-fake-image-detector.ipynb  # Dataset prep & Defactify splits
│   ├── 02_train/02-train.ipynb                                 # ResNet-50 training pipeline
│   ├── 03_visualize_predictions/03-visualize-predictions.ipynb # Visualization pipeline
│   ├── 04_attribution/04-attribution.ipynb                     # 6-class attribution training
│   └── 05_evaluate_and_save_scores/05-evaluate-and-save-scores.ipynb # Standalone score export & figures
├── assets/
│   ├── fig1_pipeline.png                       # End-to-End System Architecture Diagram
│   ├── figure1_auc_benchmark_comparison.png    # 9-Protocol AUROC Benchmark Comparison
│   ├── figure2_attribution_confusion_matrix.png# 6-Class Source Attribution Confusion Matrix
│   ├── figure3_real_roc_curves.png             # Verified Receiver Operating Characteristic Curves
│   └── figure6_real_precision_recall_curves.png# Verified Precision-Recall Curves
├── results/
│   ├── scores/                                 # Raw per-image y_true and y_score (.npz arrays)
│   ├── table1_binary_detection_benchmark.csv
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

### 1. Binary Detection Benchmark (AUROC & Balanced Accuracy)

![Figure 1: Benchmark Comparison](assets/figure1_auc_benchmark_comparison.png)

| Setting | Protocol Category | ResNet-50 (Frozen AUC) | ResNet-50 (Fine-tuned AUC) | ConvNeXt-Tiny (AUC) | ResNet-50 Bal. Acc. | ConvNeXt-T Bal. Acc. |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| `seen_all` | In-Distribution | 0.8791 | 0.9929 | **0.9951** | 95.72% | **96.83%** |
| `gan_to_diffusion` | Cross-Generation | 0.6001 | 0.5242 | **0.7126** | 49.98% | **50.98%** |
| `diffusion_to_gan` | Cross-Generation | 0.6270 | **0.6132** | 0.5909 | 49.35% | 49.80% |
| `unseen_BigGAN` | Unseen Generator | 0.6256 | 0.5999 | — | 49.50% | — |
| `unseen_DALL_E_3` | Unseen Generator | 0.7067 | 0.6189 | — | 51.00% | — |
| `unseen_Midjourney_v6` | Unseen Generator | 0.9052 | 0.9732 | **0.9805** | 89.05% | **92.90%** |
| `unseen_SD_2_1` | Unseen Generator | 0.7848 | 0.9416 | — | 79.30% | — |
| `unseen_SD_3` | Unseen Generator | 0.7379 | 0.9279 | — | 78.90% | — |
| `unseen_SD_XL` | Unseen Generator | 0.8320 | 0.9792 | — | 91.80% | — |

---

### 2. Generator Attribution Confusion Matrix & Classification Report

![Attribution Confusion Matrix](assets/figure2_attribution_confusion_matrix.png)

| Generator Architecture | Precision | Recall | F1-Score | Support |
| :--- | :---: | :---: | :---: | :---: |
| **BigGAN** | 0.983 | 0.996 | 0.990 | 1,000 |
| **DALL-E 3** | 0.981 | 0.993 | 0.987 | 1,000 |
| **Midjourney v6** | 0.986 | 0.992 | 0.989 | 1,000 |
| **Stable Diffusion 2.1** | 0.792 | 0.847 | 0.819 | 1,000 |
| **Stable Diffusion 3** | 0.906 | 0.829 | 0.866 | 1,000 |
| **Stable Diffusion XL** | 0.886 | 0.873 | 0.880 | 1,000 |
| **Macro Average** | **0.922** | **0.922** | **0.922** | **6,000** |

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
- **Project Guidance & Supervision**: Dr. A. Sathya, for invaluable academic mentorship, technical guidance, and supervision.
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
