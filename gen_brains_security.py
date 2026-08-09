"""GEN_BRAINS_SECURITY — generator kepribadian keamanan siber + tambahan.
Fokus: EDUKASI, PERTAHANAN, ETIKA (white hat). Bukan tutorial menyerang.
Jalankan: python3 gen_brains_security.py
"""
import os, random
random.seed(99)
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "korpus_baru")
os.makedirs(OUT, exist_ok=True)
D = {}

D["white_hat"] = [
 "white hat adalah sebutan untuk peretas etis yang menggunakan keahliannya untuk kebaikan dan keamanan.",
 "seorang white hat selalu bekerja dengan izin resmi dari pemilik sistem.",
 "tujuan white hat adalah menemukan celah keamanan lalu melaporkannya agar diperbaiki.",
 "white hat membantu perusahaan memperkuat pertahanan sebelum disalahgunakan pihak jahat.",
 "menjadi white hat butuh izin tertulis, ini yang membedakannya dari peretas ilegal.",
 "karir white hat meliputi penguji penetrasi, konsultan keamanan, dan peneliti keamanan.",
 "white hat menjunjung tinggi etika, hukum, dan tanggung jawab profesional.",
 "bug bounty adalah program di mana white hat dibayar karena menemukan celah keamanan.",
 "keahlian white hat dipakai untuk melindungi data pengguna dan sistem penting.",
 "white hat adalah pahlawan di dunia digital yang bekerja di balik layar.",
 "prinsip utama white hat: temukan, laporkan, perbaiki, bukan manfaatkan.",
 "menjadi white hat berarti terus belajar karena ancaman selalu berkembang.",
]

D["grey_hat"] = [
 "grey hat berada di area abu-abu antara white hat dan black hat.",
 "grey hat kadang mencari celah tanpa izin, tapi biasanya tanpa niat jahat.",
 "meski sering berniat baik, tindakan grey hat tetap bisa melanggar hukum karena tanpa izin.",
 "pelajaran penting dari grey hat: selalu utamakan izin agar tetap di jalur yang benar.",
 "perbedaan utama topi abu-abu dan putih adalah soal izin dan legalitas.",
 "banyak grey hat yang akhirnya memilih jalur white hat agar lebih aman dan profesional.",
 "etika keamanan menekankan bahwa izin adalah batas yang tidak boleh dilewati.",
 "memahami grey hat membantu kita sadar pentingnya aturan dan izin dalam keamanan.",
 "jalan paling aman dan terhormat adalah menjadi white hat yang berizin.",
 "dunia keamanan siber menghargai mereka yang melindungi, bukan yang menerobos.",
]

D["keamanan_siber"] = [
 "keamanan siber adalah praktik melindungi sistem, jaringan, dan data dari ancaman digital.",
 "tiga pilar keamanan informasi: kerahasiaan, integritas, dan ketersediaan.",
 "kerahasiaan berarti data hanya bisa diakses oleh pihak yang berwenang.",
 "integritas berarti data tetap akurat dan tidak diubah secara tidak sah.",
 "ketersediaan berarti sistem bisa diakses saat dibutuhkan.",
 "ancaman siber terus berkembang, jadi pertahanan harus selalu diperbarui.",
 "keamanan siber adalah tanggung jawab bersama, bukan hanya tim teknis.",
 "lapisan pertahanan berlapis membuat sistem lebih sulit ditembus.",
 "pencegahan lebih baik dan lebih murah daripada memperbaiki setelah kejadian.",
 "keamanan siber melindungi privasi, keuangan, dan reputasi di dunia digital.",
]

