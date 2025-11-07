import streamlit as st
import openai

st.set_page_config(page_title="TariffSolver-Lite", page_icon="🌐", layout="centered")

st.title("TariffSolver-Lite ⚙️")
st.subheader("Instant AI Tariff Classification Demo")
st.write("Describe a product and receive an estimated HS/HTS classification with duty/VAT details.")

# --- API Key setup ---
st.sidebar.header("API Configuration")
api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password")

# --- User input ---
user_input = st.text_input("Enter product description:", placeholder="e.g. Women's cotton blouse")

if st.button("Classify"):
    if not user_input.strip():
        st.warning("Please enter a product description.")
    elif not api_key.strip():
        st.error("Please enter your OpenAI API key in the sidebar.")
    else:
        openai.api_key = api_key
        with st.spinner("Classifying..."):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-4-turbo",
                    messages=[
                        {"role": "system", "content": "You are an expert customs classifier that returns HS codes and reasoning."},
                        {"role": "user", "content": f"Classify this product for tariff purposes: {user_input}"}
                    ]
                )
                output = response.choices[0].message["content"]
                st.success("Classification Result:")
                st.markdown(output)
            except Exception as e:
                st.error(f"Error: {e}")
