"""
Local Evaluation Script for AI-Generated Image Detector (ResNet-50 / ConvNeXt-Tiny)
Evaluates binary detection (Real vs Fake) or 6-class generator attribution on local image folders.
"""

import os
import argparse
import json
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
from sklearn.metrics import accuracy_score, roc_auc_score, classification_report

def build_model(num_classes=2, model_type="resnet50"):
    """Build classification model backbone."""
    if model_type == "convnext":
        m = models.convnext_tiny(weights=None)
        m.classifier[2] = nn.Linear(m.classifier[2].in_features, num_classes)
    else:
        m = models.resnet50(weights=None)
        m.fc = nn.Linear(m.fc.in_features, num_classes)
    return m

def get_transforms(crop_size=128):
    """Eval transforms matching standard ImageNet normalization."""
    return transforms.Compose([
        transforms.Resize((crop_size, crop_size)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

def evaluate_folder(model, image_dir, device, num_classes=2):
    """Evaluate image files inside directory."""
    transform = get_transforms()
    valid_exts = {".jpg", ".jpeg", ".png", ".webp", ".bmp"}
    
    image_paths = [
        os.path.join(root, file)
        for root, _, files in os.walk(image_dir)
        for file in files if os.path.splitext(file)[1].lower() in valid_exts
    ]
    
    if not image_paths:
        print(f"No valid images found in {image_dir}")
        return
        
    print(f"Found {len(image_paths)} images in {image_dir}. Running inference...")
    
    model.eval()
    results = []
    
    with torch.no_grad():
        for path in image_paths:
            try:
                img = Image.open(path).convert("RGB")
                tensor = transform(img).unsqueeze(0).to(device)
                logits = model(tensor)
                probs = torch.softmax(logits.float(), dim=1)[0].cpu().numpy()
                pred_class = int(probs.argmax())
                confidence = float(probs[pred_class])
                
                results.append({
                    "file": path,
                    "pred_class": pred_class,
                    "confidence": confidence,
                    "prob_fake": float(probs[1]) if num_classes == 2 else float(probs[pred_class])
                })
            except Exception as e:
                print(f"Error processing {path}: {e}")

    fake_count = sum(1 for r in results if r["pred_class"] == 1)
    real_count = len(results) - fake_count
    print("\n" + "="*50)
    print(f"Evaluation Summary for: {image_dir}")
    print(f"Total Images: {len(results)}")
    print(f"Predicted REAL: {real_count} ({real_count/len(results):.1%})")
    print(f"Predicted FAKE: {fake_count} ({fake_count/len(results):.1%})")
    print("="*50)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Evaluate AI-Generated Image Detector")
    parser.add_argument("--image_dir", type=str, required=True, help="Directory containing images to evaluate")
    parser.add_argument("--checkpoint", type=str, required=True, help="Path to PyTorch .pt model checkpoint")
    parser.add_argument("--model_type", type=str, default="resnet50", choices=["resnet50", "convnext"], help="Model architecture")
    parser.add_argument("--num_classes", type=int, default=2, help="2 for binary Real/Fake, 6 for generator attribution")
    
    args = parser.parse_args()
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")
    
    model = build_model(num_classes=args.num_classes, model_type=args.model_type).to(device)
    
    if os.path.exists(args.checkpoint):
        state = torch.load(args.checkpoint, map_location=device)
        if isinstance(state, dict) and "model" in state:
            state = state["model"]
        model.load_state_dict(state)
        print(f"Loaded checkpoint from: {args.checkpoint}")
    else:
        print(f"Checkpoint not found at {args.checkpoint}, initializing default weights.")
        
    evaluate_folder(model, args.image_dir, device, num_classes=args.num_classes)
