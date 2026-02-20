Sistema de clasificación automática de tumores cerebrales a partir de imágenes MRI, desarrollado como proyecto académico en el curso de Product Development Studio.

El sistema utiliza EfficientNet-B0 como arquitectura base y permite realizar inferencias tanto a través de:

🌐 Una API REST construida con FastAPI

🖥️ Un Dashboard interactivo desarrollado en Streamlit

🎯 Objetivo del Proyecto

Desarrollar un sistema completo de Deep Learning que permita clasificar imágenes MRI en 4 categorías:
- glioma
- meningioma
- pituitary
-healthy

Exponer el modelo mediante una API
Crear una interfaz visual amigable para el usuario
Documentar y versionar el desarrollo del modelo

## 📋 Requisitos

### Dependencias del Sistema
- Python 3.13+
- pip
- Git

### Dependencias de Python
Ver `requirements.txt` para la lista completa de dependencias.

## 🚀 Instalación Local

### 1. Clonar el repositorio
```bash
git clone https://github.com/gabrielananezt-code/brain-mri-tumor-classification.git
```

### 2. Crear entorno virtual
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```


#### 📁 Estructura del Proyecto
```bash
brain-mri-tumor-classification/
│
├── api/                    # API REST (FastAPI)
│   ├── main.py
│   ├── model_loader.py
│   └── ...
│
├── dashboard/              # Dashboard interactivo (Streamlit)
│   └── app.py
│
├── models/                 # Modelo entrenado y clases
│   ├── best_model_effi_t.pth
│   └── classes.json
│
├── data/                   # Datos del proyecto
├── notebooks/              # Exploración y análisis del dataset
├── README.md
└── requirements.txt
```
🌐 Ejecutar la API (FastAPI)

Desde la raíz del proyecto:
```bash
python -m uvicorn api.main:app --reload
```
Acceder a la documentación interactiva:
```bash
http://127.0.0.1:8000/docs
```
Endpoints principales:
```bash
GET / → Estado del servicio
GET /health → Verificación de funcionamiento
POST /predict → Predicción de imagen MRI
```

🖥️ Ejecutar el Dashboard (Streamlit)

Desde la raíz del proyecto:
```bash
streamlit run dashboard/app.py
```
El dashboard permite:
- Subir una imagen MRI
- Visualizar la imagen cargada
- Obtener la predicción del modelo
- Ver probabilidades por clase

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/tu_nombre`)
3. Commit tus cambios (`git commit -m 'add information'`)
4. Push a la rama (`git push origin feature/tu_nombre`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

---

**Nota**: Esta aplicación es para fines educativos y de investigación. No debe usarse como único método de diagnóstico médico.
