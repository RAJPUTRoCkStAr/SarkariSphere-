import streamlit as st
from streamlit_lottie import st_lottie
from lotti.lot import Admit_card
from datacollect import list_admit_cards

def admitjob():
    # 🧭 Hero Section
    st.markdown("""
        <div style='text-align: center; padding-top: 30px;'>
            <h1 style='color: #003366; font-size: 42px;'>🎟️ Sarkari Admit Cards</h1>
            <p style='font-size: 18px; color: #666;'>Download your official admit cards instantly — skip the redirection hassle and focus on your prep!</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("")

    # 🎥 Centered Lottie Animation
    col1, col2, col3 = st.columns([1, 5, 1])
    with col2:
        st_lottie(Admit_card, speed=1, reverse=False, loop=True, quality='high', height=340, width=720, key="admitAnim")

    st.markdown("")

    # 📦 Styled Admit Card Listings Container
    st.markdown("""
        <div style="
            background: linear-gradient(145deg, #ffffff, #f3f3f3);
            padding: 30px;
            border-radius: 16px;
            margin: 30px 0;
            box-shadow: 0 4px 16px rgba(0,0,0,0.05);
        ">
            <h3 style='color: #333; text-align: center; padding-bottom: 10px;'>📤 Download Available Admit Cards</h3>
    """, unsafe_allow_html=True)

    list_admit_cards()

    st.markdown("</div>", unsafe_allow_html=True)

    # 👣 Footer Motivation
    st.markdown("""
        <div style='text-align:center; padding: 10px 0 40px;'>
            <p style='font-size: 14px; color: #999;'>🎯 Keep your preparation strong — grab your admit card and be exam-ready!</p>
        </div>
    """, unsafe_allow_html=True)