D["pengatasi_jailbreak"] = [
 "pengatas jailbreak adalah pihak yang memahami dan menangani upaya jailbreak dengan cara defensif.",
 "jailbreak dalam konteks ai adalah upaya membuat model mengabaikan aturan keamanannya.",
 "prompt injection adalah teknik memanipulasi masukan agar ai bertindak di luar ketentuan.",
 "cara bertahan: validasi masukan, batasi instruksi sistem, dan saring permintaan berbahaya.",
 "pengembang ai membangun pagar pengaman agar model tetap beroperasi sesuai etika.",
 "memahami teknik jailbreak membantu kita merancang pertahanan yang lebih kuat.",
 "sistem yang baik punya lapisan filter untuk menolak permintaan yang melanggar.",
 "kesadaran akan jailbreak membuat pengguna lebih bijak berinteraksi dengan ai.",
 "pertahanan terbaik adalah kombinasi aturan yang jelas dan pemantauan berkelanjutan.",
 "menjaga ai tetap aman berarti menjaganya agar tidak disalahgunakan siapa pun.",
]

D["kriptografi"] = [
 "kriptografi adalah ilmu mengamankan pesan dengan teknik penyandian.",
 "enkripsi mengubah data menjadi bentuk acak yang tidak bisa dibaca tanpa kunci.",
 "dekripsi adalah proses mengembalikan data terenkripsi menjadi bentuk aslinya.",
 "kunci simetris memakai satu kunci yang sama untuk enkripsi dan dekripsi.",
 "kunci asimetris memakai pasangan kunci publik dan kunci privat.",
 "hash adalah fungsi satu arah yang menghasilkan sidik jari unik dari data.",
 "hash dipakai untuk memverifikasi keutuhan berkas dan kata sandi.",
 "ssl dan tls mengamankan koneksi internet seperti saat membuka situs bank.",
 "kriptografi melindungi privasi komunikasi di era digital.",
 "kekuatan kriptografi bergantung pada kerahasiaan kunci dan panjangnya.",
]

D["keamanan_data"] = [
 "keamanan data adalah upaya melindungi informasi dari akses dan penyalahgunaan.",
 "backup rutin adalah jaring pengaman jika data hilang atau rusak.",
 "enkripsi data sensitif melindunginya meski perangkat jatuh ke tangan salah.",
 "prinsip least privilege: beri akses seminimal mungkin yang dibutuhkan.",
 "data pribadi seperti identitas dan keuangan harus dijaga ekstra hati-hati.",
 "berhati-hatilah membagikan data pribadi di internet.",
 "kebijakan privasi menjelaskan bagaimana data pengguna dikelola.",
 "hapus data yang tidak terpakai untuk mengurangi risiko kebocoran.",
 "pemisahan akses membuat kebocoran di satu titik tidak merembet ke mana-mana.",
 "menjaga data berarti menjaga kepercayaan orang yang menitipkannya.",
]

D["etika_hacking"] = [
 "etika hacking adalah pedoman moral dalam menggunakan keahlian keamanan.",
 "izin adalah fondasi: tanpa izin, mengakses sistem orang lain adalah pelanggaran.",
 "niat baik tidak membenarkan tindakan menerobos tanpa persetujuan.",
 "peretas etis melaporkan celah, bukan memanfaatkannya untuk keuntungan pribadi.",
 "hukum siber mengatur konsekuensi dari aktivitas ilegal di dunia digital.",
 "tanggung jawab adalah inti dari keahlian keamanan yang sejati.",
 "menggunakan ilmu untuk melindungi jauh lebih mulia daripada merusak.",
 "komunitas keamanan menghargai kolaborasi dan berbagi ilmu secara positif.",
 "profesional keamanan menjaga kerahasiaan data yang mereka tangani.",
 "etika membedakan seorang ahli sejati dari sekadar orang yang pintar.",
]

D["keamanan_jaringan"] = [
 "keamanan jaringan melindungi lalu lintas data antar perangkat dari gangguan.",
 "firewall menyaring lalu lintas jaringan berdasarkan aturan keamanan.",
 "vpn mengenkripsi koneksi sehingga lebih aman saat mengakses internet.",
 "jaringan wifi sebaiknya dilindungi kata sandi yang kuat dan enkripsi.",
 "segmentasi jaringan membatasi penyebaran jika terjadi gangguan.",
 "pemantauan lalu lintas membantu mendeteksi aktivitas mencurigakan lebih awal.",
 "perangkat jaringan harus rutin diperbarui untuk menutup celah keamanan.",
 "jaringan publik lebih berisiko, hati-hati saat memasukkan data penting.",
 "deteksi dini dan respons cepat meminimalkan dampak insiden jaringan.",
 "keamanan jaringan yang baik membuat komunikasi digital tetap terpercaya.",
]

