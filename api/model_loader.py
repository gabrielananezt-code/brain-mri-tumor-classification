from pathlib import Path
import json
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image

# Paths robustos (por tu estructura)
BASE_DIR = Path(__file__).resolve().parent
REPO_ROOT = BASE_DIR.parent.parent
MODELS_DIR = REPO_ROOT / "models"

WEIGHTS_PATH = MODELS_DIR / "best_model_effi_t.pth"
CLASSES_PATH = MODELS_DIR / "classes.json"

# Clases (tu json es dict: "0": "glioma", etc.)
with open(CLASSES_PATH, "r", encoding="utf-8") as f:
    idx2class = json.load(f)

CLASS_NAMES = [idx2class[str(i)] for i in range(len(idx2class))]
NUM_CLASSES = len(CLASS_NAMES)

# Modelo EfficientNetB0 + classifier a 4 clases
model = models.efficientnet_b0(weights=None)
model.classifier[1] = nn.Linear(model.classifier[1].in_features, NUM_CLASSES)

# Cargar pesos (state_dict)
state_dict = torch.load(WEIGHTS_PATH, map_location="cpu")
model.load_state_dict(state_dict)
model.eval()

# Preprocess de INFERENCIA (3 canales)
IMG_SIZE = 180
transform = transforms.Compose([
    transforms.Resize((IMG_SIZE, IMG_SIZE)),
    transforms.Lambda(lambda im: im.convert("RGB")),  # ✅ fuerza 3 canales
    transforms.ToTensor(),
    transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5]),
])

def predict_image_pil(img: Image.Image):
    x = transform(img).unsqueeze(0)  # [1, 3, 180, 180]

    with torch.no_grad():
        logits = model(x)
        probs = torch.softmax(logits, dim=1).squeeze().tolist()

    pred_idx = int(torch.tensor(probs).argmax().item())
    prediction = CLASS_NAMES[pred_idx]

    probs_dict = {
    cls: round(float(p), 4)
    for cls, p in zip(CLASS_NAMES, probs)
    }

    return prediction, probs_dict