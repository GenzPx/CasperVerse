#!/usr/bin/env python3
"""
BELAJAR_ONLINE — CasperAI mencari data di internet & melatih DIRINYA SENDIRI! 🌐🤖

Mode:
  cari    <id|en> "topik1" "topik2"  → cari & simpan data (belum dilatih)
  gabung                              → gabung semua data_online jadi korpus_online.txt
  belajar <id|en> "topik1" "topik2"  → LOOP MANDIRI:
        cari data → masukkan ke regular.txt → latih ulang otak → update otak_casper.brain

Casper jadi bisa nambah ilmu sendiri. Contoh:
  python3 belajar_online.py belajar id "Hukum Pidana" "Pengacara"
"""
import sys, os, time, json, re, pickle, subprocess, urllib.request, urllib.parse

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
                wait = 8*(a+1); print(f"  ⏳ rate-limit, istirahat {wait}s...", flush=True)
                time.sleep(wait); continue
            time.sleep(3)
    return judul, ""

def slugify(s):
    return re.sub(r"[^\w]+","_",s.lower()).strip("_")

def cmd_cari(lang, judul_list, kembalikan=False):
    tersimpan = []
    total = 0
    for i,judul in enumerate(judul_list,1):
        title, ex = ambil_artikel(judul, lang)
        fname = f"{lang}_{slugify(judul)}.txt"
        path = os.path.join(DATA, fname)
        if ex:
            open(path,"w",encoding="utf-8").write(f"judul: {title}\nsumber: wikipedia {lang}\n\n{ex}")
            total += len(ex); tersimpan.append((fname, title, ex))
            print(f"[{i}/{len(judul_list)}] ✅ {title}: {len(ex):,} char")
        else:
            print(f"[{i}/{len(judul_list)}] ❌ {judul}: tidak ditemukan")
        time.sleep(2.5)
    print(f"🎒 terkumpul {total:,} char di data_online/")
    return tersimpan if kembalikan else None

def cmd_gabung():
    files = sorted(f for f in os.listdir(DATA) if f.endswith(".txt"))
    if not files:
        print("belum ada data. pakai: python3 belajar_online.py cari id \"topik\""); return
    blok = [open(os.path.join(DATA,f),encoding="utf-8").read() for f in files]
    open(os.path.join(HERE,"korpus_online.txt"),"w",encoding="utf-8").write("\n\n".join(blok))
    print(f"📚 {len(files)} artikel → korpus_online.txt ({sum(len(b) for b in blok):,} char)")

def _masuk_regular(tersimpan):
    """tambahkan data baru ke regular.txt (file pelatihan utama)"""
    with open(os.path.join(HERE,"regular.txt"),"a",encoding="utf-8") as reg:
        for fname,title,ex in tersimpan:
            reg.write(f"\n\n=== pelajaran dari: {fname} ===\njudul: {title}\n\n{ex}")
    print(f"📥 {len(tersimpan)} pelajaran baru masuk ke regular.txt")

def _latih_diri(epochs=120):
    """latih ulang otak 'online' lalu suntikkan ke otak_casper.brain"""
    cmd_gabung()
    tmp = os.path.join(HERE,"otak_online_tmp.brain")
    print(f"🧠 melatih ulang otak online ({epochs} epoch)...")
    subprocess.run([sys.executable, os.path.join(HERE,"train_besar.py"),
                    os.path.join(HERE,"korpus_online.txt"), tmp, str(epochs)], check=False)
    if not os.path.exists(tmp):
        print("⚠️ latihan gagal, otak tidak diperbarui"); return
    semua = pickle.load(open(os.path.join(HERE,"otak_casper.brain"),"rb"))
    semua["online"] = pickle.load(open(tmp,"rb"))
    pickle.dump(semua, open(os.path.join(HERE,"otak_casper.brain"),"wb"))
    os.remove(tmp)
    print("✨ otak_casper.brain diperbarui — Casper makin pintar!")

def cmd_belajar(lang, judul_list, epochs=120):
    tersimpan = cmd_cari(lang, judul_list, kembalikan=True)
    if not tersimpan:
        print("tidak ada data baru, latihan dibatalkan"); return
    _masuk_regular(tersimpan)
    _latih_diri(epochs)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(0)
    mode = sys.argv[1]
    if mode == "gabung":
        cmd_gabung()
    elif mode in ("cari","belajar") and len(sys.argv) >= 4 and sys.argv[2] in ("id","en"):
        if mode == "cari":
            cmd_cari(sys.argv[2], sys.argv[3:])
        else:
            cmd_belajar(sys.argv[2], sys.argv[3:])
    else:
        print(__doc__)
