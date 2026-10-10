import argparse
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
import matplotlib.pyplot as plt
import os

def build_model(num_classes=2):
    """Build ResNet50 model for Real vs Fake classification."""
    model = models.resnet50(weights=models.ResNet50_Weights.DEFAULT)
    model.fc = nn.Linear(model.fc.in_features, num_classes)
    return model

def get_transforms():
    """Eval transforms matching standard ImageNet normalization."""
    return transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

def predict_and_visualize(model, image_path, device, class_names=["REAL", "FAKE"]):
    """Fast prediction and matplotlib display for presentation."""
    transform = get_transforms()
    img_pil = Image.open(image_path).convert("RGB")
    tensor = transform(img_pil).unsqueeze(0).to(device)
    
    model.eval()
    with torch.no_grad():
        logits = model(tensor)
        prob_fake = torch.softmax(logits.float(), dim=1)[0, 1].item()
    
    pred_class = 1 if prob_fake >= 0.5 else 0
    confidence = prob_fake if pred_class == 1 else (1.0 - prob_fake)
    
    # Plot result
    plt.figure(figsize=(6, 6))
    plt.imshow(img_pil)
    plt.axis("off")
    
    color = '#2e7d32' if pred_class == 0 else '#c62828'
    title_text = f"Prediction: {class_names[pred_class]}\nConfidence: {confidence*100:.1f}%\n(Prob Fake: {prob_fake:.3f})"
    plt.title(title_text, fontsize=14, fontweight='bold', color=color, pad=12)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Real vs Fake Image Predictor")
    parser.add_argument("--image_path", type=str, required=True, help="Path to input image")
    parser.add_argument("--model_path", type=str, default=None, help="Path to model .pt checkpoint")
    args = parser.parse_args()

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = build_model().to(device)
    
    if args.model_path and os.path.exists(args.model_path):
        model.load_state_dict(torch.load(args.model_path, map_location=device))
        print(f"Loaded weights from {args.model_path}")
    else:
        print("Using initialized model head (evaluation demo mode)")
        
    predict_and_visualize(model, args.image_path, device)
