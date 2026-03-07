# Manual de Usuario
## Sistema de Clasificación de Tumores Cerebrales en Imágenes MRI

# 1. Introducción

Este sistema permite clasificar automáticamente imágenes de resonancia magnética cerebral (MRI) en cuatro categorías: **Glioma**, **Meningioma**, **Pituitary Tumor** y **Healthy (sin tumor)**. El prototipo fue desarrollado con fines académicos y experimentales, integrando un modelo de Deep Learning, una API REST y un dashboard interactivo.

La solución está compuesta por:

- Un **dashboard en Streamlit** para interacción con el usuario.
- Una **API en FastAPI** que recibe la imagen y ejecuta la inferencia.
- Un modelo entrenado en PyTorch, almacenado en formato `.pth`.
- Un archivo `classes.json` con el mapeo de clases.

---

# 2. Acceso al sistema

El sistema puede utilizarse de dos formas:

#### Dashboard web
Permite cargar una imagen MRI y visualizar el resultado de la predicción.

Dirección local esperada:

http://localhost:8501


### Documentación interactiva de la API

Permite probar directamente los endpoints del servicio.

Dirección local esperada:


http://localhost:8000/docs



> **Nota:** si el proyecto se despliega con Docker o en la nube, estas URLs deben ajustarse con la IP, dominio o puertos definitivos.

---

# 3. Flujo de uso

El flujo general del sistema es el siguiente:

1. El usuario abre el dashboard.
2. Carga una imagen MRI desde su computador.
3. El dashboard envía la imagen a la API.
4. La API realiza el preprocesamiento de la imagen.
5. El modelo ejecuta la inferencia.
6. El sistema devuelve:

- la **clase predicha**
- la **confianza principal**
- las **probabilidades por clase**
- el **tiempo de inferencia**

---

# 4. Cómo cargar una imagen

Para realizar una predicción:

1. Ingrese al **dashboard**.
2. Haga clic en el botón para **cargar archivo**.
3. Seleccione una imagen MRI desde su computador.
4. Espere la visualización previa de la imagen.
5. Presione el botón de **predicción** si el dashboard lo solicita.
6. Revise el resultado generado por el sistema.

---

# 5. Resultados mostrados

El sistema presenta al usuario:

1. **Clase predicha:** categoría más probable según el modelo.
2. **Nivel de confianza:** probabilidad asociada a la predicción principal.
3. **Probabilidades por clase:** distribución completa de salida del modelo.
4. **Tiempo de inferencia:** tiempo aproximado de respuesta del modelo.
5. **Visualización de la imagen cargada.**

Las categorías disponibles son:

- Glioma
- Meningioma
- Pituitary Tumor
- Healthy (sin tumor)

---

# 6. Recomendaciones para las imágenes

Para obtener resultados más consistentes se recomienda utilizar:

- Imágenes MRI cerebrales **claras y legibles**.
- Archivos en formatos compatibles con la aplicación.
- Imágenes que correspondan al tipo de dato usado durante el entrenamiento.

El sistema realiza automáticamente el **preprocesamiento necesario** antes de la inferencia.

---

# 7. Interpretación de resultados

La predicción mostrada corresponde a la clase con **mayor probabilidad** según el modelo.

Sin embargo:

- una probabilidad alta **no equivale a diagnóstico clínico definitivo**
- una probabilidad baja o intermedia puede reflejar **incertidumbre del modelo**
- los resultados deben interpretarse **solo como apoyo académico o experimental**

---

# 8. Consideraciones importantes

Este sistema fue desarrollado con fines académicos y **no reemplaza el criterio médico profesional**.

El prototipo puede verse afectado por:

- variaciones en la calidad de la imagen
- diferencias frente al dataset de entrenamiento
- imágenes fuera del dominio esperado por el modelo
- errores de conexión entre dashboard y API

---

# 9. Errores frecuentes

### La imagen no carga
Verifique que el archivo sea una imagen válida y esté en un formato soportado.

### No aparece el resultado
Revise que la **API esté en ejecución** y accesible desde el dashboard.

### Error de conexión
Confirme que el servicio **FastAPI esté activo** y que la URL configurada en el dashboard sea correcta.

### El sistema tarda demasiado
Espere unos segundos. Si el problema persiste, reinicie la **API y el dashboard**.

---

# 10. Uso de la API sin dashboard

También es posible usar la API directamente desde la documentación interactiva en Swagger:

http://localhost:8000/docs


Allí se puede probar el endpoint de predicción cargando una imagen MRI manualmente.

---

# 11. Observaciones finales

Este manual describe el uso funcional del prototipo actual.

Si el sistema se despliega posteriormente con **Docker** o en infraestructura de **nube**, las rutas de acceso y puertos podrán actualizarse sin cambiar la lógica general de uso del sistema.