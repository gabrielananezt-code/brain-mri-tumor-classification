# Manual de Usuario
## Sistema de Clasificación de Tumores Cerebrales en Imágenes MRI

---

## 1. Introducción

Este sistema permite clasificar automáticamente imágenes de **resonancia magnética cerebral (MRI)** en cuatro categorías:

- **Glioma**
- **Meningioma**
- **Pituitary Tumor**
- **Healthy (sin tumor)**

El prototipo fue desarrollado con fines **académicos y experimentales**, integrando un modelo de **Deep Learning**, una **API REST** y un **dashboard interactivo**.

La solución está compuesta por:

- Un **dashboard en Streamlit** que permite la interacción con el usuario.
- Una **API en FastAPI** que recibe la imagen y ejecuta la inferencia.
- Un modelo entrenado en **PyTorch**, almacenado en formato `.pth`.
- Un archivo `classes.json` con el mapeo de clases utilizadas en la predicción.

---

## 2. Acceso al sistema

El sistema puede utilizarse de dos formas principales.

### Dashboard web

Permite cargar una imagen MRI y visualizar el resultado de la predicción.

Dirección local esperada:
```bash
http://localhost:8501
```
---

### Documentación interactiva de la API

Permite probar directamente los endpoints del servicio.

Dirección local esperada:
```bash
http://localhost:8000/docs
```
---

**Nota:** si el proyecto se despliega en Docker o en la nube, estas URLs pueden cambiar dependiendo de la IP o dominio del servidor.

---

## 3. Flujo de uso del sistema

El flujo general del sistema es el siguiente:

1. El usuario abre el **dashboard web**.
2. Carga una imagen MRI desde su computador.
3. El dashboard envía la imagen a la **API FastAPI**.
4. La API realiza el **preprocesamiento de la imagen**.
5. El modelo ejecuta la **inferencia**.
6. El sistema devuelve el resultado al dashboard.

El resultado incluye:

- **Clase predicha**
- **Nivel de confianza**
- **Probabilidades por clase**
- **Tiempo de inferencia**

---

## 4. Cargar una imagen MRI

Para realizar una predicción siga los siguientes pasos:

1. Ingrese al **dashboard**.
2. Haga clic en el botón para **cargar archivo**.
3. Seleccione una imagen MRI desde su computador.
4. Espere a que el sistema muestre la **vista previa de la imagen**.
5. Presione el botón de **predicción** si el dashboard lo solicita.
6. Revise el resultado generado por el sistema.

---

## 5. Resultados mostrados

El sistema presenta al usuario la siguiente información:

### Clase predicha

Categoría más probable según el modelo de clasificación.

### Nivel de confianza

Probabilidad asociada a la predicción principal.

### Probabilidades por clase

Distribución completa de probabilidades generadas por el modelo.

### Tiempo de inferencia

Tiempo aproximado que tarda el modelo en generar la predicción.

### Visualización de la imagen

El sistema muestra la imagen MRI cargada para facilitar la interpretación.

---

## 6. Categorías disponibles

El modelo clasifica las imágenes en las siguientes categorías:

- **Glioma**
- **Meningioma**
- **Pituitary Tumor**
- **Healthy (sin tumor)**

Cada categoría representa un tipo específico de diagnóstico dentro del dataset utilizado para el entrenamiento.

---

## 7. Recomendaciones para las imágenes

Para obtener resultados más consistentes se recomienda utilizar:

- Imágenes MRI **claras y de buena calidad**.
- Archivos en **formatos compatibles con imágenes**.
- Imágenes que correspondan al **tipo de datos usado durante el entrenamiento del modelo**.

El sistema realiza automáticamente el **preprocesamiento necesario** antes de ejecutar la inferencia.

---

## 8. Interpretación de resultados

La predicción mostrada corresponde a la clase con **mayor probabilidad** según el modelo.

Sin embargo, es importante considerar que:

- una probabilidad alta **no equivale a un diagnóstico médico definitivo**
- una probabilidad baja puede indicar **incertidumbre del modelo**
- los resultados deben interpretarse únicamente como **apoyo académico o experimental**

---

## 9. Consideraciones importantes

Este sistema fue desarrollado con fines **académicos y de investigación**.

Por lo tanto:

- **no reemplaza el criterio médico profesional**
- **no debe utilizarse como herramienta de diagnóstico clínico**

El rendimiento del modelo puede verse afectado por:

- calidad de la imagen
- diferencias respecto al dataset de entrenamiento
- imágenes fuera del dominio esperado por el modelo
- errores de conexión entre dashboard y API

---

## 10. Errores frecuentes

### La imagen no carga

Verifique que el archivo sea una **imagen válida** y esté en un formato soportado.

### No aparece el resultado

Revise que la **API esté en ejecución** y accesible desde el dashboard.

### Error de conexión

Confirme que el servicio **FastAPI esté activo** y que la URL configurada sea correcta.

### El sistema tarda demasiado

Espere algunos segundos. Si el problema persiste, reinicie la **API y el dashboard**.

---

## 11. Uso de la API sin dashboard

También es posible utilizar el sistema directamente mediante la API.

Acceda a la documentación interactiva en:
```bash
http://localhost:8000/docs
```
Desde allí se puede probar el endpoint de predicción cargando manualmente una imagen MRI.

---

## 12. Observaciones finales

Este manual describe el uso funcional del prototipo actual.

Si el sistema se despliega posteriormente mediante **Docker** o en infraestructura de **nube**, las rutas de acceso y puertos podrán cambiar sin modificar la lógica general de funcionamiento del sistema.