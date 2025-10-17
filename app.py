import streamlit as st
from PIL import Image, ImageEnhance

st.set_page_config(page_title="🖼 Image Enhancer Studio", page_icon="🪄")

st.markdown(
    """
    <div style="text-align:center;">
        <h1 style="color:#4B8BBE;">🖼 Image Enhancer Studio</h1>
        <p style="font-size:18px; color:#555;">
            Upload, edit & enhance your images with ease 🚀
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Original Image", use_container_width=True)

    brightness = st.slider("Brightness", 0.0, 2.0, 1.0)
    contrast = st.slider("Contrast", 0.0, 2.0, 1.0)
    sharpness = st.slider("Sharpness", 0.0, 2.0, 1.0)
    grayscale = st.checkbox("Convert to Grayscale")

    enhancer = ImageEnhance.Brightness(image)
    img = enhancer.enhance(brightness)

    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(contrast)

    enhancer = ImageEnhance.Sharpness(img)
    img = enhancer.enhance(sharpness)

    if grayscale:
        img = img.convert("L")

    st.image(img, caption="Processed Image", use_container_width=True)

    img.save("processed.png")
    with open("processed.png", "rb") as f:
        st.download_button(
            "📥 Download Processed Image",
            f,
            file_name="processed.png",
            mime="image/png"
        )
