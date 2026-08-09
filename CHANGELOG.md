# 📝 Changelog

Semua perubahan signifikan pada project **CasperVerse** didokumentasikan di file ini.
Format mengikuti [Keep a Changelog](https://keepachangelog.com/id/1.1.0/) dan penomoran versi mengikuti [Semantic Versioning](https://semver.org/lang/id/).

---

## [3.0.0] — 2026-08-09 🏛️ Konsolidasi Besar

### 🔄 Diubah
- **Seluruh 42 otak** dilebur menjadi **satu file** `otak_casper.brain` (sebelumnya 48 file `.brain` terpisah).
- **Seluruh bahan belajar** (62 file korpus) dilebur menjadi **satu file** `regular.txt` dengan label per-blok.
- **19 script Python** dirampingkan menjadi **5 file** esensial: `casperverse.py`, `train_besar.py`, `train_token.py`, `belajar_online.py`, `evaluasi.py`.
- `casperverse.py` kini memuat otak dari file gabungan (loader `_muat_semua()`).
- `evaluasi.py` ditulis ulang menjadi *health-check* per-domain yang membaca dari `regular.txt`.

### 🗑️ Dihapus
- Script fase lama yang sudah tergantikan (`nano1.py`, `sekolah.py`, `kuliah_*.py`, `chat.py`, `ngobrol.py`, `train_specialist.py`, `gen_*.py`, `fetch_*.py`).
- Riwayat git lokal (untuk efisiensi ukuran).

### 📚 Dokumentasi
- README ditulis ulang dengan gaya profesional (daftar isi, badge, struktur lengkap).
- `CHANGELOG.md` dibuat (file ini).

> 💡 Versi ini menetapkan bentuk final yang ramping: hanya butuh **2 file** untuk menjalankan Casper.

---

## [2.3.0] — 2026-08-09 🪪 Identitas & Belajar Mandiri

### ✨ Ditambahkan
- **Otak identitas** (`identitas`): Casper mengenali dirinya sebagai *CasperAI dari CasperVerse family*, diciptakan oleh **Gen Z (genzxseventh)**.
- **Kepribadian & rules** ditanamkan: ramah, jujur, sopan, tidak mengarang fakta.
- **`belajar_online.py`**: Casper dapat mengumpulkan artikel Wikipedia (ID/EN) sendiri dan melatih otaknya.
- Otak `online` 🧭 hasil belajar mandiri (LLM, neural network, machine learning, budaya Nusantara).

### 🍽️ Data Baru
- `indo_extra3`, `inggris_extra3`, `korpus_online` (+390K karakter).

---

## [2.2.0] — 2026-08-08 🔤 Generasi Per-Token

### ✨ Ditambahkan
- **`train_token.py`**: arsitektur word-level dengan **embedding 64-dimensi** (bukan one-hot).
- Otak percakapan utama (`bicara`, `curhat`, `motivasi`, `jokes`, `gombal`) di-upgrade ke generasi token.
- **Efek streaming mengetik** di terminal, seperti LLM modern.
- Deteksi *word-boundary* pada router agar kata pendek tidak salah cocok.

### 🔧 Diperbaiki
- Kata tidak lagi terpotong ("ran" → "orang").
- Jokes berhenti tepat setelah punchline.

---

## [2.1.0] — 2026-08-08 🏋️ Peningkatan Kapasitas Massal

### 🔄 Diubah
- Otak-otak pengetahuan lemah di-upgrade ke **kapasitas besar** (konteks 16, hidden 384×192).
- Penambahan data besar-besaran (+935K karakter: budaya Indonesia, sejarah dunia, filsafat).

### 📈 Hasil
- `tanaman` 0.65 → **0.028** (rekor terendah), `sejarah` → 0.045, `kode` → 0.15, `catur` → 0.31, `filsafat` → 0.44.
- Rata-rata loss keluarga: **0.55 → 0.25**.

---

## [2.0.0] — 2026-08-08 🌌 The Multiverse

### ✨ Ditambahkan
- Otak tunggal **di-split menjadi keluarga spesialis** — lahirnya konsep CasperVerse.
- **Router konteks otomatis** berbasis kata kunci + deteksi hitungan + deteksi peribahasa.
- **Tool use**: kalkulator internal untuk soal matematika.
- Puluhan kepribadian baru: wibu, kode, hack, catur, chef, curhat, dongeng, dan banyak lagi.

---

## [1.0.0] — 2026-08-08 👶 Fase Otak Tunggal

### ✨ Ditambahkan
- Pelatihan bertahap pada satu otak: pengetahuan umum → wibu → koding → hacker etis → catur → seniman (jokes, prosa, horor).
- Mekanisme **SEEDS** agar jawaban Q&A bersih tanpa gema.
- Koreksi bug alfabet pada otak-otak kecil.

---

## [0.1.0] — 2026-08-08 🌱 Kelahiran NANO-1

### ✨ Ditambahkan
- Jaringan saraf karakter-level pertama dibangun dari nol dengan NumPy.
- Arsitektur: one-hot → 2 hidden layer (`tanh`) → softmax, optimizer Adam manual.
- Lahir dengan **109.000 parameter**, hanya mampu mengoceh.

---

<div align="center">

*Perjalanan dari 109 ribu menjadi 8,4 juta parameter — tumbuh ±77 kali lipat.* 📈

</div>
