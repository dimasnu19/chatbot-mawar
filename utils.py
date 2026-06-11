import streamlit as st

# ==========================================
# INJEKSI CSS: TEMA DEEP BLUE GLASSMORPHISM
# ==========================================
def inject_custom_css():
    st.markdown("""
    <style>
    /* Mengubah background aplikasi menjadi Deep Blue dengan efek ambient glow premium */
    .stApp {
        background-color: #0b0d1e !important;
        background-image: 
            radial-gradient(circle at 85% 10%, rgba(139, 92, 246, 0.22) 0%, transparent 40%),
            radial-gradient(circle at 10% 80%, rgba(56, 189, 248, 0.18) 0%, transparent 40%),
            radial-gradient(circle at 50% 50%, rgba(20, 24, 60, 0.1) 0%, transparent 70%) !important;
        background-attachment: fixed !important;
        color: #e2e8f0 !important;
    }

    /* Styling Teks Global */
    h1, h2, h3, h4, h5, h6 {
        color: #ffffff !important;
        font-weight: 700 !important;
        letter-spacing: -0.01em !important;
    }
    p, span, label, li {
        color: #aeb9ce !important;
    }

    /* FIX UTAMA: Memaksa Container Bawaan Menjadi Kaca Transparan Sempurna */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(25, 30, 65, 0.35) !important;
        backdrop-filter: blur(20px) !important;
        -webkit-backdrop-filter: blur(20px) !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        border-radius: 20px !important;
        box-shadow: 0 12px 40px 0 rgba(0, 0, 0, 0.5) !important;
        transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1) !important;
        padding: 5px !important;
    }
    
    /* Menghilangkan background solid bawaan Streamlit di dalam kontainer */
    div[data-testid="stVerticalBlockBorderWrapper"] > div {
        background-color: transparent !important;
    }
    
    /* Efek Hover Interaktif saat Kartu Kaca Disorot */
    div[data-testid="stVerticalBlockBorderWrapper"]:hover {
        transform: translateY(-6px) !important;
        background: rgba(35, 42, 90, 0.45) !important;
        border-color: rgba(56, 189, 248, 0.4) !important;
        box-shadow: 0 20px 50px rgba(56, 189, 248, 0.15) !important;
    }

    /* Custom Tampilan Tab Navigasi Dalam Halaman */
    button[data-baseweb="tab"] {
        background: transparent !important;
        color: #64748b !important;
        font-weight: 500 !important;
        border-bottom-width: 2px !important;
        padding: 10px 20px !important;
    }
    button[data-baseweb="tab"][aria-selected="true"] {
        color: #38bdf8 !important;
        border-bottom-color: #38bdf8 !important;
        font-weight: 700 !important;
    }

    /* Custom Tombol Berorientasi Kaca (*Glass Buttons*) */
    div.stButton > button {
        background: rgba(56, 189, 248, 0.08) !important;
        color: #38bdf8 !important;
        border: 1px solid rgba(56, 189, 248, 0.3) !important;
        border-radius: 12px !important;
        font-weight: 600 !important;
        letter-spacing: 0.5px !important;
        transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
        backdrop-filter: blur(5px) !important;
    }
    div.stButton > button:hover {
        background: linear-gradient(135deg, #38bdf8 0%, #8b5cf6 100%) !important;
        color: #ffffff !important;
        border-color: transparent !important;
        transform: scale(1.03) !important;
        box-shadow: 0 8px 25px rgba(56, 189, 248, 0.35) !important;
    }

    /* Styling Glassmorphism untuk Expander (Kamus Obat) */
    div[data-testid="stExpander"] {
        background: rgba(25, 30, 65, 0.3) !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        border-radius: 16px !important;
        backdrop-filter: blur(15px) !important;
        box-shadow: 0 8px 32px rgba(0,0,0,0.3) !important;
        margin-bottom: 15px !important;
    }
    div[data-testid="stExpander"] > details {
        background-color: transparent !important;
    }
    div[data-testid="stExpander"] details summary {
        color: #ffffff !important;
        font-weight: 600 !important;
    }

    /* Styling Glassmorphism untuk Notifikasi/Alert */
    div[data-testid="stNotification"] {
        background: rgba(25, 30, 65, 0.5) !important;
        backdrop-filter: blur(20px) !important;
        border-radius: 14px !important;
        box-shadow: 0 8px 32px rgba(0,0,0,0.3) !important;
    }
    div[data-testid="stNotification"] div[role="alert"] {
        background: transparent !important;
    }
    
    /* Custom Garis Pemisah (Divider) */
    hr {
        border-color: rgba(255, 255, 255, 0.08) !important;
        margin: 30px 0 !important;
    }
    </style>
    """, unsafe_allow_html=True)