import streamlit as st
import pandas as pd
import joblib
from datetime import datetime

# Label mapping
label_mapping = {
    'rice': 0, 'maize': 1, 'chickpea': 2, 'kidneybeans': 3, 'pigeonpeas': 4, 'mothbeans': 5,
    'mungbean': 6, 'blackgram': 7, 'lentil': 8, 'pomegranate': 9, 'banana': 10, 'mango': 11,
    'grapes': 12, 'watermelon': 13, 'muskmelon': 14, 'apple': 15, 'orange': 16, 'papaya': 17,
    'coconut': 18, 'cotton': 19, 'jute': 20, 'coffee': 21
}
reverse_label_mapping = {v: k.capitalize() for k, v in label_mapping.items()}

crop_info = {
    "Rice": "Rice is a staple food for more than half of the world's population. It requires warm temperatures and plenty of water.",
    "Maize": "Maize is versatile and used for food, feed, and industry. It grows best in well-drained fertile soils.",
    "Chickpea": "Chickpeas are rich in protein and fix nitrogen in soil, improving fertility.",
    "Kidneybeans": "Kidney beans thrive in warm climates and are high in protein and fiber.",
    "Pigeonpeas": "Pigeonpeas are drought-resistant legumes, great for improving soil health.",
    "Mothbeans": "Mothbeans tolerate heat and dry conditions, ideal for arid regions.",
    "Mungbean": "Mungbeans grow fast and enrich soil by fixing nitrogen.",
    "Blackgram": "Blackgram is nutrient-rich and improves soil through nitrogen fixation.",
    "Lentil": "Lentils are cool-season crops, rich in protein and improve soil quality.",
    "Pomegranate": "Pomegranates require warm climates and well-drained soil, and are high in antioxidants.",
    "Banana": "Bananas need tropical climates with rich soil and plenty of moisture.",
    "Mango": "Mango trees thrive in tropical and subtropical climates with dry conditions.",
    "Grapes": "Grapes grow well in moderate climates and need good drainage.",
    "Watermelon": "Watermelon prefers warm temperatures and sandy loam soil for sweetness.",
    "Muskmelon": "Muskmelons need warm climates and well-drained soil for optimal growth.",
    "Apple": "Apples require temperate climates with chilling hours during winter.",
    "Orange": "Oranges grow best in subtropical to tropical climates with ample sunlight.",
    "Papaya": "Papayas grow quickly in tropical climates with well-drained soil.",
    "Coconut": "Coconuts thrive in coastal tropical areas with sandy soil.",
    "Cotton": "Cotton requires long frost-free periods and moderate rainfall.",
    "Jute": "Jute is a bast fiber crop that needs warm and humid climates.",
    "Coffee": "Coffee grows best in tropical highlands with rich soil and shade."
}

st.set_page_config(page_title="🌾 Crop Recommender", layout="wide", page_icon="🌱")

