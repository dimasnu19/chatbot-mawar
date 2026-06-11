import streamlit as st
from utils import inject_custom_css

def show_about():
    inject_custom_css()
    st.markdown("<h2 style='color:#ffffff; font-weight:700;'>Misi Ngobat.In</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div style="background: rgba(25, 30, 65, 0.35); padding: 25px; border-radius: 16px; border: 1px solid rgba(255, 255, 255, 0.08); backdrop-filter: blur(20px); box-shadow: 0 10px 30px rgba(0,0,0,0.3);">
        <p style="margin:0; font-size: 15px; line-height: 1.7; color: #aeb9ce;">
        <b>Ngobat.In</b> lahir dari visi untuk menyediakan wadah informasi kesehatan digital yang mudah dipahami di Indonesia. 
        Kami menggabungkan antarmuka digital yang interaktif dengan teknologi Chatbot berbasis <i>Finite State Machine (FSM)</i> yang membantu pengguna mensimulasikan alur konsultasi keluhan dasar secara mandiri sebelum melangkah ke fasilitas medis.
        </p>
    </div>


    """, unsafe_allow_html=True)
    
