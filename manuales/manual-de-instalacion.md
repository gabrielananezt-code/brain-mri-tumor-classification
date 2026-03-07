# Manual de Instalación
## Sistema de Clasificación de Tumores Cerebrales en Imágenes MRI

---

## 1. Introducción

Este documento describe el proceso para instalar y ejecutar el sistema de clasificación de tumores cerebrales basado en imágenes MRI.

El sistema está compuesto por:

- una **API REST desarrollada en FastAPI**
- un **modelo de Deep Learning en PyTorch**
- un **dashboard interactivo en Streamlit**
- un **contenedor Docker** para facilitar el despliegue

El sistema puede ejecutarse:

- localmente con Python  
- mediante contenedores Docker  

---

## 2. Requisitos del sistema

Antes de iniciar la instalación asegúrese de tener instalado:

### Software requerido

- Python 3.10 o superior  
- pip  
- Git  
- Docker  
- Docker Compose (opcional)  

### Requisitos de hardware recomendados

- 4 GB de RAM o más  
- 2 GB de espacio libre en disco  

---

## 3. Clonar el repositorio

Clone el repositorio del proyecto desde GitHub:

```bash
git clone https://github.com/gabrielananezt-code/brain-mri-tumor-classification.git

cd brain-mri-tumor-classification
```

---

## 4. Instalación local con Python

Esta sección permite ejecutar el sistema sin Docker.

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

Instale las librerías necesarias:

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

Antes de ejecutar el sistema, confirme que en la carpeta `models` existan los archivos del modelo:

```bash
models/
├── best_model_effi_t.pth
└── classes.json
```

Estos archivos contienen:

- los pesos entrenados del modelo  
- el mapeo de clases utilizado para las predicciones  

---

## 6. Ejecutar la API

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

## 7. Ejecutar el dashboard

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
├── requirements.txt
└── README.md
```

---

## 10. Instalación mediante Docker

El proyecto incluye un **Dockerfile** que permite ejecutar la API y el modelo dentro de un contenedor.

### 10.1 Construir la imagen Docker

Desde la raíz del proyecto ejecute:

```bash
docker build -t brain-mri-classifier .
```

---

### 10.2 Ejecutar el contenedor

Ejecute el contenedor con:

```bash
docker run -p PUERTO_HOST:PUERTO_CONTENEDOR brain-mri-classifier
```

Ejemplo:

```bash
docker run -p 8000:8000 brain-mri-classifier
```

---

## 11. Acceso al sistema con Docker

Una vez ejecutado el contenedor:

### API

```bash
http://localhost:8000
```

### Documentación de la API

```bash
http://localhost:8000/docs
```

Si el dashboard se ejecuta en un contenedor independiente, el puerto deberá definirse en el archivo de configuración correspondiente.

---

## 12. Configuración pendiente de Docker

Cuando el Dockerfile definitivo esté disponible se deberán confirmar los siguientes parámetros:
```bash
Nombre de la imagen Docker:  
[POR DEFINIR]

Puerto de la API:  
[POR DEFINIR]

Puerto del dashboard:  
[POR DEFINIR]

Comando de ejecución del contenedor:  
[POR DEFINIR]

Ubicación interna del modelo:  
[POR DEFINIR]
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
- el `Dockerfile` se encuentre en la raíz del proyecto  
- el puerto utilizado no esté ocupado  
