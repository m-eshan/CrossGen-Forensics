"""
Script to generate verified benchmark figures and reports from real evaluation files.
"""

import os
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 10

ASSETS_DIR = "assets"
RESULTS_DIR = "results"
os.makedirs(ASSETS_DIR, exist_ok=True)
os.makedirs(RESULTS_DIR, exist_ok=True)

# ---------------------------------------------------------
# 1. PLOT: BINARY DETECTION AUROC COMPARISON (FIGURE 1)
# ---------------------------------------------------------
bench_csv = os.path.join(RESULTS_DIR, "table1_binary_detection_benchmark.csv")
if not os.path.exists(bench_csv):
    bench_csv = os.path.join(RESULTS_DIR, "binary_detection_benchmark.csv")

df = pd.read_csv(bench_csv)
exp_map = {
    'unseen_Stable_Diffusion_2_1': 'unseen_SD_2_1',
    'unseen_Stable_Diffusion_3': 'unseen_SD_3',
    'unseen_Stable_Diffusion_XL': 'unseen_SD_XL'
}
df['Display_Exp'] = df['Experiment'].replace(exp_map)

fig, ax = plt.subplots(figsize=(11, 5.5))
x = np.arange(len(df))
width = 0.28

r1 = ax.bar(x - width, df['ResNet50_Frozen_AUC'], width, label='ResNet-50 (Frozen)', color='#90caf9', edgecolor='#1976d2', linewidth=0.5)
r2 = ax.bar(x,         df['ResNet50_Finetuned_AUC'], width, label='ResNet-50 (Fine-tuned)', color='#1e88e5', edgecolor='#0d47a1', linewidth=0.5)

conv_vals = df['ConvNeXt_Tiny_AUC'].fillna(0).values
r3 = ax.bar(x + width, conv_vals, width, label='ConvNeXt-Tiny', color='#0d47a1', edgecolor='#002171', linewidth=0.5)

ax.set_ylabel('ROC-AUC Score', fontsize=11, fontweight='bold')
ax.set_title('Detection AUROC Performance Across Evaluation Protocols', fontsize=12, fontweight='bold', pad=12)
ax.set_xticks(x)
ax.set_xticklabels(df['Display_Exp'], rotation=30, ha='right', fontsize=9.5)
ax.set_ylim(0.0, 1.05)
ax.axhline(0.5, color='gray', linestyle='--', linewidth=0.8, alpha=0.7, label='Chance level (0.50)')
ax.legend(loc='lower right', frameon=True, framealpha=0.95)
plt.tight_layout()

fig1_path = os.path.join(ASSETS_DIR, "figure1_auc_benchmark_comparison.png")
plt.savefig(fig1_path, dpi=300)
plt.close()
print("Saved figure1_auc_benchmark_comparison.png")

# ---------------------------------------------------------
# 2. GENERATOR ATTRIBUTION REPORT & CONFUSION MATRIX (FIGURE 2)
# ---------------------------------------------------------
attr_path = os.path.join(RESULTS_DIR, "attribution_metrics.json")
if os.path.exists(attr_path):
    with open(attr_path) as f:
        attr_data = json.load(f)

    cm = np.array(attr_data['confusion_matrix'])
    classes = ['BigGAN', 'DALL-E 3', 'Midjourney v6', 'SD 2.1', 'SD 3', 'SDXL']

    rows = []
    for i, cls in enumerate(classes):
        tp = cm[i, i]
        fn = cm[i, :].sum() - tp
        fp = cm[:, i].sum() - tp
        prec = tp / (tp + fp)
        rec = tp / (tp + fn)
        f1 = 2 * prec * rec / (prec + rec)
        rows.append({
            'generator': cls,
            'precision': round(prec, 3),
            'recall': round(rec, 3),
            'f1_score': round(f1, 3),
            'support': int(cm[i, :].sum())
        })

    df_attr = pd.DataFrame(rows)
    macro_row = {
        'generator': 'Macro Average',
        'precision': round(df_attr['precision'].mean(), 3),
        'recall': round(df_attr['recall'].mean(), 3),
        'f1_score': round(df_attr['f1_score'].mean(), 3),
        'support': int(df_attr['support'].sum())
    }
    df_attr = pd.concat([df_attr, pd.DataFrame([macro_row])], ignore_index=True)
    df_attr.to_csv(os.path.join(RESULTS_DIR, "generator_attribution_full_report.csv"), index=False)
    print("Saved generator_attribution_full_report.csv")

    acc = attr_data['overall_accuracy'] * 100
    f1_val = attr_data['macro_f1']

    plt.figure(figsize=(8, 6.5))
    sns.heatmap(
        cm,
        annot=True,
        fmt='d',
        cmap='Blues',
        xticklabels=classes,
        yticklabels=classes,
        linewidths=0.6,
        cbar=True
    )
    plt.title(f'Generator Attribution Confusion Matrix (ResNet-50)\nOverall Accuracy: {acc:.2f}% | Macro F1: {f1_val:.4f}',
              fontsize=12, fontweight='bold', pad=12)
    plt.xlabel('Predicted Generator', fontsize=11, fontweight='bold')
    plt.ylabel('True Generator', fontsize=11, fontweight='bold')
    plt.xticks(rotation=30, ha='right')
    plt.tight_layout()

    fig2_path = os.path.join(ASSETS_DIR, "figure2_attribution_confusion_matrix.png")
    plt.savefig(fig2_path, dpi=300)
    plt.close()
    print("Saved figure2_attribution_confusion_matrix.png")

print("All verified assets generated successfully.")
