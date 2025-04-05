import streamlit as st
from streamlit_lottie import st_lottie
from lotti.lot import job_detail
from datacollect import list_jobs, detail_job

def openjob():
    if "selected_job" in st.session_state:
        detail_job()
    else:
        # 🧭 Hero Section
        st.markdown("""
            <div style='text-align: center; padding-top: 30px;'>
                <h1 style='color: #003366; font-size: 42px;'>🧑‍💼 Latest Government Job Listings</h1>
                <p style='font-size: 18px; color: #666;'>Handpicked Sarkari opportunities with direct apply links — updated daily for your career goals.</p>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("")

        # 🎥 Centered Lottie Animation
        col1, col2, col3 = st.columns([1, 5, 1])
        with col2:
            st_lottie(job_detail, speed=1, reverse=False, loop=True, quality='high', height=340, width=720, key="jobAnim")

        st.markdown("")

        # 🗃️ Styled Job Listings Container
        st.markdown("""
            <div style="
                background: linear-gradient(145deg, #ffffff, #f3f3f3);
                padding: 30px;
                border-radius: 16px;
                margin: 30px 0;
                box-shadow: 0 4px 16px rgba(0,0,0,0.05);
            ">
                <h3 style='color: #333; text-align: center; padding-bottom: 10px;'>📋 Open Positions You Can Apply For</h3>
        """, unsafe_allow_html=True)

        list_jobs()

        st.markdown("</div>", unsafe_allow_html=True)

        # 👣 Footer Motivation
        st.markdown("""
            <div style='text-align:center; padding: 10px 0 40px;'>
                <p style='font-size: 14px; color: #999;'>🌟 Don't just dream of a government job — apply today and make it real.</p>
            </div>
        """, unsafe_allow_html=True)
