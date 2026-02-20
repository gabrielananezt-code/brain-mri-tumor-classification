from fastapi import FastAPI, UploadFile, File
from PIL import Image
from api.model_loader import predict_image_pil

app = FastAPI(title="Brain MRI Tumor Classifier API")

@app.get("/")
def root():
    return {"message": "Brain MRI API funcionando 🚀"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/model-info")
def model_info():
    return {
        "model": "EfficientNetB0",
        "input_size": 180,
        "num_classes": 4,
        "classes": ["glioma", "healthy", "meningioma", "pituitary"]
    }

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    img = Image.open(file.file)
    pred, probs = predict_image_pil(img)

    confidence = max(probs.values())

    return {
    "prediction": pred,
    "confidence": round(confidence, 4),
    "probabilities": probs
    }