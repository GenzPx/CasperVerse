"""EVALUASI — health-check otak Casper, per-domain.
Ngukur loss tiap otak karakter-level terhadap korpus domainnya sendiri
(diambil dari blok berlabel di regular.txt). Makin kecil = makin hafal.
Pakai: python3 evaluasi.py
"""
import pickle, numpy as np, re

# otak -> file sumber (label blok di regular.txt)
MAP = {
 "bola":      ["bola_id.txt"],
 "catur":     ["chess_en.txt","chess_drills.txt"],
 "chef":      ["masak_id.txt","resep_sintetis.txt"],
 "filsafat":  ["filsafat_en.txt","filsafat_extra.txt"],
 "game":      ["game_id.txt","game_slang.txt"],
 "hack":      ["korpus_hacker.txt"],
 "horor":     ["horor_teori_en.txt","hantu_id.txt","jiwa_horor.txt"],
 "indo":      ["korpus.txt","korpus_umum2.txt","indo_extra.txt","indo_extra2.txt","indo_extra3.txt"],
 "inggris":   ["english_umum.txt","inggris_extra.txt","inggris_extra2.txt","inggris_extra3.txt"],
 "kode":      ["korpus_kode.txt"],
 "prosa":     ["jiwa_prosa.txt"],
 "rp":        ["korpus_rp.txt"],
 "sains":     ["sains_en.txt"],
 "sejarah":   ["sejarah_id.txt"],
 "wibu":      ["korpus_wibu.txt"],
 "musik":     ["musik_id.txt"],
 "film":      ["film_id.txt"],
 "sehat":     ["sehat_id.txt"],
 "hewan":     ["hewan_id.txt"],
 "otomotif":  ["otomotif_id.txt"],
 "gadget":    ["gadget_id.txt"],
 "dongeng":   ["dongeng.txt"],
 "matematika":["matematika.txt"],
 "fakta":     ["fakta.txt"],
 "kamus":     ["kamus_en.txt"],
 "uang":      ["uang.txt"],
 "logika":    ["logika.txt"],
 "wisata":    ["wisata_id.txt"],
 "badminton": ["badminton_id.txt","badminton_hype.txt"],
 "peribahasa":["peribahasa.txt"],
 "kutipan":   ["kutipan.txt"],
 "psikologi": ["psikologi.txt"],
 "belajar":   ["belajar.txt"],
 "tanaman":   ["tanaman_id.txt"],
 "online":    ["korpus_online.txt"],
 "hukum":     ["hukum.txt"],
 "kriminal":  ["kriminal_full.txt"],
 "politik":   ["politik.txt"],
 "hardware":  ["hardware.txt"],
 "animasi":   ["animasi.txt"],
 "ips":       ["ips.txt"],
}

# --- parse regular.txt jadi {nama_file: isi} ---
txt = open("regular.txt", encoding="utf-8").read()
bagian = {}
for m in re.finditer(r"=== pelajaran dari: (.+?) ===\n(.*?)(?=\n=== pelajaran dari: |\Z)", txt, re.S):
    bagian[m.group(1)] = m.group(2).strip()

SEMUA = pickle.load(open("otak_casper.brain", "rb"))
rng = np.random.default_rng(5); BATCH = 1024
hasil = []
for nama, files in MAP.items():
    if nama not in SEMUA: continue
    brain = SEMUA[nama]
    if isinstance(brain, dict): continue
    korpus = "\n\n".join(bagian[f] for f in files if f in bagian)
    if not korpus: continue
    W1,b1,W2,b2,W3,b3,vocab,ivocab,L = brain
    V = len(vocab); unk = vocab.get(" ", 0)
    data = np.array([vocab.get(c, unk) for c in korpus], dtype=np.int32)
    N = len(data) - L
    sel = rng.choice(N, min(100_000, N), replace=False)
    tot, seen = 0.0, 0
    for s in range(0, len(sel)-BATCH, BATCH):
        pos = sel[s:s+BATCH]
        X = np.zeros((BATCH, L*V), dtype=np.float32)
        for k,p in enumerate(pos):
            X[k, np.arange(L)*V + data[p:p+L]] = 1.0
        y = data[pos+L]
        h1 = np.tanh(X@W1+b1); h2 = np.tanh(h1@W2+b2)
        logits = h2@W3+b3
        ex = np.exp(logits-logits.max(1,keepdims=True))
        pr = ex/ex.sum(1,keepdims=True)
        tot += -np.log(pr[np.arange(BATCH),y]+1e-9).mean()*BATCH
        seen += BATCH
    hasil.append((nama, tot/seen))

hasil.sort(key=lambda x: x[1])
print(f"{'otak':12s} {'loss':>8s}")
print("-"*22)
for nama, loss in hasil:
    print(f"{nama:12s} {loss:>8.4f}")
print("-"*22)
print(f"otak dievaluasi  : {len(hasil)}")
print(f"rata-rata loss   : {np.mean([x[1] for x in hasil]):.4f}")
print(f"otak di bawah 0.1: {sum(1 for _,l in hasil if l<0.1)}")
