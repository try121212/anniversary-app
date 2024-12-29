import streamlit as st
import time

# Page configuration
st.set_page_config(page_title="Happy Anniversary Baby!", layout="wide")

# Styling
st.markdown(
    """
    <style>
    body {
        background-color: #FFE4E1;
        font-family: 'Courier New', Courier, monospace;
        text-align: center;
    }
    .title {
        color: #FF1493;
        font-size: 3em;
        font-weight: bold;
        animation: colorchange 5s infinite;
    }
    .hearts {
        color: #FF69B4;
        font-size: 2.5em;
    }
    @keyframes colorchange {
        0% { color: #FF1493; }
        25% { color: #FF69B4; }
        50% { color: #FFB6C1; }
        75% { color: #FF69B4; }
        100% { color: #FF1493; }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown("<div class='title'>Happy Anniversary, Baby! 🎉❤️</div>", unsafe_allow_html=True)

# Heart animation
hearts = "💖💘💞💕💓💗💝"
for heart in hearts:
    st.write(heart, end=" ")
    time.sleep(0.2)

# Main message
st.markdown(
    """
    <div style='color: #FF69B4; font-size: 1.5em;'>
    You are my sunshine, my moonlight, and my everything. 🌞🌜✨<br>
    Today, we celebrate our love, and I promise for your every need. 🥰
    </div>
    """,
    unsafe_allow_html=True
)

# Confetti effect (add-on for visuals)
st.snow()

# Optional additional effects
st.balloons()

# Closing statement
st.markdown(
    """
    <div style='color: #FF1493; font-size: 1.5em;'>
    Forever yours, with all my love ❤️.
    </div>
    """,
    unsafe_allow_html=True
)

# Footer message
st.markdown(
    """
    <div style='color: #FFB6C1; font-size: 1em;'>
    PS: Sorry I forgot the date, but here's to making it unforgettable! 😘
    </div>
    """,
    unsafe_allow_html=True
)
