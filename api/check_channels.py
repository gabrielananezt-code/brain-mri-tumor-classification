from pathlib import Path
import torch

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR.parent.parent / "models" / "best_model_effi_t.pth"

sd = torch.load(MODEL_PATH, map_location="cpu")

# Buscamos el primer conv (en efficientnet suele ser features.0.0.weight)
w = sd["features.0.0.weight"]
print("features.0.0.weight shape:", tuple(w.shape))
print("in_channels:", w.shape[1])