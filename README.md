<div align="center">

# 🌌 CasperVerse

**Satu tubuh, 42 kepribadian — AI karakter-level yang dibangun dari nol dengan NumPy murni.**

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)](https://www.python.org)
[![NumPy](https://img.shields.io/badge/NumPy-Murni-013243?logo=numpy&logoColor=white)](https://numpy.org)
[![Otak](https://img.shields.io/badge/Otak-42-orange)](#-arsitektur)
[![Parameter](https://img.shields.io/badge/Parameter-8%2C4_juta-green)](#-arsitektur)
[![Platform](https://img.shields.io/badge/Platform-Termux_%7C_PC-3DDC84?logo=android)](#-instalasi)
[![Lisensi](https://img.shields.io/badge/Lisensi-MIT-yellow)](LICENSE)

*Casper bukan AI besar. Casper adalah AI kecil yang dibesarkan dengan sabar.*

</div>

---

## 📑 Daftar Isi

- [Tentang CasperVerse](#-tentang-caspervers)
- [Fitur Utama](#-fitur-utama)
- [Arsitektur](#-arsitektur)
- [Daftar Kepribadian](#-daftar-kepribadian)
- [Instalasi](#-instalasi)
- [Penggunaan](#-penggunaan)
- [Pipeline Belajar](#-pipeline-belajar)
- [Struktur Project](#-struktur-project)
- [Changelog](#-changelog)
- [Roadmap](#-roadmap)
- [Lisensi](#-lisensi)

---

## 🤖 Tentang CasperVerse

**CasperVerse** adalah eksperimen AI yang dibangun **sepenuhnya dari nol** — tanpa PyTorch, tanpa TensorFlow, tanpa API eksternal, dan berjalan **100% offline**. Seluruh sistem terdiri dari jaringan saraf karakter-level dan token-level kecil yang dilatih dengan backpropagation murni menggunakan NumPy.

Project ini dimulai dari satu otak sederhana bernama **NANO-1** (109 ribu parameter), lalu tumbuh melalui proses "pengasuhan" bertahap — diberi data, dilatih, di-upgrade — hingga menjadi keluarga berisi **42 kepribadian** dengan total **8,4 juta parameter**.

Sejak `v3.0`, CasperVerse dikonsolidasi menjadi bentuk paling ramping: **satu file otak, satu file korpus, lima file script**.

> 🪪 *"Saya adalah CasperAI dari CasperVerse family, diciptakan oleh satu orang bernama Gen Z yang kerap disebut genzxseventh."*

---

## ✨ Fitur Utama

| | Fitur | Deskripsi |
|---|---|---|
| 🧠 | **42 Otak dalam 1 File** | Semua kepribadian tersimpan di `otak_casper.brain` |
| 🎯 | **Router Konteks Otomatis** | Setiap pertanyaan diarahkan ke pakar yang tepat |
| 🔤 | **Generasi Per-Token + Streaming** | Otak percakapan menghasilkan kata utuh per langkah, dengan efek mengetik seperti LLM modern |
| 🛠️ | **Tool Use (Kalkulator)** | Soal hitungan dijawab dengan mesin — teknik yang sama dengan LLM produksi |
| 🌐 | **Belajar Mandiri dari Internet** | `belajar_online.py` mengumpulkan artikel Wikipedia secara otomatis |
| 🪪 | **Identitas & Kepribadian** | Casper tahu siapa dirinya, siapa penciptanya, dan aturan perilakunya |
| 📱 | **Ringan & Offline** | Berjalan di HP lewat Termux tanpa internet, RAM ±50MB |

---

## 🏗️ Arsitektur

### Dua Generasi Jaringan Saraf

Setiap "otak" adalah feedforward neural network (2 hidden layer, aktivasi `tanh`, optimizer Adam — semuanya diimplementasikan manual di NumPy):

| | Karakter-level | Token-level |
|---|---|---|
| Satuan generasi | per huruf | per kata utuh |
| Representasi input | one-hot | **embedding 64-dimensi** |
| Kapasitas | konteks 8 / 16 karakter | konteks 8 kata |
| Kualitas | rentan kata terpotong | kalimat utuh & koheren |
| Dipakai oleh | 36 otak pengetahuan | 6 otak percakapan |

### Varian Kapasitas

- 🧠 **Standar** — konteks 8, hidden 256×128
- 🧠 **Besar** — konteks 16, hidden 384×192 (untuk domain pengetahuan luas)

### Tool Use

Otak karakter tidak bisa benar-benar berhitung. Maka saat router mendeteksi ekspresi aritmetika, Casper menggunakan **kalkulator internal** dan mengembalikan hasilnya — pola *tool use* yang sama dengan LLM modern.

### Kualitas (Loss)

Loss mengukur seberapa sering model "kaget" oleh karakter/token berikutnya:

| Loss | Interpretasi |
|---|---|
| `~4.5` | Acak (kondisi saat lahir) |
| `0.5 – 1.0` | Masih belajar |
| `0.1 – 0.3` | Mahir |
| `< 0.1` | Hafal di luar kepala |

Rata-rata loss keluarga saat ini: **0.25** (16 otak di kelas elite).

---

## 🎭 Daftar Kepribadian

**Pengetahuan & Sains** — `sains` 🔬 · `indo` 🇮🇩 · `inggris` 🌍 · `sejarah` 📜 · `filsafat` 🤔 · `psikologi` 🧠 · `fakta` 🤯 · `online` 🧭

**Hobi & Hiburan** — `wibu` 🎌 · `kode` 💻 · `hack` 🖤 · `game` 🎮 · `bola` ⚽ · `badminton` 🏸 · `catur` ♟️ · `musik` 🎵 · `film` 🎬 · `hewan` 🐾 · `tanaman` 🌱 · `wisata` 🏝️ · `otomotif` 🏍️ · `gadget` 📱

**Kehidupan & Perasaan** — `curhat` 🫂 · `motivasi` 🔥 · `uang` 💰 · `sehat` 💪 · `belajar` 📚 · `chef` 🍳 · `kamus` 🗣️

**Budaya & Kreativitas** — `jokes` 😂 · `prosa` ✒️ · `dongeng` 📖 · `peribahasa` 📜 · `kutipan` 💬 · `logika` 🧩 · `matematika` 🔢 · `gombal` 🌹

**Inti** — `bicara` 🗨️ (suara default) · `identitas` 🪪 (jati diri) · `rp` 🎭 (roleplay) · `casperc` 👻 (otak orisinal)

---

## 📲 Instalasi

### Termux (Android)

```bash
# 1. Pasang Termux dari F-Droid (bukan Play Store)
# 2. Pasang dependensi
pkg update -y && pkg upgrade -y
pkg install python unzip -y
pip install numpy

# 3. Ekstrak project
mkdir ~/casperverse && cd ~/casperverse
termux-setup-storage
cp /sdcard/Download/casperverse.zip .
unzip casperverse.zip

# 4. Jalankan
python casperverse.py
```

### PC (Linux / macOS / Windows)

```bash
git clone https://github.com/GenzPx/CasperVerse.git
cd CasperVerse
pip install numpy
python casperverse.py
```

---

## 💬 Penggunaan

Ketik apa saja — router memilih pakar secara otomatis:

```
lu > kamu siapa
🪪 CASPER-IDENTITAS > namaku casperai. aku lahir di casperverse family,
                      diciptakan oleh gen z yang sering dipanggil genzxseventh.

lu > 7 x 8 =
🔢 CASPER-MATEMATIKA > 7 x 8 = 56

lu > aku lagi sedih
🫂 CASPER-CURHAT > lu nggak harus pura-pura kuat di depan gue.
```

### Command Opsional

| Command | Fungsi |
|---|---|
| `/pakar` | daftar semua kepribadian |
| `/pakai <nama>` | kunci ke satu pakar |
| `/auto` | kembali ke mode router otomatis |
| `/suhu <0.3–1.0>` | atur kreativitas |
| `/panjang <n>` | atur panjang jawaban |
| `/bantu` · `/keluar` | bantuan · keluar |

---

## 🎓 Pipeline Belajar

Casper bisa terus diajari. Tiga langkah standarnya:

```bash
# 1. Kumpulkan data baru dari internet
python3 belajar_online.py id "Perahu Pinisi" "Tari Kecak"
python3 belajar_online.py gabung

# 2. Latih otak baru / lanjut latihan
python3 train_besar.py korpus_online.txt otak_baru.brain 120
python3 train_token.py percakapan.txt otak_ngobrol.brain 100

# 3. Cek kualitas semua otak
python3 evaluasi.py
```

`belajar_online.py` memakai User-Agent sopan, jeda otomatis, dan retry saat terkena rate-limit.

---

## 📂 Struktur Project

```
CaspeVerse/
├── casperverse.py      # Aplikasi utama (router + chat + streaming)
├── otak_casper.brain   # Seluruh 42 otak dalam satu file
├── regular.txt         # Seluruh bahan belajar dalam satu file
├── train_besar.py      # Trainer otak pengetahuan
├── train_token.py      # Trainer otak percakapan (per-token)
├── belajar_online.py   # Pengumpul data internet mandiri
├── evaluasi.py         # Health-check seluruh otak
├── README.md
├── CHANGELOG.md
└── LICENSE
```

> 💡 **Fakta:** untuk menjalankan Casper, hanya dibutuhkan **2 file** — `casperverse.py` + `otak_casper.brain`.

---

## 📝 Changelog

Lihat [CHANGELOG.md](CHANGELOG.md) untuk riwayat lengkap versi — dari lahirnya NANO-1 hingga konsolidasi v3.0.

---

## 🗺️ Roadmap

- [x] 42 otak spesialis dalam satu file
- [x] Router konteks otomatis
- [x] Generasi per-token + streaming
- [x] Tool use (kalkulator)
- [x] Identitas, kepribadian & rules
- [x] Belajar mandiri dari internet
- [ ] Memori percakapan (short-term)
- [ ] Lebih banyak karakter roleplay
- [ ] Dukungan bahasa daerah
- [ ] Installer satu perintah

---

## 🤝 Kontribusi

Project ini adalah eksperimen personal yang dibesarkan dengan penuh kesabaran. Ide, issue, dan pull request diterima dengan senang hati.

---

## 📄 Lisensi

Dirilis di bawah lisensi **MIT** — bebas digunakan, dimodifikasi, dan dibagikan. Lihat [LICENSE](LICENSE) untuk detail.

---

<div align="center">

**Dibangun dengan 🧠 + ❤️ + banyak epoch**

*"Casper membuktikan: AI kecil yang dibesarkan dengan sabar bisa menjadi keluarga yang luar biasa."*

⭐ Jika project ini membuatmu tersenyum, berikan bintang.

</div>
