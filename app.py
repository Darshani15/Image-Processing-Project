import streamlit as st
from PIL import Image, ImageEnhance

st.set_page_config(page_title="🖼️ Image Enhancer Studio", page_icon="🪄", layout="centered")

st.markdown(
    """
    <style>
        .stApp {
            background: linear-gradient(135deg, #6A11CB 0%, #2575FC 100%);
            color: white;
        }
        .title-text {
            text-align: center;
            font-size: 42px;
            font-weight: 800;
            color: #FFD700;
            text-shadow: 2px 2px 6px rgba(0,0,0,0.3);
            font-family: 'Trebuchet MS', sans-serif;
        }
        .subtitle-text {
            text-align: center;
            font-size: 18px;
            color: #FFFFFF;
            opacity: 0.85;
            font-family: 'Segoe UI', sans-serif;
            margin-bottom: 30px;
        }
        .stFileUploader label {
            color: #fff !important;
            font-weight: bold;
        }
        label {
            color: #fff !important;
            font-weight: 600;
        }
        .stNumberInput input {
            background-color: #ffffffdd;
            color: #000;
            border-radius: 8px;
        }
        div[data-testid="stDownloadButton"] button {
            background-color: #FFD700;
            color: #000;
            font-weight: bold;
            border-radius: 8px;
            padding: 10px 20px;
        }
        div[data-testid="stDownloadButton"] button:hover {
            background-color: #FFA500;
            color: #fff;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<h1 class="title-text">🪄 Image Enhancer Studio</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle-text">Upload, edit & enhance your images with style 🚀</p>', unsafe_allow_html=True)

uploaded_file = st.file_uploader("📸 Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="🌟 Original Image", use_container_width=True)

    brightness = st.number_input("✨ Brightness", value=1.0, step=0.1)
    contrast = st.number_input("🎨 Contrast", value=1.0, step=0.1)
    sharpness = st.number_input("🪞 Sharpness", value=1.0, step=0.1)
    grayscale = st.checkbox("🖤 Convert to Grayscale")

    enhancer = ImageEnhance.Brightness(image)
    img = enhancer.enhance(brightness)
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(contrast)
    enhancer = ImageEnhance.Sharpness(img)
    img = enhancer.enhance(sharpness)

    if grayscale:
        img = img.convert("L")

    st.image(img, caption="✅ Processed Image", use_container_width=True)

    img.save("processed.png")
    with open("processed.png", "rb") as f:
        st.download_button(
            "📥 Download Enhanced Image",
            f,
            file_name="processed.png",
            mime="image/png"
        )

