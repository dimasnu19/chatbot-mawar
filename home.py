import streamlit as st
from utils import inject_custom_css

def show_home():
    inject_custom_css()
    
    # ==================== HERO SECTION ====================
    st.markdown("""
    <div style="
        background: radial-gradient(circle at 30% 20%, rgba(56,189,248,0.08) 0%, rgba(15,18,45,0.9) 70%);
        backdrop-filter: blur(40px);
        -webkit-backdrop-filter: blur(40px);
        padding: 60px 45px;
        border-radius: 30px;
        border: 1px solid rgba(255, 255, 255, 0.06);
        color: white;
        margin-bottom: 45px;
        text-align: center;
        box-shadow: 0 25px 60px rgba(0, 0, 0, 0.55);
        position: relative;
        overflow: hidden;
    ">
        <div style="display: inline-block; background: rgba(56, 189, 248, 0.1); color: #38bdf8; padding: 8px 24px; border-radius: 50px; font-size: 0.8rem; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; border: 1px solid rgba(56, 189, 248, 0.3); margin-bottom: 20px;">
            Platform Kesehatan Digital Indonesia
        </div>
        <h1 style="
            color: #ffffff;
            margin: 10px 0 15px 0;
            font-size: 2.8rem;
            font-weight: 800;
            line-height: 1.2;
            letter-spacing: -0.02em;
        ">
            Ngobat<span style="color: #38bdf8;">.In</span>
        </h1>
        <p style="
            color: #b9c2d9;
            font-size: 1.15rem;
            max-width: 750px;
            margin: 0 auto 25px auto;
            line-height: 1.7;
        ">
            Sahabat kesehatan digital Anda: skrining gejala interaktif, ensiklopedia obat terlengkap, 
            dan panduan gaya hidup sehat — semuanya dalam satu platform mudah diakses.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ==================== ORGAN ANATOMI (2 BARIS) ====================
    st.markdown("<h3 style='color: #ffffff; font-weight: 700; font-size: 1.6rem; margin-bottom: 25px;'>🧬 Jelajahi Anatomi & Penyakit Organ Vital</h3>", unsafe_allow_html=True)
    
    # Baris pertama
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        _organ_card("🫀", "Jantung", "Kardiovaskular", "Sistem peredaran darah & pompa kehidupan. Pelajari risiko koroner, aritmia, dan gagal jantung.", "btn_jantung", "Detail_Jantung")
    with col2:
        _organ_card("🫁", "Paru-paru", "Respirasi", "Pertukaran oksigen vital. Kenali asma, PPOK, dan pneumonia lebih dalam.", "btn_paru", "Detail_Paru-paru")
    with col3:
        _organ_card("🧠", "Otak", "Saraf Pusat", "Pusat kendali tubuh & memori. Waspadai stroke, epilepsi, dan migrain.", "btn_otak", "Detail_Otak")
    with col4:
        _organ_card("🥖", "Lambung", "Pencernaan", "Regulasi asam & enzim. Pahami GERD, tukak lambung, dan gastritis.", "btn_lambung", "Detail_Lambung")

    # Baris kedua (tambahan agar lebih lengkap)
    col5, col6, col7, col8 = st.columns(4)
    with col5:
        _organ_card("🫘", "Hati", "Metabolisme", "Detoksifikasi & produksi empedu. Sirosis, hepatitis, dan perlemakan hati.", "btn_hati", "Detail_Hati")
    with col6:
        _organ_card("🫗", "Ginjal", "Filtrasi", "Penyaring darah & keseimbangan cairan. Batu ginjal, gagal ginjal, infeksi saluran kemih.", "btn_ginjal", "Detail_Ginjal")
    with col7:
        _organ_card("🩸", "Pankreas", "Endokrin", "Produksi insulin & enzim. Diabetes melitus dan pankreatitis.", "btn_pankreas", "Detail_Pankreas")
    with col8:
        _organ_card("🦴", "Tulang & Sendi", "Muskuloskeletal", "Struktur tubuh & pergerakan. Osteoporosis, arthritis, dan cedera.", "btn_tulang", "Detail_Tulang")

    # ==================== LAYANAN UNGGULAN ====================
    st.markdown("<hr style='margin: 45px 0 35px 0; border-color: rgba(255,255,255,0.06);'>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #ffffff; font-weight: 700; font-size: 1.6rem; margin-bottom: 25px;'>✨ Layanan Utama Ngobat.In</h3>", unsafe_allow_html=True)
    
    s1, s2, s3 = st.columns(3)
    with s1:
        with st.container(border=True):
            st.markdown("<div style='font-size: 2.8rem; margin-bottom: 10px;'>🤖</div>", unsafe_allow_html=True)
            st.markdown("<h4 style='color:#38bdf8; font-weight:600;'>Chatbot Ngobat.In</h4>", unsafe_allow_html=True)
            st.markdown("""
            <p style='font-size:0.9rem; line-height:1.6; color:#b9c2d9;'>
                Chatbot cerdas berbasis <em>Finite State Machine</em> siap mendengarkan keluhan Anda 
                dalam bahasa alami dan memberikan analisis awal yang edukatif — temukan di pojok kanan bawah!
            </p>
            """, unsafe_allow_html=True)
    with s2:
        with st.container(border=True):
            st.markdown("<div style='font-size: 2.8rem; margin-bottom: 10px;'>📖</div>", unsafe_allow_html=True)
            st.markdown("<h4 style='color:#a78bfa; font-weight:600;'>Kamus Obat Lengkap</h4>", unsafe_allow_html=True)
            st.markdown("""
            <p style='font-size:0.9rem; line-height:1.6; color:#b9c2d9;'>
                Eksplorasi obat bebas, resep, hingga herbal berstandar BPOM. Dilengkapi indikasi, 
                efek samping, dan peringatan keamanan.
            </p>
            """, unsafe_allow_html=True)
    with s3:
        with st.container(border=True):
            st.markdown("<div style='font-size: 2.8rem; margin-bottom: 10px;'>💚</div>", unsafe_allow_html=True)
            st.markdown("<h4 style='color:#f472b6; font-weight:600;'>Jurnal Hidup Sehat</h4>", unsafe_allow_html=True)
            st.markdown("""
            <p style='font-size:0.9rem; line-height:1.6; color:#b9c2d9;'>
                Panduan nutrisi, olahraga, tidur, dan kesehatan mental berbasis bukti untuk 
                membantu Anda membangun kebiasaan baik setiap hari.
            </p>
            """, unsafe_allow_html=True)

    # ==================== CALL TO ACTION ====================
    st.markdown("<hr style='margin: 45px 0 35px 0; border-color: rgba(255,255,255,0.06);'>", unsafe_allow_html=True)
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, rgba(56,189,248,0.1), rgba(168,85,247,0.08));
        border-radius: 24px;
        padding: 35px 30px;
        border: 1px solid rgba(56,189,248,0.2);
        text-align: center;
        margin-bottom: 20px;
    ">
        <h3 style="color: #ffffff; margin: 0 0 12px 0; font-size: 1.5rem;">💬 Mulai Konsultasi Gejala Sekarang</h3>
        <p style="color: #b9c2d9; margin: 0 0 20px 0; font-size: 1rem;">
            Klik ikon kapsul di pojok kiri bawah untuk berbicara dengan Ngobat.In.
        </p>
        <span style="background: rgba(255,255,255,0.05); color: #38bdf8; padding: 6px 20px; border-radius: 30px; font-size: 0.85rem;">
            👉 Cukup ceritakan keluhan Anda, dan dapatkan arahan awal.
        </span>
    </div>
    """, unsafe_allow_html=True)


