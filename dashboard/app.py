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
st.warning(
    "⚠️ Este sistema es un prototipo académico y no reemplaza un diagnóstico médico profesional."
)
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

        with st.spinner("Procesando imagen..."):

            try:
                files = {
                    "file": (uploaded.name, uploaded.getvalue(), uploaded.type)
                }

                response = requests.post(API_URL, files=files)

            except Exception:
                st.error("❌ No se pudo conectar con la API. Verifica que esté corriendo.")
                st.stop()

        if response.status_code != 200:
            st.error("❌ Error en la API.")
            st.stop()

        result = response.json()

        prediction = result["prediction"]
        probabilities = result["probabilities"]

        # 🔥 Ahora usamos el tiempo real que devuelve la API
        inference_time = result.get("inference_time_ms", None)

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

        if inference_time:
            st.metric("Tiempo de inferencia (API)", f"{inference_time:.2f} ms")

        # 🔥 TOP-2 CLASES
        sorted_probs = sorted(
            probabilities.items(),
            key=lambda x: x[1],
            reverse=True
        )

        st.subheader("Top 2 clases más probables")
        st.write(f"1️⃣ {sorted_probs[0][0]}: {sorted_probs[0][1]*100:.2f}%")
        st.write(f"2️⃣ {sorted_probs[1][0]}: {sorted_probs[1][1]*100:.2f}%")

        st.subheader("Distribución de probabilidades")
        st.bar_chart(probabilities)

else:
    st.info("Carga una imagen para comenzar.")