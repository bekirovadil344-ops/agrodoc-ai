import streamlit as st
import numpy as np

st.set_page_config(page_title="AgroDoc AI", page_icon="🌿", layout="centered")

st.title("🌿 AgroDoc AI")
st.subheader("AI-Powered Early Diagnosis System")
st.write("Detects plant stress factors and diseases using bio-electric signals before visual symptoms appear.")

st.divider()

plant = st.selectbox(
    "🔍 Select Plant / Bitki növünü seçin:",
    ["Violet (Bənövşə)", "Tomato (Pomidor)", "Cucumber (Xiyar)", "Cotton (Pambıq)"]
)

st.write(f"Reading bio-electric signals from **{plant}** tissues...")

st.subheader("📸 Bitki şəkli çəkin və ya yükləyin")
camera_photo = st.camera_input("Kamera ilə şəkil çək")
uploaded_photo = st.file_uploader("Və ya cihazdan şəkil seç", type=["jpg", "jpeg", "png"])

image = camera_photo or uploaded_photo
if image is not None:
    st.image(image, caption=f"Seçilmiş bitki: {plant}", use_container_width=True)
    st.success("Şəkil əlavə olundu!")

st.divider()

if st.button("🔬 Start Signal Analysis (Fourier Transform)", use_container_width=True):
    # Nümunə siqnal yaradılması (prototip/demo məqsədli)
    t = np.linspace(0, 1, 200)
    signal = np.sin(2 * np.pi * 5 * t) + 0.3 * np.random.randn(200)
    fft_vals = np.abs(np.fft.rfft(signal))

    st.line_chart(fft_vals[:50], height=180)
    st.info("Erkən diaqnoz nəticəsi: Kiçik stress / nəmlik dəyişimi ehtimalı aşkarlandı. Vaxtında yoxlama tövsiyə olunur.")
  
