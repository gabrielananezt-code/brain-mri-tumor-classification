from fastapi import FastAPI, UploadFile, File, HTTPException
from PIL import Image
from api.model_loader import predict_image_pil
from io import BytesIO
import time

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

    # Validar que sea imagen
    if not file.content_type or not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="El archivo debe ser una imagen (JPG/PNG).")

    try:
        contents = await file.read()
        img = Image.open(BytesIO(contents)).convert("RGB")
    except Exception:
        raise HTTPException(status_code=400, detail="No se pudo procesar la imagen (archivo corrupto o formato inválido).")

    try:
        start = time.time()
        pred, probs = predict_image_pil(img)
        inference_time_ms = round((time.time() - start) * 1000, 2)
    except Exception:
        raise HTTPException(status_code=500, detail="Error interno del modelo.")

    confidence = max(probs.values())

    return {
        "prediction": pred,
        "confidence": round(confidence, 4),
        "probabilities": probs,
        "inference_time_ms": inference_time_ms
    }