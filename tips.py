import streamlit as st
from utils import inject_custom_css

def show_tips():
    inject_custom_css()
    
    # ==================== HEADER PROFESIONAL ====================
    st.markdown("""
        <h1 style='font-size:2rem; font-weight:700; margin-bottom:0; color:#ffffff;'>
            📋 Jurnal Gaya Hidup Sehat
        </h1>
        <p style='margin-top:0; color:#b0b0b0; font-size:1rem;'>
            Panduan praktis berbasis bukti untuk membangun kebiasaan kecil setiap hari – investasi terbaik bagi kesehatan fisik, mental, dan produktivitas jangka panjang.
        </p>
    """, unsafe_allow_html=True)
    st.divider()
    
    # ==================== NAVIGASI TAB ====================
    tab1, tab2, tab3, tab4 = st.tabs([
        "🥗 Nutrisi & Hidrasi", 
        "🏃 Aktivitas & Postur", 
        "😴 Tidur & Kesehatan Mental", 
        "🛡️ Kebiasaan Sehat Lainnya"
    ])
    
    # ==================== TAB 1: NUTRISI & HIDRASI ====================
    with tab1:
        st.info("**Nutrisi seimbang adalah fondasi utama. Pilih makanan utuh, batasi yang diproses, dan jaga ritme makan.**")
        
        col1, col2 = st.columns(2)
        with col1:
            with st.expander("💧 **Hidrasi Optimal**", expanded=True):
                st.markdown("""
                - **Jumlah:** Minimal 2 liter (8–10 gelas) per hari untuk dewasa; lebih banyak jika berkeringat banyak.
                - **Indikator:** Warna urine kuning pucat → terhidrasi baik. Urine keruh atau gelap → butuh lebih banyak air.
                - **Cara:** Minum segelas air setelah bangun tidur, sebelum makan, dan secara berkala. Gunakan botol bertanda waktu.
                - **Fakta:** Dehidrasi ringan (1-2% berat badan) sudah menurunkan konsentrasi dan performa fisik.
                """)
            
            with st.expander("🥗 **Piring Makan Sehat (Isi Piringku)**"):
                st.markdown("""
                - **Komposisi:** 50% sayur & buah, 25% protein (ayam, ikan, tahu, tempe), 25% karbohidrat kompleks (nasi merah, ubi, jagung).
                - **Tips:** Mulai dengan sayur, lalu protein, baru karbohidrat – membantu mengontrol lonjakan gula darah.
                - **Makanan utuh vs olahan:** Prioritaskan makanan segar, hindari makanan ultra-proses (snack kemasan, sosis, mie instan) yang tinggi garam dan lemak trans.
                """)
            
            with st.expander("🍳 **Sarapan & Ritme Makan**"):
                st.markdown("""
                - **Sarapan:** Sumber energi pagi – pilih protein dan serat (telur + roti gandum, oatmeal + buah). Melewatkan sarapan rutin dikaitkan dengan peningkatan risiko diabetes tipe 2.
                - **Jam makan:** Makan malam setidaknya 2-3 jam sebelum tidur agar pencernaan optimal dan tidak mengganggu kualitas tidur.
                - **Porsi:** Gunakan piring lebih kecil, kunyah perlahan (20-30 kali per suapan) untuk memberi waktu sinyal kenyang.
                """)
        
        with col2:
            with st.expander("🍬 **Batasi Gula, Garam, Lemak**"):
                st.markdown("""
                - **Gula:** Maksimal 4 sdm (50 g) per hari menurut Kemenkes. Satu kaleng minuman bersoda bisa mengandung >30 g gula.
                - **Garam:** ≤ 1 sdt (5 g) per hari. Hindari penambahan garam berlebih; waspadai natrium tersembunyi di makanan kaleng/instan.
                - **Lemak jahat:** Kurangi gorengan dan lemak trans; gunakan minyak sehat seperti minyak zaitun, kanola, atau alpukat.
                - **Pemanis buatan:** Meski nol kalori, beberapa studi menunjukkan dapat memicu craving gula; konsumsi secukupnya.
                """)
            
            with st.expander("☀️ **Vitamin D & Sinar Matahari**"):
                st.markdown("""
                - **Paparan pagi:** Berjemur 10–15 menit antara pukul 07.00–09.00, tanpa tabir surya di area lengan dan kaki.
                - **Manfaat:** Sintesis vitamin D untuk imunitas, penyerapan kalsium, dan pencegahan osteoporosis.
                - **Bila kurang sinar:** Pertimbangkan suplemen vitamin D3 (setelah konsultasi dokter).
                """)
            
            with st.expander("🧃 **Konsumsi Serat & Prebiotik**"):
                st.markdown("""
                - **Target serat:** 25-30 g per hari dari sayur, buah, kacang-kacangan, biji-bijian.
                - **Prebiotik:** Pisang, bawang putih, asparagus, oat – memberi makan bakteri baik usus.
                - **Probiotik:** Yogurt tanpa gula, tempe, kimchi – membantu keseimbangan mikrobiota.
                """)
    
    # ==================== TAB 2: AKTIVITAS & POSTUR ====================
    with tab2:
        st.info("**Gerakan adalah obat alami. Aktivitas fisik teratur memperbaiki metabolisme, suasana hati, dan daya tahan tubuh.**")
        
        col1, col2 = st.columns(2)
        with col1:
            with st.expander("🏃‍♂️ **Olahraga Rutin**", expanded=True):
                st.markdown("""
                - **Rekomendasi WHO:** 150-300 menit aktivitas intensitas sedang (jalan cepat, bersepeda) per minggu, atau 75-150 menit intensitas tinggi (lari, HIIT).
                - **Latihan kekuatan:** 2 sesi per minggu (push-up, squat, angkat beban ringan) untuk menjaga massa otot.
                - **Manfaat kardio:** Menurunkan tekanan darah, memperbaiki profil lipid, membakar lemak viseral.
                - **Konsistensi > intensitas:** Mulai dari 10 menit per hari jika sibuk, tingkatkan bertahap.
                """)
            
            with st.expander("🪑 **Postur & Ergonomi Kerja**"):
                st.markdown("""
                - **Posisi duduk:** Punggung lurus bersandar, lutut sejajar panggul, telapak kaki rata di lantai.
                - **Layar:** Atur ketinggian sehingga mata sejajar dengan 1/3 atas layar, jarak 50-70 cm.
                - **Istirahat mikro:** Setiap 30-45 menit, berdiri, berjalan kecil, atau lakukan peregangan 1-2 menit.
                - **Peregangan:** Gerakan leher, bahu, pergelangan tangan, dan pinggul untuk mencegah sindrom terowongan karpal dan nyeri punggung bawah.
                """)
        
        with col2:
            with st.expander("🤸 **Fleksibilitas & Pemanasan**"):
                st.markdown("""
                - **Pemanasan dinamis:** Sebelum olahraga, lakukan gerakan memutar sendi dan jalan di tempat.
                - **Pendinginan:** Setelah latihan, lakukan peregangan statis (tahan 15-30 detik) untuk mempercepat pemulihan.
                - **Yoga atau pilates:** Meningkatkan fleksibilitas, mengurangi nyeri kronis, dan membantu manajemen stres.
                """)
            
            with st.expander("🚶 **Langkah Harian & Aktivitas Non-olahraga**"):
                st.markdown("""
                - **Target langkah:** 8.000-10.000 langkah per hari. Gunakan pedometer atau smartphone.
                - **NEAT (Non-Exercise Activity Thermogenesis):** Bergerak di luar olahraga – naik tangga, menyapu, berkebun – meningkatkan pembakaran kalori harian.
                - **Istirahat aktif:** Ganti duduk dengan berdiri saat telepon, lakukan meeting sambil berjalan ringan.
                """)
    
    # ==================== TAB 3: TIDUR & KESEHATAN MENTAL ====================
    with tab3:
        st.info("**Tidur berkualitas dan manajemen stres sama pentingnya dengan nutrisi – keduanya saling memengaruhi.**")
        
        col1, col2 = st.columns(2)
        with col1:
            with st.expander("😴 **Sleep Hygiene (7-8 Jam)**", expanded=True):
                st.markdown("""
                - **Jadwal tetap:** Tidur dan bangun pada jam yang sama setiap hari, termasuk akhir pekan.
                - **Ritual sebelum tidur:** Mandi air hangat, membaca buku fisik, meditasi ringan – hindari layar 60 menit sebelumnya.
                - **Lingkungan tidur:** Gelap, sejuk (18-22°C), minim suara. Gunakan tirai blackout.
                - **Batasi:** Kafein 6 jam sebelum tidur, alkohol (mengganggu siklus REM), dan makan berat menjelang tidur.
                - **Fakta:** Kurang tidur kronis meningkatkan risiko hipertensi, obesitas, dan penurunan imunitas.
                """)
            
            with st.expander("🧠 **Manajemen Stres & Kesehatan Mental**"):
                st.markdown("""
                - **Teknik relaksasi:** Pernapasan dalam (4-7-8), meditasi mindfulness, atau jurnal syukur – efektif menurunkan kortisol.
                - **Batasi berita negatif:** Kurangi paparan berita berlebihan (doomscrolling) yang dapat memicu kecemasan.
                - **Hobi & me-time:** Alokasikan waktu untuk kegiatan yang menyenangkan minimal 20 menit per hari.
                - **Dukungan sosial:** Mengobrol dengan teman atau keluarga melepaskan oksitosin yang menenangkan.
                """)
        
        with col2:
            with st.expander("🚫 **Digital Detox & Kesehatan Mata**"):
                st.markdown("""
                - **Aturan 20-20-20:** Setiap 20 menit menatap layar, lihat objek sejauh 20 kaki (6 m) selama 20 detik.
                - **Filter blue light:** Aktifkan mode malam atau gunakan kacamata anti radiasi jika bekerja di depan komputer seharian.
                - **Screen time sebelum tidur:** Cahaya biru menekan melatonin, hormon tidur. Jauhkan ponsel dari tempat tidur.
                - **Detoks digital:** Tetapkan satu hari tanpa media sosial sebulan sekali untuk menjernihkan pikiran.
                """)
            
            with st.expander("🤝 **Kesehatan Emosional & Sosial**"):
                st.markdown("""
                - **Ekspresikan emosi:** Menulis jurnal atau berbicara dengan orang terpercaya mencegah penumpukan stres.
                - **Bersyukur:** Tulis tiga hal yang disyukuri setiap malam – studi menunjukkan peningkatan kesejahteraan subjektif.
                - **Koneksi sosial:** Interaksi tatap muka meningkatkan kadar serotonin dan dopamin.
                """)
    
    # ==================== TAB 4: KEBIASAAN SEHAT LAINNYA ====================
    with tab4:
        st.info("**Kebiasaan kecil yang dilakukan konsisten akan memberikan dampak besar bagi pencegahan penyakit.**")
        
        col1, col2 = st.columns(2)
        with col1:
            with st.expander("🧼 **Kebersihan & Sanitasi Diri**", expanded=True):
                st.markdown("""
                - **Cuci tangan:** Pakai sabun dan air mengalir, terutama sebelum makan, setelah dari toilet, dan setelah menyentuh permukaan umum.
                - **Kebersihan gigi:** Sikat gigi dua kali sehari, benang gigi (flossing) untuk cegah karies dan penyakit gusi.
                - **Kamar tidur:** Ganti seprai seminggu sekali, jemur bantal secara berkala untuk mengurangi tungau debu.
                """)
            
            with st.expander("🫁 **Kesehatan Pernapasan & Paru**"):
                st.markdown("""
                - **Hindari rokok & asap rokok:** Merokok adalah faktor risiko utama kanker paru, PPOK, dan penyakit jantung.
                - **Udara bersih:** Gunakan masker saat polusi tinggi, pasang air purifier jika perlu.
                - **Latihan napas:** Pernapasan diafragma (perut) meningkatkan kapasitas paru dan menenangkan sistem saraf.
                """)
        
        with col2:
            with st.expander("⚖️ **Manajemen Berat Badan Ideal**"):
                st.markdown("""
                - **IMT (Indeks Massa Tubuh):** Ukur secara berkala, target IMT normal 18.5-24.9 kg/m².
                - **Defisit kalori sehat:** Kurangi 300-500 kkal per hari untuk penurunan 0.5-1 kg per minggu – tanpa melewatkan gizi.
                - **Jangan bandingkan:** Fokus pada komposisi tubuh (lemak vs otot) bukan hanya angka timbangan.
                """)
            
            with st.expander("📋 **Pemeriksaan Kesehatan Rutin**"):
                st.markdown("""
                - **Cek kesehatan tahunan:** Cek tekanan darah, gula darah, kolesterol, asam urat, dan fungsi hati/ginjal.
                - **Deteksi dini:** Kanker serviks (pap smear), kanker payudara (SADARI), dan kanker usus (kolonoskopi sesuai usia).
                - **Vaksinasi:** Lengkapi vaksin dasar dan booster, termasuk influenza tahunan.
                """)
        
        # Tips tambahan dalam satu kolom penuh di bawah
        with st.expander("💡 **Fakta & Tips Tambahan**"):
            st.markdown("""
            - **Manfaat tertawa:** Tertawa selama 10-15 menit membakar 10-40 kalori, menurunkan kortisol, dan meningkatkan endorfin.
            - **Puasa intermiten:** Pola makan dengan jendela waktu tertentu (misal 8 jam makan, 16 jam puasa) dapat membantu perbaikan seluler (autofagi), namun perlu disesuaikan dengan kondisi individu.
            - **Cold exposure (paparan dingin):** Mandi air dingin di pagi hari dapat meningkatkan kewaspadaan, sirkulasi darah, dan memperkuat sistem imun.
            - **Hidup selaras alam:** Kontak dengan alam (forest bathing) terbukti mengurangi tekanan darah dan meningkatkan mood.
            - **Konsumsi probiotik:** Mikrobiota usus yang sehat memengaruhi mood (gut-brain axis). Makanan fermentasi dan serat cukup penting.
            """)
    
    # ==================== FOOTER DISCLAIMER ====================
    st.divider()
    st.caption(
        "📘 **Sumber & Catatan:** Tips di atas disusun berdasarkan panduan Kementerian Kesehatan RI, WHO, dan literatur kedokteran terkini. "
        "Informasi ini bersifat edukatif dan tidak menggantikan saran profesional. Konsultasikan dengan dokter atau ahli gizi untuk kondisi khusus."
    )