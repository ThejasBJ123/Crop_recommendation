import streamlit as st
import google.generativeai as genai  

# Configure Gemini AI
genai.configure(api_key="AIzaSyABhOJDBPVl2eZ1KenFEFEock9yr_FBDh0")  # replace with your actual key

# Set Streamlit page config
st.set_page_config(page_title="Agriculture-G-AI - Smart Crop Recommendation", layout="wide")

# Custom styling
def set_bg_style():
    st.markdown(
        """
        <style>
            body {
                background: linear-gradient(to right, #e6f9e6, #f0fff0);
                color: #2e2e2e;
            }
            .stButton>button {
                background-color: #90EE90;
                color: white;
                font-size: 16px;
                padding: 10px;
                border-radius: 8px;
            }
            .stButton>button:hover {
                background-color: #218838;
            }
            .stTextInput>div>div>input {
                border-radius: 8px;
            }
            table {
                width: 100%;
                border-collapse: collapse;
                margin: 15px 0;
                font-size: 16px;
            }
            th, td {
                border: 1px solid #2e7d32;
                padding: 8px 12px;
                text-align: left;
            }
            th {
                background-color: #a5d6a7;
                color: #1b5e20;
            }
            tr:nth-child(even) {
                background-color: #f1f8e9;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

set_bg_style()

def recommend_crop_gemini(soil_type, pH, nitrogen, phosphorus, potassium, rainfall, temperature, location):
    """Use Gemini AI to recommend a crop based on input parameters."""
    prompt = f"""
    Based on the following soil and weather conditions, suggest the best crop(s) to grow in {location}:
    - Soil Type: {soil_type}
    - Soil pH: {pH}
    - Nitrogen Level: {nitrogen} ppm
    - Phosphorus Level: {phosphorus} ppm
    - Potassium Level: {potassium} ppm
    - Annual Rainfall: {rainfall} mm
    - Average Temperature: {temperature} °C

    Provide region-specific recommendations and explain briefly why the suggested crop is suitable.
    Show results in a **Markdown table** with these columns:
    | Crop | Suitability Reason | Sowing Time | Harvesting Time |

    Start with: "Based on the provided conditions, the recommended crop(s) are:" 
    End with: "Thank you for using the Smart Crop Recommendation System at Agriculture-G-AI 🌾🌾🌾."
    """

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)

    return response.text if response and hasattr(response, "text") else "Could not fetch recommendation."

# Streamlit UI
st.markdown(
    "<h1 style='color: #2e7d32;'>🌾 Smart Crop Recommendation System at Agriculture-G-AI</h1>",
    unsafe_allow_html=True
)
st.markdown("<p style='font-size:18px;'>Enter your soil and weather details below to get AI-powered crop suggestions.</p>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    soil_type = st.selectbox("🌱 Soil Type", ["Sandy", "Clay", "Loamy", "Silty", "Peaty", "Saline"])
    pH = st.slider("📏 Soil pH", 4.0, 9.0, 6.5)
    nitrogen = st.number_input("🧪 Nitrogen Level (ppm)", 0, 200, 50)
    phosphorus = st.number_input("🧪 Phosphorus Level (ppm)", 0, 200, 50)

with col2:
    potassium = st.number_input("🧪 Potassium Level (ppm)", 0, 200, 50)
    rainfall = st.number_input("🌧️ Annual Rainfall (mm)", 200, 3000, 1200)
    temperature = st.number_input("🌡️ Average Temperature (°C)", 0, 50, 25)
    location = st.text_input("📍 Location (City/District/State)", "")

st.markdown("<p style='color: #888; font-size: 14px;'>Ensure all details are correct for the best recommendations.</p>", unsafe_allow_html=True)

# Predict button
if st.button("🚀 Recommend Crop"):
    if location:
        crop_recommendation = recommend_crop_gemini(soil_type, pH, nitrogen, phosphorus, potassium, rainfall, temperature, location)
        st.success("🌾 Recommended Crop(s):")
        st.write(crop_recommendation)  # ✅ renders markdown table cleanly
    else:
        st.warning("⚠️ Please enter a location for region-specific recommendations.")

