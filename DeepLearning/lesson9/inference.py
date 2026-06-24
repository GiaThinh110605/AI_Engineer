import argparse
import torch
import torch.nn as nn
from torchvision.models import resnet18
from torchvision import transforms
from PIL import Image

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--image-path", "-i", type=str, default="/Users/mac/Downloads/AI_Engineer/Dataset/animals/val/cat/16.jpeg")
    return parser.parse_args()

def inference():
    args = get_args()
    device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
    
    # 1. Load Model
    model = resnet18()
    model.fc = nn.Linear(512, 10)
    model.load_state_dict(torch.load("best.pt", map_location=device))
    model.to(device).eval()
    
    # 2. Đọc và biến đổi ảnh
    img = Image.open(args.image_path).convert("RGB")
    transform = transforms.Compose([transforms.Resize((224, 224)), transforms.ToTensor()])
    tensor = transform(img).unsqueeze(0).to(device)
    
    # 3. Dự đoán
    with torch.no_grad():
        pred_id = torch.argmax(model(tensor)).item()
        print("=> Dự đoán Class ID:", pred_id)

if __name__ == "__main__":
    inference()