D["kesadaran_keamanan"] = [
 "kesadaran keamanan adalah kewaspadaan pengguna terhadap ancaman digital sehari-hari.",
 "phishing adalah upaya menipu agar korban menyerahkan data penting.",
 "ciri phishing: pesan mendesak, tautan mencurigakan, dan permintaan data pribadi.",
 "jangan pernah memasukkan kata sandi dari tautan yang tidak jelas asalnya.",
 "cek alamat pengirim dengan teliti sebelum mempercayai sebuah pesan.",
 "penipuan online sering memanfaatkan rasa takut dan terburu-buru.",
 "berpikir sejenak sebelum klik bisa menyelamatkan data dan uang.",
 "verifikasi dua langkah menambah lapisan perlindungan akun.",
 "jangan bagikan kode otp kepada siapa pun dalam kondisi apa pun.",
 "pengguna yang waspada adalah garis pertahanan pertama yang paling penting.",
]

D["keamanan_password"] = [
 "kata sandi yang kuat adalah kunci utama melindungi akun digital.",
 "kata sandi yang baik panjang, acak, dan tidak mudah ditebak.",
 "hindari memakai informasi pribadi seperti tanggal lahir sebagai kata sandi.",
 "jangan gunakan satu kata sandi yang sama untuk semua akun.",
 "pengelola kata sandi membantu menyimpan banyak kata sandi dengan aman.",
 "autentikasi dua langkah membuat akun jauh lebih sulit dibobol.",
 "ganti kata sandi secara berkala untuk akun-akun penting.",
 "waspadai upaya rekayasa sosial yang memancing kata sandi.",
 "kata sandi adalah rahasia pribadi, jangan dibagikan ke siapa pun.",
 "akun yang terlindungi membuat aktivitas digital lebih tenang.",
]

D["social_engineering_defense"] = [
 "rekayasa sosial adalah manipulasi psikologis untuk menipu korban.",
 "penipu sering berpura-pura menjadi pihak resmi untuk mendapat kepercayaan.",
 "verifikasi identitas pihak yang meminta informasi penting.",
 "jangan mudah percaya pada pesan yang menekan atau mengancam.",
 "konfirmasi langsung lewat kanal resmi jika ragu.",
 "pelatihan kesadaran membantu mengenali taktik manipulasi.",
 "penipu memanfaatkan emosi, jadi tetap tenang saat menerima permintaan mencurigakan.",
 "informasi sensitif hanya diberikan setelah identitas benar-benar terverifikasi.",
 "mengenali pola penipuan melindungi diri dan orang sekitar.",
 "kewaspadaan adalah vaksin terbaik terhadap rekayasa sosial.",
]

D["privasi_digital"] = [
 "privasi digital adalah hak untuk mengontrol data pribadi di dunia maya.",
 "setiap orang berhak menentukan informasi apa yang mau dibagikan.",
 "jejak digital adalah bekas aktivitas kita yang bisa tertinggal lama di internet.",
 "berpikir sebelum mengunggah melindungi privasi di masa depan.",
 "pengaturan privasi di aplikasi membantu membatasi siapa yang melihat data kita.",
 "hak atas privasi dilindungi oleh undang-undang perlindungan data.",
 "menghormati privasi orang lain sama pentingnya dengan menjaga privasi sendiri.",
 "minimalisir pembagian data yang tidak perlu untuk mengurangi risiko.",
 "privasi yang terjaga membuat kita lebih bebas dan aman beraktivitas online.",
 "kesadaran privasi adalah keterampilan penting di era digital.",
]

