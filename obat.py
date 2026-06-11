import streamlit as st
from utils import inject_custom_css

def show_obat():
    inject_custom_css()
    
    # ==================== HEADER PROFESIONAL ====================
    st.markdown("""
        <h1 style='font-size:2rem; font-weight:700; margin-bottom:0; color:#ffffff;'>
            💊 Kamus Obat Farmasi & Tradisional
        </h1>
        <p style='margin-top:0; color:#b0b0b0; font-size:1rem;'>
            Jelajahi klasifikasi, indikasi, efek samping, dan peruntukan obat berdasarkan pedoman keamanan BPOM Indonesia.
            <br><strong>Seluruh informasi bersifat edukatif dan bukan pengganti saran dokter.</strong>
        </p>
    """, unsafe_allow_html=True)
    st.divider()
    
    # ==================== FITUR PENCARIAN ====================
    search_query = st.text_input(
        "🔍 **Cari obat atau golongan**",
        placeholder="Contoh: Paracetamol, Antibiotik, Jamu...",
        help="Ketik nama obat, golongan, atau kata kunci untuk menyaring informasi."
    ).lower().strip()
    
    # ==================== DEFINISI TAB ====================
    tab1, tab2, tab3, tab4 = st.tabs([
        "🟢 Obat Bebas (OTC)", 
        "🔵 Obat Bebas Terbatas", 
        "🔴 Obat Keras (Resep)", 
        "🌿 Obat Tradisional"
    ])
    
    # Fungsi pembantu: menampilkan expander hanya jika cocok dengan pencarian
    def show_expander(label, content_func, *args, **kwargs):
        if search_query in label.lower() or search_query in str(kwargs.get('help','')).lower():
            with st.expander(label, **kwargs):
                content_func()
                return True
        return False
    
    # ==================== TAB 1: OBAT BEBAS ====================
    with tab1:
        st.info("**🟢 Golongan Obat Bebas (OTC)** – Ditandai lingkaran hijau dengan garis tepi hitam. Aman digunakan tanpa resep untuk keluhan ringan yang bersifat sementara.")
        
        col1, col2 = st.columns(2)
        
        with col1:
            def analgesik_content():
                st.markdown("**💊 Analgesik & Antipiretik Dasar**")
                st.markdown("- **Contoh:** Paracetamol (Asetaminofen)")
                st.markdown("- **Indikasi:** Menurunkan demam dan meredakan nyeri ringan (sakit kepala, sakit gigi, nyeri haid).")
                st.warning("⚠️ **Waspada:** Dosis maksimal 4 gram per hari. Overdosis dapat menyebabkan kerusakan hati (hepatotoksik).")
            show_expander("💊 Analgesik & Antipiretik Dasar", analgesik_content)
            
            def antasida_content():
                st.markdown("**🛡️ Antasida (Maag & Lambung)**")
                st.markdown("- **Contoh:** Promag, Mylanta (Aluminium Hidroksida + Magnesium Hidroksida)")
                st.markdown("- **Indikasi:** Meredakan nyeri ulu hati, perut kembung, rasa penuh, dan refluks asam lambung ringan.")
                st.markdown("- **Aturan pakai:** Dikunyah dahulu sebelum ditelan, diminum saat perut kosong (1 jam sebelum makan).")
            show_expander("🛡️ Antasida (Maag & Lambung)", antasida_content)
        
        with col2:
            def suplemen_content():
                st.markdown("**✨ Suplemen, Vitamin & Mineral**")
                st.markdown("- **Contoh:** Vitamin C, Vitamin D3, Zink, Zat Besi (Sangobion)")
                st.markdown("- **Fungsi:** Memelihara daya tahan tubuh, mencegah anemia, mempercepat pemulihan pasca sakit.")
                st.markdown("- **Perhatian:** Vitamin C dosis tinggi (>1000 mg/hari) dapat menyebabkan batu ginjal pada individu rentan. Imbangi dengan banyak minum air.")
            show_expander("✨ Suplemen, Vitamin & Mineral", suplemen_content)
            
            def topikal_content():
                st.markdown("**🧴 Obat Topikal Dasar**")
                st.markdown("- **Contoh:** Minyak Kayu Putih, Balsem, Bedak Salicyl, Salep Luka")
                st.markdown("- **Penggunaan:** Hanya untuk pemakaian luar; memberikan sensasi hangat/dingin, meredakan gatal ringan, nyeri otot lokal, atau luka ringan.")
            show_expander("🧴 Obat Topikal Dasar", topikal_content)
    
    # ==================== TAB 2: OBAT BEBAS TERBATAS ====================
    with tab2:
        st.info("**🔵 Golongan Obat Bebas Terbatas** – Bertanda lingkaran biru, disertai peringatan khusus (P.No.1 s.d P.No.6). Dapat dibeli tanpa resep, namun wajib dipahami aturan dan batasannya.")
        
        with st.expander("📌 **Tanda Peringatan Obat Bebas Terbatas**", expanded=False):
            st.markdown("""
            - **P.No. 1:** Awas! Obat Keras. Bacalah aturan pakainya.
            - **P.No. 2:** Awas! Obat Keras. Hanya untuk dikumur, jangan ditelan.
            - **P.No. 3:** Awas! Obat Keras. Hanya untuk bagian luar dari badan.
            - **P.No. 4:** Awas! Obat Keras. Hanya untuk dibakar.
            - **P.No. 5:** Awas! Obat Keras. Tidak boleh ditelan.
            - **P.No. 6:** Awas! Obat Keras. Obat wasir, jangan ditelan.
            """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            def antihistamin_content():
                st.markdown("**🤧 Antihistamin Generasi 1**")
                st.markdown("- **Contoh:** CTM (Chlorpheniramine Maleate), Diphenhydramine")
                st.markdown("- **Indikasi:** Alergi ringan (gatal, bersin, ruam, biduran).")
                st.warning("💤 **Efek utama:** Mengantuk berat. Dilarang mengemudi atau mengoperasikan mesin setelah mengonsumsinya.")
            show_expander("🤧 Antihistamin Generasi 1", antihistamin_content)
            
            def antimual_content():
                st.markdown("**🤢 Anti-Emetik (Anti Mabuk)**")
                st.markdown("- **Contoh:** Dimenhydrinate (Antimo)")
                st.markdown("- **Indikasi:** Mencegah mual dan muntah akibat mabuk perjalanan.")
                st.markdown("- **Tips:** Minum 30 menit sebelum perjalanan. Menimbulkan kantuk; dianjurkan untuk penumpang, bukan pengemudi.")
            show_expander("🤢 Anti-Emetik (Anti Mabuk)", antimual_content)
        
        with col2:
            def batuk_content():
                st.markdown("**🗣️ Obat Batuk**")
                st.markdown("- **Batuk Kering:** Dextromethorphan (menekan refleks batuk).")
                st.markdown("- **Batuk Berdahak:** Guaifenesin, Bromhexine (pengencer dahak).")
                st.warning("🚫 Jangan gunakan penekan batuk (antitusif) jika batuk berdahak, karena dahak akan tertahan di paru.")
            show_expander("🗣️ Obat Batuk", batuk_content)
            
            def antidiare_content():
                st.markdown("**💩 Antidiare**")
                st.markdown("- **Contoh:** Loperamide (penggunaan singkat), Attapulgite, Kaolin-Pektin")
                st.markdown("- **Fungsi:** Memperlambat gerak usus atau menyerap racun.")
                st.markdown("- **Peringatan:** Hentikan segera jika diare berhenti agar tidak menyebabkan sembelit. Jangan digunakan pada diare berdarah/disertai demam tinggi.")
            show_expander("💩 Antidiare", antidiare_content)
    
    # ==================== TAB 3: OBAT KERAS ====================
    with tab3:
        st.error("**🔴 Golongan Obat Keras** – Bertanda lingkaran merah dengan huruf 'K'. **Hanya boleh dibeli dan digunakan dengan resep dokter.**")
        
        col1, col2 = st.columns(2)
        
        with col1:
            def antibiotik_content():
                st.markdown("**🦠 Antibiotik**")
                st.markdown("- **Contoh:** Amoxicillin, Cefadroxil, Azithromycin, Ciprofloxacin")
                st.markdown("- **Indikasi:** Infeksi bakteri (radang tenggorokan, ISK, dll).")
                st.error("⛔ **Aturan Wajib:** Harus dihabiskan sesuai durasi yang diresepkan dokter, meskipun gejala sudah hilang. Menghentikan sebelum waktunya menyebabkan resistensi antibiotik.")
            show_expander("🦠 Antibiotik", antibiotik_content)
            
            def antihipertensi_content():
                st.markdown("**🩸 Antihipertensi (Penurun Tekanan Darah)**")
                st.markdown("- **Contoh:** Amlodipine, Captopril, Bisoprolol, Candesartan")
                st.markdown("- **Fungsi:** Mengontrol tekanan darah tinggi untuk mencegah stroke dan serangan jantung.")
                st.markdown("- **Kepatuhan:** Harus diminum setiap hari pada jam yang sama; jangan dihentikan tanpa instruksi dokter.")
            show_expander("🩸 Antihipertensi", antihipertensi_content)
        
        with col2:
            def nsaid_content():
                st.markdown("**🔥 NSAID Keras (Anti-Inflamasi Non-Steroid)**")
                st.markdown("- **Contoh:** Asam Mefenamat, Natrium Diklofenak, Meloxicam, Ketorolac")
                st.markdown("- **Indikasi:** Nyeri sedang-berat (sakit gigi pasca cabut, nyeri sendi, kram haid berat).")
                st.warning("⚠️ **Risiko Lambung:** Wajib diminum sesudah makan. Pemakaian jangka panjang dapat menyebabkan tukak lambung atau perdarahan saluran cerna.")
            show_expander("🔥 NSAID Keras", nsaid_content)
            
            def kortikosteroid_content():
                st.markdown("**🛑 Kortikosteroid (Anti-Radang Kuat)**")
                st.markdown("- **Contoh:** Dexamethasone, Methylprednisolone")
                st.markdown("- **Indikasi:** Radang berat, asma akut, alergi parah, penyakit autoimun.")
                st.warning("⚠️ **Efek Jangka Panjang:** Moon face (wajah membulat), osteoporosis, diabetes, dan penurunan imunitas. Tidak boleh dihentikan mendadak tanpa tapering off.")
            show_expander("🛑 Kortikosteroid", kortikosteroid_content)
        
        # Satu kolom penuh untuk obat metabolik
        def metabolik_content():
            st.markdown("**🍬 Obat Diabetes & Dislipidemia**")
            st.markdown("- **Diabetes:** Metformin, Glimepiride – menurunkan gula darah.")
            st.markdown("- **Kolesterol:** Simvastatin, Atorvastatin – menurunkan LDL dan trigliserida.")
            st.markdown("- **Waktu minum:** Simvastatin sebaiknya diminum malam hari karena sintesis kolesterol puncak terjadi saat tidur.")
        show_expander("🍬 Obat Diabetes & Kolesterol", metabolik_content)
    
    # ==================== TAB 4: OBAT TRADISIONAL ====================
    with tab4:
        st.success("**🌿 Golongan Obat Tradisional** – Pengobatan berbasis bahan alam yang diklasifikasi dan diawasi BPOM berdasarkan tingkat pembuktian ilmiah.")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            def jamu_content():
                st.markdown("**🌱 Jamu**")
                st.image("https://via.placeholder.com/80?text=Jamu", width=60)  # ganti dengan logo asli jika ada
                st.markdown("- **Logo:** Ranting daun dalam lingkaran")
                st.markdown("- **Bukti:** Empiris turun-temurun, tanpa uji klinis.")
                st.markdown("- **Contoh:** Tolak Angin, Antangin, Kuku Bima")
            show_expander("🌱 Jamu (Ranting Daun)", jamu_content)
        
        with col2:
            def oht_content():
                st.markdown("**⭐ Obat Herbal Terstandar (OHT)**")
                st.image("https://via.placeholder.com/80?text=OHT", width=60)
                st.markdown("- **Logo:** Tiga bintang dalam lingkaran")
                st.markdown("- **Bukti:** Telah melewati uji praklinis (hewan) → keamanan & khasiat terstandarisasi.")
                st.markdown("- **Contoh:** Diapet, Kiranti, Lelap")
            show_expander("⭐ OHT (Tiga Bintang)", oht_content)
        
        with col3:
            def fitofarmaka_content():
                st.markdown("**❄️ Fitofarmaka**")
                st.image("https://via.placeholder.com/80?text=Fito", width=60)
                st.markdown("- **Logo:** Kristal salju (heksagonal)")
                st.markdown("- **Bukti:** Telah melalui uji klinis pada manusia → setara dengan obat modern.")
                st.markdown("- **Contoh:** Stimuno (imunomodulator), Tensigard, Inlacin")
            show_expander("❄️ Fitofarmaka (Kristal Salju)", fitofarmaka_content)
    
    # ==================== FOOTER DISCLAIMER ====================
    st.divider()
    st.caption("📘 **Disclaimer:** Informasi ini disusun berdasarkan data BPOM dan literatur farmasi terkini. Tidak untuk mendiagnosis atau menggantikan konsultasi dengan tenaga kesehatan profesional. Selalu baca aturan pakai dan konsultasikan dengan dokter atau apoteker sebelum menggunakan obat, terutama obat keras dan obat tradisional dengan klaim tertentu.")