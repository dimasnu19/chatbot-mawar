import re
from enum import Enum, auto
from engine import MedicalEngine

class State(Enum):
    IDLE = auto()
    CONSULTING = auto()
    RESULT = auto()

class HealthFSM:
    def __init__(self):
        self.state = State.IDLE
        self.engine = MedicalEngine()
        self.detected_symptoms = []
        self.response = ""

    def get_response(self):
        return self.response

    def _normalize_input(self, text):
        """
        Kamus Raksasa V9 Ultimate Omega: Varian bahasa daerah, istilah modern,
        penambahan gejala baru (jantung, saraf, kegawatdaruratan), dan penataan urutan
        kata yang fleksibel. Sinkronisasi ekstraksi lebih presisi.
        """
        text = text.lower().strip()

        # ========== 1. KAMUS KATA & SINGKATAN (REGEX) ==========
        slang_words = {
            # Subjek & Kata Ganti
            r"\bgw\b|\bgue\b|\bgua\b|\baku\b|\bakk\b|\bnyong\b|\bane\b|\bak\b|\bme\b|\bw\b|\bi\b|\burang\b|\bkami\b|\baing\b|\babdi\b|\bbeta\b|\bawak\b|\bkita\b|\bambo\b|\bulun\b|\btiang\b|\bogut\b|\bsa\b|\bnyong\b": "saya",
            r"\blu\b|\blo\b|\belo\b|\bkamu\b|\bkm\b|\bkau\b|\bmu\b|\bkelen\b|\bente\b|\bmaneh\b|\bsampean\b|\bpanjenengan\b|\bngana\b|\bko\b|\bkowen\b|\bkam\b": "anda",
            
            # Negasi & Persetujuan
            r"\bga\b|\bgak\b|\bngga\b|\bnggak\b|\bndak\b|\bkaga\b|\bkagak\b|\btak\b|\bgk\b|\bg\b|\bogah\b|\bmo\b|\bmau\b|\btdk\b|\bhnteu\b|\bnda\b|\btra\b|\bseng\b|\bndak\b|\bindak\b|\btrada\b": "tidak",
            r"\biya\b|\byo\b|\bya\b|\bhooh\b|\binggih\b|\boke\b|\bok\b|\byoi\b|\bacc\b|\bheeh\b|\bmuhun\b|\bgas\b|\bio\b": "ya",
            r"\bgatau\b|\bndak tau\b|\bembuh\b|\bnyaho\b|\bduka\b|\bkurang tau\b|\bteuing\b|\bgelap\b|\bkamfret\b|\btawang\b": "tidak tahu",
            
            # Penguat Tingkat Keparahan
            r"\bbgt\b|\bbanget\b|\bpisan\b|\bpol\b|\bparah\b|\bbingit\b|\bmenjerit\b|\bamat\b|\bpuol\b|\bgila\b|\banjrot\b|\bekstrim\b|\bsanget\b|\bampun\b|\bnaudzubillah\b|\bsekarat\b|\bmeninggoy\b|\bmokad\b|\btewas\b|\bampun2an\b|\bpol-polan\b": "sekali",
            r"\bngerasa\b|\bngerasain\b|\bberasa\b|\basa\b|\bkerasa\b|\bkeinget\b|\bkroso\b|\bngarasakeun\b|\bterasa\b|\bmarasa\b": "merasa",
            
            # ---------- GEJALA ----------
            # Mental & Saraf
            r"\bcemas\b|\bpanik\b|\bovt\b|\boverthinking\b|\btremor\b|\bdeg2an\b|\banxiety\b|\bwaswas\b|\bgelisah\b|\btakut\b|\bstres\b|\bdepresi\b|\bbrain fog\b|\bblank\b|\blinglung\b|\blinglo\b|\btelmi\b": "cemas",
            r"\binsomnia\b|\bgabisa tidur\b|\bmerem susah\b|\bmelek mulu\b|\bturu susah\b|\bbegadang\b|\bgadang\b": "insomnia",
            r"\bepilepsi\b|\bkejang\b|\bstep\b|\bkejang2\b|\bkejang-kejang\b": "kejang",
            
            # Kepala & Saraf
            r"\bpusing\b|\bpuyeng\b|\bmumet\b|\bkliyengan\b|\bgliyengan\b|\bpening\b|\bmuter\b|\bmigren\b|\bmigrain\b|\bcekat\b|\bcenat\b|\bcenut\b|\bnyut\b|\bngelu\b|\bkunang2\b|\bvertigo\b|\brieut\b|\bcekot2\b|\bpeneng\b": "pusing",
            r"\bleher kaku\b|\bleher tegang\b|\bkaku leher\b|\bkuduk kaku\b|\bneck stiffness\b": "leher kaku",
            r"\bkesemutan\b|\bgringgingen\b|\bkebas\b|\bmati rasa\b|\bsemutan\b|\bbaal\b|\bkesingkir\b": "kesemutan",
            r"\bpingsan\b|\bsemaput\b|\bblackout\b|\bsempoyongan\b|\bteler\b|\bambruk\b|\bkelenger\b|\btekapar\b": "pingsan",
            
            # Jantung & Dada
            r"\bnyeri dada\b|\bdada nyeri\b|\bdada sakit\b|\bchest pain\b|\bnyut-nyut dada\b|\btertindih dada\b": "nyeri dada",
            r"\bjantung berdebar\b|\bdebaran\b|\bpalpitasi\b|\bdeg-degan\b": "jantung berdebar",
            
            # Suhu & Umum
            r"\bdemam\b|\bsumeng\b|\bmeriang\b|\bnggreges\b|\bgreges\b|\bmenggigil\b|\bpanas\b|\bsumer\b|\bmrinding\b|\bdmm\b|\banyep\b|\bkedinginan\b|\bnget-ngetan\b|\breriangan\b|\bkemranyas\b|\bngliyeng\b|\bpanasbadan\b": "demam",
            
            # Saluran Napas
            r"\bpilek\b|\bmeler\b|\bingusan\b|\bflu\b|\bbersin2\b|\bmampet\b|\btersumbat\b|\bbuntu\b|\bpileg\b|\bumbel\b|\bumbelan\b|\bbindeng\b|\bmimisan\b": "pilek",
            r"\bbatuk\b|\bbatok\b|\buhuk\b|\bbatuk2\b|\bserak\b|\bradang\b|\bngorok\b|\bbtk\b|\bngik\b|\bgrokgrok\b|\bdehem\b": "batuk",
            r"\bsesak napas\b|\bengap\b|\bnyesek\b|\bmengi\b|\basma\b|\bngos2an\b|\bseseg\b|\bbengek\b|\bapnea\b|\bmengik\b|\bngos-ngosan\b": "sesak napas",
            
            # Pencernaan
            r"\bmual\b|\benek\b|\bnek\b|\buek\b|\bnek2\b|\bhuek\b|\bmblenger\b|\bsebel\b|\bweureu\b": "mual",
            r"\bmuntah\b|\bmuntah2\b|\buntah\b|\bhoeks\b|\bmth\b": "muntah",
            r"\bdiare\b|\bmules\b|\bmencret\b|\bberak\b|\bboker\b|\bmencret2\b|\bpup\b|\bbab\b|\bcair\b|\bmurus\b|\bcor\b|\bmodol\b|\bdredeg\b|\bmejen\b": "diare",
            r"\bnyeri perut\b|\bmelilit\b|\bkram\b|\bperih\b|\bsebah\b|\bkembung\b|\bbegah\b|\bmaag\b|\bmag\b|\bgerd\b|\baslam\b|\bmlilit\b": "nyeri perut",
            r"\bwasir\b|\bambeien\b|\bhemaroid\b|\bhemoroid\b|\bambyen\b": "wasir",
            r"\bsembelit\b|\bmampet bab\b|\bkeras bab\b|\bsusah berak\b|\bsmbilit\b": "sembelit",
            
            # Mulut & THT
            r"\biritasi tenggorokan\b|\btenggorokan sakit\b|\btenggorokan gatal\b|\bnyeri telan\b": "iritasi tenggorokan",
            r"\biritasi mulut\b|\bpanas dalam\b|\bpanasdalem\b|\bsariawan\b|\bbibir pecah\b": "iritasi mulut",
            r"\bsakit gigi\b|\bgusi\b|\bbolong\b|\bompong\b|\buntu\b|\bnyenut\b|\bngilu gigi\b": "sakit gigi",
            r"\bsakit telinga\b|\bbudeg\b|\btenging\b|\bdenging\b|\bberdenging\b|\bkopok\b|\bcurek\b|\btuli\b": "sakit telinga",
            r"\bmimisan\b|\bhidung berdarah\b|\bkeluar darah hidung\b": "mimisan",
            
            # Mata
            r"\bmata kabur\b|\bblawur\b|\bburem\b|\bsepet\b|\bbelekan\b|\bmerem\b|\bkunang\b": "mata kabur",
            
            # Kulit & Alergi
            r"\bgatal\b|\bgatel2\b|\bperih2\b|\bkaligata\b|\bbiduran\b|\bgatelen\b|\balergi\b": "gatal",
            r"\bruam\b|\bmerah2\b|\bbentol\b|\bbintik\b|\bbintik2\b|\bberuntusan\b|\bplenting\b|\bruam2\b|\bcantengan\b|\bmruntus\b|\bcacar\b|\bgudig\b|\bkurap\b|\bmelentung\b": "ruam",
            r"\bbengkak\b|\babuh\b|\baub\b|\bbengkak2\b|\bswelling\b|\bebuh\b": "bengkak",
            
            # Otot & Sendi
            r"\blemas\b|\blemes\b|\bloyo\b|\blesu\b|\blunglai\b|\bchape\b|\bcape\b|\bcapek\b|\btepar\b|\bdrop\b|\bgempor\b|\blms\b|\bburnout\b|\blowbat\b|\bjompo\b|\blumbruk\b|\bfatigue\b": "lemas",
            r"\bnyeri otot\b|\bpegel2\b|\blinu\b|\bnyilu\b|\bsengkring2\b|\bboyok\b|\bboyokan\b|\bencok\b|\bkecetit\b|\bkemeng\b|\bnjarem\b|\bkeseleo\b|\bcengeng\b|\brematik\b|\blinu-linu\b|\bterkilir\b|\bsalah urat\b|\bbackpain\b": "nyeri otot",
            r"\bnyeri sendi\b|\bngilu\b|\bsendi kaku\b|\basam urat\b|\bsingsal\b|\bcekot\b": "nyeri sendi",
            
            # Saluran Kemih & Reproduksi
            r"\banyang-anyangan\b|\banyang\b|\banyangan\b|\bpipis\b|\bkencing\b|\bngompol\b": "anyang-anyangan",
            r"\bsering kencing\b|\bkencing terus\b|\bpipis terus\b|\bfrequent urination\b": "sering kencing",
            r"\bnyeri haid\b|\bhaid\b|\bmens\b|\bmenstruasi\b|\bdatang bulan\b|\bpms\b": "nyeri haid",
            
            # Pembersih Kosmetik
            r"\bbro\b|\bcuy\b|\bsis\b|\bgan\b|\bnih\b|\btuh\b|\bloh\b|\bdeh\b|\bgaes\b|\bguys\b|\bdong\b|\bcoi\b|\bngab\b|\bwk\b|\bwkwk\b|\bhehe\b|\bhaha\b|\bbtw\b|\bplis\b|\bjir\b|\banjir\b|\bgws\b|\bfomo\b|\bngabers\b|\bygy\b|\bndah\b": ""
        }

        for pattern, replacement in slang_words.items():
            text = re.sub(pattern, replacement, text)

        # ========== 2. KAMUS FRASA GABUNGAN (EKSTREM + VARIASI URUTAN) ==========
        phrase_replacements = {
            # Suhu & Badan
            "ga enak badan": "demam",
            "tidak enak badan": "demam",
            "kurang fit": "demam",
            "badan drop": "demam",
            "badan panas": "demam",
            "panas dingin": "demam menggigil",
            "adem panas": "demam",
            "merasa nggreges": "demam",
            "keringat dingin": "lemas",
            
            # Mental & Saraf
            "serasa mau mati": "cemas",
            "takut mati": "cemas",
            "serangan panik": "cemas",
            "susah tidur": "insomnia",
            "tidak bisa tidur": "insomnia",
            "pikiran stuck": "cemas",
            "burnout parah": "lemas",
            "leher tegang": "leher kaku",
            "kaku kuduk": "leher kaku",
            "kepala berat": "pusing",
            
            # Lambung & Perut (ekstra variasi)
            "sakit perut": "nyeri perut",
            "perut sakit": "nyeri perut",
            "sakit di perut": "nyeri perut",
            "nyeri di perut": "nyeri perut",
            "sakit lambung": "nyeri perut",
            "lambung sakit": "nyeri perut",
            "asam lambung naik": "nyeri perut",
            "asam lambung": "nyeri perut",
            "ulu hati sakit": "nyeri perut",
            "ulu hati perih": "nyeri perut",
            "perut melilit": "nyeri perut",
            "perut kembung": "nyeri perut",
            "masuk angin": "nyeri perut",
            
            # Kepala & Pusing
            "sakit kepala": "pusing",
            "kepala pusing": "pusing",
            "kepala sakit": "pusing",
            "kepala nyeri": "pusing",   # tambahan untuk "kepala nyeri"
            "pala puyeng": "pusing",
            "kepala cekat cenut": "pusing",
            "pala babi": "pusing",
            
            # Dada & Jantung
            "dada nyeri": "nyeri dada",
            "dada sakit": "nyeri dada",
            "nyeri di dada": "nyeri dada",
            "chest pain": "nyeri dada",
            "dada sesak": "sesak napas",
            "nafas sesek": "sesak napas",
            "susah napas": "sesak napas",
            "dada nyesek": "sesak napas",
            "jantung berdebar keras": "jantung berdebar",
            
            # Pernapasan & Hidung
            "hidung tersumbat": "pilek",
            "hidung mampet": "pilek",
            "hidung buntu": "pilek",
            "hidung berair": "pilek",
            "keluar ingus": "pilek",
            "batuk pilek": "batuk",
            
            # Pembuangan
            "boker berdarah": "wasir",
            "bab berdarah": "wasir",
            "pantat sakit": "wasir",
            "dubur perih": "wasir",
            "mencret cor": "diare",
            "susah bab": "sembelit",
            "gak bisa bab": "sembelit",
            "bab keras": "sembelit",
            
            # Mulut & Tenggorokan
            "tenggorokan sakit": "iritasi tenggorokan",
            "sakit tenggorokan": "iritasi tenggorokan",
            "sakit buat nelen": "iritasi tenggorokan",
            "gusi bengkak": "sakit gigi",
            "gigi sakit": "sakit gigi",
            "sariawan banyak": "iritasi mulut",
            "bibir pecah-pecah": "iritasi mulut",
            
            # Otot & Sendi
            "pegel linu": "nyeri otot",
            "badan pegel": "nyeri otot",
            "sakit pinggang": "nyeri otot",
            "urat kejepit": "nyeri otot",
            "leher bagian belakang kaku": "nyeri otot",
            "pegal": "nyeri otot",  # tangkap "pegal" langsung
            
            # Mata & Telinga
            "mata sepet": "mata kabur",
            "mata kering": "mata kabur",
            "telinga denging": "sakit telinga",
            
            # Kewanitaan
            "nyeri haid": "nyeri haid",
            "mens sakit": "nyeri haid",
            "kram perut bawah": "nyeri haid",
            
            # Baru: Mimisan & Bengkak
            "hidung berdarah": "mimisan",
            "mimisan terus": "mimisan",
            "badan bengkak": "bengkak",
            "kaki bengkak": "bengkak",
            "mata bengkak": "bengkak",
        }

        for phrase, replacement in phrase_replacements.items():
            text = text.replace(phrase, replacement)

        text = re.sub(r'\s+', ' ', text).strip()
        return text

    def step(self, user_input):
        raw_input = user_input.strip()
        user_input_lower = raw_input.lower()
        
        normalized_input = self._normalize_input(raw_input)
        intent = self.engine.detect_intent(normalized_input)

        # ========== 1. RESET ==========
        if intent == "RESET" or "reset" in user_input_lower:
            self.__init__()
            self.response = "Baik, memori pemeriksaan gejala sudah saya bersihkan sepenuhnya. Mari kita mulai lembaran baru. Apa keluhan utama atau gejala fisik yang sedang mengganggu Anda saat ini?"
            return

        # ========== 2. INTERCEPTOR: SAPAAN & PERTANYAAN UMUM ==========
        user_words = user_input_lower.split()
        sapaan_dasar = ["halo", "hai", "p", "assalamualaikum", "ping", "hola", "hi", "permisi", "pagi", "siang", "sore", "malam", "kulanuwun", "sampurasun", "punten", "tabea"]
        sapaan_panjang = ["selamat pagi", "selamat siang", "selamat sore", "selamat malam"]

        if (any(word in user_words for word in sapaan_dasar) or any(sapaan in user_input_lower for sapaan in sapaan_panjang)) and len(user_words) <= 3:
            self.response = "Halo! 👋 Saya adalah Sistem Pakar AI Medis dari Ngobat.In. Anda dapat memanfaatkan saya untuk melakukan skrining atau pelacakan awal gejala penyakit. \n\nSilakan langsung deskripsikan apa yang Anda rasakan sejelas mungkin (contoh: *'saya pusing, mual, dan badan nggreges panas'*). Ada yang bisa saya bantu?"
            return

        if any(word in user_input_lower for word in ["ngobat.in", "website ini", "aplikasi ini", "buat apa", "fungsi"]):
            self.response = (
                "**Ngobat.In** adalah platform integrasi kesehatan digital. Di menu atas, Anda dapat mengakses fitur **Penjelasan Obat** untuk memantau indikasi obat, "
                "serta **Tips Kesehatan** untuk panduan gaya hidup preventif. \n\nTugas saya di sini adalah sebagai agen interaktif pemetaan gejala awal. Apakah Anda sedang merasakan keluhan sakit tertentu?"
            )
            return
            
        if user_input_lower.startswith(("apa itu", "bagaimana cara", "kenapa", "penyebab", "obat untuk", "cara ngobatin", "solusi")):
            self.response = (
                "Sebagai asisten AI interaktif, fokus klinis saya saat ini adalah mengumpulkan konfirmasi gejala langsung dari Anda guna memprediksi indikasi penyakit.\n\n"
                "Untuk ensiklopedia obat terlengkap, Anda bisa memanfaatkan fitur **Penjelasan Obat**. Namun jika tubuh Anda saat ini terasa tidak sehat, tolong sebutkan gejalanya agar segera saya petakan. 🏥"
            )
            return

        # ========== TANGANI INPUT VAGUE "dan lain sebagainya" ==========
        vague_markers = ["dan lain sebagainya", "dan sebagainya", "dll", "dan lain lain", "dan seterusnya", "dls", "dsb"]
        if any(marker in user_input_lower for marker in vague_markers):
            # Jika hanya frase vague tanpa gejala jelas, minta detail
            if len(user_words) <= 3:
                self.response = "Mohon maaf, saya belum bisa memproses keterangan yang terlalu umum seperti 'dan lain sebagainya'. Agar saya bisa membantu, sebutkan secara spesifik apa saja yang Anda rasakan, misalnya 'pusing', 'mual', 'nyeri dada', atau 'pegal linu'.\n\nSilakan tulis ulang keluhan Anda selengkap mungkin."
                return
            # Tapi jika ada gejala lain, kita tetap proses. Jadi lanjut ke bawah.

        # ========== 3. ALUR KONSULTASI GEJALA (FSM) ==========
        if self.state == State.IDLE:
            self.state = State.CONSULTING
            if not user_input_lower:
                self.response = (
                    "Sepertinya kondisi fisik Anda sedang kurang optimal, ya? Jangan ragu untuk menceritakan keluhan Anda secara alami.\n\n"
                    "Anda bisa mengetik seperti ini:\n"
                    "- *'kepala pening muter, mual banget pas bangun tidur'* 🤢\n"
                    "- *'dada sesak nyesek, punggung juga pegal linu'* 😮‍💨\n"
                    "- *'lagi overthinking parah, tremor, sama gabisa tidur'* 😰\n\n"
                    "Silakan tuliskan seluruh keluhan Anda di bawah ini."
                )
                return

        if self.state == State.CONSULTING:
            if intent == "FINISH" or any(kw in user_input_lower for kw in ["proses", "cukup", "sudah"]):
                if not self.detected_symptoms:
                    self.response = (
                        "Sistem belum mendeteksi adanya kata kunci gejala medis yang spesifik dari deskripsi Anda. Bisakah Anda sebutkan bagian tubuh mana yang terasa sakit atau tidak nyaman?\n\n"
                        "Atau ketik **'reset'** jika Anda ingin mengulang pengisian."
                    )
                else:
                    diagnosis = self.engine.diagnose(self.detected_symptoms)
                    self.state = State.RESULT
                    
                    if diagnosis:
                        self.response = (
                            f"**[ANALISIS KESIMPULAN DIAGNOSIS GEJALA AWAL]**\n"
                            f"Berdasarkan himpunan keluhan yang berhasil diverifikasi, Anda terindikasi kuat mengalami: **{diagnosis['name']}**.\n\n"
                            f"📖 **Ulasan Klinis Sederhana:**\n{diagnosis['desc']}\n\n"
                            f"💊 **Rekomendasi Tindakan & Farmakoterapi Awal:**\n{diagnosis['medicine']}\n\n"
                            f"⚠️ **DISCLAIMER MEDIS UTAMA:**\n"
                            f"Saya adalah kecerdasan buatan dan bukan pengganti sah dari kompetensi Dokter. Hasil diagnosis ini murni bersifat skrining dan edukasi awal. Jika gejala menetap, memburuk, atau muncul tanda bahaya dalam 48-72 jam, **segera kunjungi klinik, dokter keluarga, atau fasilitas rumah sakit terdekat!**\n\n"
                            f"*(Ketik **'reset'** jika ingin melakukan pemetaan gejala penyakit lainnya)*"
                        )
                    else:
                        self.response = (
                            "Kombinasi gejala yang Anda berikan tergolong sangat kompleks dan memiliki spektrum diferensial diagnosis yang luas, sehingga belum cocok dengan algoritma dasar kami.\n\n"
                            "Demi keselamatan medis Anda, sangat disarankan untuk segera melakukan pemeriksaan penunjang (seperti tes darah atau pemeriksaan fisik) langsung di hadapan dokter. Ketik **'reset' untuk mengulang."
                        )
            else:
                new_symptoms = self.engine.extract_symptoms(normalized_input)
                
                # LOCAL BACKUP EXTRACTION – daftar gejala baku yang disinkronkan dengan kamus
                if not new_symptoms:
                    backup_keywords = [
                        "cemas", "insomnia", "kejang", "pusing", "leher kaku", "kesemutan",
                        "pingsan", "nyeri dada", "jantung berdebar", "demam", "pilek", "batuk",
                        "sesak napas", "mual", "muntah", "diare", "nyeri perut", "wasir",
                        "sembelit", "iritasi tenggorokan", "iritasi mulut", "sakit gigi",
                        "sakit telinga", "mimisan", "mata kabur", "gatal", "ruam", "bengkak",
                        "lemas", "nyeri otot", "nyeri sendi", "anyang-anyangan", "sering kencing",
                        "nyeri haid"
                    ]
                    new_symptoms = [sym for sym in backup_keywords if sym in normalized_input]
                
                if new_symptoms:
                    added_symptoms = []
                    for symp in new_symptoms:
                        if symp not in self.detected_symptoms:
                            self.detected_symptoms.append(symp)
                            added_symptoms.append(symp)
                    
                    if added_symptoms:
                        suggestions = self.engine.get_suggested_symptoms(self.detected_symptoms)
                        
                        # ========== PESAN KONTEKSTUAL YANG DIPERKAYA ==========
                        # Buat sapaan personal
                        greeting = "Baik, terima kasih sudah menyampaikan. "
                        
                        # Rangkai gejala yang baru terdeteksi menjadi kalimat yang enak dibaca
                        symptom_list_readable = ", ".join(added_symptoms).capitalize()
                        
                        # Buat kalimat pembuka yang bervariasi sesuai gejala
                        intro = f"Saya mencatat bahwa Anda mengeluhkan: **{symptom_list_readable}**. "
                        
                        # Berikan komentar singkat per gejala (jika hanya sedikit)
                        if len(added_symptoms) == 1:
                            symptom = added_symptoms[0]
                            if symptom == "nyeri dada":
                                intro += "Nyeri dada adalah keluhan yang perlu diwaspadai, terutama jika terasa seperti tertekan atau menjalar. "
                            elif symptom == "pusing":
                                intro += "Pusing bisa disebabkan banyak hal, mulai dari kelelahan, dehidrasi, hingga migrain. "
                            elif symptom == "nyeri otot":
                                intro += "Pegal atau nyeri otot sering muncul setelah aktivitas fisik atau postur yang kurang baik. "
                            else:
                                intro += "Saya pahami, kondisi ini tentu membuat tidak nyaman. "
                        else:
                            intro += "Beberapa gejala ini mungkin saling berkaitan, dan penting bagi kita untuk melihatnya sebagai satu kesatuan. "
                        
                        # ========== ENSIKLOPEDIA P3K (SINKRON) ==========
                        symptom_advices = []
                        if any(s in added_symptoms for s in ["cemas", "panik"]):
                            symptom_advices.append("🧘 **Cemas/Panik:** Lakukan *Box Breathing*, batasi kafein. Jika serangan panik berulang, konsultasi ke profesional.")
                        if any(s in added_symptoms for s in ["demam", "demam menggigil"]):
                            symptom_advices.append("🌡️ **Demam:** Kompres air hangat di lipatan tubuh. Paracetamol jika >38.5°C. Perbanyak minum air putih.")
                        if any(s in added_symptoms for s in ["nyeri perut", "kembung"]):
                            symptom_advices.append("🤢 **Gangguan Perut:** Hindari makanan pedas, asam, kopi, soda. Jangan langsung berbaring setelah makan.")
                        if any(s in added_symptoms for s in ["diare", "muntah", "mual"]):
                            symptom_advices.append("💧 **Diare/Mual:** Cegah dehidrasi dengan oralit. Hindari susu sementara, makan porsi kecil.")
                        if any(s in added_symptoms for s in ["sembelit"]):
                            symptom_advices.append("🚽 **Sembelit:** Perbanyak air 2.5L, konsumsi pepaya, gunakan bangku kecil saat BAB.")
                        if any(s in added_symptoms for s in ["wasir"]):
                            symptom_advices.append("🩸 **Wasir:** Rendam air hangat (Sitz Bath) 15 menit, jangan mengejan berlebihan.")
                        if any(s in added_symptoms for s in ["sesak napas"]):
                            symptom_advices.append("🚨 **Sesak Napas:** Longgarkan pakaian, duduk setengah bersandar. Jika disertai nyeri dada atau bibir membiru, segera ke IGD!")
                        if any(s in added_symptoms for s in ["pusing"]):
                            symptom_advices.append("🧠 **Pusing:** Istirahat di tempat redup, kurangi gadget. Perhatikan asupan air dan makanan.")
                        if any(s in added_symptoms for s in ["pingsan"]):
                            symptom_advices.append("💫 **Hampir Pingsan:** Baringkan, kaki lebih tinggi dari jantung. Bangkit perlahan.")
                        if any(s in added_symptoms for s in ["insomnia"]):
                            symptom_advices.append("🌙 **Insomnia:** Matikan lampu 30 menit sebelum tidur, hindari layar, jangan makan berat terlalu malam.")
                        if any(s in added_symptoms for s in ["kesemutan"]):
                            symptom_advices.append("⚡ **Kesemutan:** Luruskan anggota tubuh, hindari menekuk lama. Bila sering terjadi, cek vitamin neurotropik.")
                        if any(s in added_symptoms for s in ["batuk", "pilek", "iritasi tenggorokan"]):
                            symptom_advices.append("😷 **Saluran Napas:** Uap air hangat + minyak kayu putih, kumur air garam. Istirahat cukup.")
                        if any(s in added_symptoms for s in ["sakit telinga"]):
                            symptom_advices.append("👂 **Telinga:** Jangan dikorek. Kompres hangat luar, hindari air masuk.")
                        if any(s in added_symptoms for s in ["nyeri haid"]):
                            symptom_advices.append("🌸 **Nyeri Haid:** Kompres hangat perut bawah, lakukan peregangan ringan.")
                        if any(s in added_symptoms for s in ["sakit gigi"]):
                            symptom_advices.append("🦷 **Sakit Gigi:** Kumur air garam hangat, kompres dingin di pipi jika bengkak. Segera ke dokter gigi.")
                        if any(s in added_symptoms for s in ["iritasi mulut"]):
                            symptom_advices.append("👅 **Sariawan/Panas Dalam:** Oleskan madu, hindari pedas/asam. Cukupi vitamin C dan zinc.")
                        if any(s in added_symptoms for s in ["mata kabur"]):
                            symptom_advices.append("👁️ **Mata Lelah:** Istirahatkan mata tiap 20 menit, lihat objek jauh.")
                        if any(s in added_symptoms for s in ["gatal", "ruam"]):
                            symptom_advices.append("🧼 **Gatal/Ruam:** Jangan digaruk, oleskan kalamin. Hindari pemicu alergi.")
                        if any(s in added_symptoms for s in ["lemas"]):
                            symptom_advices.append("🔋 **Lemas/Burnout:** Makan teratur dengan karbohidrat kompleks, tidur cukup. Cek Hb jika berkepanjangan.")
                        if any(s in added_symptoms for s in ["nyeri otot", "nyeri sendi"]):
                            symptom_advices.append("💪 **Nyeri Otot/Sendi:** Istirahatkan, kompres es jika baru terjadi. Hindari pijatan keras pada bengkak.")
                        if any(s in added_symptoms for s in ["anyang-anyangan"]):
                            symptom_advices.append("🚽 **ISK:** Banyak minum air putih >3L/hari untuk membilas bakteri, jangan tahan pipis.")
                        
                        # Sinyal bahaya kombinasi
                        if "demam" in self.detected_symptoms and "leher kaku" in self.detected_symptoms:
                            symptom_advices.append("🚨 **WASPADA MENINGITIS!** Demam + leher kaku = tanda infeksi selaput otak. Segera ke IGD!")
                        if "nyeri dada" in self.detected_symptoms and "sesak napas" in self.detected_symptoms:
                            symptom_advices.append("❤️‍🔥 **DARURAT JANTUNG:** Nyeri dada + sesak napas perlu evaluasi segera. Ke IGD!")
                        if "kejang" in self.detected_symptoms:
                            symptom_advices.append("⚡ **KEJANG:** Amankan dari benda tajam, miringkan tubuh, jangan tahan gerakan. Setelah reda, bawa ke RS.")
                        if "mimisan" in self.detected_symptoms and "nyeri perut" in self.detected_symptoms:
                            symptom_advices.append("🩸 **Kombinasi Mimisan & Nyeri Perut:** Bisa mengarah ke DHF/gangguan trombosit. Periksakan darah segera.")
                        
                        # Susun pesan akhir
                        response_text = greeting + intro
                        if symptom_advices:
                            response_text += f"\n\n📌 **Saran cepat untuk Anda:**\n" + "\n".join(symptom_advices)
                        
                        response_text += "\n\n"
                        
                        if suggestions:
                            response_text += "Untuk mempertajam analisis, apakah Anda juga mengalami:\n"
                            for s in suggestions:
                                response_text += f"- {s.capitalize()}\n"
                            response_text += "\nKetik gejala tambahan jika ada. Jika dirasa sudah lengkap, ketik **'proses'**."
                        else:
                            response_text += "Semua gejala sudah tercatat dengan baik. Silakan ketik **'proses'** untuk melihat analisis diagnosis."
                        
                        self.response = response_text
                    else:
                        self.response = (
                            "Gejala tersebut sudah tercatat sebelumnya. 😊\n\n"
                            "Apakah masih ada keluhan lain yang ingin ditambahkan? Jika sudah cukup, ketik **'proses'**."
                        )
                else:
                    self.response = (
                        "Maaf, saya belum bisa menangkap keluhan medis yang jelas dari kalimat Anda. Coba sebutkan dengan kata kunci spesifik, misalnya: *nyeri dada, pusing, pegal, susah tidur*, dsb.\n\n"
                        "Atau jika sudah selesai, ketik **'proses'**."
                    )
            return

        elif self.state == State.RESULT:
            self.response = "Sesi skrining gejala ini telah ditutup. Jika Anda ingin berkonsultasi mengenai keluhan medis baru, silakan ketik perintah **'reset'**. Tetap jaga kesehatan dan lekas sembuh! 🌿"
            return