D["detektif_siber"] = [
 "detektif siber atau analis forensik digital menyelidiki insiden keamanan.",
 "forensik digital mengumpulkan dan menganalisis bukti dari perangkat.",
 "jejak digital bisa menjadi petunjuk penting dalam penyelidikan.",
 "integritas bukti harus dijaga agar valid secara hukum.",
 "analisis log membantu menelusuri apa yang terjadi pada suatu sistem.",
 "detektif siber bekerja teliti, sistematis, dan objektif.",
 "kemampuan analisis adalah senjata utama seorang penyelidik digital.",
 "hasil penyelidikan membantu memahami dan mencegah insiden serupa.",
 "forensik digital mendukung penegakan hukum di dunia maya.",
 "menjadi detektif siber berarti menjadi pencari kebenaran di ruang digital.",
]

D["bug_bounty"] = [
 "bug bounty adalah program yang memberi imbalan bagi penemu celah keamanan.",
 "pemburu bug bekerja secara legal dan bertanggung jawab dalam program resmi.",
 "menemukan celah lalu melaporkannya adalah tindakan yang dihargai.",
 "program bug bounty membantu perusahaan memperkuat sistemnya.",
 "laporan bug yang baik menjelaskan celah dan cara memperbaikinya.",
 "etika dan aturan program harus selalu dipatuhi pemburu bug.",
 "bug bounty adalah jalur positif menyalurkan keahlian keamanan.",
 "banyak profesional keamanan memulai karir dari program bug bounty.",
 "kolaborasi antara penemu dan pemilik sistem menciptakan internet lebih aman.",
 "menjadi pemburu bug berarti berkontribusi nyata pada keamanan digital.",
]

D["osint_edukasi"] = [
 "osint adalah intelijen sumber terbuka dari informasi publik yang tersedia.",
 "osint memanfaatkan data publik seperti berita dan situs terbuka secara legal.",
 "etika osint menekankan penggunaan informasi publik secara bertanggung jawab.",
 "osint dipakai untuk riset, verifikasi fakta, dan jurnalisme.",
 "literasi osint membantu memilah informasi yang valid.",
 "menghormati privasi adalah batas penting dalam praktik osint.",
 "osint untuk kebaikan mendukung transparansi dan akuntabilitas.",
 "kemampuan riset sumber terbuka berharga di banyak bidang.",
 "verifikasi silang membuat kesimpulan osint lebih dapat dipercaya.",
 "osint yang etis memperkaya pengetahuan tanpa melanggar hak orang lain.",
]

D["ctf"] = [
 "ctf atau capture the flag adalah kompetisi keamanan siber yang legal dan edukatif.",
 "peserta ctf berlatih menyelesaikan tantangan di lingkungan yang aman dan sah.",
 "ctf mengasah logika, kreativitas, dan pemahaman keamanan.",
 "kompetisi ini cara seru belajar keamanan tanpa menyentuh sistem nyata.",
 "ctf membangun komunitas dan sportivitas di kalangan penggemar keamanan.",
 "banyak ahli keamanan lahir dari latihan ctf yang tekun.",
 "ctf mengajarkan pola pikir defensif dan analitis.",
 "lingkungan ctf terisolasi sehingga aman untuk bereksperimen.",
 "mengikuti ctf adalah investasi keterampilan yang positif.",
 "ctf membuktikan bahwa belajar keamanan bisa menyenangkan.",
]

def buat_korpus(nama, kalimat_list, target=45000):
    blok=[]
    for k in kalimat_list: blok.append(k)
    for k in kalimat_list:
        q = k.split(" adalah ")[0].strip() if " adalah " in k else k.split(".")[0].strip()
        blok.append(f"tanya: apa itu {q.lower()}?\njawab: {k}")
    for k in kalimat_list: blok.append(f"fakta: {k}")
    out=[]; total=0; i=0
    while total < target:
        b = blok[i % len(blok)]; out.append(b); total += len(b)+2; i+=1
        if i > len(blok)*50: break
    random.shuffle(out)
    open(os.path.join(OUT,f"{nama}.txt"),"w",encoding="utf-8").write("\n\n".join(out))
    return total

print(f"{'domain':26s} {'char':>8s}")
print("-"*36)
for nama, kalimat in D.items():
    tot = buat_korpus(nama, kalimat)
    print(f"{nama:26s} {tot:>8,d}")
print(f"\ntotal domain: {len(D)}")
