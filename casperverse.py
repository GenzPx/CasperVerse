#!/usr/bin/env python3
"""
CASPERVERSE — CASPER-C dengan 11 otak spesialis + router konteks.
Dia milih pakar yang tepat berdasarkan topik omongan lu.
Pakai: python3 casperverse.py
"""
import os, sys, re, time as _time

try:
    import numpy as np
except ImportError:
    print("numpy belum ada. jalanin dulu:  pip install numpy"); sys.exit(1)
import pickle

HERE = os.path.dirname(os.path.abspath(__file__))
L = 8
rng = np.random.default_rng()

PAKAR = {
 "catur":    ("♟️  CASPER-GM (grandmaster catur)", "spesialis_catur.brain",
              ["catur","chess","skak","checkmate","opening","gambit","sicilian","ruy lopez",
               "bidak","pion","menteri","benteng","grandmaster","e4","d4","c5"]),
 "kode":     ("💻 CASPER-CODE (programmer)", "spesialis_kode.brain",
              ["kode","code","coding","ngoding","python","def ","function","fungsi","program",
               "script","error","bug","compile","variabel","loop","algoritma"]),
 "hack":     ("🖤 CASPER-HACK (hacker etis)", "spesialis_hack.brain",
              ["hack","hacker","terminal","ssh","server","root","firewall","keamanan","siber",
               "cyber","password","jaringan","port","sudo","bash","linux","enkripsi","vpn"]),
 "wibu":     ("🎌 CASPER-WIBU (otaku)", "spesialis_wibu.brain",
              ["anime","manga","wibu","otaku","naruto","one piece","waifu","senpai","cosplay",
               "light novel","vtuber","shonen","seiyuu","manga"]),
 "sains":    ("🔬 CASPER-SAINS (ilmuwan)", "spesialis_sains.brain",
              ["sains","fisika","kimia","biologi","quantum","kuantum","relativitas","atom",
               "evolusi","genetik","dna","neuron","galaksi","alam semesta","lubang hitam",
               "black hole","gravitasi","termodinamika","big bang","ilmu"]),
 "horor":    ("👻 CASPER-HOROR (pencerita gelap)", "spesialis_horor.brain",
              ["horor","horror","hantu","seram","menyeramkan","kuntilanak","pocong","genderuwo",
               "tuyul","jelangkung","kuyang","penampakan","creepy","ghost","haunted","misteri"]),
 "rp":       ("🎭 CASPER-RP (aktor roleplay)", "spesialis_rp.brain",
              ["roleplay","rp ","berperan","jadi kai","jadi rara","jadi surya","jadi arga",
               "jadi nala","jadi bara","karakter","persona","kai ","rara ","prof. surya",
               "detektif arga","nala ","bara ","kartu karakter"]),
 "inggris":  ("🌍 CASPER-ENGLISH (general knowledge)", "spesialis_inggris.brain",
              ["english","in english","tell me about","what is","what are","explain",
               "why do","how does","who was","describe","history of"]),
 "curhat":   ("🫂 CASPER-CURHAT (pendengar setia)", "token_curhat.brain",
              ["curhat","sedih","galau","capek","cape","lelah","kesel","kecewa","patah hati",
               "kesepian","cemas","overthinking","nangis","stres","stress","putus asa",
               "hampa","nggak semangat","gak semangat","menyerah","sendirian"]),
 "bola":     ("⚽ CASPER-BOLA (komentator)", "spesialis_bola.brain",
              ["bola","sepak bola","sepakbola","timnas","liga","gol","messi","ronaldo",
               "persija","persib","piala dunia","premier league","klub","pertandingan",
               "striker","kiper","wasit","liga 1"]),
 "chef":     ("🍳 CASPER-CHEF (koki)", "spesialis_chef.brain",
              ["masak","resep","makanan","nasi goreng","rendang","sate","bakso","kuliner",
               "dapur","bumbu","laper","lapar","sarapan","makan malam","makan siang",
               "gado-gado","soto","sambal","pempek","gudeg"]),
 "sejarah":  ("📜 CASPER-SEJARAH (ahli sejarah)", "spesialis_sejarah.brain",
              ["sejarah","kerajaan","majapahit","sriwijaya","kemerdekaan","penjajahan",
               "voc","borobudur","diponegoro","sumpah pemuda","mataram","kolonial"]),
 "game":     ("🎮 CASPER-GAME (gamer)", "spesialis_game.brain",
              ["game","gaming","mabar","mobile legends","esports","push rank","ngegame",
               "konsol","nintendo","playstation","dota","pubg","ml ","main game"]),
 "musik":    ("🎵 CASPER-MUSIK (musisi)", "spesialis_musik.brain",
              ["musik","lagu","gitar","piano","drum","dangdut","penyanyi","band",
               "orkestra","alat musik","nyanyi","konser"]),
 "film":     ("🎬 CASPER-FILM (sinefil)", "spesialis_film.brain",
              ["film","bioskop","sutradara","aktor","aktris","animasi","genre",
               "nonton","layar lebar","sinema"]),
 "sehat":    ("💪 CASPER-SEHAT (sahabat sehat)", "spesialis_sehat.brain",
              ["sehat","kesehatan","gizi","olahraga","vitamin","tidur","diet",
               "imunisasi","dokter","obat","sakit","nutrisi"]),
 "hewan":    ("🐾 CASPER-HEWAN (pencinta satwa)", "spesialis_hewan.brain",
              ["hewan","binatang","kucing","anjing","burung","harimau","gajah",
               "komodo","peliharaan","satwa"]),
 "otomotif": ("🏍️ CASPER-OTOMOTIF (anak motor)", "spesialis_otomotif.brain",
              ["motor","mobil","otomotif","mesin","honda","yamaha","transmisi",
               "knalpot","bensin","servis","kampas rem"]),
 "gadget":   ("📱 CASPER-GADGET (tech reviewer)", "spesialis_gadget.brain",
              ["hp","handphone","gadget","smartphone","android","aplikasi",
               "sosmed","baterai","charger","layar hp","kuota"]),
 "motivasi": ("🔥 CASPER-MOTIVASI (coach semangat)", "token_motivasi.brain",
              ["motivasi","semangat","inspirasi","bangkit",
               "motivasiin","nyemangatin"]),
 "dongeng":  ("📖 CASPER-DONGENG (pendongeng)", "spesialis_dongeng.brain",
              ["dongeng","cerita rakyat","legenda","malin kundang","timun mas",
               "sangkuriang","pesan moral","kancil","roro jonggrang","si pitung"]),
 "matematika":("🔢 CASPER-MATEMATIKA (ahli hitung)", "spesialis_matematika.brain",
              ["matematika","hitung","tambah","kurang","kali","bagi","perkalian",
               "rumus","rata-rata","pecahan","persen","berapa hasil"]),
 "fakta":    ("🤯 CASPER-FAKTA (ensiklopedi unik)", "spesialis_fakta.brain",
              ["fakta","tahukah kamu","fakta unik","unik banget"]),
 "kamus":    ("🗣️ CASPER-KAMUS (guru bahasa)", "spesialis_kamus.brain",
              ["bahasa inggrisnya","bahasa inggris dari","artinya apa","translate",
               "terjemahin","kosakata","english nya"]),
 "uang":     ("💰 CASPER-UANG (penasehat finansial)", "spesialis_uang.brain",
              ["uang","nabung","menabung","investasi","gaji","inflasi","keuangan",
               "dana darurat","paylater","saham","reksadana"]),
 "logika":   ("🧩 CASPER-LOGIKA (master teka-teki)", "spesialis_logika.brain",
              ["logika","teka-teki","tebak logika","asah otak","tes logika"]),
 "wisata":   ("🏝️ CASPER-WISATA (pemandu jalan)", "spesialis_wisata.brain",
              ["wisata","liburan","traveling","bali","bromo","prambanan","pantai",
               "destinasi","yogyakarta","bandung","danau toba","kawah ijen"]),
 "badminton":("🏸 CASPER-BADMINTON (fans sejati)", "spesialis_badminton.brain",
              ["badminton","bulu tangkis","bulutangkis","smash","susi susanti",
               "taufik","all england","thomas cup","jonatan","ginting","raket","kok"]),
 "peribahasa":("📜 CASPER-PERIBAHASA (penjaga budaya)", "spesialis_peribahasa.brain",
              ["peribahasa","pepatah","perumpamaan","pameo","habis manis sepah dibuang",
               "sedia payung","sedikit demi sedikit","tong kosong","besar pasak",
               "nasi sudah menjadi bubur","bagai air di daun talas","malu bertanya",
               "bersatu kita teguh","alah bisa karena biasa","katak dalam tempurung",
               "tak ada gading","kecil-kecil cabai rawit","jauh di mata","berakit-rakit"]),
 "kutipan": ("💬 CASPER-KUTIPAN (kolektor kata bijak)", "spesialis_kutipan.brain",
              ["kutipan","quotes","kata bijak","kata soekarno","kata einstein",
               "kata kartini","kata mutiara"]),
 "psikologi":("🧠 CASPER-PSIKOLOGI (pengamat jiwa)", "spesialis_psikologi.brain",
              ["psikologi","overthinking","minder","move on","perasaan","mood",
               "mental","stres pikiran","kepribadian"]),
 "belajar": ("📚 CASPER-BELAJAR (coach belajar)", "spesialis_belajar.brain",
              ["belajar","ujian","pomodoro","menghafal","tugas sekolah","uts","uas",
               "skripsi","konsentrasi"]),
 "tanaman": ("🌱 CASPER-TANAMAN (tukang kebun)", "spesialis_tanaman.brain",
              ["tanaman","kaktus","anggrek","bonsai","hidroponik","berkebun",
               "pupuk","kompos","menanam","kebun"]),
 "identitas":("🪪 CASPER-IDENTITAS (jati diri)", "token_identitas.brain",
              ["kamu siapa","siapa kamu","siapa yang bikin","siapa pencipta","yang menciptakan",
               "siapa orang tuamu","siapa namamu","siapa nama kamu","casperverse","genzxseventh",
               "siapa ayahmu","siapa bapakmu","penciptamu","creator kamu","kenalkan dirimu",
               "dari mana kamu berasal"]),
 "bicara":   ("🗨️ CASPER-BICARA (juru bicara fasih)", "token_bicara.brain",
              ["ngobrol","cerita dong","temenin","basa-basi","sapa","obrolan",
               "kamu siapa","apa kabar","lagi ngapain","menurut kamu"]),
 "online":   ("🧭 CASPER-ONLINE (penjelajah internet)", "spesialis_online.brain",
              ["large language model","llm","neural network","machine learning","nlp",
               "natural language","kecerdasan buatan","apa itu ai","ai itu apa",
               "kecak","sasando","keraton yogyakarta","keraton"]),
 "jokes":    ("😂 CASPER-JOKES (pelawak)", "token_jokes.brain",
              ["joke","jokes","lucu","tebak","receh","humor","ngakak","wkwk","haha",
               "bapak-bapak","dark joke","hibur","lawak"]),
 "prosa":    ("✒️  CASPER-PROSA (novelis & cocoklog)", "spesialis_prosa.brain",
              ["puisi","prosa","sastra","novel","menulis","hujan","senja","makna","teori",
               "konspirasi","cocoklogi","simulasi","fermi","renungan","quote"]),
 "gombal":   ("🌹 CASPER-GOMBAL (bucin)", "token_gombal.brain",
              ["gombal","pantun","sayang","cinta","pacar","gebetan","cantik","ganteng",
               "naksir","jodoh","rindu","pdkt","baper"]),
 "filsafat": ("🤔 CASPER-FILSAFAT (pemikir)", "spesialis_filsafat.brain",
              ["filsafat","filosofi","stoik","eksistensial","absurd","nihil","etika","moral",
               "makna hidup","free will","kehendak bebas","kebahagiaan","arti hidup",
               "kesadaran","kematian"]),
 "indo":     ("🇮🇩 CASPER-INDO (umum)", "spesialis_indo.brain", []),
}

