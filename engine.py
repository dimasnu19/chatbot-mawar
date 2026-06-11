import re

class MedicalEngine:
    def __init__(self):
        self.disease_db = {
            "influenza_akut": {
                "name": "Infeksi Saluran Pernapasan (Influenza Sistemik)",
                "symptoms": ["demam", "pusing", "pilek", "bersin", "myalgia"],
                "medicine": "Rekomendasi Farmasi: Paracetamol untuk regulasi demam, dan Pseudoephedrine sebagai dekongestan pengurang penyumbatan sinus.",
                "desc": "Invasi virus akut yang berfokus pada mukosa saluran pernapasan atas, memicu pelepasan pirogen ke hipotalamus yang menyebabkan peningkatan suhu basal tubuh, disertai hipersekresi lendir hidung."
            },
            "dispepsia": {
                "name": "Anomali Sekresi Asam Lambung (Sindrom Dispepsia)",
                "symptoms": ["mual", "muntah", "nyeri ulu hati", "kembung", "refluks"],
                "medicine": "Rekomendasi Farmasi: Suspensi Antasida cair sebagai lini pertama penetral asam basa, disusul Omeprazole (dengan anjuran apoteker).",
                "desc": "Adanya kerusakan keseimbangan antara produksi cairan asam lambung yang terlalu agresif dan melemahnya sistem pelindung mukosa organ pencernaan. Kondisi ini acap kali memaksa gas dan sisa asam terdorong ke arah esofagus (refluks)."
            },
            "bronkitis_ringan": {
                "name": "Iritasi Lanjutan Trakeobronkial (Gejala Batuk Khusus)",
                "symptoms": ["batuk", "tenggorokan gatal", "dahak", "serak"],
                "medicine": "Rekomendasi Farmasi: Komponen Guaifenesin bertindak optimal melarutkan dahak membandel. Sediaan Dextromethorphan diperuntukkan khusus bagi batuk kering nir-sputum.",
                "desc": "Sebuah mekanisme pertahanan tubuh (refleks fisiologis) yang diaktifkan oleh otak untuk secara paksa menembakkan patogen, debu, maupun akumulasi mukus lengket yang menghalangi pertukaran oksigen murni pada struktur paru bawah."
            },
            "radang_tenggorokan": {
                "name": "Faringitis (Radang Tenggorokan)",
                "symptoms": ["sakit menelan", "tenggorokan gatal", "serak", "demam"],
                "medicine": "Rekomendasi Farmasi: Tablet hisap antiseptik (Lozenges) untuk meredakan nyeri lokal, dikombinasikan dengan Paracetamol apabila disertai peningkatan suhu tubuh.",
                "desc": "Kondisi inflamasi pada dinding faring (tenggorokan) yang umumnya diinduksi oleh infeksi virus ringan maupun bakteri, memicu sensasi perih atau abrasi yang signifikan saat proses menelan cairan maupun makanan padat."
            },
            "gastroenteritis": {
                "name": "Gastroenteritis (Episode Diare Akut)",
                "symptoms": ["mencret", "sakit perut", "lemas", "kram"],
                "medicine": "Rekomendasi Farmasi: Prioritas utama asupan Oralit berulang untuk hidrasi seluler. Pemberian Loperamide harus dibarengi tingkat kehati-hatian ekstra agar patogen tak terperangkap.",
                "desc": "Manifestasi dari usus besar yang mengalami iritasi toksik atau keracunan flora asing, sehingga gagal menjalankan tugas esensialnya dalam menyerap kembali air ke sistem sirkulasi, memaksa pelepasan feses yang mengandung dominan air secara simultan."
            },
            "dermatitis_alergi": {
                "name": "Reaksi Histamin Kulit (Dermatitis Kontak / Urtikaria)",
                "symptoms": ["gatal", "ruam merah", "bentol", "edema"],
                "medicine": "Rekomendasi Farmasi: Sediaan topikal berupa Bedak Salicyl/Calamine guna mendinginkan permukaan dermis. Konsumsi oral Cetirizine untuk penekanan reaksi histaminikal dari dalam.",
                "desc": "Respons imunologis hipersensitif yang terjadi kala sel darah putih merilis histamin secara masif ke peredaran darah perifer kulit. Proses ini mengakibatkan pelebaran tajam pembuluh darah kecil (vasodilatasi) yang bermanifestasi berupa ruam dan gatal ekstrem."
            }
        }

        # Kamus sinonim yang diperluas secara komprehensif untuk mendeteksi variasi bahasa natural
        self.synonym_map = {
            "demam": ["demam", "panas", "meriang", "suhu badan naik", "sumeng", "menggigil", "badan panas", "badan kegerahan", "panas dingin", "suhu tubuh tinggi", "badan gerah"],
            "pusing": ["pusing", "sakit kepala", "vertigo", "kliyengan", "pening", "berkunang", "kepala sakit", "kepala nyut", "kepala berat", "kepala muter", "pusing muter", "cenat cenut"],
            "pilek": ["pilek", "hidung tersumbat", "meler", "ingusan", "bindeng", "rhinorrhea", "hidung mampet", "susah napas", "hidung berair", "flu", "hidung merah", "hidung memerah"],
            "bersin": ["bersin", "bersin-bersin", "hachi", "hidung gatal", "gatel hidung"],
            "mual": ["mual", "eneg", "ingin muntah", "perut tidak enak", "nausea", "pengen muntah", "perut mual", "mau muntah", "eneg perut"],
            "muntah": ["muntah", "muntah-muntah", "emesis", "keluar makanan", "huek", "muntah terus"],
            "nyeri ulu hati": ["nyeri ulu hati", "perih", "sakit perut atas", "lambung perih", "epigastrium", "ulu hati sakit", "dada panas", "ulu hati perih", "asam lambung naik", "dada perih"],
            "kembung": ["kembung", "begah", "perut penuh", "distensi", "gas", "perut buncit", "banyak angin", "perut bergas", "masuk angin", "perut kencang"],
            "mencret": ["mencret", "diare", "bab cair", "feses cair", "buang air terus", "bolak balik wc", "berak cair", "bab air", "murus"],
            "sakit perut": ["sakit perut", "mulas", "melilit", "kram perut", "perut melilit", "perut sakit", "perut nyeri", "mules", "lambung sakit"],
            "batuk": ["batuk", "batuk kering", "batuk berdahak", "tussis", "uhuk", "batuk-batuk", "batuk terus"],
            "tenggorokan gatal": ["tenggorokan gatal", "gatal di leher", "faring gatal", "kerongkongan gatal", "leher gatal"],
            "dahak": ["dahak", "berdahak", "riak", "lendir", "sputum", "ada dahaknya", "tenggorokan berlendir", "banyak dahak"],
            "sakit menelan": ["sakit menelan", "sakit buat nelan", "nyeri telan", "susah menelan", "susah nelen", "ga bisa nelen", "tidak bisa menelan", "tenggorokan sakit", "nyeri tenggorokan", "sakit buat makan"],
            "serak": ["suara serak", "suara habis", "suara hilang", "serak", "bindeng"],
            "gatal": ["gatal", "pruritus", "gatel", "gatal-gatal", "badan gatal", "kulit gatal", "cekit cekit"],
            "ruam merah": ["ruam", "merah-merah", "bercak merah", "eritema", "kulit memerah", "bercak di kulit", "kulit kemerahan", "kemerahan", "kulit merah"],
            "bentol": ["bentol", "biduran", "kaligata", "bentol-bentol", "bengkak di kulit", "bentol merah"],
            "lemas": ["lemas", "capek", "lesu", "letih", "fatigue", "astenia", "tidak ada tenaga", "badan lemas", "loyo", "lemes", "kurang tenaga", "lelah"]
        }

        self.re_done = r"\b(cukup|selesai|sudah|tidak ada|berikan hasil|diagnosa|periksa|cek|hasil|proses|lanjut)\b"
        self.re_reset = r"\b(reset|batal|ulang|mulai dari awal)\b"

    def clean_text(self, text):
        """
        Fungsi untuk membersihkan input pengguna dari tanda baca dan kata-kata imbuhan
        yang tidak memiliki relevansi medis (Stopwords), agar pencocokan sinonim lebih akurat.
        """
        text = text.lower()
        # Menghapus tanda baca umum
        text = re.sub(r'[^\w\s]', ' ', text)
        
        # Daftar kata yang sering diinput namun memecah struktur frasa utama
        stop_words = [
            "saya", "aku", "merasa", "rasanya", "banget", "sekali", "terasa", 
            "sih", "dong", "deh", "punya", "mengalami", "kena", "kayak", 
            "seperti", "itu", "ini", "sedang", "lagi", "agak", "lumayan"
        ]
        
        words = text.split()
        cleaned_words = [w for w in words if w not in stop_words]
        return " ".join(cleaned_words)

    def extract_symptoms(self, text):
        cleaned_input = self.clean_text(text)
        detected_symptoms = set()
        
        for standard_symptom, aliases in self.synonym_map.items():
            for alias in aliases:
                # Pencocokan pola kini dilakukan pada teks yang telah difilter
                if re.search(rf"\b{alias}\b", cleaned_input):
                    detected_symptoms.add(standard_symptom)
                    break 
        return list(detected_symptoms)

    def diagnose(self, detected_symptoms):
        if not detected_symptoms:
            return None

        best_match = None
        max_score = 0

        for key, data in self.disease_db.items():
            score = len(set(detected_symptoms).intersection(set(data["symptoms"])))
            if score > max_score:
                max_score = score
                best_match = key

        if best_match:
            return self.disease_db[best_match]
        return None

    def get_suggested_symptoms(self, detected_symptoms):
        if not detected_symptoms:
            return []

        symptom_counts = {}
        for data in self.disease_db.values():
            if set(detected_symptoms).intersection(set(data["symptoms"])):
                for symp in data["symptoms"]:
                    if symp not in detected_symptoms:
                        symptom_counts[symp] = symptom_counts.get(symp, 0) + 1

        sorted_suggestions = sorted(symptom_counts.keys(), key=lambda x: symptom_counts[x], reverse=True)
        return sorted_suggestions[:3]

    def detect_intent(self, text):
        text = text.lower()
        if re.search(self.re_reset, text):
            return "RESET"
        if re.search(self.re_done, text):
            return "FINISH"
        return "CONSULT"