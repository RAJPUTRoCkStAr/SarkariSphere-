import streamlit as st
from streamlit_lottie import st_lottie
from lotti.lot import Front_page  
def home():
    st.markdown("<h1 style='color:#003366;'>📘 SarkariSphere</h1>", unsafe_allow_html=True)

    # ---- Hero Section ----
    col1, col2 = st.columns([2, 2])
    with col1:
        st.markdown("""
            <h3 style='color:#222;'>Your Gateway to Government Opportunities</h3>
            <p style='font-size:16px; line-height:1.6; color:#444;'>
                <b>SarkariSphere</b> is your one-stop destination for all updates related to government jobs across India. 
                From the latest job postings to admit cards, results, and official notifications — we bring everything under one platform.
            </p>
            <p style='font-size:16px; color:#444;'>No more hopping across websites. Stay informed, stay ahead. 🔍</p>
            <p style='font-size:16px; color:#0066cc;'><i>Built for job seekers, students, and aspirants with simplicity and speed in mind.</i></p>
        """, unsafe_allow_html=True)

    with col2:
        st_lottie(Front_page, speed=1, reverse=True, loop=True, quality='medium', height=380, width=680, key=None)

    st.markdown("---")

    # ---- 🛠 How it Works Section ----
    st.markdown("### 🛠 How It Works")
    how_cols = st.columns(3)
    with how_cols[0]:
        st.markdown("#### 🔍 Explore Listings")
        st.write("Find opportunities across SSC, UPSC, Railways, Banking, State-level, and more.")

    with how_cols[1]:
        st.markdown("#### 📄 Understand Requirements")
        st.write("Check job details, eligibility, deadlines, age limits, and application fees.")

    with how_cols[2]:
        st.markdown("#### 🚀 Take Action")
        st.write("Get direct links to apply online, download admit cards, and check your results instantly.")

    st.markdown("---")

    # ---- 🚀 Why SarkariSphere ----
    st.markdown("### 🚀 Why Choose SarkariSphere?")
    st.markdown("""
    - ✅ Clean and distraction-free user interface  
    - ⚡ Lightning-fast scraping and live updates  
    - 🔗 One-click access to official notifications and application portals  
    - 📅 Deadline-aware filters so you never miss an opportunity  
    - 📥 Direct download links for results and admit cards
    """)

    st.markdown("---")

    # ---- 🔮 Future Enhancements ----
    st.markdown("### 🔮 What's Coming Next")
    st.markdown("""
    We're building more value into the platform! Upcoming features include:
    
    - 📱 A mobile-friendly UI for better access on-the-go  
    - 🧠 Smart job recommendations using AI  
    - 📧 Job alerts via email and WhatsApp  
    - 📝 Resume builder and PDF export tools  
    - 🗂 Save & bookmark jobs for future reference  
    - 🌍 Multilingual support including Hindi and regional languages
    """)

    st.markdown("---")

    # ---- Footer ----
    st.markdown("""
    <div style='text-align: center; padding-top: 20px; font-size: 14px; color: #888;'>
        © 2025 <b>SarkariSphere</b> | Empowering India’s job seekers — Made with ❤️ by <a href='#' style='color: #094de0;'>Sumit Kumar Singh</a>
    </div>
    """, unsafe_allow_html=True)