OTAK_FILE = os.path.join(HERE, "otak_casper.brain")
_semua_otak = None
def _muat_semua():
    global _semua_otak
    if _semua_otak is None:
        if not os.path.exists(OTAK_FILE):
            return {}
        _semua_otak = pickle.load(open(OTAK_FILE, "rb"))
    return _semua_otak

otak = {}
def load(nama):
    if nama not in otak:
        semua = _muat_semua()
        if nama not in semua:
            return None
        otak[nama] = semua[nama]
    return otak[nama]

def hitung(teks):
    """kalkulator internal casper — tool use, kayak LLM pro"""
    m = re.search(r"(\d+(?:[.,]\d+)?)\s*([x×:/*+\-])\s*(\d+(?:[.,]\d+)?)", teks)
    if not m: return None
    a, op, b = m.groups()
    a = float(a.replace(",", ".")); b = float(b.replace(",", "."))
    opmap = {"x":"*","×":"*",":":"/","/":"/","+":"+","-":"-"}
    try:
        if opmap[op] == "/" and b == 0: return None
        hasil = eval(f"{a}{opmap[op]}{b}", {"__builtins__": {}}, {})
    except Exception:
        return None
    if hasil == int(hasil): hasil = int(hasil)
    return f"{a:g} {op} {b:g} = {hasil}"

