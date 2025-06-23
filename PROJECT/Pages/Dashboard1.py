import streamlit as st
import base64

# Set page configuration
st.set_page_config(page_title="🌾 Soil Prediction Dashboard", layout="wide")

# 🔹 Background from local image
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
            .center {{
                display: flex;
                justify-content: center;
                align-items: center;
                flex-direction: column;
                text-align: center;
            }}
            iframe {{
                border-radius: 12px;
                box-shadow: 0 0 20px rgba(0, 0, 0, 0.2);
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    except:
        st.warning("⚠️ Background image not found. Default background applied.")

add_bg_from_local("soil1.jpg")

# Content starts
st.markdown('<div class="center">', unsafe_allow_html=True)

st.markdown("<h1>🌱 Soil Fertility Data Analysis</h1>", unsafe_allow_html=True)
st.markdown("<p>This dashboard provides soil analysis and prediction insights using Power BI.</p>", unsafe_allow_html=True)

# Embed Power BI iframe in center
powerbi_url = "https://app.powerbi.com/reportEmbed?reportId=606f5918-5c84-4fed-a17e-b13d8f145b9f&autoAuth=true&ctid=7402bea1-1360-40f4-8265-f62014f87ab5"

st.markdown(
    f"""
    <iframe title="SOIL PREDICTION"
        width="1350"
        height="600"
        src="{powerbi_url}"
        frameborder="0"
        allowFullScreen="true">
    </iframe>
    """,
    unsafe_allow_html=True
)

st.markdown('</div>', unsafe_allow_html=True)
