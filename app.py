import streamlit as st
from PIL import Image, ImageEnhance

st.set_page_config(page_title="🎨 Pic Perfect : Online Image Processing", page_icon="✨")

st.markdown(
    """
    <div style="text-align:center; background-color:#E8F5E9; padding:20px; border-radius:10px;">
        <h1 style="color:#2E7D32;">🎨 Pic Perfect : Online Image Processing</h1>
        <p style="font-size:18px; color:#1B5E20;">
            Upload, edit & enhance your images with ease 🌿
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

uploaded_file = st.file_uploader("📸 Upload an image", type=["jpg", "jpeg", "png"])

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
        <div style="text-align:center; background-color:#C8E6C9; padding:10px; border-radius:8px;">
            <h3 style="color:#1B5E20;">↻ ⏳Processed Image 🔜</h3>
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