def _organ_card(emoji, title, subtitle, desc, key, target_page):
    """Komponen kartu organ yang profesional dan konsisten."""
    with st.container(border=True):
        st.markdown(f"<div style='font-size: 3rem; text-align: center; margin-bottom: 8px;'>{emoji}</div>", unsafe_allow_html=True)
        st.markdown(f"<h4 style='color:#ffffff; font-weight:600; text-align:center; margin:0;'>{title}</h4>", unsafe_allow_html=True)
        st.markdown(f"<p style='color:#64748b; font-size:0.7rem; text-align:center; text-transform:uppercase; letter-spacing:1px; margin:4px 0 8px 0;'>{subtitle}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color:#94a3b8; font-size:0.82rem; text-align:center; min-height: 55px; line-height:1.5;'>{desc}</p>", unsafe_allow_html=True)
        if st.button("🔍 Jelajahi", key=key, use_container_width=True):
            st.session_state.current_page = target_page
            st.rerun()


# ==================== FUNGSI DETAIL ORGAN ====================
def show_organ_detail(page_name):
    inject_custom_css()
    organ_name = page_name.replace("Detail_", "")
    
    col1, col2 = st.columns([5, 1])
    with col1:
        st.markdown(f"<h2 style='color:#ffffff; font-weight:700; margin-bottom: 0px;'>Anatomi Klinis: <span style='color:#38bdf8;'>{organ_name.replace('-', ' ').title()}</span></h2>", unsafe_allow_html=True)
    with col2:
        if st.button("← Kembali", use_container_width=True):
            st.session_state.current_page = "Home"
            st.rerun()
            
    st.markdown("<hr style='margin: 15px 0 25px 0;'>", unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["🩺 Patofisiologi & Penyakit", "🚑 Pertolongan Pertama", "💊 Terapi & Obat"])
    
    if organ_name == "Jantung":
        with tab1:
            st.markdown("### 🫀 Anatomi & Fungsi Klinis")
            st.write("Jantung adalah organ otot berongga yang bertindak sebagai pusat sistem kardiovaskular. Fungsi utamanya adalah memompa darah kaya oksigen dan nutrisi ke seluruh jaringan tubuh, serta membawa darah deoksigenasi kembali ke paru-paru.")
            st.markdown("### ⚠️ Patologi & Gangguan Umum")
            st.markdown("""
            * **Penyakit Jantung Koroner (PJK):** Penumpukan plak kolesterol (aterosklerosis) pada dinding arteri koroner yang menyumbat suplai darah dan oksigen ke otot jantung. Gejala khas meliputi *angina* (nyeri dada seperti tertindih benda berat).
            * **Aritmia:** Gangguan pada impuls listrik jantung yang menyebabkan detak jantung menjadi terlalu cepat (takikardia), terlalu lambat (bradikardia), atau tidak beraturan (fibrilasi).
            * **Gagal Jantung (Heart Failure):** Kondisi kronis di mana jantung kehilangan kemampuan memompa darah secara efisien untuk memenuhi kebutuhan metabolik tubuh.
            """)
        with tab2:
            st.error("**🚨 PROTOKOL DARURAT: Dugaan Serangan Jantung (Infark Miokard)**")
            st.markdown("""
            1. **Segera Hubungi Bantuan Medis (119/Ambulans):** Jangan menunda atau mencoba menyetir sendiri ke rumah sakit.
            2. **Istirahatkan Pasien:** Minta pasien duduk di kursi, lantai, atau bersandar (posisi setengah duduk) untuk mengurangi beban kerja jantung. Longgarkan pakaian yang ketat.
            3. **Berikan Aspirin (Jika Tidak Alergi):** Kunyah dan telan satu tablet aspirin (biasanya 160-325 mg) untuk membantu mencegah pembekuan darah lebih lanjut.
            4. **Obat Nitrat Pribadi:** Jika pasien memiliki resep Nitrogliserin (obat ditaruh di bawah lidah), bantu mereka mengonsumsinya.
            5. **Persiapkan CPR:** Jika pasien kehilangan kesadaran dan nadi tidak teraba, segera lakukan Resusitasi Jantung Paru (CPR).
            """)
        with tab3:
            st.info("💡 **Catatan Medis:** Penggunaan obat harus selalu di bawah pengawasan Dokter Spesialis Jantung (Sp.JP).")
            st.markdown("### 💊 Klasifikasi Farmakologi Umum")
            st.markdown("""
            * **Antiplatelet & Antikoagulan:** (Contoh: *Aspirin, Clopidogrel, Warfarin*). Berfungsi mencegah agregasi trombosit dan pembentukan gumpalan darah mematikan.
            * **Beta-blockers:** (Contoh: *Bisoprolol, Metoprolol*). Menurunkan denyut jantung dan tekanan darah sehingga beban kerja otot jantung berkurang.
            * **Vasodilator/Nitrat:** (Contoh: *Nitroglycerin*). Melebarkan pembuluh darah secara cepat untuk meredakan nyeri dada (angina).
            * **ACE Inhibitors:** (Contoh: *Ramipril, Captopril*). Membantu merelaksasi pembuluh darah dan mencegah remodeling jantung pasca serangan.
            """)

    elif organ_name == "Paru-paru":
        with tab1:
            st.markdown("### 🫁 Anatomi & Fungsi Klinis")
            st.write("Paru-paru adalah organ utama sistem respirasi. Organ ini bertanggung jawab atas proses pertukaran gas esensial: memasukkan oksigen ke dalam aliran darah dan mengeluarkan karbon dioksida sebagai produk limbah metabolisme melalui jutaan kantung udara (alveolus).")
            st.markdown("### ⚠️ Patologi & Gangguan Umum")
            st.markdown("""
            * **Asma Bronkial:** Penyakit inflamasi kronis yang menyebabkan saluran udara membengkak, menyempit, dan memproduksi lendir berlebih, memicu mengi dan sesak napas.
            * **Penyakit Paru Obstruktif Kronik (PPOK/COPD):** Kerusakan paru-paru progresif, sering kali akibat merokok, yang mencakup emfisema dan bronkitis kronis.
            * **Pneumonia:** Infeksi akut pada salah satu atau kedua paru-paru (disebabkan oleh bakteri, virus, atau jamur) yang menyebabkan alveolus meradang dan berisi cairan/nanah.
            """)
        with tab2:
            st.warning("**🚑 PROTOKOL PENANGANAN: Serangan Sesak Napas/Asma Akut**")
            st.markdown("""
            1. **Tenangkan Pasien:** Kepanikan akan membuat otot pernapasan menegang dan memperburuk sesak napas.
            2. **Posisikan Duduk Tripod:** Minta pasien duduk dan mencondongkan tubuh sedikit ke depan dengan bertumpu pada lengan (posisi tripod) untuk memaksimalkan ekspansi rongga dada.
            3. **Gunakan *Rescue Inhaler*:** Segera berikan inhaler pelega (biasanya salbutamol/albuterol). Gunakan *spacer* jika ada untuk penyerapan optimal.
            4. **Teknik *Pursed-lip Breathing*:** Instruksikan pasien menarik napas dari hidung dan membuang perlahan melalui bibir yang dikerucutkan (seperti meniup lilin).
            5. **Bawa ke UGD:** Jika bibir/kuku membiru (sianosis) atau inhaler tidak memberikan efek dalam 10-15 menit.
            """)
        with tab3:
            st.info("💡 **Catatan Medis:** Terapi paru seringkali melibatkan perangkat inhalasi langsung ke saluran pernapasan.")
            st.markdown("### 💊 Klasifikasi Farmakologi Umum")
            st.markdown("""
            * **Bronkodilator Kerja Cepat (SABA):** (Contoh: *Salbutamol*). Merelaksasi otot di sekitar saluran napas dengan sangat cepat pada saat serangan akut.
            * **Kortikosteroid Inhalasi (ICS):** (Contoh: *Budesonide, Fluticasone*). Obat pengontrol jangka panjang untuk menekan peradangan mendasar pada paru-paru.
            * **Mukolitik & Ekspektoran:** (Contoh: *Ambroxol, Guaifenesin*). Mengencerkan dahak tebal agar lebih mudah dikeluarkan melalui batuk.
            """)

    elif organ_name == "Otak":
        with tab1:
            st.markdown("### 🧠 Anatomi & Fungsi Klinis")
            st.write("Otak adalah komando utama sistem saraf pusat, terdiri dari miliaran neuron. Organ ini mengendalikan segala aspek fungsi manusia, termasuk memori, emosi, keterampilan motorik, visi, pernapasan, dan suhu tubuh.")
            st.markdown("### ⚠️ Patologi & Gangguan Umum")
            st.markdown("""
            * **Stroke:** Kondisi gawat darurat medis yang terjadi karena terputusnya suplai darah ke otak. Terbagi menjadi *Iskemik* (penyumbatan oleh bekuan darah) dan *Hemoragik* (pecahnya pembuluh darah otak).
            * **Epilepsi:** Gangguan neurologis kronis yang ditandai dengan aktivitas listrik abnormal di otak, memicu kejang berulang.
            * **Migrain & Vertigo:** Gangguan vaskular saraf yang memicu nyeri kepala berdenyut ekstrem (migrain) atau sensasi pusing berputar yang intens (vertigo).
            """)
        with tab2:
            st.error("**🚨 PROTOKOL DARURAT: Deteksi Dini Stroke (Metode F.A.S.T)**")
            st.markdown("""
            *Time is Brain* (Waktu adalah Otak). Setiap detik sangat berharga.
            * **F - Face (Wajah):** Minta pasien tersenyum. Apakah salah satu sisi wajahnya turun/perot?
            * **A - Arms (Lengan):** Minta pasien mengangkat kedua tangan. Apakah salah satu tangan jatuh perlahan atau tidak bisa diangkat?
            * **S - Speech (Bicara):** Ajak berbicara. Apakah kata-katanya tidak jelas (pelo) atau sulit dipahami?
            * **T - Time (Waktu):** Jika ada satu saja tanda di atas, **CATAT WAKTU KEJADIAN** dan panggil ambulans segera.
            **Langkah Tambahan:** Jangan berikan pasien makanan, minuman, atau obat apa pun (termasuk aspirin) untuk mencegah tersedak jika terjadi kelumpuhan otot menelan.
            """)
        with tab3:
            st.info("💡 **Catatan Medis:** Penanganan penyakit saraf membutuhkan diagnostik pencitraan (CT Scan/MRI) sebelum pemberian obat.")
            st.markdown("### 💊 Klasifikasi Farmakologi Umum")
            st.markdown("""
            * **Trombolitik/Fibrinolitik (tPA):** Obat darurat penghancur gumpalan darah yang harus diberikan dalam jendela waktu 3-4,5 jam pertama serangan stroke iskemik (Golden Period).
            * **Antikonvulsan:** (Contoh: *Phenytoin, Levetiracetam*). Digunakan untuk menstabilkan impuls listrik otak dan mencegah kejang.
            * **Triptan & Ergotamin:** Obat spesifik untuk menghentikan serangan migrain akut dengan menyempitkan kembali pembuluh darah otak yang melebar.
            """)

    elif organ_name == "Lambung":
        with tab1:
            st.markdown("### 🥖 Anatomi & Fungsi Klinis")
            st.write("Lambung adalah organ pencernaan berbentuk kantong elastis. Berperan menyimpan makanan, mencampurnya dengan cairan gastrik (asam klorida pekat dan enzim pepsin), lalu memecahnya menjadi cairan kental (kimus) sebelum dikirim ke usus halus.")
            st.markdown("### ⚠️ Patologi & Gangguan Umum")
            st.markdown("""
            * **GERD (Gastroesophageal Reflux Disease):** Melemahnya katup esofagus yang menyebabkan asam lambung naik kembali ke kerongkongan, memicu sensasi terbakar di dada (*heartburn*).
            * **Tukak Lambung (Gastric Ulcer):** Luka lecet pada lapisan mukosa/dinding dalam lambung, sering dipicu oleh infeksi bakteri *H. pylori* atau penggunaan obat antinyeri (NSAID) jangka panjang.
            * **Gastritis (Maag):** Peradangan akut atau kronis pada lapisan lambung akibat stres, alkohol, atau jadwal makan tidak teratur.
            """)
        with tab2:
            st.warning("**🍽️ PROTOKOL PENANGANAN: Serangan Asam Lambung & Nyeri Ulu Hati**")
            st.markdown("""
            1. **Atur Posisi Tubuh:** Jangan berbaring rata! Jika ingin rebahan, pastikan posisi dada dan kepala lebih tinggi (gunakan 2-3 bantal) agar gravitasi menahan asam lambung tidak naik ke kerongkongan.
            2. **Longgarkan Pakaian:** Lepaskan ikat pinggang atau celana ketat untuk mengurangi tekanan ekstra pada area perut (intra-abdomen).
            3. **Minum Air Hangat:** Konsumsi air putih hangat secara perlahan untuk membantu membilas asam dari kerongkongan. Hindari susu segar secara berlebihan, karena meskipun menenangkan sementara, lemak susu dapat memicu rebound asam lambung setelahnya.
            4. **Hindari Makan Berat:** Hentikan sementara asupan kafein, makanan pedas, asam, atau berminyak.
            """)
        with tab3:
            st.info("💡 **Catatan Medis:** Perubahan gaya hidup dan pola diet sama pentingnya dengan medikasi untuk masalah lambung.")
            st.markdown("### 💊 Klasifikasi Farmakologi Umum")
            st.markdown("""
            * **Antasida:** (Contoh: *Alumunium Hidroksida, Magnesium Hidroksida*). Bekerja dengan cepat menetralkan tingkat keasaman (pH) lambung saat gejala menyerang.
            * **Proton Pump Inhibitors (PPI):** (Contoh: *Omeprazole, Lansoprazole*). Menghambat sel parietal lambung untuk menghentikan produksi asam secara drastis, sangat efektif untuk penyembuhan tukak lambung.
            * **H2-Receptor Antagonists:** (Contoh: *Ranitidine, Famotidine*). Mengurangi produksi asam lambung dengan memblokir sinyal histamin.
            """)

    elif organ_name == "Hati":
        with tab1:
            st.markdown("### 🫘 Anatomi & Fungsi Klinis")
            st.write("Hati adalah organ metabolik terbesar yang melakukan detoksifikasi racun, sintesis protein plasma, produksi empedu untuk pencernaan lemak, dan penyimpanan glikogen. Setiap menit sekitar 1,5 liter darah difiltrasi di sini.")
            st.markdown("### ⚠️ Patologi & Gangguan Umum")
            st.markdown("""
            * **Hepatitis:** Peradangan hati akut/kronis akibat virus (A, B, C), alkohol, atau autoimun. Dapat berkembang menjadi sirosis.
            * **Sirosis Hati:** Pembentukan jaringan parut progresif menggantikan sel hati sehat, sering disebabkan oleh alkoholisme kronis atau hepatitis B/C.
            * **Perlemakan Hati (Fatty Liver):** Penumpukan lemak >5% dari berat hati, terkait dengan obesitas, diabetes, dan sindrom metabolik.
            """)
        with tab2:
            st.warning("**🧪 PROTOKOL DUKUNGAN: Menjaga Fungsi Hati**")
            st.markdown("""
            1. **Batasi Alkohol:** Alkohol adalah toksin utama hati. Bagi yang berisiko, hentikan total.
            2. **Hindari Obat Berlebihan:** Jangan konsumsi paracetamol melebihi dosis (maks 4g/hari) karena berpotensi hepatotoksik.
            3. **Vaksinasi Hepatitis:** Lengkapi vaksin hepatitis A dan B.
            4. **Konsumsi Makanan Sehat:** Perbanyak sayuran hijau, kurangi lemak jenuh dan gula.
            """)
        with tab3:
            st.info("💡 **Catatan Medis:** Sebagian besar penyakit hati memerlukan diagnosis laboratorium (SGOT/SGPT) dan pencitraan.")
            st.markdown("### 💊 Klasifikasi Farmakologi Umum")
            st.markdown("""
            * **Hepatoprotektor:** (Contoh: *Silymarin, Curcuma*). Membantu regenerasi sel hati dan antioksidan.
            * **Antiviral Hepatitis:** (Contoh: *Tenofovir, Entecavir*). Untuk hepatitis B kronis guna menekan replikasi virus.
            * **Ursodeoxycholic Acid (UDCA):** Mengurangi toksisitas asam empedu pada kolestasis.
            """)

    elif organ_name == "Ginjal":
        with tab1:
            st.markdown("### 🫗 Anatomi & Fungsi Klinis")
            st.write("Ginjal adalah sepasang organ filtrasi berbentuk kacang yang menyaring ~200 liter darah/hari. Fungsi utamanya: mengeliminasi limbah nitrogen (ureum, kreatinin), mengatur keseimbangan elektrolit, tekanan darah (renin), dan produksi eritropoietin untuk sel darah merah.")
            st.markdown("### ⚠️ Patologi & Gangguan Umum")
            st.markdown("""
            * **Batu Ginjal (Nefrolitiasis):** Kristal keras dari mineral dan garam yang terbentuk di saluran kemih. Menyebabkan nyeri kolik hebat.
            * **Penyakit Ginjal Kronis (PGK):** Penurunan fungsi ginjal secara progresif selama >3 bulan. Stadium akhir memerlukan dialisis.
            * **Infeksi Saluran Kemih (ISK) Atas:** Infeksi pada pelvis ginjal (pielonefritis) yang dapat merusak jaringan ginjal.
            """)
        with tab2:
            st.error("**🚰 PROTOKOL: Mencegah Perburukan Ginjal**")
            st.markdown("""
            1. **Hidrasi Cukup:** Minum 2-3 liter air per hari, terutama jika rentan batu ginjal.
            2. **Batasi Garam & Protein Berlebih:** Diet rendah garam (<5g/hari) dan protein sesuai anjuran.
            3. **Hati-hati Obat Nefrotoksik:** Hindari NSAID jangka panjang tanpa resep dokter.
            4. **Kontrol Gula Darah & Tekanan Darah:** Dua penyebab utama gagal ginjal.
            """)
        with tab3:
            st.info("💡 **Catatan Medis:** Pemeriksaan fungsi ginjal (ureum/kreatinin, eGFR) perlu rutin bagi yang berisiko.")
            st.markdown("### 💊 Klasifikasi Farmakologi Umum")
            st.markdown("""
            * **Diuretik:** (Contoh: *Furosemide*). Membantu pembuangan kelebihan cairan pada edema.
            * **ACE Inhibitor/ARB:** (Contoh: *Lisinopril, Candesartan*). Menurunkan tekanan darah dan melindungi ginjal diabetisi.
            * **Peluruh Batu Ginjal:** (Contoh: *Tamsulosin*). Merelaksasi ureter untuk memudahkan pengeluaran batu.
            """)

    elif organ_name == "Pankreas":
        with tab1:
            st.markdown("### 🩸 Anatomi & Fungsi Klinis")
            st.write("Pankreas adalah organ ganda (endokrin & eksokrin). Fungsi endokrin: menghasilkan insulin dan glukagon untuk mengontrol gula darah. Fungsi eksokrin: mengeluarkan enzim pencernaan (amilase, lipase) ke usus halus.")
            st.markdown("### ⚠️ Patologi & Gangguan Umum")
            st.markdown("""
            * **Diabetes Melitus Tipe 1 & 2:** Gangguan produksi insulin (tipe 1) atau resistensi insulin (tipe 2) yang menyebabkan hiperglikemia kronis.
            * **Pankreatitis:** Peradangan mendadak pada pankreas, sering dipicu oleh batu empedu atau alkohol. Enzim pencernaan bocor dan mencerna pankreas sendiri.
            * **Kanker Pankreas:** Tumor ganas dengan prognosis buruk karena sering terdeteksi lambat.
            """)
        with tab2:
            st.error("**⚠️ PROTOKOL DARURAT: Kenali Gejala Pankreatitis Akut**")
            st.markdown("""
            1. **Nyeri Hebat Perut Atas:** Menjalar ke punggung seperti ditusuk, disertai mual/muntah.
            2. **Segera Puasakan:** Jangan makan/minum apapun untuk mengistirahatkan pankreas.
            3. **Cari Bantuan Medis Darurat:** Pankreatitis memerlukan perawatan intensif di rumah sakit.
            """)
        with tab3:
            st.info("💡 **Catatan Medis:** Diabetes memerlukan pemantauan gula darah mandiri dan modifikasi gaya hidup.")
            st.markdown("### 💊 Klasifikasi Farmakologi Umum")
            st.markdown("""
            * **Insulin & Analog:** Untuk diabetes tipe 1 dan beberapa tipe 2.
            * **Antidiabetik Oral:** (Contoh: *Metformin, Glimepiride, Dapagliflozin*). Menurunkan gula darah.
            * **Enzim Pankreas Suplemen:** (Contoh: *Pancrelipase*). Untuk insufisiensi eksokrin pasca pankreatitis.
            """)

    elif organ_name == "Tulang" or organ_name == "Tulang & Sendi":
        with tab1:
            st.markdown("### 🦴 Anatomi & Fungsi Klinis")
            st.write("Sistem muskuloskeletal terdiri dari 206 tulang, sendi, ligamen, dan otot. Fungsinya meliputi penopang tubuh, pergerakan, perlindungan organ vital, dan produksi sel darah di sumsum tulang.")
            st.markdown("### ⚠️ Patologi & Gangguan Umum")
            st.markdown("""
            * **Osteoporosis:** Penurunan kepadatan tulang sehingga tulang keropos dan rentan patah, terutama pada wanita pasca menopause.
            * **Osteoarthritis (Pengapuran Sendi):** Degenerasi kartilago sendi kronis yang menyebabkan nyeri, kaku, dan terbatasnya gerak.
            * **Artritis Reumatoid:** Penyakit autoimun yang menyerang membran sinovial sendi, menyebabkan peradangan simetris, bengkak, dan deformitas.
            """)
        with tab2:
            st.warning("**🩼 PROTOKOL: Pertolongan Pertama Cedera Tulang/Sendi**")
            st.markdown("""
            1. **Imobilisasi:** Jangan gerakkan bagian yang dicurigai patah. Gunakan bidai sederhana (papan, karton) untuk fiksasi.
            2. **Kompres Dingin:** Segera beri kompres es (dibungkus kain) pada area cedera selama 15-20 menit untuk mengurangi bengkak.
            3. **Elevasi:** Posisikan area cedera lebih tinggi dari jantung jika memungkinkan.
            4. **Segera ke IGD:** Untuk penanganan definitif (rontgen, gips, atau operasi).
            """)
        with tab3:
            st.info("💡 **Catatan Medis:** Suplemen kalsium dan vitamin D penting, namun konsultasikan dosis dengan dokter.")
            st.markdown("### 💊 Klasifikasi Farmakologi Umum")
            st.markdown("""
            * **Analgesik & NSAID:** (Contoh: *Ibuprofen, Natrium Diklofenak*). Meredakan nyeri dan inflamasi sendi.
            * **Bisfosfonat:** (Contoh: *Alendronate*). Menghambat resorpsi tulang pada osteoporosis.
            * **Suplemen:** Kalsium karbonat/sitrat + Vitamin D3.
            * **DMARDs (Disease-Modifying Antirheumatic Drugs):** (Contoh: *Methotrexate*). Untuk arthritis reumatoid guna menekan progresi autoimun.
            """)