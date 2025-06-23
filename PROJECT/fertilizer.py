# Fertilizer Recommendation Web App - Enhanced Version with Polished UI
import streamlit as st
import pandas as pd
import joblib
import base64
import time
from streamlit_lottie import st_lottie
import requests
from fpdf import FPDF

# ----------------- CONFIG -----------------
st.set_page_config(
    page_title="\U0001F33E Fertilizer Recommender", 
    layout="wide", 
    page_icon="\U0001F331",
    initial_sidebar_state="collapsed"
)

# Load animation from Lottie
def load_lottieurl(url: str):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

# Enhanced background with lighter overlay
def add_bg_from_local(image_file):
    try:
        with open(image_file, "rb") as f:
            encoded_string = base64.b64encode(f.read())
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: linear-gradient(rgba(255, 255, 255, 0.85), rgba(255, 255, 255, 0.85)), 
                                 url(data:image/jpg;base64,{encoded_string.decode()});
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                background-attachment: fixed;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    except:
        st.markdown("""
            <style>
            .stApp {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                background-attachment: fixed;
            }
            </style>
        """, unsafe_allow_html=True)

add_bg_from_local("ferti.jpg")

# ----------------- LOAD FILES -----------------
try:
    model = joblib.load("fertilizer_model.pkl")
    le_soil = joblib.load("le_soil.pkl")
    le_crop = joblib.load("le_crop.pkl")
    le_fert = joblib.load("le_fert.pkl")
except:
    st.error("❌ Model or encoders not found. Please ensure all required files are in the directory.")
    st.stop()

# ----------------- ANIMATIONS -----------------
loading_anim = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_usmfx6bp.json")
celebration_anim = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_sk5h1kfn.json")

# ----------------- ENHANCED STYLES -----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

html, body, [class*="css"]  {
    font-family: 'Inter', sans-serif;
    color: #1a3b2e;
    scroll-behavior: smooth;
}

.main-title {
    font-size: 4rem;
    font-weight: 700;
    color: #2c5f2d;
    text-align: center;
    background: #eaf6ec;
    padding: 2rem 1rem;
    border-radius: 20px;
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.12);
}

.subtitle {
    font-size: 1.5rem;
    font-weight: 500;
    color: #14532d;
    text-align: center;
    background: #f5fdf7;
    padding: 1rem 2rem;
    border-radius: 16px;
    margin: 1rem auto 2rem auto;
    width: 90%;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
}

.form-container {
    background: white;
    border-radius: 16px;
    padding: 2rem;
    box-shadow: 0 12px 35px rgba(0, 0, 0, 0.08);
    margin-bottom: 2rem;
}

.section-header {
    font-size: 1.8rem;
    font-weight: 700;
    border-left: 5px solid #2e7d32;
    padding-left: 1rem;
    margin-bottom: 1rem;
}

.stNumberInput input,
.stSelectbox div[data-baseweb="select"] {
    background-color: #f8fcf9;
    border-radius: 12px;
    font-size: 1rem;
    color: #1a3b2e;
    padding: 0.6rem;
}

.stButton > button {
    background: #2e7d32;
    color: white;
    padding: 0.75rem 2rem;
    border: none;
    border-radius: 8px;
    font-size: 1.2rem;
    transition: background 0.3s ease;
    box-shadow: 0 5px 15px rgba(46, 125, 50, 0.3);
}

.stButton > button:hover {
    background: #256029;
}

.result-container {
    background: #f3fdf5;
    border-left: 6px solid #2e7d32;
    border-radius: 12px;
    padding: 1.5rem;
    margin: 2rem 0;
}

