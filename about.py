import streamlit as st
from utils import inject_custom_css

def show_about():
    inject_custom_css()
    
    # ==================== HERO SECTION ====================
    st.markdown("""
        <div style="text-align: center; padding: 2rem 0 1rem 0;">
            <h1 style="font-size: 2.4rem; font-weight: 800; margin-bottom: 0.2rem; color: #ffffff;">
                💊 Ngobat.In
            </h1>
            <p style="font-size: 1.1rem; color: #a0b0d0; margin-top: 0; font-weight: 400;">
                Platform Skrining & Edukasi Kesehatan Digital Indonesia
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # ==================== MISI UTAMA ====================
    st.markdown("""
    <div style="background: rgba(20, 28, 58, 0.6); padding: 30px 25px; border-radius: 20px; 
                border: 1px solid rgba(255, 255, 255, 0.08); backdrop-filter: blur(25px);
                box-shadow: 0 15px 35px rgba(0,0,0,0.4); margin-bottom: 2rem;">
        <div style="display: flex; align-items: flex-start; gap: 20px;">
            <div style="font-size: 3rem; opacity: 0.9;">🎯</div>
            <div>
                <h2 style="margin: 0 0 10px 0; color: #ffffff; font-weight: 600;">Misi Kami</h2>
                <p style="margin: 0; font-size: 1rem; line-height: 1.8; color: #cbd5e1;">
                    <b>Ngobat.In</b> hadir untuk menjembatani kesenjangan akses informasi kesehatan yang andal di Indonesia. 
                    Kami menyediakan layanan <b>skrining gejala awal berbasis AI</b>, 
                    ensiklopedia obat, serta panduan gaya hidup sehat dalam satu platform interaktif yang mudah digunakan.
                    Tujuan kami bukanlah menggantikan dokter, melainkan memberdayakan masyarakat dengan pengetahuan 
                    agar lebih sadar kesehatan dan mampu mengambil keputusan yang tepat sebelum mengunjungi fasilitas medis.
                </p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # ==================== FITUR UNGGULAN (3 KOLOM) ====================
    st.markdown("<h2 style='color: #ffffff; margin-bottom: 1rem;'>✨ Fitur Utama</h2>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="background: rgba(25, 30, 65, 0.45); padding: 25px 18px; border-radius: 18px;
                    border: 1px solid rgba(255, 255, 255, 0.08); height: 100%;
                    box-shadow: 0 8px 20px rgba(0,0,0,0.25);">
            <div style="font-size: 2.5rem; margin-bottom: 10px;">🤖</div>
            <h3 style="color: #ffffff; margin: 0 0 12px 0; font-size: 1.2rem;">Tanya Chatbot</h3>
            <p style="color: #b9c2d9; font-size: 0.9rem; line-height: 1.6;">
                Chatbot berbasis <em>Finite State Machine</em> memandu Anda menceritakan keluhan 
                dengan bahasa alami dan memberikan analisis awal yang edukatif sebelum ke dokter.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background: rgba(25, 30, 65, 0.45); padding: 25px 18px; border-radius: 18px;
                    border: 1px solid rgba(255, 255, 255, 0.08); height: 100%;
                    box-shadow: 0 8px 20px rgba(0,0,0,0.25);">
            <div style="font-size: 2.5rem; margin-bottom: 10px;">📚</div>
            <h3 style="color: #ffffff; margin: 0 0 12px 0; font-size: 1.2rem;">Kamus Obat Lengkap</h3>
            <p style="color: #b9c2d9; font-size: 0.9rem; line-height: 1.6;">
                Informasi terperinci tentang obat bebas, obat resep, hingga herbal berstandar BPOM. 
                Lengkap dengan indikasi, efek samping, dan peringatan keamanan.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="background: rgba(25, 30, 65, 0.45); padding: 25px 18px; border-radius: 18px;
                    border: 1px solid rgba(255, 255, 255, 0.08); height: 100%;
                    box-shadow: 0 8px 20px rgba(0,0,0,0.25);">
            <div style="font-size: 2.5rem; margin-bottom: 10px;">🌿</div>
            <h3 style="color: #ffffff; margin: 0 0 12px 0; font-size: 1.2rem;">Gaya Hidup Sehat</h3>
            <p style="color: #b9c2d9; font-size: 0.9rem; line-height: 1.6;">
                Kumpulan tips nutrisi, aktivitas fisik, manajemen stres, dan kebiasaan positif 
                yang didukung data ilmiah untuk investasi kesehatan jangka panjang.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # ==================== MENGAPA NGABAT.IN? ====================
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h2 style='color: #ffffff; margin-bottom: 1rem;'>🌟 Mengapa Ngobat.In?</h2>", unsafe_allow_html=True)
    
    why_col1, why_col2 = st.columns(2)
    with why_col1:
        st.markdown("""
        <div style="background: rgba(30, 35, 70, 0.5); padding: 22px; border-radius: 16px; 
                    border-left: 4px solid #4ade80; margin-bottom: 15px;">
            <h4 style="color: #ffffff; margin: 0 0 8px 0;">🔬 Teknologi Interaktif</h4>
            <p style="color: #b9c2d9; margin: 0; font-size: 0.9rem;">
                Chatbot kami menggunakan <b>Finite State Machine</b> untuk meniru alur pikir tenaga medis 
                dalam menggali gejala. Bukan sekadar chatbot biasa, melainkan sistem yang terstruktur dan kontekstual.
            </p>
        </div>
        <div style="background: rgba(30, 35, 70, 0.5); padding: 22px; border-radius: 16px; 
                    border-left: 4px solid #facc15; margin-bottom: 15px;">
            <h4 style="color: #ffffff; margin: 0 0 8px 0;">📱 Desain Responsif & Ramah</h4>
            <p style="color: #b9c2d9; margin: 0; font-size: 0.9rem;">
                Antarmuka modern yang mudah diakses melalui web dan mobile, dengan tampilan yang bersih 
                dan intuitif bagi semua kalangan.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    with why_col2:
        st.markdown("""
        <div style="background: rgba(30, 35, 70, 0.5); padding: 22px; border-radius: 16px; 
                    border-left: 4px solid #60a5fa; margin-bottom: 15px;">
            <h4 style="color: #ffffff; margin: 0 0 8px 0;">🛡️ Edukasi Berbasis Data</h4>
            <p style="color: #b9c2d9; margin: 0; font-size: 0.9rem;">
                Seluruh konten obat dan gaya hidup disusun merujuk pada pedoman BPOM, Kemenkes RI, 
                serta sumber medis kredibel. Kami mengutamakan akurasi informasi.
            </p>
        </div>
        <div style="background: rgba(30, 35, 70, 0.5); padding: 22px; border-radius: 16px; 
                    border-left: 4px solid #f472b6; margin-bottom: 15px;">
            <h4 style="color: #ffffff; margin: 0 0 8px 0;">❤️ Fokus pada Pencegahan</h4>
            <p style="color: #b9c2d9; margin: 0; font-size: 0.9rem;">
                Lebih dari sekadar “mengobati”, kami mendorong literasi kesehatan preventif melalui 
                jurnal hidup sehat dan deteksi dini gejala.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # ==================== DISCLAIMER PENTING ====================
    st.markdown("<br>", unsafe_allow_html=True)
    st.warning("""
    ⚠️ **Peringatan Medis**
    
    Ngobat.In adalah alat bantu edukasi dan skrining awal, **bukan pengganti diagnosis dokter**. 
    Informasi yang diberikan tidak boleh dijadikan satu-satunya dasar pengambilan keputusan medis. 
    Jika Anda mengalami gejala serius, segera hubungi tenaga kesehatan profesional atau kunjungi 
    fasilitas kesehatan terdekat.
    """)
    
    # ==================== FOOTER ====================
    st.divider()
    st.markdown("""
    <div style="text-align: center; color: #8b9dc0; font-size: 0.85rem; padding: 10px 0 20px 0;">
        © 2025 Ngobat.In – Platform Edukasi Kesehatan Digital Indonesia<br>
        <span style="opacity: 0.7;">Dibangun dengan kepedulian, didukung teknologi AI.</span>
    </div>
    """, unsafe_allow_html=True)