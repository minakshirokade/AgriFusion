import streamlit as st
import base64

# Page config with better theme
st.set_page_config(
    page_title="🌾 Soil Fertility Analyzer",
    layout="wide",
    page_icon="🌱",
    initial_sidebar_state="expanded"
)

# Background setup with glassmorphism effect
def add_bg_from_local(image_file):
    with open(image_file, "rb") as file:
        encoded_string = base64.b64encode(file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/jpg;base64,{encoded_string});
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            font-family: 'Poppins', sans-serif;
        }}

        .main-container {{
            background: rgba(255, 255, 255, 0.85);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border-radius: 24px;
            border: 1px solid rgba(255, 255, 255, 0.3);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
            margin: 30px auto;
            max-width: 2000px;
            padding: 5px;          /* Add padding for neatness */
            text-align: center;     /* 👈 This will center all text inside */
            color: #333;
        }}

        .title {{
            color: #2e7d32;
            font-weight: 700;
            font-size: 2.5rem;
            margin-bottom: 20px;
            text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1);
            }}      

        .card {{
            background: rgba(255, 255, 255, 0.95);
            border-radius: 16px;
            padding: 30px;
            margin-bottom: 30px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
            border-left: 5px solid #4caf50;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }}

        .card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.12);
        }}

        .card-title {{
            color: #2e7d32;
            font-size: 1.5rem;
            font-weight: 600;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            gap: 10px;
        }}

        .card-content {{
            color: #424242;
            font-size: 1rem;
            line-height: 1.7;
            margin-bottom: 20px;
        }}

        div.stButton > button {{
            background: linear-gradient(135deg, #66bb6a, #43a047);
            color: white;
            border: none;
            border-radius: 10px;
            padding: 14px 24px;
            font-size: 1rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
        }}

        div.stButton > button:hover {{
            background: linear-gradient(135deg, #57a35a, #2e7d32);
            transform: translateY(-2px);
            box-shadow: 0 6px 16px rgba(0, 0, 0, 0.3);
            color: white;
        }}

        div.stButton {{
            display: flex;
            justify-content: center;
        }}

        .footer-container {{
            background: rgba(255, 255, 255, 0.95);
            border-radius: 16px;
            padding: 25px;
            margin-top: 50px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
            border-left: 5px solid #8d6e63;
            text-align: center;
        }}

        @media (max-width: 768px) {{
            .main-container {{
                padding: 30px 20px;
                margin: 20px 15px;
            }}
            .card {{
                padding: 25px 20px;
            }}
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Add background image
add_bg_from_local("soil1.jpg")

# Add custom font
st.markdown("""
<link href='https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap' rel='stylesheet'>
""", unsafe_allow_html=True)

# Main container
st.markdown("""
<div class='main-container'>
    <h1 class='title'>🌿 AgriFusion 🌿</h1>
""", unsafe_allow_html=True)

st.markdown("""
<div class='card'>
    <h2 class='card-title'>🧪 Soil Health Analysis</h2>
    <p class='card-content'>
    Soil Health Analysis is a scientific process that involves a detailed assessment of soil’s physical, chemical, and biological properties to evaluate its capability to sustain agricultural productivity and support plant growth. Healthy soil serves as the foundation of successful farming — it ensures robust crop yields, enhances nutrient uptake, improves water retention, and promotes biodiversity within the soil ecosystem. A comprehensive soil health assessment examines the balance of essential macronutrients like Nitrogen (N), Phosphorus (P), and Potassium (K), as well as vital secondary nutrients and micronutrients such as Sulfur (S), Zinc (Zn), Iron (Fe), Copper (Cu), Manganese (Mn), and Boron (B). These nutrients play specific roles in plant metabolism, enzyme activation, root development, and resistance to pests and diseases. Moreover, the analysis includes critical indicators like soil pH, which determines nutrient availability; Electrical Conductivity (EC), reflecting soil salinity levels; and Organic Carbon (OC), which signifies soil fertility, microbial activity, and organic matter content. Soil with balanced nutrients and proper structure fosters stronger root systems, reduces the risk of erosion, and boosts the resilience of crops against environmental stress. Regular Soil Health Analysis not only diagnoses nutrient deficiencies or toxicities but also empowers farmers to adopt data-driven approaches in choosing fertilizers, selecting crop types, planning irrigation schedules, and practicing crop rotation. It also aids in reducing input costs and environmental damage by avoiding the over-application of chemical fertilizers. Ultimately, a well-maintained and monitored soil profile leads to sustainable agriculture, higher crop productivity, better soil conservation, and long-term food security.
    </p>
""", unsafe_allow_html=True)
# Two-column buttons for Soil Health
with st.container():
    col1, col2 = st.columns([1, 1])

    with col1:
        analyze_clicked = st.button("🔍 Analyze Soil Health", key="analyze_button1", use_container_width=True)
        if analyze_clicked:
            st.switch_page("pages/stream_soil.py")

    with col2:
        dashboard_clicked = st.button("📊 View Dashboard", key="dashboard_button1", use_container_width=True)
        if dashboard_clicked:
            st.switch_page("pages/Dashboard1.py")

# --- Fertilizer Recommendation Card ---
st.markdown("""
<div class='card'>
    <h2 class='card-title'>💡 Fertilizer Recommendation</h2>
    <p class='card-content'>
    Fertilizer Recommendation is a data-driven approach that involves providing customized guidance on the type, quantity, and timing of fertilizers based on the specific nutritional profile of the soil. Every crop has unique nutrient requirements at different growth stages, and applying the right fertilizer in the right amount is essential for optimizing plant health and maximizing yield. Overuse or misuse of fertilizers can lead to soil degradation, nutrient imbalance, water pollution, and increased farming costs, while underuse may result in poor crop development and low productivity.Through detailed soil analysis, this system identifies deficiencies in key macronutrients such as Nitrogen (N), Phosphorus (P), and Potassium (K), as well as important micronutrients like Zinc (Zn), Iron (Fe), and Boron (B). Based on these insights, it recommends the most appropriate fertilizers — whether organic (like compost or green manure) or inorganic (such as urea, DAP, or SSP) — along with their optimal application rates. Additionally, it considers soil pH, moisture content, and crop type to ensure site-specific nutrient management (SSNM), which enhances nutrient use efficiency and minimizes environmental impact.This intelligent recommendation system empowers farmers to make informed decisions, reduce input costs, enhance soil fertility, and achieve sustainable agricultural practices. It promotes responsible fertilizer use, which not only benefits crop health but also contributes to long-term soil conservation, food security, and climate resilience. With the help of machine learning and real-time analytics, farmers can now access precise, location-specific, and crop-optimized fertilizer strategies like never before.
    </p>
""", unsafe_allow_html=True)

# Two-column buttons for Fertilizer Recommendation
with st.container():
    col1, col2 = st.columns([1, 1])

    with col1:
        analyze_clicked = st.button("🌾 Get Fertilizer Advice", key="analyze_button2", use_container_width=True)
        if analyze_clicked:
            st.switch_page("pages/fertilizer.py")

    with col2:
        dashboard_clicked = st.button("📊 View Dashboard", key="dashboard_button2", use_container_width=True)
        if dashboard_clicked:
            st.switch_page("pages/Dashboard2.py")

# --- Crop Suitability Card ---
st.markdown("""
<div class='card'>
    <h2 class='card-title'>🌱 Crop Suitability Analysis</h2>
    <p class='card-content'>
   Crop Suitability Analysis is a vital agricultural practice that helps identify the most appropriate crops for a specific soil and climatic condition. Not all soils are suitable for every type of crop — factors like soil texture, pH, organic matter, nutrient composition, drainage capacity, and micro/macro-nutrient availability play a crucial role in determining which crops can thrive in a given environment. This analysis bridges the gap between soil health and agricultural productivity by aligning crop selection with natural resource conditions.By leveraging data-driven techniques and machine learning models, our system evaluates key soil parameters such as Nitrogen, Phosphorus, Potassium, pH levels, Electrical Conductivity, and micronutrients like Zinc, Iron, and Manganese. Based on this comprehensive profile, it recommends crops that are biologically and economically viable for the farmer. For instance, acidic soils may be more suitable for crops like potatoes or pineapples, while neutral to alkaline soils may favor wheat or barley. The system also considers regional climatic conditions, rainfall patterns, and irrigation availability to improve recommendation accuracy.Implementing crop suitability analysis enables farmers to maximize yields, reduce crop failure risks, and conserve soil health. It also encourages diversified cropping patterns, which helps prevent nutrient depletion and supports sustainable farming. Moreover, this approach can guide decisions for crop rotation, intercropping, and seasonal planning, further enhancing long-term productivity. With real-time, intelligent insights, farmers are empowered to make informed choices that align with both ecological conditions and market demand.
    </p>
""", unsafe_allow_html=True)

# Two-column buttons for Crop Suitability
with st.container():
    col1, col2 = st.columns([1, 1])

    with col1:
        analyze_clicked = st.button("🌽 Find Suitable Crops", key="analyze_button3", use_container_width=True)
        if analyze_clicked:
            st.switch_page("pages/Crop.py")

    with col2:
        dashboard_clicked = st.button("📊 View Dashboard", key="dashboard_button3", use_container_width=True)
        if dashboard_clicked:
            st.switch_page("pages/Dashboard3.py")

# --- Footer ---
st.markdown("""
<div class='footer-container'>
    <p>© 2025 Soil Fertility Analyzer | Developed with ❤️ using Streamlit</p>
    <p style="font-size:0.85rem; color: #555;">For professional agricultural advice, consult with a certified agronomist.</p>
</div>
</div>
""", unsafe_allow_html=True)
