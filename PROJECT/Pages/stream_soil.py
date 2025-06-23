# Soil Fertility Web App
import streamlit as st
import pandas as pd
import joblib
import base64
import time
import datetime
from streamlit_lottie import st_lottie
import requests
from fpdf import FPDF

# Set page config
st.set_page_config(page_title="🌾 Soil Fertility Analyzer", layout="wide", page_icon="🌱")

# Function to add background image
# Function to add background image with fine-tuned transparency
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-color: rgba(255, 255, 255, 0.6);  /* Base transparency */
            background-blend-mode: lighten;
        }}
        
        /* Individual component transparencies */
        .title, .subtitle {{
            background-color: rgba(255, 255, 255, 0.85) !important;
        }}
        
        .stForm {{
            background-color: rgba(255, 255, 255, 0.8) !important;
        }}
        
        .stAlert, .stInfo, .stWarning {{
            background-color: rgba(255, 255, 255, 0.85) !important;
        }}
        
        .footer {{
            background-color: rgba(255, 255, 255, 0.8) !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Add background image
add_bg_from_local('soil1.jpg')

# Load animation
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# PDF report generator
def generate_pdf_report(data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Soil Fertility Report", ln=1, align='C')
    for key, value in data.items():
        pdf.cell(200, 10, txt=f"{key}: {value}", ln=1)
    return pdf.output(dest='S').encode('latin1')

# Load Lottie animations
loading_anim = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_usmfx6bp.json")
celebration_anim = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_sk5h1kfn.json")

# Load model
try:
    model = joblib.load("soil_fertility_model.pkl")
except:
    st.error("❌ Model not found.")
    model = None

# Title with improved contrast for background
st.markdown("""
    <style>
    .title {
        color: #2e7d32;
        text-align: center;
        background-color: rgba(255, 255, 255, 0.7);
        padding: 10px;
        border-radius: 10px;
    }
    .subtitle {
        color: #1b5e20;
        text-align: center;
        background-color: rgba(255, 255, 255, 0.7);
        padding: 5px;
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='title'>🌿 Soil Fertility Analyzer</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Analyze soil nutrients and predict fertility level</p>", unsafe_allow_html=True)

# Form input with semi-transparent background
st.markdown("""
    <style>
    .stForm {
        background-color: rgba(255, 255, 255, 0.8) !important;
        padding: 20px !important;
        border-radius: 10px !important;
    }
    </style>
""", unsafe_allow_html=True)

with st.form("soil_input"):
    st.subheader("📋 Enter Soil Nutrient Values")

    col1, col2, col3 = st.columns(3)
    with col1:
        N = st.number_input("Nitrogen (N) [kg/ha]", 6.0, 383.0, 100.0, help="Unit: kg/ha | Range: 6 - 383")
        P = st.number_input("Phosphorus (P) [kg/ha]", 2.9, 125.0, 50.0, help="Unit: kg/ha | Range: 2.9 - 125")
        K = st.number_input("Potassium (K) [kg/ha]", 11.0, 887.0, 150.0, help="Unit: kg/ha | Range: 11 - 887")
        pH = st.number_input("pH [0-14]", 0.9, 11.15, 6.5, help="Unit: pH | Range: 0.9 - 11.15")
    with col2:
        EC = st.number_input("Electrical Conductivity (EC) [dS/m]", 0.1, 0.95, 0.5, help="Unit: dS/m | Range: 0.1 - 0.95")
        OC = st.number_input("Organic Carbon (OC) [%]", 0.1, 24.0, 0.75, help="Unit: % | Range: 0.1 - 24")
        S = st.number_input("Sulfur (S) [ppm]", 0.64, 31.0, 10.0, help="Unit: mg/kg | Range: 0.64 - 31")
        Zn = st.number_input("Zinc (Zn) [ppm]", 0.07, 42.0, 0.5, help="Unit: mg/kg | Range: 0.07 - 42")
    with col3:
        Fe = st.number_input("Iron (Fe) [ppm]", 0.21, 44.0, 4.0, help="Unit: mg/kg | Range: 0.21 - 44")
        Cu = st.number_input("Copper (Cu) [ppm]", 0.09, 3.02, 0.5, help="Unit: mg/kg | Range: 0.09 - 3.02")
        Mn = st.number_input("Manganese (Mn) [ppm]", 0.11, 31.0, 5.0, help="Unit: mg/kg | Range: 0.11 - 31")
        B = st.number_input("Boron (B) [ppm]", 0.06, 2.82, 0.5, help="Unit: mg/kg | Range: 0.06 - 2.82")

    submitted = st.form_submit_button("🚀 Analyze Soil")

# Prediction
if submitted:
    with st.spinner("🔄 Analyzing..."):
        if loading_anim:
            st_lottie(loading_anim, height=100)
        time.sleep(2)

        features = pd.DataFrame([[N, P, K, pH, EC, OC, S, Zn, Fe, Cu, Mn, B]],
                                 columns=["N", "P", "K", "Ph", "EC", "OC", "S", "Zn", "Fe", "Cu", "Mn", "B"])

        if model:
            pred = model.predict(features)[0]
        else:
            pred = 1  # Fallback

        # Labels
        fertility_labels = {
            0: ("🚫 Low Fertility", "red"),
            1: ("✅ Moderate Fertility", "orange"),
            2: ("🌟 High Fertility", "green")
        }
        label, color = fertility_labels.get(pred, ("❓ Unknown", "gray"))

    # Display Result with better visibility
    st.markdown(f"""
    <div style='text-align:center; padding: 20px; background-color:rgba(255, 255, 255, 0.8); border-radius:10px;'>
        <h2>🔍 Soil Fertility Result</h2>
        <h1 style='color:{color};'>{label}</h1>
    </div>
    """, unsafe_allow_html=True)

    if pred == 2 and celebration_anim:
        st_lottie(celebration_anim, height=150)
        st.balloons()

    # Tips with better visibility
    st.markdown("""
    <style>
    .stWarning, .stInfo {
        background-color: rgba(255, 255, 255, 0.8) !important;
        border-radius: 5px !important;
        padding: 10px !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.subheader("💡 Suggestions")
    if N < 50:
        st.warning("➤ Low Nitrogen: Add compost or urea")
    if P < 20:
        st.warning("➤ Low Phosphorus: Apply Single Super Phosphate")
    if pH < 6:
        st.info("➤ Acidic Soil: Add lime")
    elif pH > 8:
        st.info("➤ Alkaline Soil: Add gypsum or sulfur")

    # Download PDF
    st.download_button(
        "📄 Download Report",
        generate_pdf_report(features.iloc[0].to_dict()),
        "Soil_Fertility_Report.pdf",
        "application/pdf"
    )

# Footer with better visibility
st.markdown("""
<style>
.footer {
    background-color: rgba(255, 255, 255, 0.8);
    padding: 10px;
    border-radius: 5px;
    text-align: center;
    color: #333;
    font-size: 0.9em;
}
</style>
<div class="footer">
    <hr>
    © 2025 Soil Analyzer | Powered by Streamlit
</div>
""", unsafe_allow_html=True)