.prediction-display {
    font-size: 2rem;
    background: linear-gradient(to right, #4caf50, #66bb6a);
    padding: 1.2rem;
    border-radius: 12px;
    color: white;
    text-align: center;
    font-weight: bold;
    margin: 1rem 0;
    animation: glow 1.5s infinite alternate;
}

@keyframes glow {
    from { box-shadow: 0 0 10px #4caf50; }
    to { box-shadow: 0 0 25px #66bb6a; }
}

.suggestion-container {
    background: #fffbe6;
    padding: 1rem 1.5rem;
    border-left: 5px solid #ff9800;
    border-radius: 8px;
    margin: 1rem 0;
    font-size: 1.05rem;
}

.footer {
    background: #e8f5e9;
    text-align: center;
    padding: 1.5rem;
    border-radius: 12px;
    font-size: 1rem;
    color: #1a3b2e;
    margin-top: 3rem;
}

.footer h4 {
    font-size: 1.2rem;
    margin-bottom: 0.5rem;
}

.footer p {
    font-size: 0.9rem;
    margin: 0;
}

.stDownloadButton button {
    background: #2e7d32;
    color: white;
    padding: 0.7rem 1.5rem;
    font-size: 1.1rem;
    border-radius: 10px;
    box-shadow: 0 5px 15px rgba(46, 125, 50, 0.3);
}

.stDownloadButton button:hover {
    background: #256029;
}
</style>
""", unsafe_allow_html=True)


# ----------------- TITLE -----------------
st.markdown("""
    <div class="main-title">
        🌾 Fertilizer Recommendation System
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="subtitle">
        🔬 Get personalized fertilizer recommendations based on your soil conditions and crop requirements
    </div>
""", unsafe_allow_html=True)

# ----------------- PDF REPORT -----------------
def generate_pdf_report(data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=16)
    pdf.cell(200, 10, txt="Fertilizer Recommendation Report", ln=1, align='C')
    pdf.ln(10)
    pdf.set_font("Arial", size=12)
    
    for key, value in data.items():
        pdf.cell(200, 8, txt=f"{key}: {value}", ln=1)
        pdf.ln(2)
    
    return pdf.output(dest='S').encode('latin1')

# ----------------- FORM -----------------
st.markdown('<div class="form-container">', unsafe_allow_html=True)

with st.form("fertilizer_input"):
    st.markdown('<h3 class="section-header">📋 Enter Soil & Crop Parameters</h3>', unsafe_allow_html=True)
    
    # Environmental Parameters
    st.markdown("#### 🌡️ Environmental Conditions")
    st.markdown("<div style='font-size: 1.1rem; color: #0d4a12; font-weight: 600; margin-bottom: 1rem;'>Please enter the environmental conditions for your farming location:</div>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        temperature = st.number_input(
            "🌡️ Temperature (°C)", 
            min_value=10.0, 
            max_value=50.0, 
            value=30.0,
            help="Average temperature in your region"
        )
        
    with col2:
        humidity = st.number_input(
            "💧 Humidity (%)", 
            min_value=10.0, 
            max_value=90.0, 
            value=50.0,
            help="Relative humidity percentage"
        )
        
    with col3:
        moisture = st.number_input(
            "🏞️ Soil Moisture (%)", 
            min_value=10.0, 
            max_value=80.0, 
            value=40.0,
            help="Soil moisture content percentage"
        )
    
    st.markdown("---")
    
    # Soil and Crop Parameters
    st.markdown("#### 🌱 Soil & Crop Information")
    st.markdown("<div style='font-size: 1.1rem; color: #0d4a12; font-weight: 600; margin-bottom: 1rem;'>Select your soil type and the crop you want to grow:</div>", unsafe_allow_html=True)
    col4, col5 = st.columns(2)
    
    with col4:
        soil_type = st.selectbox(
            "🏔️ Soil Type", 
            le_soil.classes_,
            help="Select your soil type"
        )
        
    with col5:
        crop_type = st.selectbox(
            "🌾 Crop Type", 
            le_crop.classes_,
            help="Select the crop you want to grow"
        )
    
    st.markdown("---")
    
    # Nutrient Parameters
    st.markdown("#### 🧪 Soil Nutrient Content (kg/ha)")
    st.markdown("<div style='font-size: 1.1rem; color: #0d4a12; font-weight: 600; margin-bottom: 1rem;'>Enter the current nutrient levels in your soil (get soil testing done for accurate values):</div>", unsafe_allow_html=True)
    col6, col7, col8 = st.columns(3)
    
    with col6:
        nitrogen = st.number_input(
            "🟢 Nitrogen (N)", 
            min_value=0, 
            max_value=100, 
            value=30,
            help="Nitrogen content in soil"
        )
        
    with col7:
        potassium = st.number_input(
            "🟡 Potassium (K)", 
            min_value=0, 
            max_value=50, 
            value=20,
            help="Potassium content in soil"
        )
        
    with col8:
        phosphorous = st.number_input(
            "🔴 Phosphorous (P)", 
            min_value=0, 
            max_value=50, 
            value=15,
            help="Phosphorous content in soil"
        )

    st.markdown("<br>", unsafe_allow_html=True)
    submitted = st.form_submit_button("🚀 Get Fertilizer Recommendation")

st.markdown('</div>', unsafe_allow_html=True)

# ----------------- PREDICTION -----------------
if submitted:
    # Loading animation
    with st.spinner("🔄 Analyzing your soil and crop data..."):
        if loading_anim:
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st_lottie(loading_anim, height=120)
        time.sleep(2)

        # Encode categorical variables
        encoded_soil = le_soil.transform([soil_type])[0]
        encoded_crop = le_crop.transform([crop_type])[0]

        # Create input dataframe
        input_df = pd.DataFrame([[
            temperature, humidity, moisture,
            encoded_soil, encoded_crop,
            nitrogen, potassium, phosphorous
        ]], columns=[
            'Temperature', 'Humidity', 'Moisture', 'Soil Type', 'Crop Type',
            'Nitrogen', 'Potassium', 'Phosphorous'
        ])

        # Make prediction
        prediction = model.predict(input_df)
        fertilizer = le_fert.inverse_transform(prediction)[0]

    # Display results
    st.markdown('<div class="result-container">', unsafe_allow_html=True)
    
    # Large Prediction Display
    st.markdown(f'''
        <div class="prediction-display">
            🎯 RECOMMENDED FERTILIZER: {fertilizer}
        </div>
    ''', unsafe_allow_html=True)
    
    # Success message with animation
    st.success(f"✅ **Analysis Complete!** Based on your soil and crop parameters, we recommend using **{fertilizer}** for optimal growth and yield.")
    
    if celebration_anim:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st_lottie(celebration_anim, height=150)

    # Display input summary
    st.markdown("### 📊 Input Summary")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("🌡️ Temperature", f"{temperature}°C")
        st.metric("🟢 Nitrogen", f"{nitrogen} mg/kg")
        
    with col2:
        st.metric("💧 Humidity", f"{humidity}%")
        st.metric("🟡 Potassium", f"{potassium} mg/kg")
        
    with col3:
        st.metric("🏞️ Moisture", f"{moisture}%")
        st.metric("🔴 Phosphorous", f"{phosphorous} mg/kg")
        
    with col4:
        st.metric("🏔️ Soil Type", soil_type)
        st.metric("🌾 Crop Type", crop_type)

    st.markdown('</div>', unsafe_allow_html=True)

    # Intelligent Suggestions
    st.markdown("### 💡 Personalized Recommendations")
    st.markdown("<div style='font-size: 1.2rem; color: #0d4a12; font-weight: 600; margin-bottom: 1.5rem;'>Based on your soil analysis, here are our expert recommendations:</div>", unsafe_allow_html=True)
    
    suggestions = []
    
    if nitrogen < 20:
        suggestions.append("🟢 **Low Nitrogen Detected**: Consider applying Urea (46-0-0) or organic compost to boost nitrogen levels for better plant growth.")
    
    if phosphorous < 15:
        suggestions.append("🔴 **Low Phosphorous**: Apply Single Super Phosphate (SSP) or Diammonium Phosphate (DAP) to improve root development and flowering.")
    
    if potassium < 15:
        suggestions.append("🟡 **Low Potassium**: Use Muriate of Potash (MOP) or Sulphate of Potash to enhance disease resistance and fruit quality.")
    
    if temperature > 35:
        suggestions.append("🌡️ **High Temperature**: Ensure adequate irrigation and consider shade nets to protect your crops from heat stress.")
    
    if humidity > 70:
        suggestions.append("💧 **High Humidity**: Improve drainage and air circulation to prevent fungal diseases.")
    
    if not suggestions:
        suggestions.append("✅ **Optimal Conditions**: Your soil parameters look good! The recommended fertilizer should work perfectly for your crop.")

    for i, suggestion in enumerate(suggestions, 1):
        st.info(f"**Tip {i}:** {suggestion}")

    # Download Report
    st.markdown("### 📄 Download Your Detailed Report")
    st.markdown("<div style='font-size: 1.1rem; color: #0d4a12; font-weight: 600; margin-bottom: 1rem;'>Get a comprehensive PDF report with all your soil parameters and fertilizer recommendations:</div>", unsafe_allow_html=True)
    report_data = {
        "Temperature": f"{temperature}°C",
        "Humidity": f"{humidity}%",
        "Moisture": f"{moisture}%",
        "Soil Type": soil_type,
        "Crop Type": crop_type,
        "Nitrogen": f"{nitrogen} mg/kg",
        "Potassium": f"{potassium} mg/kg",
        "Phosphorous": f"{phosphorous} mg/kg",
        "Recommended Fertilizer": fertilizer
    }
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.download_button(
            "📄 Download Detailed Report (PDF)",
            generate_pdf_report(report_data),
            f"Fertilizer_Recommendation_{fertilizer.replace(' ', '_')}.pdf",
            "application/pdf",
            use_container_width=True
        )

# ----------------- FOOTER -----------------
st.markdown("""
<div class="footer">
    <hr style="border: 1px solid rgba(76, 175, 80, 0.5); margin: 1rem auto; width: 80%;">
    <h4 style="color: #2e7d32; margin: 0.5rem 0;">🌱 Smart Agriculture Technology</h4>
    <p style="margin: 0.5rem 0;">© 2025 Fertilizer Recommender | Powered by Machine Learning & Streamlit</p>
    <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem; color: #666;">
        Helping farmers make data-driven decisions for sustainable agriculture 🌾
    </p>
</div>
""", unsafe_allow_html=True)