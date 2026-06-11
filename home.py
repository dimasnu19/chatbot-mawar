import streamlit as st
from utils import inject_custom_css

def show_home():
    inject_custom_css()
    
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, rgba(32, 37, 85, 0.45), rgba(15, 18, 45, 0.65));
        backdrop-filter: blur(30px);
        -webkit-backdrop-filter: blur(30px);
        padding: 55px 40px;
        border-radius: 24px;
        border: 1px solid rgba(255, 255, 255, 0.08);
        color: white;
        margin-bottom: 40px;
        text-align: center;
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5);
    ">
        <span style="background: rgba(56, 189, 248, 0.12); color: #38bdf8; padding: 6px 18px; border-radius: 30px; font-size: 11px; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; border: 1px solid rgba(56, 189, 248, 0.25); display: inline-block; margin-bottom: 15px;">
            Pusat Edukasi & Informasi Kesehatan Digital
        </span>
        <h1 style="color: #ffffff; margin-top: 10px; font-size: 36px; font-weight: 800; letter-spacing: -0.03em; line-height: 1.2;">
            Platform Konten Kesehatan & Chatbot Interaktif
        </h1>
        <p style="color: #aeb9ce; font-size: 15px; max-width: 800px; margin: 18px auto 0px auto; line-height: 1.7; font-weight: 400;">
            Pelajari panduan kesehatan seputar fungsi organ tubuh, temukan informasi valid mengenai klasifikasi obat-obatan, dan manfaatkan asisten chatbot interaktif untuk panduan awal penanganan gejala kesehatan Anda.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<h3 style='color: #ffffff; font-weight: 700; font-size: 22px; margin-bottom: 25px;'>Anatomi & Informasi Sistem Organ</h3>", unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        with st.container(border=True):
            st.markdown("<h1 style='margin:0; font-size:45px; text-align:center;'>🫀</h1>", unsafe_allow_html=True)
            st.markdown("<h4 style='margin:10px 0 5px 0; color:#ffffff; font-weight:600; text-align:center;'>Jantung</h4>", unsafe_allow_html=True)
            st.markdown("<p style='margin:0 0 15px 0; color:#94a3b8; font-size:13px; text-align:center; min-height: 45px; line-height:1.4;'>Sistem kardiovaskular & sirkulasi darah vital.</p>", unsafe_allow_html=True)
            if st.button("Buka Anatomi", key="btn_jantung", use_container_width=True):
                st.session_state.current_page = "Detail_Jantung"
                st.rerun()

    with col2:
        with st.container(border=True):
            st.markdown("<h1 style='margin:0; font-size:45px; text-align:center;'>🫁</h1>", unsafe_allow_html=True)
            st.markdown("<h4 style='margin:10px 0 5px 0; color:#ffffff; font-weight:600; text-align:center;'>Paru-paru</h4>", unsafe_allow_html=True)
            st.markdown("<p style='margin:0 0 15px 0; color:#94a3b8; font-size:13px; text-align:center; min-height: 45px; line-height:1.4;'>Sistem respirasi & pertukaran oksigen tubuh.</p>", unsafe_allow_html=True)
            if st.button("Buka Anatomi", key="btn_paru", use_container_width=True):
                st.session_state.current_page = "Detail_Paru-paru"
                st.rerun()
            
    with col3:
        with st.container(border=True):
            st.markdown("<h1 style='margin:0; font-size:45px; text-align:center;'>🧠</h1>", unsafe_allow_html=True)
            st.markdown("<h4 style='margin:10px 0 5px 0; color:#ffffff; font-weight:600; text-align:center;'>Otak</h4>", unsafe_allow_html=True)
            st.markdown("<p style='margin:0 0 15px 0; color:#94a3b8; font-size:13px; text-align:center; min-height: 45px; line-height:1.4;'>Sistem saraf pusat & pusat kendali memori.</p>", unsafe_allow_html=True)
            if st.button("Buka Anatomi", key="btn_otak", use_container_width=True):
                st.session_state.current_page = "Detail_Otak"
                st.rerun()
            
    with col4:
        with st.container(border=True):
            st.markdown("<h1 style='margin:0; font-size:45px; text-align:center;'>🥖</h1>", unsafe_allow_html=True)
            st.markdown("<h4 style='margin:10px 0 5px 0; color:#ffffff; font-weight:600; text-align:center;'>Lambung</h4>", unsafe_allow_html=True)
            st.markdown("<p style='margin:0 0 15px 0; color:#94a3b8; font-size:13px; text-align:center; min-height: 45px; line-height:1.4;'>Sistem pencernaan & regulasi asam lambung.</p>", unsafe_allow_html=True)
            if st.button("Buka Anatomi", key="btn_lambung", use_container_width=True):
                st.session_state.current_page = "Detail_Lambung"
                st.rerun()

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #ffffff; font-weight: 700; font-size: 22px; margin-bottom: 25px;'>Layanan Edukasi Ngobat.In</h3>", unsafe_allow_html=True)
    
    feat1, feat2, feat3 = st.columns(3)
    with feat1:
        with st.container(border=True):
            st.markdown("<h5 style='color:#38bdf8; font-weight:600; margin-bottom:12px;'>💬 Chatbot Interaktif</h5>", unsafe_allow_html=True)
            st.markdown("<p style='font-size:13.5px; line-height:1.6; margin:0;'>Gunakan tombol obrolan di pojok kanan bawah untuk mengonsultasikan atau mencari tahu arah kemungkinan keluhan sakit yang sedang dialami.</p>", unsafe_allow_html=True)
    with feat2:
        with st.container(border=True):
            st.markdown("<h5 style='color:#a78bfa; font-weight:600; margin-bottom:12px;'>📚 Informasi Obat</h5>", unsafe_allow_html=True)
            st.markdown("<p style='font-size:13.5px; line-height:1.6; margin:0;'>Pelajari berbagai jenis penggolongan obat-obatan medis, peringatan dosis, hingga indikasi penting pada menu 'Penjelasan Obat'.</p>", unsafe_allow_html=True)
    with feat3:
        with st.container(border=True):
            st.markdown("<h5 style='color:#f472b6; font-weight:600; margin-bottom:12px;'>🚨 Tindakan Pertama</h5>", unsafe_allow_html=True)
            st.markdown("<p style='font-size:13.5px; line-height:1.6; margin:0;'>Dapatkan informasi edukatif yang tervalidasi mengenai prosedur pertolongan darurat awal (*First-Aid*) pada kelainan fungsi organ.</p>", unsafe_allow_html=True)


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