from pathlib import Path
import torch

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR.parent.parent / "models" / "best_model_effi_t.pth"

print("BASE_DIR:", BASE_DIR)
print("MODEL_PATH:", MODEL_PATH)
print("EXISTS?:", MODEL_PATH.exists())

obj = torch.load(MODEL_PATH, map_location="cpu")
print("TYPE:", type(obj))

if isinstance(obj, dict):
    print("DICT keys sample:", list(obj.keys())[:15])