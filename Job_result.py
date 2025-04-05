import streamlit as st
from streamlit_lottie import st_lottie
from lotti.lot import Result
from datacollect import list_results

def resultjob():
    st.markdown("""
        <div style='text-align: center; padding-top: 30px;'>
            <h1 style='color: #003366; font-size: 42px;'>📊 Government Exam Results</h1>
            <p style='font-size: 18px; color: #666;'>Skip the noise. Directly download your Sarkari exam results with just one click.</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("")

    col1, col2, col3 = st.columns([1, 5, 1])
    with col2:
        st_lottie(Result, speed=1, reverse=False, loop=True, quality='high', height=340, width=720, key="resultAnim")

    st.markdown("")

    st.markdown("""
        <div style="
            background: linear-gradient(145deg, #ffffff, #f2f2f2);
            padding: 30px;
            border-radius: 16px;
            margin: 30px 0;
            box-shadow: 0 4px 16px rgba(0,0,0,0.06);
        ">
            <h3 style='color: #222; text-align: center; padding-bottom: 10px;'>📥 Latest Declared Results</h3>
    """, unsafe_allow_html=True)

    list_results()

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("""
        <div style='text-align:center; padding: 10px 0 40px;'>
            <p style='font-size: 14px; color: #999;'>Remember: Success is a series of small wins. 📈</p>
        </div>
    """, unsafe_allow_html=True)
