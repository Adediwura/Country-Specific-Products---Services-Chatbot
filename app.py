import streamlit as st
import os
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

# Set environment variable
os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]  # Replace with your actual API key

def generate_text(content):
    # Extract the country from the prompt
    country = extract_country(content)

    # Construct a prompt tailored to the country
    prompt = f"What is {country} known for? List specific products or services."

    # Create a ChatGoogleGenerativeAI model and a HumanMessage
    model = ChatGoogleGenerativeAI(model="gemini-pro")  # Or "gemini-advanced", "gemini-basic"  # Replace with a suitable model name
    message = HumanMessage(content=prompt)

    # Stream the response
    response = model.stream([message])

    # Process the response and return the generated text
    generated_text = ""
    for chunk in response:
        generated_text += chunk.content
    return generated_text

def extract_country(text):
    # Implement a more sophisticated country extraction method if needed
    # For simplicity, assume the country is mentioned at the beginning
    words = text.split()
    if len(words) > 0:
        return words[0].capitalize()
    return None

# Streamlit app starts here
st.title("Country-Specific Products and Services")

user_input = st.text_area("Enter a country:")

if st.button("Generate Text"):
    generated_text = generate_text(user_input)
    st.write(generated_text)