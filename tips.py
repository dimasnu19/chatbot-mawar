import streamlit as st
from utils import inject_custom_css

def show_tips():
    inject_custom_css()
    st.markdown("<h2 style='color:#ffffff; font-weight:700; border-bottom: 1px solid rgba(255,255,255,0.08); padding-bottom:10px;'>Jurnal Gaya Hidup Sehat</h2>", unsafe_allow_html=True)
    st.write("Investasikan waktu untuk membangun kebiasaan kecil setiap hari demi kesehatan fisik dan mental jangka panjang.")
    
    st.markdown("<br>", unsafe_allow_html=True) # Jarak kosong sedikit
    
    col1, col2 = st.columns(2)
    
    # ==========================================
    # KOLOM 1: NUTRISI, HIDRASI & FISIK DASAR
    # ==========================================
    with col1:
        st.success("**💧 Hidrasi Optimal**")
        st.write("Minum minimal 2 liter (8-10 gelas) air per hari. Warna urine yang kuning pucat atau bening adalah indikator utama bahwa tubuh Anda cukup terhidrasi.")
        
        st.info("**🥗 Piring Makan Sehat (Isi Piringku)**")
        st.write("Pastikan 50% piring Anda berisi sayur dan buah, 25% protein (hewani atau nabati), dan 25% karbohidrat kompleks. Hindari makan berlebih sebelum kenyang.")
        
        st.warning("**☀️ Paparan Sinar Matahari Pagi**")
        st.write("Sempatkan berjemur 10-15 menit di pagi hari (sebelum jam 10:00). Ini sangat krusial untuk sintesis Vitamin D yang menjaga imunitas dan kepadatan tulang.")
        
        st.error("**🚭 Batasi Gula & Makanan Olahan**")
        st.write("Batasi asupan gula harian maksimal 4 sendok makan (50 gram). Konsumsi makanan *ultra-processed* memicu inflamasi kronis dan risiko penyakit metabolik (seperti diabetes).")

        st.success("**🧼 Kebersihan Diri & Lingkungan**")
        st.write("Cuci tangan dengan sabun mengalir sebelum makan. Rutin ganti seprai seminggu sekali dan pastikan sirkulasi udara di dalam kamar tidur selalu berganti.")

    # ==========================================
    # KOLOM 2: ISTIRAHAT, AKTIVITAS & MENTAL
    # ==========================================
    with col2:
        st.info("**🛌 Regulasi Tidur yang Berkualitas**")
        st.write("Tidur 7-8 jam per malam. Saat berada di fase *deep sleep*, tubuh melakukan perbaikan sel rusak, menstabilkan hormon, dan memperkuat sistem kekebalan tubuh.")
        
        st.warning("**🏃‍♂️ Aktivitas Fisik Rutin**")
        st.write("Lakukan olahraga intensitas sedang (jalan cepat, berenang, jogging ringan, bersepeda) minimal 150 menit per minggu. Jangan lupa peregangan (*stretching*)!")
        
        st.error("**🧘‍♂️ Manajemen Stres & Kesehatan Mental**")
        st.write("Stres kronis memicu tingginya hormon kortisol yang dapat menurunkan daya tahan tubuh. Sempatkan *me-time*, meditasi, atau mengobrol dengan orang terdekat.")
        
        st.success("**📱 Digital Detox & Aturan Layar**")
        st.write("Terapkan aturan 20-20-20: setiap 20 menit menatap layar gawai, tataplah objek sejauh 20 kaki (6 meter) selama 20 detik. Hindari gawai 1 jam sebelum tidur agar tidak terkena paparan *blue light*.")
        
        st.info("**🪑 Postur Tubuh & Ergonomi Kerja**")
        st.write("Jika Anda bekerja duduk seharian, pastikan punggung tegak bersandar dan layar sejajar dengan mata. Bangun dan regangkan otot punggung setiap 1 jam untuk mencegah saraf terjepit.")