def _kw(k, t):
    # kata pendek harus cocok sebagai kata utuh (biar "bali" nggak nyangkut di "gombalin")
    ks = k.strip()
    if len(ks) <= 4:
        return re.search(r"\b" + re.escape(ks) + r"\b", t) is not None
    return ks in t

PERIBAHASA_POPULER = ["habis manis sepah dibuang","sedia payung sebelum hujan",
 "sedikit demi sedikit","tong kosong nyaring","besar pasak daripada tiang",
 "nasi sudah menjadi bubur","bagai air di daun talas","malu bertanya sesat",
 "bersatu kita teguh","alah bisa karena biasa","katak dalam tempurung",
 "tak ada gading yang tak retak","kecil-kecil cabai rawit","jauh di mata dekat di hati",
 "berakit-rakit ke hulu","bagai pinang dibelah dua","sambil menyelam minum air",
 "di mana bumi dipijak","gajah mati meninggalkan gading","ada gula ada semut",
 "kalah jadi abu menang jadi arang","tak kenal maka tak sayang"]

def route(teks):
    t = teks.lower()
    for p in PERIBAHASA_POPULER:
        if p in t:
            return "peribahasa"
    skor = {}
    for nama, (_,_,kws) in PAKAR.items():
        skor[nama] = sum(1 for k in kws if _kw(k, t))
    # deteksi hitungan matematika: angka + operator + angka
    if re.search(r"\d\s*[x×:/*+\-]\s*\d", t) or re.search(r"\d\s*=\s*$", t):
        skor["matematika"] = skor.get("matematika",0) + 2
    terbaik = max(skor.values())
    if terbaik == 0:
        return "bicara"  # suara fasih sebagai default
    for nama in PAKAR:  # urutan PAKAR = prioritas saat seri
        if skor[nama] == terbaik:
            return nama

