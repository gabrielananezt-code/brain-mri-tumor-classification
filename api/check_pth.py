from pathlib import Path
import torch

BASE_DIR = Path(__file__).resolve().parent      # .../brain-mri-tumor-classification/api
REPO_ROOT = BASE_DIR.parent                     # .../brain-mri-tumor-classification
MODEL_PATH = REPO_ROOT / "models" / "best_model_effi_t.pth"

print("BASE_DIR:", BASE_DIR)
print("REPO_ROOT:", REPO_ROOT)
print("MODEL_PATH:", MODEL_PATH)
print("EXISTS?:", MODEL_PATH.exists())

obj = torch.load(MODEL_PATH, map_location="cpu")
print("TYPE:", type(obj))

if isinstance(obj, dict):
    print("DICT keys sample:", list(obj.keys())[:15])