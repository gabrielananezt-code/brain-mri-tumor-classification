import os
import requests
import streamlit as st
from PIL import Image
import time

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="Brain MRI Classifier",
    page_icon="🧠",
    layout="centered"
)

API_URL = os.getenv("API_URL", "http://127.0.0.1:8000/predict")

# ---------------- UI HEADER ----------------
st.title("🧠 Brain MRI Tumor Classifier")
st.markdown("Herramienta de apoyo para clasificación automática de estudios MRI.")

st.divider()

# ---------------- FILE UPLOAD ----------------
uploaded = st.file_uploader(
    "Sube una imagen MRI",
    type=["jpg", "jpeg", "png"]
)

if uploaded:
    img = Image.open(uploaded)

    st.image(img, caption="Imagen cargada", use_container_width=True)

    if st.button("🔍 Ejecutar predicción", type="primary"):

        start_time = time.time()

        with st.spinner("Procesando imagen..."):
            files = {"file": (uploaded.name, uploaded.getvalue(), uploaded.type)}
            response = requests.post(API_URL, files=files)

        end_time = time.time()

        if response.status_code != 200:
            st.error("Error en la API")
            st.stop()

        result = response.json()
        prediction = result["prediction"]
        probabilities = result["probabilities"]

        confidence = max(probabilities.values())

        # ---------------- RESULT ----------------
        st.divider()
        st.subheader("Resultado")

        # Indicador visual según confianza
        if confidence >= 0.8:
            st.success(f"Predicción: **{prediction.upper()}**")
        elif confidence >= 0.6:
            st.warning(f"Predicción: **{prediction.upper()}**")
        else:
            st.error(f"Predicción: **{prediction.upper()}**")

        st.metric("Confianza", f"{confidence*100:.2f}%")
        st.metric("Tiempo de inferencia", f"{(end_time-start_time)*1000:.0f} ms")

        st.subheader("Distribución de probabilidades")
        st.bar_chart(probabilities)

else:
    st.info("Carga una imagen para comenzar.")