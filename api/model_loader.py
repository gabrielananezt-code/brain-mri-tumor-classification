from pathlib import Path
import json
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image

BASE_DIR = Path(__file__).resolve().parent
REPO_ROOT = BASE_DIR.parent
MODELS_DIR = REPO_ROOT / "models"

WEIGHTS_PATH = MODELS_DIR / "best_model_effi_t.pth"
CLASSES_PATH = MODELS_DIR / "classes.json"

if not WEIGHTS_PATH.exists():
    raise FileNotFoundError(f"No encuentro pesos en: {WEIGHTS_PATH}")
if not CLASSES_PATH.exists():
    raise FileNotFoundError(f"No encuentro clases en: {CLASSES_PATH}")

with open(CLASSES_PATH, "r", encoding="utf-8") as f:
    idx2class = json.load(f)

CLASS_NAMES = [idx2class[str(i)] for i in range(len(idx2class))]
NUM_CLASSES = len(CLASS_NAMES)

model = models.efficientnet_b0(weights=None)
model.classifier[1] = nn.Linear(model.classifier[1].in_features, NUM_CLASSES)

state_dict = torch.load(WEIGHTS_PATH, map_location="cpu")
model.load_state_dict(state_dict)
model.eval()
torch.set_grad_enabled(False)

IMG_SIZE = 180
transform = transforms.Compose([
    transforms.Resize((IMG_SIZE, IMG_SIZE)),
    transforms.Lambda(lambda im: im.convert("RGB")),
    transforms.ToTensor(),
    transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5]),
])

def predict_image_pil(img: Image.Image):
    x = transform(img).unsqueeze(0)

    logits = model(x)
    probs = torch.softmax(logits, dim=1).squeeze().tolist()

    pred_idx = int(torch.tensor(probs).argmax().item())
    prediction = CLASS_NAMES[pred_idx]

    probs_dict = {cls: round(float(p), 4) for cls, p in zip(CLASS_NAMES, probs)}
    return prediction, probs_dict