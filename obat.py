import streamlit as st
from utils import inject_custom_css

def show_obat():
    inject_custom_css()
    st.markdown("<h2 style='color:#ffffff; font-weight:700; border-bottom: 1px solid rgba(255,255,255,0.08); padding-bottom:10px;'>Kamus Obat Farmasi & Tradisional</h2>", unsafe_allow_html=True)
    st.write("Jelajahi klasifikasi obat, pahami indikasi, efek samping, serta peruntukannya berdasarkan pedoman keamanan BPOM Indonesia.")
    
    # Membagi menjadi 4 Tab berdasarkan Golongan Obat
    tab1, tab2, tab3, tab4 = st.tabs(["🟢 Obat Bebas (OTC)", "🔵 Obat Bebas Terbatas", "🔴 Obat Keras (Resep)", "🌿 Obat Tradisional"])
    
    # ==========================================
    # TAB 1: OBAT BEBAS
    # ==========================================
    with tab1:
        st.success("**Golongan Obat Bebas:** Ditandai dengan lingkaran hijau bergaris tepi hitam. Aman dibeli tanpa resep dokter untuk menangani keluhan ringan.")
        
        with st.expander("💊 Analgesik & Antipiretik Dasar (Pereda Nyeri & Demam)", expanded=True):
            st.write("**Contoh:** Paracetamol (Asetaminofen).")
            st.write("**Fungsi:** Menurunkan suhu tubuh saat demam dan meredakan nyeri ringan (sakit kepala, sakit gigi).")
            st.warning("**Peringatan:** Aman untuk lambung, namun konsumsi dosis berlebih (>4 gram sehari) dapat memicu kerusakan hati (Hepatotoksik).")

        with st.expander("🛡️ Antasida (Obat Maag & Asam Lambung)"):
            st.write("**Contoh:** Promag, Mylanta (kandungan Aluminium & Magnesium Hidroksida).")
            st.write("**Fungsi:** Meredakan gejala maag, perut kembung, dan rasa perih di lambung.")
            st.write("**Peringatan:** Wajib dikunyah terlebih dahulu sebelum ditelan dan dikonsumsi saat perut kosong (1 jam sebelum makan).")

        with st.expander("✨ Suplemen, Vitamin & Mineral"):
            st.write("**Contoh:** Vitamin C, Vitamin D3, Zink, Zat Besi (Sangobion).")
            st.write("**Fungsi:** Menjaga daya tahan tubuh, mencegah anemia, dan membantu pemulihan pasca sakit.")
            st.write("**Peringatan:** Konsumsi Vitamin C dosis tinggi harus diimbangi minum air putih yang banyak agar tidak membebani kerja ginjal.")

        with st.expander("🧴 Obat Topikal Dasar (Luar Tubuh)"):
            st.write("**Contoh:** Minyak Kayu Putih, Balsem Otot, Bedak Salicyl.")
            st.write("**Fungsi:** Memberikan sensasi hangat, meredakan gatal ringan, dan nyeri otot luar.")

    # ==========================================
    # TAB 2: OBAT BEBAS TERBATAS
    # ==========================================
    with tab2:
        st.info("**Golongan Obat Bebas Terbatas:** Ditandai lingkaran biru. Dapat dibeli tanpa resep, namun wajib memperhatikan tanda peringatan (Kotak Hitam P.No.1 - P.No.6).")
        
        # Penjelasan Tanda Peringatan
        st.markdown("""
        **Tanda Peringatan Wajib Perhatian:**
        * **P.No. 1:** Awas! Obat Keras. Bacalah aturan pakainya.
        * **P.No. 2:** Awas! Obat Keras. Hanya untuk dikumur, jangan ditelan.
        * **P.No. 3:** Awas! Obat Keras. Hanya untuk bagian luar dari badan.
        * **P.No. 4:** Awas! Obat Keras. Hanya untuk dibakar.
        * **P.No. 5:** Awas! Obat Keras. Tidak boleh ditelan.
        * **P.No. 6:** Awas! Obat Keras. Obat wasir, jangan ditelan.
        """)

        with st.expander("🤧 Antihistamin Generasi 1 (Obat Alergi)", expanded=True):
            st.write("**Contoh:** CTM (Chlorpheniramine Maleate).")
            st.write("**Fungsi:** Memblokir histamin untuk meredakan gatal, bersin, dan ruam kulit.")
            st.warning("**Efek Samping:** Sangat menyebabkan kantuk berat. Jangan mengemudi setelah minum obat ini.")

        with st.expander("🗣️ Obat Batuk (Antitusif & Ekspektoran)"):
            st.write("**Contoh:** Dextromethorphan (Batuk Kering), Guaifenesin (Batuk Berdahak).")
            st.write("**Peringatan:** Jangan gunakan penekan batuk kering (Antitusif) jika batuk Anda berdahak, karena dahak akan menumpuk di paru-paru.")

        with st.expander("🤢 Anti-Emetik (Obat Anti-Mabuk Perjalanan)"):
            st.write("**Contoh:** Dimenhydrinate (Antimo).")
            st.write("**Fungsi:** Mencegah mual dan muntah akibat mabuk kendaraan.")
            st.write("**Peringatan:** Diminum 30 menit sebelum perjalanan. Menimbulkan efek kantuk.")

        with st.expander("💩 Antidiare (Penghenti Diare)"):
            st.write("**Contoh:** Loperamide (penggunaan terbatas), Attapulgite.")
            st.write("**Fungsi:** Memperlambat gerak usus atau menyerap racun dan cairan berlebih.")
            st.write("**Peringatan:** Hentikan segera jika diare sudah mampet untuk mencegah sembelit.")

    # ==========================================
    # TAB 3: OBAT KERAS (RESEP)
    # ==========================================
    with tab3:
        st.error("**Golongan Obat Keras:** Ditandai lingkaran merah dengan huruf 'K'. **Hanya boleh dibeli dan digunakan dengan resep dokter.**")
        
        with st.expander("🦠 Antibiotik (Pembunuh Bakteri)", expanded=True):
            st.write("**Contoh:** Amoxicillin, Cefadroxil, Azithromycin, Ciprofloxacin.")
            st.write("**Fungsi:** Membunuh bakteri penyebab infeksi.")
            st.error("**Aturan Wajib:** HARUS DIHABISKAN sesuai dosis dokter meskipun gejala sudah hilang. Jika dihentikan sembarangan, bakteri akan menjadi kebal (*Resistensi Antibiotik*).")

        with st.expander("🔥 NSAID Keras (Anti-inflamasi Non-Steroid)"):
            st.write("**Contoh:** Asam Mefenamat, Meloxicam, Ketorolac, Natrium Diklofenak.")
            st.write("**Fungsi:** Meredakan peradangan dan nyeri intensitas sedang-berat (nyeri sendi, pasca operasi, kram haid hebat).")
            st.warning("**Peringatan:** Sangat keras untuk lambung. Wajib diminum sesudah makan. Risiko pendarahan lambung jika digunakan jangka panjang.")

        with st.expander("🩸 Antihipertensi (Penurun Tensi Darah)"):
            st.write("**Contoh:** Amlodipine, Captopril, Bisoprolol, Candesartan.")
            st.write("**Fungsi:** Mengontrol tekanan darah tinggi untuk mencegah serangan jantung dan stroke.")
            st.write("**Peringatan:** Harus diminum rutin setiap hari pada jam yang sama.")

        with st.expander("🍬 Obat Antidiabetes & Kolesterol"):
            st.write("**Contoh:** Metformin, Glimepiride (Diabetes) | Simvastatin, Atorvastatin (Kolesterol).")
            st.write("**Fungsi:** Mengontrol kadar gula darah dan menurunkan plak kolesterol jahat (LDL).")
            st.write("**Peringatan:** Simvastatin sebaiknya diminum pada malam hari karena produksi kolesterol tertinggi terjadi saat tubuh beristirahat.")

        with st.expander("🛑 Kortikosteroid (Obat Anti-radang Kuat)"):
            st.write("**Contoh:** Dexamethasone, Methylprednisolone.")
            st.write("**Fungsi:** Menekan sistem imun untuk mengatasi radang berat, asma, alergi parah, dan autoimun.")
            st.warning("**Efek Samping:** Pemakaian jangka panjang memicu *Moon Face* (wajah bengkak/bulat), keropos tulang, dan diabetes.")

    # ==========================================
    # TAB 4: OBAT TRADISIONAL (BPOM)
    # ==========================================
    with tab4:
        st.success("**Golongan Obat Tradisional:** Alternatif pengobatan dari alam yang telah diakui dan diklasifikasikan oleh BPOM Indonesia.")
        
        with st.expander("🌿 Jamu (Logo Ranting Daun)", expanded=True):
            st.write("**Definisi:** Obat tradisional yang khasiatnya dibuktikan berdasarkan pengalaman empiris (turun-temurun).")
            st.write("**Contoh:** Tolak Angin, Antangin, Kuku Bima.")
            st.write("**Syarat:** Aman digunakan dan memenuhi persyaratan mutu BPOM, namun belum melewati uji klinis/medis.")

        with st.expander("⭐ Obat Herbal Terstandar / OHT (Logo 3 Bintang)"):
            st.write("**Definisi:** Obat herbal yang sudah melalui **Uji Praklinis** (diuji pada hewan percobaan) untuk membuktikan keamanan dan khasiatnya.")
            st.write("**Contoh:** Diapet, Kiranti, Lelap.")
            st.write("**Syarat:** Bahan baku harus distandarisasi agar kualitasnya konsisten di setiap produksi.")

        with st.expander("❄️ Fitofarmaka (Logo Kristal Salju)"):
            st.write("**Definisi:** Tingkatan tertinggi obat herbal. Sudah melewati **Uji Klinis** (diuji pada manusia).")
            st.write("**Contoh:** Stimuno, Tensigard, Inlacin.")
            st.write("**Keunggulan:** Khasiat dan keamanannya sudah disetarakan dengan obat-obatan medis modern (farmasi), sehingga sering diresepkan oleh dokter.")