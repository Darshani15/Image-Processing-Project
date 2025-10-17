import streamlit as st
from PIL import Image, ImageEnhance

st.set_page_config(page_title="🎨 Pic Perfect", page_icon="✨")

st.markdown(
    """
    <style>
        .stApp {
            background-color: #D0F4F4;
        }
        /* Style file uploader */
        div.stFileUploader > label {
            background-color: #4DB6AC;
            color: #004C4C;
            font-weight: bold;
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            display: block;
            cursor: pointer;
            margin-bottom: 20px;
        }
        div.stFileUploader > label:hover {
            background-color: #26A69A;
            color: #FFFFFF;
        }
        /* Center section text */
        .title-section {
            text-align:center; 
            background-color:#B2DFDB; 
            padding:20px; 
            border-radius:10px;
        }
        .title-section h1 {
            color:#006666;
        }
        .title-section p {
            font-size:18px;
            color:#004C4C;
        }
        /* Processed image section */
        .processed-section {
            text-align:center; 
            background-color:#B2DFDB; 
            padding:10px; 
            border-radius:8px;
            margin-top:20px;
        }
        .processed-section h3 {
            color:#006666;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="title-section">
        <h1>🎨 Pic Perfect</h1>
        <p>Upload, edit & enhance your images with ease 🌿</p>
    </div>
    """,
    unsafe_allow_html=True
)

uploaded_file = st.file_uploader("📂 Drag & Drop or Browse your image", type=["jpg", "jpeg", "png"], accept_multiple_files=False)

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Original Image", use_container_width=True)

    brightness = st.slider("☀ Brightness", 0.0, 2.0, 1.0)
    contrast = st.slider("🌓 Contrast", 0.0, 2.0, 1.0)
    sharpness = st.slider("✏ Sharpness", 0.0, 2.0, 1.0)
    grayscale = st.checkbox("⚪ Convert to Grayscale")

    enhancer = ImageEnhance.Brightness(image)
    img = enhancer.enhance(brightness)
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(contrast)
    enhancer = ImageEnhance.Sharpness(img)
    img = enhancer.enhance(sharpness)

    if grayscale:
        img = img.convert("L")

    st.markdown(
        """
        <div class="processed-section">
            <h3>↻ ⏳ Processed Image 🔜</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.image(img, caption="Processed Image", use_container_width=True)

    img.save("processed.png")
    with open("processed.png", "rb") as f:
        st.download_button(
            "💾 Download Processed Image",
            f,
            file_name="processed.png",
            mime="image/png"
        )