# format percakapan tiap otak Q&A (biar jawab langsung, nggak nge-echo ngawur)
SEEDS = {
 "identitas": "tanya: {q}\njawab: ",
 "bicara":    "tanya: {q}\njawab: ",
 "curhat":    "curhat: {q}.\ncasper-c: ",
 "uang":      "tanya keuangan: {q}?\njawab: ",
 "psikologi": "tanya psikologi: {q}?\njawab: ",
 "motivasi":  "curhat motivasi: {q}.\nsemangat: ",
 "peribahasa":"tanya: {q}\njawab: ",
 "logika":    "soal logika: {q}\njawaban: ",
 "kamus":     "kosakata: bahasa inggris dari {q} adalah ",
 "fakta":     "tahukah kamu? ",
 "belajar":   "tips belajar: ",
 "kutipan":   "kutipan soekarno: ",
}

def generate(brain, seed, n=300, temp=0.5):
    W1,b1,W2,b2,W3,b3,vocab,ivocab,Lb = brain
    V = len(vocab); unk = vocab.get(" ", 0)
    ids = [vocab.get(c, unk) for c in seed[-Lb:].rjust(Lb)]
    out = []
    for _ in range(n):
        X = np.zeros((Lb,V),dtype=np.float32); X[np.arange(Lb), ids[-Lb:]] = 1.0
        h1 = np.tanh(X.reshape(1,-1)@W1+b1); h2 = np.tanh(h1@W2+b2)
        logits = (h2@W3+b3)[0]/temp
        ex = np.exp(logits-logits.max()); pr = ex/ex.sum()
        c = rng.choice(V, p=pr); out.append(ivocab[c]); ids.append(c)
    txt = seed + "".join(out)
    cut = txt.rfind(" ")
    return txt[:cut] if cut > len(seed) else txt

