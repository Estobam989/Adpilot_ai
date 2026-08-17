
import streamlit as st
import google.generativeai as genai

st.set_page_config(
    page_title="Gemini Streamlit Template",
    page_icon="✨",
    layout="centered"
)

st.title("✨ Gemini API Streamlit Template")

# Configure Gemini API
try:
    # Access the API key securely from .streamlit/secrets.toml
    # Make sure you have GEMINI_API_KEY="your_api_key" in that file
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
except KeyError:
    st.error("GEMINI_API_KEY not found in .streamlit/secrets.toml. Please add your API key.")
    st.stop()
except Exception as e:
    st.error(f"Error configuring Gemini API: {e}")
    st.stop()

# Initialize the GenerativeModel
# You can choose a different model if needed, e.g., 'gemini-pro'
model = genai.GenerativeModel('gemini-1.5-flash')

st.write("Enter a prompt and let Gemini generate some text for you!")

# User input for the prompt
user_prompt = st.text_area("Enter your prompt here:", "Write a short story about a brave knight.")

if st.button("Generate Text"):
    if user_prompt:
        with st.spinner("Generating response..."):
            try:
                response = model.generate_content(user_prompt)
                st.subheader("Generated Text:")
                st.write(response.text)
            except Exception as e:
                st.error(f"An error occurred during generation: {e}")
    else:
        st.warning("Please enter a prompt to generate text.")

st.markdown("---")
st.info("To run this app: Save this code to `streamlit_gemini_template.py`, ensure your `secrets.toml` has `GEMINI_API_KEY`, and then run `!streamlit run streamlit_gemini_template.py` in a Colab cell, potentially with localtunnel for external access.")