def add_custom_styles():
    background_url = "https://images.unsplash.com/photo-1501004318641-b39e6451bec6?auto=format&fit=crop&w=1470&q=80"
    st.markdown(f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

        .stApp::before {{
            content: "";
            position: fixed;
            top: 0; left: 0;
            width: 100vw; height: 100vh;
            background-color: rgba(255, 255, 255, 0.4);
            z-index: -1;
        }}

        .stApp {{
            background: url('{background_url}') no-repeat center center fixed;
            background-size: cover;
            font-family: 'Inter', sans-serif;
            color: #1a1a1a;
        }}

        .main-container {{
            background: transparent !important;
            padding: 2.5rem;
            margin: 1rem 0;
            box-shadow: none !important;
            color: white;
            text-shadow: 1px 1px 3px rgba(0,0,0,0.7);
        }}

        .main-title {{
            font-size: 4.0rem;
            font-weight: 700;
            text-align: center;
            color: #e0f2f1;
            text-shadow: 2px 2px 8px rgba(0,0,0,0.9);
            margin-bottom: 0.25rem;
            user-select: none;
        }}

        .subtitle {{
            text-align: center;
            font-size: 1.5rem;
            color: black;
            font-weight: 500;
            margin-bottom: 2rem;
            user-select: none;
        }}

        .stForm {{
            background: rgba(255, 255, 255, 0.85);
            border-radius: 16px;
            padding: 2rem;
            border: 1px solid rgba(76, 175, 80, 0.3);
            color: #1a1a1a;
            box-shadow: 0 8px 20px rgba(0,0,0,0.15);
        }}

        .stButton > button {{
            background: linear-gradient(135deg, #4caf50, #388e3c) !important;
            color: white !important;
            font-weight: 600 !important;
            font-size: 30px !important;
            border: none !important;
            border-radius: 12px !important;
            padding: 14px 32px !important;
            width: 100% !important;
            transition: all 0.3s ease !important;
            box-shadow: 0 4px 15px rgba(76, 175, 80, 0.3) !important;
            text-transform: uppercase !important;
            letter-spacing: 0.5px !important;
        }}

        .stButton > button:hover {{
            background: linear-gradient(135deg, #388e3c, #4caf50) !important;
            transform: translateY(-2px) !important;
            box-shadow: 0 6px 20px rgba(76, 175, 80, 0.5) !important;
        }}

        /* Form input label & number input */
        .stForm label {{
            font-size: 1.5rem !important;
            font-weight: 600 !important;
            margin-bottom: 0.4rem !important;
        }}
        input[type="number"] {{
            font-size: 1.2rem !important;
            padding: 10px 14px !important;
            border-radius: 10px !important;
        }}
        .stForm .stNumberInput {{
            margin-bottom: 1.5rem !important;
        }}

        .result-card {{
            background: rgba(46, 125, 50, 0.8);
            border-radius: 20px;
            padding: 2rem;
            text-align: center;
            margin: 2rem 0;
            box-shadow: 0 10px 30px rgba(0,0,0,0.7);
            color: #e0f2f1;
            user-select: none;
        }}
        .result-title {{
            font-size: 2rem;
            font-weight: 700;
            margin-bottom: 1rem;
        }}
        .result-crop {{
            font-size: 3rem;
            font-weight: 900;
            margin: 1rem 0;
        }}
        .crop-info {{
            background: rgba(139, 195, 74, 0.4);
            border-radius: 16px;
            padding: 1.5rem;
            margin-top: 1rem;
            color: #1b5e20;
            font-weight: 600;
            font-size: 1.1rem;
            box-shadow: 0 6px 12px rgba(0,0,0,0.5);
            text-align: justify;
            user-select: none;
        }}
        .enhanced-footer {{
            background: rgba(46, 125, 50, 0.6);
            border-radius: 16px;
            text-align: center;
            padding: 2rem;
            margin-top: 3rem;
            color: #dcedc8;
            font-weight: 500;
        }}
        </style>
    """, unsafe_allow_html=True)

add_custom_styles()

st.markdown("<h1 class='main-title'>🌿 Your Intelligent Crop Advisor</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Enter your soil and climate parameters to get the best crop recommendations</p>", unsafe_allow_html=True)

st.markdown("<div class='main-container'>", unsafe_allow_html=True)

st.markdown("""
<div class='info-box' style='background: rgba(255, 255, 255, 0.8); border-radius: 12px; padding: 1.5rem; margin-bottom: 1.5rem; color: #1a1a1a; font-weight: 500;'>
    💡 <strong>Welcome to AgriFusion!</strong><br>
    Enter your soil and environmental parameters below to get personalized crop recommendations!
</div>
""", unsafe_allow_html=True)

@st.cache_resource(show_spinner=False)
def load_model():
    try:
        return joblib.load("crop_recommendation_model.pkl")
    except FileNotFoundError:
        st.error("❌ Model file 'crop_recommendation_model.pkl' not found.")
        return None
    except Exception as e:
        st.error(f"❌ Error loading model: {str(e)}")
        return None

model = load_model()

with st.form("crop_input_form"):
    st.markdown("### 📊 *Soil & Environmental Parameters*")
    col1, col2, col3 = st.columns(3, gap="large")
    with col1:
        N = st.number_input("Nitrogen content (Kg/Ha)", min_value=0, max_value=150, value=50)
        K = st.number_input("Potassium content (Kg/Ha)", min_value=5, max_value=250, value=50)
        temperature = st.number_input("Temperature (°C)", min_value=5.0, max_value=45.0, value=25.0, step=0.1)
    with col2:
        P = st.number_input("Phosphorus content (Kg/Ha)", min_value=5, max_value=150, value=40)
        ph = st.number_input("Soil pH", min_value=3.5, max_value=9.9, value=6.5, step=0.1)
        humidity = st.number_input("Humidity (%)", min_value=14.3, max_value=99.98, value=60.0, step=0.1)
    with col3:
        rainfall = st.number_input("Rainfall (mm)", min_value=20.2, max_value=298.6, value=100.0, step=0.1)

    submitted = st.form_submit_button("Predict Crop")

st.markdown("</div>", unsafe_allow_html=True)

if submitted and model:
    try:
        input_features = [[N, P, K, temperature, humidity, ph, rainfall]]
        prediction_encoded = model.predict(input_features)[0]
        predicted_crop = reverse_label_mapping.get(prediction_encoded, "Unknown").capitalize()

        st.markdown(f"""
        <div class='result-card'>
            <h2 class='result-title'>🌟 Recommended Crop for You</h2>
            <div class='result-crop'>{predicted_crop}</div>
            <div class='crop-info'>{crop_info.get(predicted_crop, "Detailed information about this crop is not available.")}</div>
        </div>
        """, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Error during prediction: {e}")

st.markdown("""
<div class="enhanced-footer">
    Developed with ❤️ by AgriFusion &nbsp; 
</div>
""", unsafe_allow_html=True)
