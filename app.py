import streamlit as st
from streamlit_option_menu import option_menu
import time
from fsm import HealthFSM as FSM

# IMPORT HALAMAN YANG TELAH DIPISAH
from home import show_home, show_organ_detail
from obat import show_obat
from tips import show_tips
from about import show_about

# ==========================================
# KONFIGURASI HALAMAN
# ==========================================
st.set_page_config(
    page_title="Ngobat.In - Platform Informasi Kesehatan Terpadu",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# INJEKSI CSS GLOBAL & DESAIN KAPSUL OBAT MENGAPUNG
# ==========================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght=300;400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    /* Background Utama Halaman */
    .stApp {
        background: linear-gradient(135deg, #0b0f19 0%, #11152c 100%) !important;
        background-attachment: fixed !important;
        color: #e2e8f0 !important;
    }
    
    header {visibility: hidden;}
    [data-testid="collapsedControl"] {display: none;}
    
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 0rem;
        max-width: 1400px;
    }

    /* FIX: Menghilangkan sisa background putih pada komponen navbar */
    div[data-testid="stCustomComponentV1"], 
    iframe[title="streamlit_option_menu.option_menu"] {
        background-color: transparent !important;
    }

    .nav-logo-container {
        padding: 15px 0px 15px 0px;
        display: flex;
        align-items: center;
        justify-content: flex-start;
    }
    .nav-logo {
        font-size: 34px;
        font-weight: 800;
        color: #ffffff;
        letter-spacing: -0.5px;
    }
    .nav-logo span {
        color: #0884a6;
    }

    /* ==================================================
       PERBAIKAN TOTAL: TOMBOL KAPSUL OBAT MENGAPUNG NYATA
       ================================================== */
    
    /* Menjamin kontainer Popover berada di lapisan paling atas kanan-bawah layar */
    div[data-testid="stPopover"] {
        position: fixed !important;
        bottom: 35px !important;
        right: 35px !important;
        z-index: 999999 !important;
        display: block !important;
        visibility: visible !important;
    }

    /* Mengubah tombol bawaan menjadi bentuk Kapsul Medis (Merah & Putih) */
    div[data-testid="stPopover"] button {
        width: 65px !important;
        height: 110px !important;
        border-radius: 50px !important;
        /* Membuat efek belahan kapsul 50% Merah dan 50% Putih */
        background: linear-gradient(to bottom, #ff3b30 50%, #ffffff 50%) !important;
        border: 3px solid #2a2f55 !important;
        box-shadow: 0 12px 30px rgba(255, 61, 0, 0.3), inset 0 -8px 10px rgba(0,0,0,0.15) !important;
        cursor: pointer;
        transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        transform-origin: center;
        animation: pillFloating 3s ease-in-out infinite !important; /* Efek Mengapung */
    }

    /* Menyisipkan simbol palang medis kecil di tengah kapsul */
    div[data-testid="stPopover"] button::before {
        content: "🏥" !important;
        font-size: 20px !important;
        position: absolute !important;
        z-index: 10;
        filter: drop-shadow(0 2px 4px rgba(0,0,0,0.3));
    }

    /* Hilangkan teks tulisan bawaan di dalam tombol popover */
    div[data-testid="stPopover"] button p {
        display: none !important;
    }

    /* Efek Animasi Mengapung yang Halus */
    @keyframes pillFloating {
        0% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-15px) rotate(5deg); }
        100% { transform: translateY(0px) rotate(0deg); }
    }

    /* Efek Interaktif Ketika Disentuh/Kursor Diarahkan (Hover) */
    div[data-testid="stPopover"] button:hover {
        box-shadow: 0 20px 40px rgba(255, 59, 48, 0.5), 0 0 20px rgba(56, 189, 248, 0.4) !important;
        filter: brightness(1.1);
    }

    /* Jendela Pop-up Chatbot (Muncul Tepat di Atas Kapsul) */
    div[data-testid="stPopoverBody"] {
        background-color: #12162e !important;
        border: 2px solid #38bdf8 !important;
        border-radius: 20px !important;
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.7) !important;
        width: 380px !important;
        max-width: 85vw !important;
        position: fixed !important;
        bottom: 160px !important; /* Jarak aman di atas kapsul */
        right: 35px !important;
        z-index: 1000000 !important;
    }

    /* Menghias bagian dalam form input chat */
    .stChatInputContainer {
        background-color: #0b0f19 !important;
        border: 1px solid #2a2f55 !important;
        border-radius: 10px !important;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# INISIALISASI SESI
# ==========================================
if "bot" not in st.session_state:
    st.session_state.bot = FSM()
    st.session_state.bot.step("")
    st.session_state.history = [{"role": "assistant", "content": st.session_state.bot.get_response()}]

if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"

# ==========================================
# TOP NAVIGATION BAR (SOLID DESIGN)
# ==========================================
st.markdown('<div class="nav-logo-container"><div class="nav-logo">Ngobat.<span>In</span></div></div>', unsafe_allow_html=True)

menu_options = ["Home", "Penjelasan Obat", "Tips Kesehatan", "About Us"]

try:
    default_idx = menu_options.index(st.session_state.current_page)
except ValueError:
    default_idx = 0 

selected_menu = option_menu(
    menu_title=None,
    options=menu_options,
    icons=["house", "capsule", "heart-pulse", "info-circle"], 
    menu_icon="cast",
    default_index=default_idx,
    orientation="horizontal",
    styles={
        "container": {
            "padding": "8px !important", 
            "background-color": "#171a33 !important",
            "border": "1px solid #2a2f55 !important",
            "border-radius": "12px !important",
            "margin": "0px auto 35px auto !important",
            "box-shadow": "0 4px 15px rgba(0, 0, 0, 0.3) !important"
        },
        "icon": {
            "color": "#94a3b8 !important", 
            "font-size": "15px !important"
        }, 
        "nav-link": {
            "font-size": "14px !important", 
            "font-weight": "500 !important",
            "text-align": "center !important", 
            "margin": "0px 5px !important", 
            "padding": "10px 20px !important",
            "color": "#94a3b8 !important", 
            "background-color": "transparent !important", 
            "border-radius": "8px !important",
            "--hover-color": "#1e2243"
        },
        "nav-link-selected": {
            "background-color": "#21274d !important",
            "color": "#ffffff !important", 
            "font-weight": "700 !important", 
            "border": "1px solid #38bdf8 !important",
            "border-radius": "8px !important",
            "box-shadow": "none !important"
        },
    }
)

# Sinkronisasi rute navigasi
if not st.session_state.current_page.startswith("Detail_"):
    st.session_state.current_page = selected_menu
elif selected_menu != "Home": 
    st.session_state.current_page = selected_menu

# ==========================================
# ROUTING HALAMAN
# ==========================================
if st.session_state.current_page == "Home":
    show_home()
elif st.session_state.current_page.startswith("Detail_"):
    show_organ_detail(st.session_state.current_page)
elif st.session_state.current_page == "Penjelasan Obat":
    show_obat()
elif st.session_state.current_page == "Tips Kesehatan":
    show_tips()
elif st.session_state.current_page == "About Us":
    show_about()

# ==================================================
# WIDGET CHATBOL POP-UP (PEMICU KAPSUL OBAT)
# ==================================================
with st.popover("Buka Chatbot"): 
    st.markdown("<h4 style='color:#ffffff; font-weight:800; font-size: 18px; margin-bottom: 0px;'>Yuk Ngobat.In</h4>", unsafe_allow_html=True)
    st.markdown("<p style='color:#38bdf8; font-size:12px; margin-top:2px;'>STanyakan gejalamu disini</p>", unsafe_allow_html=True)
    st.markdown("<hr style='margin: 10px 0px; border-color: rgba(255, 255, 255, 0.1);'>", unsafe_allow_html=True)
    
    chat_container = st.container(height=350)
    with chat_container:
        for msg in st.session_state.history:
            avatar_icon = "🏥" if msg["role"] == "assistant" else "👤"
            with st.chat_message(msg["role"], avatar=avatar_icon):
                st.write(msg["content"])
                
    user_input = st.chat_input("Ada keluhan apa? Ceritakan di sini...")
    if user_input:
        st.session_state.history.append({"role": "user", "content": user_input})
        with chat_container:
            with st.chat_message("user", avatar="👤"): 
                st.write(user_input)
            with st.chat_message("assistant", avatar="🏥"):
                with st.spinner("Menganalisis..."):
                    time.sleep(0.5) 
                    st.session_state.bot.step(user_input)
                    bot_reply = st.session_state.bot.get_response()
                    st.write(bot_reply)
        st.session_state.history.append({"role": "assistant", "content": bot_reply})
        st.rerun()

# ==========================================
# FOOTER
# ==========================================
st.markdown("""
<div style="text-align: center; margin-top: 60px; padding-top: 20px; border-top: 1px solid #2a2f55;">
    <p style="color: #64748b; font-size: 12px;">© 2026 Ngobat.In - Platform Konten Edukasi Kesehatan.</p>
</div>
""", unsafe_allow_html=True)