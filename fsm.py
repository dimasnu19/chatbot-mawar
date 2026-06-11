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
        Mengubah bahasa informal, singkatan, slang, dan typo umum masyarakat
        menjadi istilah baku yang dapat dikenali oleh MedicalEngine.
        """
        text = text.lower().strip()

        # 1. Kamus substitusi kata per kata (menggunakan regex kata utuh biar aman)
        slang_words = {
            r"\bgw\b|\bgue\b|\bgua\b|\baku\b|\bakk\b|\bnyong\b": "saya",
            r"\bga\b|\bgak\b|\bngga\b|\bnggak\b|\bndak\b|\bkaga\b|\bkagak\b|\btak\b": "tidak",
            r"\bbgt\b|\bbanget\b|\bpisan\b|\bpol\b": "sekali",
            r"\bngerasa\b|\bngerasain\b|\bberasa\b": "merasa",
            r"\bpala\b|\bkoplo\b": "kepala",
            r"\bpuyeng\b|\bmumet\b|\bkliyengan\b|\bpening\b": "pusing",
            r"\bsumeng\b|\bmeriang\b|\banget\b|\bbadan panas\b": "demam",
            r"\bmeler\b|\bingusan\b|\bflu\b|\bbersin2\b|\bbersin\b": "pilek",
            r"\bbatok\b|\buhuk\b|\bbatuk2\b": "batuk",
            r"\benek\b|\bnek\b|\buek\b|\bpengen muntah\b": "mual",
            r"\bmules\b|\bmencret\b|\bberak\b|\bboker\b|\bmencret2\b": "diare",
            r"\bmelilit\b|\bmules bgt\b": "nyeri perut",
            r"\bgatel\b|\bgatel2\b": "gatal",
            r"\bmerah2\b|\bbentol\b|\bbintik\b": "ruam",
            r"\bnafas sesek\b|\bengap\b|\bnyesek\b": "sesak napas",
            r"\bkrn\b|\bkenapa\b|\bnyari\b": "karena",
            r"\bbro\b|\bcuy\b|\bsis\b|\bgan\b|\bndra\b|\bnih\b|\btuh\b|\bloh\b|\bdeh\b": "" # hapus pemanis kalimat
        }

        for pattern, replacement in slang_words.items():
            text = re.sub(pattern, replacement, text)

        # 2. Kamus substitusi frasa/kalimat gabungan
        phrase_replacements = {
            "ga enak badan": "demam",
            "tidak enak badan": "demam",
            "kurang fit": "demam",
            "badan drop": "demam",
            "sakit perut": "nyeri perut",
            "sakit kepala": "pusing",
            "tenggorokan sakit": "iritasi tenggorokan",
            "sakit tenggorokan": "iritasi tenggorokan",
            "tenggorokan gatal": "iritasi tenggorokan",
            "gatal tenggorokan": "iritasi tenggorokan"
        }

        for phrase, replacement in phrase_replacements.items():
            text = text.replace(phrase, replacement)

        # Membersihkan spasi ganda akibat penghapusan kata pemanis
        text = re.sub(r'\s+', ' ', text).strip()
        return text

    def step(self, user_input):
        raw_input = user_input.strip()
        user_input_lower = raw_input.lower()
        
        # Jalankan proses normalisasi teks informal ke formal
        normalized_input = self._normalize_input(raw_input)
        
        # Ekstraksi Intent berdasarkan teks yang sudah dinormalisasi
        intent = self.engine.detect_intent(normalized_input)

        # ==========================================
        # 1. GLOBAL COMMAND: RESET
        # ==========================================
        if intent == "RESET" or "reset" in user_input_lower:
            self.__init__()
            self.response = "Baik, memori konsultasi sebelumnya sudah saya bersihkan. Mari kita mulai dari awal. Ada keluhan kesehatan atau pertanyaan yang bisa saya bantu hari ini?"
            return

        # ==========================================
        # 2. INTERCEPTOR: SAPAAN & PERTANYAAN UMUM
        # ==========================================
        if any(word in user_input_lower for word in ["halo", "hai", "selamat pagi", "selamat siang", "selamat malam", "p", "assalamualaikum"]) and len(user_input_lower.split()) <= 3:
            self.response = "Halo! 👋 Saya adalah Asisten AI dari Ngobat.In. Anda bisa menanyakan seputar website ini, atau langsung ceritakan keluhan yang sedang Anda rasakan (misalnya: *'gw ngerasa meriang dan puyeng nih'*). Apa yang bisa saya bantu?"
            return

        if any(word in user_input_lower for word in ["ngobat.in", "website ini", "aplikasi ini", "buat apa", "fungsi"]):
            self.response = (
                "**Ngobat.In** adalah platform edukasi kesehatan terpadu. Di sini Anda bisa mengeksplorasi informasi organ tubuh, "
                "mencari tahu fungsi berbagai obat di menu 'Penjelasan Obat', membaca 'Tips Kesehatan', serta melakukan skrining gejala penyakit awal melalui saya. "
                "\n\nApakah ada gejala penyakit yang ingin Anda konsultasikan saat ini?"
            )
            return
            
        if user_input_lower.startswith(("apa itu", "bagaimana cara", "kenapa", "penyebab", "obat untuk")):
            self.response = (
                "Sebagai asisten AI, fokus utama saya adalah membantu memetakan gejala yang Anda alami saat ini untuk mencari kemungkinan penyakitnya.\n\n"
                "Untuk informasi detail mengenai obat dan pola hidup, Anda bisa langsung mengecek menu **Penjelasan Obat** and **Tips Kesehatan** di atas. \n\n"
                "Namun, jika Anda sedang merasa sakit, silakan sebutkan gejalanya (contoh: *'perut saya mual dan kepala pusing'*) agar kita bisa mulai menganalisis kondisi Anda. 🏥"
            )
            return

        # ==========================================
        # 3. ALUR KONSULTASI GEJALA (FSM)
        # ==========================================
        if self.state == State.IDLE:
            self.state = State.CONSULTING
            self.response = (
                "Waduh, badannya lagi kerasa kurang fit ya? Kasih tahu saya apa saja yang dirasakan biar saya bantu analisis awal.\n\n"
                "Silakan ceritakan senatural mungkin, contohnya:\n"
                "- *'kepala pusing banget bro ama meler nih'* 🤧\n"
                "- *'perut melilit ngerasa pengen muntah'* 🤢\n\n"
                "Ketik keluhan Anda di bawah ini, ya."
            )
            return

        elif self.state == State.CONSULTING:
            if intent == "FINISH" or "proses" in user_input_lower:
                if not self.detected_symptoms:
                    self.response = (
                        "Maaf, saya belum berhasil menangkap gejala medis yang spesifik dari cerita Anda. Bisa tolong sebutkan bagian mana yang sakit atau keluhan apa yang paling mengganggu?\n\n"
                        "Atau ketik **'reset'** jika Anda ingin mengulangi dari awal."
                    )
                else:
                    diagnosis = self.engine.diagnose(self.detected_symptoms)
                    self.state = State.RESULT
                    
                    if diagnosis:
                        self.response = (
                            f"**Hasil Analisis Gejala Awal:**\n"
                            f"Berdasarkan keluhan yang Anda sebutkan, ada indikasi kemungkinan Anda mengalami: **{diagnosis['name']}**.\n\n"
                            f"📖 **Penjelasan Singkat:**\n{diagnosis['desc']}\n\n"
                            f"💊 **Saran Penanganan Awal:**\n{diagnosis['medicine']}\n\n"
                            f"⚠️ **Catatan Penting AI:**\n"
                            f"Saya adalah kecerdasan buatan, bukan dokter sungguhan. Analisis ini hanya bersifat referensi awal. Jika kondisi Anda memburuk atau tidak membaik, **segera periksakan diri ke dokter atau fasilitas kesehatan terdekat**.\n\n"
                            f"*(Ketik **'reset'** jika Anda ingin mengecek gejala yang lain)*"
                        )
                    else:
                        self.response = (
                            "Hmm, kombinasi gejala yang Anda sebutkan cukup kompleks dan belum bisa saya temukan kecocokannya secara presisi di database kami.\n\n"
                            "Saya sangat menyarankan Anda untuk berkonsultasi langsung dengan dokter agar mendapatkan pemeriksaan fisik yang akurat. Ketik **'reset'** untuk mencoba gejala lain."
                        )
                        
            else:
                # Menggunakan text hasil normalisasi untuk diekstrak gejalanya oleh Engine
                new_symptoms = self.engine.extract_symptoms(normalized_input)
                
                if new_symptoms:
                    added_symptoms = []
                    for symp in new_symptoms:
                        if symp not in self.detected_symptoms:
                            self.detected_symptoms.append(symp)
                            added_symptoms.append(symp)
                    
                    if added_symptoms:
                        suggestions = self.engine.get_suggested_symptoms(self.detected_symptoms)
                        
                        response_text = f"Oke, saya catat keluhannya: **{', '.join(added_symptoms).capitalize()}**.\n\n"
                        
                        if suggestions:
                            response_text += "Untuk memastikan analisisnya lebih tepat, apakah Anda juga merasakan tanda-tanda ini?\n"
                            for s in suggestions:
                                response_text += f"- {s.capitalize()}\n"
                                
                            response_text += (
                                "\nKalau iya, langsung ketikkan saja keluhannya. "
                                "Tapi kalau dirasa sudah cukup, ketik **'proses'** untuk melihat kesimpulannya."
                            )
                        else:
                            response_text += (
                                "Gejala yang Anda sampaikan sudah cukup spesifik.\n\n"
                                "Silakan ketik **'proses'** untuk melihat hasil analisanya, ya!"
                            )
                        
                        self.response = response_text
                        
                    else:
                        self.response = (
                            "Gejala itu sudah saya masukkan ke daftar catatan sebelumnya. 😊\n\n"
                            "Ada tambahan keluhan lain? Jika sudah semua, ketik **'proses'**."
                        )
                        
                else:
                    self.response = (
                        "Aduh, saya agak kurang menangkap keluhan medisnya. Bisa sebutkan gejala tubuh yang lebih umum? \n"
                        "Misalnya seperti: *Demam*, *Mual*, *Batuk*, *Pusing*, *Pilek*, atau *Diare*.\n\n"
                        "Atau jika Anda merasa gejalanya sudah lengkap dicatat sebelumnya, ketik **'proses'**."
                    )
            return

        elif self.state == State.RESULT:
            self.response = "Sesi konsultasi untuk gejala ini sudah selesai. Jika ada keluhan baru yang dirasakan, silakan ketik **'reset'** untuk mengulang analisis gres. Semoga sehat selalu! 🌿"
            return