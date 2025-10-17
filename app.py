import streamlit as st
from PIL import Image, ImageEnhance

st.set_page_config(page_title="🧪Image Lab: Edit & Enhance", page_icon="🪄", layout="centered")

st.markdown(
    """
    <style>
        .stApp {
            background: linear-gradient(135deg, #FF6B6B 0%, #845EC2 100%);
            color: white;
        }
        .title-text {
            text-align: center;
            font-size: 44px;
            font-weight: 900;
            color: #FFD700;
            text-shadow: 3px 3px 8px rgba(0,0,0,0.4);
            font-family: 'Trebuchet MS', sans-serif;
        }
        .subtitle-text {
            text-align: center;
            font-size: 20px;
            color: #F8F9FA;
            opacity: 0.9;
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
            background-color: #ffffffcc;
            color: #000;
            border-radius: 10px;
            padding: 5px 10px;
        }
        div[data-testid="stDownloadButton"] button {
            background-color: #FFD700;
            color: #000;
            font-weight: bold;
            border-radius: 12px;
            padding: 12px 25px;
            font-size: 16px;
        }
        div[data-testid="stDownloadButton"] button:hover {
            background-color: #FFB800;
            color: #fff;
        }
        .stImage > img {
            border-radius: 15px;
            box-shadow: 0px 10px 20px rgba(0,0,0,0.4);
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<h1 class="title-text">🧪 Image Lab: Edit & Enhance</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle-text">Upload, edit & enhance your images with style ✨</p>', unsafe_allow_html=True)

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