# ---------- generasi PER-TOKEN (word-level, kayak LLM) ----------
TTY = sys.stdout.isatty()

def _detok_step(s, tok):
    if re.match(r"^[^\w\s]+$", tok):      # tanda baca: tempel tanpa spasi
        return s + tok
    return (s + " " + tok) if s else tok

def generate_token(brain, seed_text, n_tokens=60, temp=0.5, stream=True,
                   stop_chars=(".", "?", "!"), min_stop=6):
    E,W1,b1,W2,b2,W3,b3 = brain["E"],brain["W1"],brain["b1"],brain["W2"],brain["b2"],brain["W3"],brain["b3"]
    t2i, i2t, Lb, D = brain["token2id"], brain["id2token"], brain["L"], brain["D"]
    V = len(t2i)
    stop = set(stop_chars)
    toks = re.findall(r"\w+|[^\w\s]", seed_text.lower())
    ids = [t2i.get(t, 0) for t in toks][-Lb:]
    ids = [0]*(Lb-len(ids)) + ids
    delay = 0.04 if (stream and TTY) else 0.0
    hasil, tampil = [], ""
    for i in range(n_tokens):
        ctx = np.array(ids[-Lb:], dtype=np.int32).reshape(1, Lb)
        Xemb = E[ctx].reshape(1, Lb*D)
        h1 = np.tanh(Xemb@W1+b1); h2 = np.tanh(h1@W2+b2)
        logits = (h2@W3+b3)[0]/temp
        ex = np.exp(logits-logits.max()); pr = ex/ex.sum()
        tid = int(rng.choice(V, p=pr))
        tok = i2t.get(tid, "")
        ids.append(tid); hasil.append(tok)
        if stream:
            baru = _detok_step(tampil, tok)
            print(baru[len(tampil):], end="", flush=True)
            tampil = baru
            if delay: _time.sleep(delay)
        if tok in stop and i >= min_stop: # berhenti rapi di akhir kalimat
            break
    full = "".join((t if re.match(r"^[^\w\s]+$", t) else (" "+t)) for t in hasil)
    return full.strip()

def is_token(brain):
    return isinstance(brain, dict) and brain.get("type") == "token"

