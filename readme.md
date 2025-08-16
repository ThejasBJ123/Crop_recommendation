🌱 Agriculture-G-AI – Smart Crop Recommendation

A Streamlit web app powered by Google Gemini AI that provides smart crop recommendations based on soil type, weather, and region.

🚀 Features

Crop recommendation based on user input

Integration with Google Gemini (Generative AI)

Interactive and user-friendly Streamlit UI

Real-time AI-powered suggestions for farmers

🛠️ Installation
1. Clone the repository
git clone https://github.com/your-username/agriculture-g-ai.git
cd agriculture-g-ai

2. Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows

3. Install dependencies
pip install -r requirements.txt

4. Set up your API key

Create a .env file in the project root and add your Gemini API key:

GOOGLE_API_KEY=your_api_key_here

▶️ Usage

Run the Streamlit app:

streamlit run app.py


Open your browser at http://localhost:8501.

📂 Project Structure
agriculture-g-ai/
│── app.py               # Main Streamlit app
│── requirements.txt     # Dependencies
│── README.md            # Documentation
│── .env                 # API key (not to be shared)

📜 Example Code (app.py)
import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Streamlit UI
st.set_page_config(page_title="Agriculture-G-AI - Smart Crop Recommendation", layout="wide")
st.title("🌱 Agriculture-G-AI - Smart Crop Recommendation")

soil_type = st.text_input("Enter soil type (e.g., sandy, clay, loamy):")
region = st.text_input("Enter your region:")
weather = st.text_input("Enter weather condition (e.g., rainy, dry, humid):")

if st.button("Get Recommendation"):
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"Suggest the best crops for {soil_type} soil in {region} with {weather} weather."
    response = model.generate_content(prompt)
    st.subheader("✅ Recommended Crops")
    st.write(response.text)

📦 Requirements (requirements.txt)
streamlit
python-dotenv
google-generativeai
