#!/usr/bin/env python3
"""
BELAJAR_ONLINE — CasperAI mengumpulkan data dari internet SENDIRIAN! 🌐

Fungsi: mengambil artikel Wikipedia (Indonesia/Inggris) tentang topik apa pun,
menyimpannya ke data_online/, lalu bisa digabung jadi korpus untuk dilatih.

Cara pakai:
  1. Ambil data per topik:
       python3 belajar_online.py id "Nasi Padang" "Rumah Gadang" "Danau Toba"
       python3 belajar_online.py en "Quantum computing" "Black hole"
  2. Gabung semua data yang sudah diambil jadi satu korpus:
       python3 belajar_online.py gabung
     -> menghasilkan korpus_online.txt
  3. Latih otaknya (biar ilmunya nempel):
       python3 train_besar.py korpus_online.txt spesialis_online.brain 120

Catatan: pakai User-Agent sopan + jeda + retry otomatis kalau kena rate-limit.
"""
import sys, os, time, json, re, urllib.request, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data_online")
os.makedirs(DATA, exist_ok=True)
UA = "CasperAIBot/1.0 (educational self-learning project by genzxseventh; contact: GenzPx@users.noreply.github.com)"

def ambil_artikel(judul, lang="id", tries=5):
    api = f"https://{lang}.wikipedia.org/w/api.php"
    params = {"action":"query","prop":"extracts","explaintext":"1",
              "format":"json","redirects":"1","titles":judul}
    url = api + "?" + urllib.parse.urlencode(params)
    for a in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=40) as r:
                d = json.load(r)
            for p in d["query"]["pages"].values():
                return p.get("title", judul), p.get("extract", "")
            return judul, ""
        except Exception as e:
            if "429" in str(e) or "too many" in str(e).lower():
                wait = 8 * (a + 1)
                print(f"  ⏳ rate-limit, istirahat {wait}s...", flush=True)
                time.sleep(wait)
                continue
            time.sleep(3)
    return judul, ""

def slugify(s):
    return re.sub(r"[^\w]+", "_", s.lower()).strip("_")

def cmd_ambil(lang, judul_list):
    total = 0
    for i, judul in enumerate(judul_list, 1):
        title, ex = ambil_artikel(judul, lang)
        path = os.path.join(DATA, f"{lang}_{slugify(judul)}.txt")
        if ex:
            header = f"judul: {title}\nsumber: wikipedia {lang}\n\n"
            open(path, "w", encoding="utf-8").write(header + ex)
            total += len(ex)
            print(f"[{i}/{len(judul_list)}] ✅ {title}: {len(ex):,} char -> {os.path.basename(path)}")
        else:
            print(f"[{i}/{len(judul_list)}] ❌ {judul}: tidak ditemukan")
        time.sleep(2.5)
    print(f"\n🎒 selesai! total {total:,} char terkumpul di data_online/")

def cmd_gabung():
    files = sorted(f for f in os.listdir(DATA) if f.endswith(".txt"))
    if not files:
        print("belum ada data. ambil dulu: python3 belajar_online.py id \"topik\"")
        return
    blok = []
    for f in files:
        blok.append(open(os.path.join(DATA, f), encoding="utf-8").read())
    out = os.path.join(HERE, "korpus_online.txt")
    open(out, "w", encoding="utf-8").write("\n\n".join(blok))
    print(f"📚 {len(files)} artikel digabung -> korpus_online.txt ({sum(len(b) for b in blok):,} char)")
    print("selanjutnya latih otaknya:")
    print("  python3 train_besar.py korpus_online.txt spesialis_online.brain 120")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(0)
    if sys.argv[1] == "gabung":
        cmd_gabung()
    elif sys.argv[1] in ("id", "en"):
        cmd_ambil(sys.argv[1], sys.argv[2:])
    else:
        print("format: python3 belajar_online.py id|en \"topik1\" \"topik2\" ...")
        print("        python3 belajar_online.py gabung")