BANNER = f"""
  ==============================================
     C A S P E R V E R S E  ::  1 tubuh, {len(PAKAR)} pakar
     ketik apa aja — dia otomatis pilih pakarnya
     /pakar  /pakai <nama>  /auto  /bantu  /keluar
  ==============================================
"""

def main():
    print(BANNER)
    temp, n = 0.5, 300
    paksa = None
    while True:
        try:
            user = input("lu > ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\ncasperverse ditutup. 👋"); break
        if not user: continue
        if user in ("/keluar","/exit","/quit"):
            print("casperverse ditutup. 👋"); break
        if user == "/bantu":
            print("""
  /pakar           daftar semua pakar
  /pakai <nama>    kunci ke satu pakar (misal: /pakai jokes)
  /auto            balikin ke mode router otomatis
  /suhu <angka>    kreativitas (0.3-1.0)
  /panjang <angka> panjang jawaban
"""); continue
        if user == "/pakar":
            for nama,(label,_,_) in PAKAR.items():
                print(f"  {nama:10s} {label}")
            continue
        if user.startswith("/pakai"):
            nm = user.split()[1] if len(user.split())>1 else ""
            if nm in PAKAR: paksa = nm; print(f"  terkunci ke {PAKAR[nm][0]}")
            else: print("  nama nggak dikenal. coba /pakar")
            continue
        if user == "/auto":
            paksa = None; print("  mode router otomatis aktif"); continue
        if user.startswith("/suhu"):
            try: temp = float(user.split()[1]); print(f"  suhu -> {temp}")
            except Exception: print("  format: /suhu 0.5")
            continue
        if user.startswith("/panjang"):
            try: n = int(user.split()[1]); print(f"  panjang -> {n}")
            except Exception: print("  format: /panjang 300")
            continue

        nama = paksa or route(user)
        brain = load(nama)
        if brain is None:
            print(f"  otak {PAKAR[nama][1]} belum ada di folder ini"); continue

        # --- matematika: tool use (kalkulator) dulu ---
        if nama == "matematika":
            h = hitung(user)
            if h:
                print(f"{PAKAR[nama][0]} > {h}\n"); continue

        # --- siapkan seed sesuai pakar ---
        if nama == "rp":
            chars = ["kai","rara","surya","arga","nala","bara"]
            t = user.lower()
            dipilih = next((c for c in chars if c in t), "kai")
            seed = f"user: {t}\n{dipilih}: "
        elif nama == "jokes":
            t = user.lower()
            if "dark" in t: seed = "dark joke: "
            elif "pun" in t or "english" in t: seed = "pun: "
            else: seed = "jokes bapak-bapak: "
        elif nama == "gombal":
            seed = "pantun: " if "pantun" in user.lower() else "gombalan: "
        elif nama in SEEDS:
            seed = SEEDS[nama].format(q=user.lower())
        else:
            seed = user.lower() + " "

        label = PAKAR[nama][0]
        # --- otak TOKEN: generasi per-token + streaming ngetik ---
        if is_token(brain):
            print(f"{label} > ", end="", flush=True)
            if nama == "jokes":
                generate_token(brain, seed, n_tokens=max(30, n//5), temp=temp,
                               stream=True, stop_chars=(".", "!"), min_stop=8)
            elif nama == "gombal":
                generate_token(brain, seed, n_tokens=max(30, n//5), temp=temp,
                               stream=True, stop_chars=(".",), min_stop=8)
            else:
                generate_token(brain, seed, n_tokens=max(25, n//5), temp=temp, stream=True)
            print("\n")
            continue

        # --- otak KARAKTER: generasi lama ---
        jawab = generate(brain, seed, n, temp)
        if nama == "rp":
            jawab = jawab.split("\n",1)[1] if "\n" in jawab else jawab
        elif nama in SEEDS and jawab.startswith(seed):
            jawab = jawab[len(seed):].strip()
        print(f"{label} > {jawab}\n")

if __name__ == "__main__":
    main()
