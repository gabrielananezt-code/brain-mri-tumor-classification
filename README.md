
# 🧠 Brain MRI Tumor Classification System

Sistema de clasificación automática de tumores cerebrales a partir de imágenes de resonancia magnética (MRI), desarrollado como proyecto académico en el curso **Product Development Studio**.

El sistema integra modelamiento en Deep Learning, gestión de experimentos con MLflow y despliegue mediante una API REST y un dashboard interactivo.

---

## 🎯 Objetivo del Proyecto

Desarrollar un sistema completo de clasificación automática basado en aprendizaje profundo que permita identificar el tipo de tumor cerebral a partir de una imagen MRI.

El modelo clasifica las imágenes en cuatro categorías:

* **Glioma**
* **Meningioma**
* **Pituitary Tumor**
* **Healthy (sin tumor)**

El proyecto contempla:

* Entrenamiento y comparación de múltiples arquitecturas (CNN desde cero y Transfer Learning)
* Selección del mejor modelo (EfficientNet-B0 fine-tuned)
* Registro y seguimiento de experimentos con MLflow (AWS EC2)
* Empaquetamiento del modelo entrenado
* Exposición del modelo mediante API REST (FastAPI)
* Desarrollo de un dashboard interactivo (Streamlit)
* Versionamiento del código y trazabilidad del modelo

---

## 🏗 Arquitectura del Sistema

El flujo completo es:

```
Usuario → Dashboard (Streamlit) → API (FastAPI) → Modelo PyTorch → Respuesta JSON → Visualización
```

El modelo ganador (EfficientNet-B0 fine-tuned) fue entrenado con GPU y registrado en MLflow.
El artefacto final se empaqueta en formato `.pth` junto con el archivo `classes.json`.

---

## 📦 Requisitos

### Requisitos del sistema

* Python 3.10+
* pip
* Git

### Dependencias de Python

Ver archivo `requirements.txt`.
Incluye:

* fastapi
* uvicorn
* python-multipart
* streamlit
* torch
* torchvision
* torchaudio
* pillow
* requests
* numpy
* pandas

---

## 🚀 Instalación Local

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/gabrielananezt-code/brain-mri-tumor-classification.git
cd brain-mri-tumor-classification
```

### 2️⃣ Crear entorno virtual

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# 🌐 Ejecutar la API (FastAPI)

Desde la raíz del proyecto:

```bash
python -m uvicorn api.main:app --reload
```

Acceder a la documentación interactiva:

```
http://127.0.0.1:8000/docs
```

### Endpoints disponibles

* `GET /` → Estado del servicio
* `GET /health` → Verificación de funcionamiento
* `GET /model-info` → Información del modelo cargado
* `POST /predict` → Predicción de imagen MRI

La respuesta del endpoint `/predict` incluye:

* Predicción
* Confianza
* Probabilidades por clase
* Tiempo de inferencia (ms)

---

# 🖥️ Ejecutar el Dashboard (Streamlit)

Desde la raíz del proyecto:

```bash
python -m streamlit run dashboard/app.py
```

El dashboard permite:

* Subir una imagen MRI
* Visualizar la imagen cargada
* Ejecutar predicción
* Ver confianza del modelo
* Visualizar distribución de probabilidades
* Consultar tiempo de inferencia

Incluye advertencia ética sobre uso académico.

---

## 📁 Estructura del Proyecto

```bash
brain-mri-tumor-classification/
│
├── api/                    # API REST (FastAPI)
│   ├── main.py
│   ├── model_loader.py
│
├── dashboard/              # Interfaz Streamlit
│   └── app.py
│
├── models/                 # Modelo entrenado y clases
│   ├── best_model_effi_t.pth
│   └── classes.json
│
├── notebooks/              # EDA y experimentación
├── data/                   # Datos (no versionados en Git)
├── requirements.txt
└── README.md
```

---

## 🔬 Modelamiento

Se evaluaron tres arquitecturas:

1. CNN desde cero (baseline)
2. CNN con regularización (Dropout)
3. EfficientNet-B0 con fine-tuning

El modelo seleccionado fue EfficientNet-B0 fine-tuned, alcanzando:

* Accuracy ≈ 0.99
* F1 macro ≈ 0.99
* Mejor estabilidad en validación

Los experimentos fueron gestionados mediante MLflow en un servidor AWS EC2.

---

## ⚖ Consideraciones Éticas

Este sistema:

* Es un prototipo académico
* Utiliza datos públicos anonimizados
* No reemplaza diagnóstico médico profesional
* No está validado clínicamente

Debe utilizarse únicamente con fines educativos y de investigación.

---

## 🤝 Contribución

1. Crear una rama:

   ```bash
   git checkout -b feature/nueva_feature
   ```

2. Commit:

   ```bash
   git commit -m "Descripción clara del cambio"
   ```

3. Push:

   ```bash
   git push origin feature/nueva_feature
   ```

4. Abrir Pull Request.


