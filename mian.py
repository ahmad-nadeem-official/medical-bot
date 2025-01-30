import streamlit as st
from PIL import Image
import google.generativeai as genai


genai.configure(api_key=())

st.set_page_config(page_title="Image to text chatbot", page_icon="🧠")
st.title("🧪 Image to text chatbot")

try:
    model = genai.GenerativeModel("gemini-1.5-flash")
except Exception as e:
    st.error(f"Error initializing the AI model: {e}")

# Image Uploader
uploaded_file = st.file_uploader("Upload an organ image (JPEG format)", type=["jpeg", "jpg", "png"])

if uploaded_file is not None:
    try:
        st.write("Uploaded file received.")
        # Display Uploaded Image
        organ_image = Image.open(uploaded_file)
        st.image(organ_image, caption="Uploaded Image", use_container_width=200)

        # Generate Content Section
        prompt = st.text_input("Ask the AI about this image", "Tell me about this image")

        if st.button("Generate Response"):
            with st.spinner("Generating response..."):
                try:
                    response = model.generate_content([prompt, organ_image])
                    st.success("Response generated successfully!")
                    st.text_area("Response from AI", response.text, height=500)
                except Exception as e:
                    st.error(f"Error generating response: {e}")
    except Exception as e:
        st.error(f"Error processing the image: {e}")
else:
    st.info("Please upload another image to get started.")