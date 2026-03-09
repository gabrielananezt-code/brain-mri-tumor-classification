# Manual de Instalación
## Sistema de Clasificación de Tumores Cerebrales en Imágenes MRI

---

## 1. Introducción

Este documento describe el proceso para **instalar y ejecutar** el sistema de clasificación de tumores cerebrales basado en imágenes MRI.

La solución está compuesta por los siguientes componentes:

- Una **API REST desarrollada en FastAPI** que realiza la inferencia del modelo.
- Un **dashboard interactivo en Streamlit** para que el usuario cargue imágenes.
- Un **modelo de Deep Learning entrenado en PyTorch** almacenado en formato `.pth`.
- Un sistema de **contenedores Docker** que permite ejecutar todos los servicios de manera reproducible.

La arquitectura del sistema utiliza **dos contenedores Docker**:

- **API FastAPI**
- **Dashboard Streamlit**

Ambos servicios se coordinan mediante **Docker Compose**.

---

## 2. Requisitos del sistema

Antes de ejecutar el sistema asegúrese de tener instalado:

### Software requerido

- Docker  
- Docker Compose Plugin  
- Git  

### Verificar instalación de Docker

Ejecutar en la terminal:
```bash
docker --version
```
### Verificar Docker Compose

Ejecutar en la terminal:
```bash
docker compose version
```
---

## 3. Clonar el repositorio

Clone el repositorio del proyecto desde GitHub ejecutando:
```bash
git clone https://github.com/gabrielananezt-code/brain-mri-tumor-classification.git
```
Luego ingrese a la carpeta del proyecto:
```bash
cd brain-mri-tumor-classification
```
---

## 4. Instalación local con Python (opcional)

Esta sección permite ejecutar el sistema **sin Docker**.

### 4.1 Crear entorno virtual

Se recomienda crear un entorno virtual para aislar las dependencias.

#### Windows
```bash
python -m venv venv  
venv\Scripts\activate
```
#### Linux / Mac
```bash
python -m venv venv  
source venv/bin/activate
```
---

### 4.2 Instalar dependencias

Instale las librerías necesarias ejecutando:
```bash
pip install -r requirements.txt
```
Las principales dependencias incluyen:

- torch  
- torchvision  
- fastapi  
- uvicorn  
- streamlit  
- pillow  
- numpy  

---

## 5. Verificar artefactos del modelo

Antes de ejecutar el sistema, confirme que en la carpeta **models** existan los archivos del modelo.

Estructura esperada:
```bash
models/  
├── best_model_effi_t.pth  
└── classes.json  
```
Estos archivos contienen:

- los pesos entrenados del modelo  
- el mapeo de clases utilizado para las predicciones  

---

## 6. Ejecutar la API (modo local)

Desde la raíz del proyecto ejecute:
```bash
python -m uvicorn api.main:app --reload
```
La API quedará disponible en:
```bash
http://localhost:8000
```
La documentación automática estará disponible en:
```bash
http://localhost:8000/docs
```
---

## 7. Ejecutar el dashboard (modo local)

Abra una nueva terminal y ejecute:
```bash
python -m streamlit run dashboard/app.py
```
El dashboard quedará disponible en:
```bash
http://localhost:8501
```
---

## 8. Verificación del sistema

Para confirmar que el sistema funciona correctamente:

1. Inicie la API  
2. Inicie el dashboard  
3. Abra el dashboard en el navegador  
4. Cargue una imagen MRI  
5. Verifique que el sistema muestre:

- imagen cargada  
- clase predicha  
- confianza de predicción  
- probabilidades por clase  
- tiempo de inferencia  

---

## 9. Estructura del proyecto

La estructura principal del repositorio es la siguiente:
```bash
brain-mri-tumor-classification  
│  
├── api  
│ ├── main.py  
│ └── model_loader.py  
│  
├── dashboard  
│ └── app.py  
│  
├── models  
│ ├── best_model_effi_t.pth  
│ └── classes.json  
│  
├── notebooks  
├── scripts  
├── data  
├── manuales  
│ ├── manual-de-usuario.md  
│ └── manual-de-instalacion.md  
│  
├── docker-compose.yml  
├── Dockerfile.api  
├── Dockerfile.dashboard  
│  
├── requirements.txt  
└── README.md  
```
---

## 10. Instalación mediante Docker

El proyecto incluye dos contenedores Docker:

- uno para la **API**
- uno para el **dashboard**

Estos contenedores se ejecutan mediante **Docker Compose**.

### 10.1 Construir los contenedores

Desde la raíz del proyecto ejecute:
```bash
docker compose build
```
---

### 10.2 Ejecutar los contenedores

Ejecute:
```bash
docker compose up -d
```
Esto iniciará automáticamente:

- el contenedor de la **API**
- el contenedor del **dashboard**

---

## 11. Acceso al sistema con Docker

Una vez ejecutados los contenedores, los servicios estarán disponibles en:

### Dashboard
```bash
http://localhost:8501
```
### API
```bash
http://localhost:8000
```
### Documentación interactiva de la API
```bash
http://localhost:8000/docs
```
---

## 12. Configuración de Docker

La configuración actual del sistema define los siguientes servicios.

### Contenedor API

- Base de imagen: `python:3.10-slim`
- Puerto expuesto: **8000**
- Comando de ejecución:
```bash
uvicorn api.main:app --host 0.0.0.0 --port 8000
```
El modelo es copiado dentro del contenedor en la ruta:
```bash
/app/models
```
---

### Contenedor Dashboard

- Base de imagen: `python:3.10-slim`
- Puerto expuesto: **8501**
- Comando de ejecución:
```bash
streamlit run dashboard/app.py --server.address=0.0.0.0 --server.port=8501
```
---

### Comunicación entre servicios

El dashboard envía las imágenes a la API mediante la URL interna:
```bash
http://api:8000/predict
```
---

### Comando principal de ejecución

El sistema completo se ejecuta con:
```bash
docker compose build  
docker compose up -d
```
---

## 13. Solución de problemas

### Error al cargar el modelo

Verifique que los archivos `.pth` y `classes.json` estén presentes en la carpeta `models`.

### Error de dependencias

Ejecute nuevamente:
```bash
pip install -r requirements.txt
```
### El dashboard no se conecta a la API

Verifique:

- que la API esté en ejecución  
- que el puerto configurado sea correcto  

### Error al ejecutar Docker

Confirme que:

- Docker esté instalado  
- el archivo `docker-compose.yml` esté en la raíz del proyecto  
- el puerto utilizado no esté ocupado  



