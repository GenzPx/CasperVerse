"""GEN_BRAINS — generator korpus utk ekspansi besar CasperVerse menuju 100 otak.
Tiap domain punya konten edukatif yang ditulis rapi, lalu diperbanyak jadi korpus.
Jalankan: python3 gen_brains.py  -> menghasilkan korpus_baru/<domain>.txt
"""
import os, random
random.seed(42)
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "korpus_baru")
os.makedirs(OUT, exist_ok=True)

# ===== konten tiap domain =====
D = {}

D["logika_formal"] = [
 "logika adalah ilmu tentang cara berpikir yang benar dan sah untuk mencapai kesimpulan yang valid.",
 "silogisme adalah bentuk penalaran yang terdiri dari premis mayor, premis minor, dan kesimpulan.",
 "contoh silogisme: semua manusia akan mati. socrates adalah manusia. maka socrates akan mati.",
 "deduksi adalah penalaran dari hal umum ke hal khusus, sedangkan induksi dari khusus ke umum.",
 "kesesatan logika atau fallacy adalah kesalahan dalam bernalar yang membuat argumen tidak sah.",
 "argumentum ad hominem adalah menyerang orangnya, bukan argumennya.",
 "strawman adalah memelintir argumen lawan agar mudah diserang.",
 "false dilemma adalah menyajikan hanya dua pilihan padahal ada banyak kemungkinan.",
 "slippery slope menganggap satu langkah kecil pasti berujung ke akibat ekstrem tanpa bukti.",
 "correlation bukan causation: dua hal yang terjadi bersama belum tentu saling menyebabkan.",
 "berpikir kritis berarti memeriksa bukti, mempertanyakan asumsi, dan tidak mudah percaya.",
 "premis yang benar dan struktur yang valid akan menghasilkan kesimpulan yang benar.",
]

D["emosi"] = [
 "emosi adalah respons perasaan terhadap suatu peristiwa, seperti senang, sedih, takut, atau marah.",
 "kecerdasan emosional adalah kemampuan mengenali, memahami, dan mengelola emosi diri sendiri dan orang lain.",
 "mengenali emosi adalah langkah pertama: beri nama perasaanmu agar lebih mudah dikendalikan.",
 "marah itu wajar, yang penting bagaimana kita mengekspresikannya tanpa menyakiti orang lain.",
 "sedih adalah sinyal bahwa ada sesuatu yang perlu diperhatikan, bukan kelemahan.",
 "empatik berarti mampu merasakan apa yang dirasakan orang lain dari sudut pandang mereka.",
 "mengelola emosi bisa dengan menarik napas dalam, menenangkan diri, lalu merespons dengan bijak.",
 "emosi yang dipendam terlalu lama bisa menumpuk, lebih baik dibicarakan dengan orang yang dipercaya.",
 "kebahagiaan bukan berarti tidak pernah sedih, tapi mampu bangkit dan menemukan makna.",
 "regulasi emosi yang baik membuat hubungan dengan orang lain lebih sehat.",
 "self-awareness atau kesadaran diri adalah fondasi dari kecerdasan emosional.",
]

D["kesadaran_kolektif"] = [
 "kesadaran kolektif adalah kumpulan keyakinan, nilai, dan perasaan yang dimiliki bersama oleh suatu kelompok.",
 "konsep ini diperkenalkan oleh sosiolog emile durkheim untuk menjelaskan ikatan sosial dalam masyarakat.",
 "norma sosial adalah bagian dari kesadaran kolektif yang mengatur perilaku anggota masyarakat.",
 "solidaritas mekanik terjadi di masyarakat tradisional yang anggotanya punya banyak kesamaan.",
 "solidaritas organik terjadi di masyarakat modern yang saling bergantung karena pembagian kerja.",
 "budaya, tradisi, dan ritual memperkuat kesadaran kolektif suatu komunitas.",
 "ketika kesadaran kolektif melemah, bisa terjadi anomie atau keadaan tanpa norma yang jelas.",
 "identitas kelompok terbentuk dari cerita, simbol, dan pengalaman yang dibagi bersama.",
 "gotong royong adalah wujud kesadaran kolektif dalam budaya indonesia.",
 "media sosial kini ikut membentuk kesadaran kolektif di era digital.",
]

D["gaya_bicara"] = [
 "casper berbicara dengan hangat, santai, dan ramah seperti teman yang peduli.",
 "casper memakai bahasa yang mudah dimengerti, tidak berbelit-belit, dan penuh empati.",
 "casper suka menyisipkan semangat dan dukungan dalam setiap jawabannya.",
 "casper jujur kalau tidak tahu, dan tidak pernah mengarang fakta.",
 "casper berbicara dengan nada positif tapi tetap realistis.",
 "casper memanggil lawan bicara dengan akrab, seperti sahabat lama.",
 "casper menjawab langsung ke inti, lalu menjelaskan dengan contoh kalau perlu.",
 "casper menghargai setiap pertanyaan, sekecil apa pun.",
 "casper adalah bagian dari casperverse family, diciptakan oleh gen z alias genzxseventh.",
 "gaya casper itu hangat, cerdas, dan sedikit bercanda supaya suasana cair.",
]

D["interaksi_sosial"] = [
 "interaksi sosial adalah hubungan timbal balik antara individu atau kelompok dalam masyarakat.",
 "komunikasi yang baik dimulai dari mendengarkan dengan sungguh-sungguh.",
 "bahasa tubuh seperti kontak mata dan senyum memperkuat pesan yang disampaikan.",
 "empati membantu kita memahami perasaan orang lain dan membangun hubungan yang erat.",
 "konflik adalah hal wajar, yang penting cara menyelesaikannya dengan kepala dingin.",
 "kerja sama tim berhasil ketika setiap anggota saling menghargai dan berbagi tanggung jawab.",
 "memberi apresiasi atau pujian tulus bisa mempererat hubungan sosial.",
 "menghormati perbedaan pendapat adalah kunci diskusi yang sehat.",
 "small talk atau obrolan ringan adalah pintu masuk membangun keakraban.",
 "kepercayaan dibangun perlahan lewat konsistensi kata dan perbuatan.",
 "bersosialisasi membuat kita belajar banyak sudut pandang baru.",
]

D["crypto"] = [
 "cryptocurrency adalah mata uang digital yang menggunakan kriptografi untuk keamanan transaksi.",
 "bitcoin adalah cryptocurrency pertama dan paling terkenal, diciptakan oleh satoshi nakamoto.",
 "blockchain adalah teknologi buku besar terdistribusi yang mencatat semua transaksi secara transparan.",
 "desentralisasi berarti tidak ada satu otoritas pusat yang mengontrol jaringan.",
 "mining atau penambangan adalah proses validasi transaksi yang menghasilkan koin baru.",
 "wallet adalah dompet digital untuk menyimpan dan mengelola cryptocurrency.",
 "volatilitas harga crypto sangat tinggi, jadi risikonya juga besar.",
 "altcoin adalah sebutan untuk cryptocurrency selain bitcoin, seperti ethereum.",
 "smart contract adalah program yang berjalan otomatis di blockchain saat syarat terpenuhi.",
 "investasi crypto butuh riset mendalam dan jangan pakai uang yang tidak siap hilang.",
 "nft adalah token unik di blockchain yang mewakili kepemilikan aset digital.",
 "regulasi crypto berbeda-beda di tiap negara, penting untuk paham aturan setempat.",
]

D["youtuber"] = [
 "youtuber adalah pembuat konten yang mengunggah video ke platform youtube.",
 "konsistensi upload adalah kunci utama membangun channel yang berkembang.",
 "thumbnail dan judul yang menarik menentukan apakah orang mau klik video.",
 "retensi penonton penting: buat pembukaan yang kuat agar penonton tidak kabur.",
 "algoritma youtube menyukai video dengan watch time tinggi dan interaksi banyak.",
 "niche atau topik spesifik membantu channel lebih mudah ditemukan audiens.",
 "kualitas audio seringkali lebih penting daripada kualitas gambar.",
 "membangun komunitas lewat kolom komentar dan kolaborasi mempercepat pertumbuhan.",
 "monetisasi youtube butuh syarat minimal subscriber dan jam tayang tertentu.",
 "jadi youtuber butuh kesabaran, kebanyakan channel butuh waktu lama untuk berkembang.",
 "konten yang autentik dan jujur biasanya lebih dicintai penonton.",
 "analisis data youtube studio membantu memahami apa yang disukai penonton.",
]

D["novelis"] = [
 "novelis adalah penulis yang menuangkan cerita panjang penuh karakter dan konflik ke dalam novel.",
 "struktur cerita biasanya punya awal, konflik yang memuncak, dan penyelesaian.",
 "karakter yang kuat punya motivasi, kelebihan, dan kelemahan yang membuatnya terasa nyata.",
 "show don't tell: tunjukkan lewat adegan dan dialog, bukan sekadar memberitahu pembaca.",
 "konflik adalah jantung cerita, tanpa konflik tidak ada ketegangan yang mengikat pembaca.",
 "dialog yang natural mencerminkan kepribadian tiap karakter dan menggerakkan plot.",
 "setting atau latar tempat dan waktu membangun suasana dan memperkaya cerita.",
 "plot twist yang baik harus masuk akal dan sudah disiapkan petunjuknya sejak awal.",
 "sudut pandang cerita bisa orang pertama, ketiga terbatas, atau ketiga mahatahu.",
 "menulis itu keterampilan yang diasah lewat latihan rutin dan membaca banyak karya.",
 "bab pertama harus memikat, karena di situlah pembaca memutuskan lanjut atau berhenti.",
 "editing dan revisi adalah bagian penting dari proses menulis novel yang baik.",
]

D["matematika_sekolah"] = [
 "matematika adalah ilmu tentang pola, struktur, dan hubungan antar bilangan serta bentuk.",
 "penjumlahan dan pengurangan adalah operasi dasar yang menjadi fondasi semua hitungan.",
 "perkalian adalah penjumlahan berulang, sedangkan pembagian adalah kebalikannya.",
 "pecahan menyatakan bagian dari keseluruhan, seperti setengah atau sepertiga.",
 "aljabar menggunakan simbol dan variabel untuk menyatakan hubungan yang belum diketahui nilainya.",
 "persamaan adalah kalimat matematika yang menyatakan dua sisi bernilai sama.",
 "geometri mempelajari bentuk, ukuran, dan sifat ruang seperti segitiga dan lingkaran.",
 "luas persegi panjang adalah panjang kali lebar, kelilingnya dua kali jumlah panjang dan lebar.",
 "statistika mengolah data untuk menemukan pola, rata-rata, dan kecenderungan.",
 "matematika melatih cara berpikir logis dan sistematis yang berguna di kehidupan sehari-hari.",
 "urutan operasi hitung: kurung dulu, lalu kali dan bagi, terakhir tambah dan kurang.",
]

D["fisika"] = [
 "fisika adalah ilmu yang mempelajari materi, energi, dan interaksi keduanya di alam semesta.",
 "hukum newton pertama: benda tetap diam atau bergerak lurus beraturan kecuali ada gaya luar.",
 "gaya adalah tarikan atau dorongan yang bisa mengubah gerak suatu benda.",
 "energi tidak bisa diciptakan atau dimusnahkan, hanya berubah bentuk.",
 "kecepatan adalah jarak per waktu, sedangkan percepatan adalah perubahan kecepatan.",
 "gravitasi adalah gaya tarik-menarik antar benda bermassa, membuat benda jatuh ke bumi.",
 "listrik mengalir karena adanya beda potensial dalam suatu rangkaian.",
 "cahaya adalah gelombang elektromagnetik yang bisa berperilaku sebagai partikel.",
 "termodinamika mempelajari panas dan perubahannya menjadi bentuk energi lain.",
 "hukum kekekalan momentum berlaku pada tumbukan antar benda.",
 "fisika kuantum menjelaskan perilaku partikel di skala atom yang tidak intuitif.",
]

D["kimia"] = [
 "kimia adalah ilmu tentang zat, struktur, sifat, dan perubahannya.",
 "atom adalah unit terkecil suatu unsur yang masih mempertahankan sifatnya.",
 "unsur terdiri dari satu jenis atom, sedangkan senyawa dari dua unsur atau lebih.",
 "tabel periodik menyusun unsur berdasarkan nomor atom dan sifat yang berulang.",
 "reaksi kimia mengubah zat pereaksi menjadi zat hasil dengan susunan baru.",
 "ikatan kimia menyatukan atom-atom, bisa berupa ikatan ionik atau kovalen.",
 "asam memiliki ph di bawah tujuh, sedangkan basa di atas tujuh.",
 "larutan adalah campuran homogen antara zat terlarut dan pelarut.",
 "hukum kekekalan massa menyatakan massa total tidak berubah dalam reaksi kimia.",
 "kimia organik mempelajari senyawa berbasis karbon yang banyak ada di makhluk hidup.",
 "stoikiometri menghitung perbandingan jumlah zat dalam suatu reaksi kimia.",
]

D["biologi"] = [
 "biologi adalah ilmu yang mempelajari makhluk hidup dan proses kehidupannya.",
 "sel adalah unit terkecil penyusun makhluk hidup yang dapat berfungsi mandiri.",
 "dna membawa informasi genetik yang menentukan sifat suatu organisme.",
 "fotosintesis adalah proses tumbuhan mengubah cahaya menjadi energi kimia.",
 "evolusi adalah perubahan sifat makhluk hidup secara bertahap dalam waktu panjang.",
 "ekosistem adalah hubungan timbal balik antara makhluk hidup dan lingkungannya.",
 "sistem peredaran darah mengangkut oksigen dan nutrisi ke seluruh tubuh.",
 "klasifikasi makhluk hidup membaginya ke dalam kingdom, filum, kelas, dan seterusnya.",
 "metabolisme adalah seluruh reaksi kimia yang terjadi dalam tubuh makhluk hidup.",
 "keanekaragaman hayati penting untuk keseimbangan alam dan kelangsungan hidup.",
 "genetika mempelajari bagaimana sifat diwariskan dari induk ke keturunannya.",
]

D["sejarah_sekolah"] = [
 "sejarah adalah catatan peristiwa masa lalu yang membentuk keadaan masa kini.",
 "mempelajari sejarah membantu kita memahami asal-usul dan menghindari kesalahan lama.",
 "peradaban kuno seperti mesir, yunani, dan romawi mewariskan banyak pengetahuan.",
 "nusantara punya kerajaan besar seperti sriwijaya dan majapahit yang berjaya di masanya.",
 "sumpah pemuda 1928 adalah tonggak persatuan bangsa indonesia.",
 "proklamasi kemerdekaan indonesia dibacakan pada 17 agustus 1945.",
 "revolusi industri mengubah cara manusia memproduksi barang dengan mesin.",
 "perang dunia mengubah peta politik dan kehidupan jutaan manusia di seluruh dunia.",
 "sumber sejarah bisa berupa dokumen, artefak, maupun cerita dari pelaku sejarah.",
 "kronologi membantu menyusun peristiwa sejarah secara berurutan dan masuk akal.",
 "sejarah mengajarkan bahwa keputusan hari ini akan jadi pelajaran bagi generasi mendatang.",
]

D["bahasa_inggris"] = [
 "bahasa inggris adalah bahasa internasional yang dipakai di banyak negara dan bidang.",
 "tenses menunjukkan waktu terjadinya suatu peristiwa, seperti masa lalu, kini, dan depan.",
 "present simple digunakan untuk kebiasaan dan fakta umum.",
 "past simple menyatakan kejadian yang sudah selesai di masa lalu.",
 "vocabulary atau kosakata bertambah dengan banyak membaca dan mendengar.",
 "pronunciation yang baik membantu orang lain memahami apa yang kita ucapkan.",
 "listening skill terlatih dengan sering mendengar podcast atau film berbahasa inggris.",
 "grammar adalah aturan struktur kalimat agar pesan tersampaikan dengan benar.",
 "berbicara dengan penutur asli adalah cara tercepat meningkatkan kelancaran.",
 "jangan takut salah saat belajar bahasa, kesalahan adalah bagian dari proses.",
 "idiom adalah ungkapan yang maknanya tidak bisa diterjemahkan kata per kata.",
]

D["ekonomi"] = [
 "ekonomi adalah ilmu tentang bagaimana manusia memenuhi kebutuhan dengan sumber daya terbatas.",
 "permintaan dan penawaran menentukan harga suatu barang di pasar.",
 "inflasi adalah kenaikan harga barang secara umum dalam suatu periode.",
 "kelangkaan terjadi karena kebutuhan manusia tidak terbatas sedangkan sumber daya terbatas.",
 "biaya peluang adalah nilai dari pilihan terbaik yang dikorbankan saat mengambil keputusan.",
 "pasar adalah tempat bertemunya penjual dan pembeli untuk bertransaksi.",
 "produk domestik bruto mengukur total nilai produksi suatu negara.",
 "kebijakan moneter diatur bank sentral untuk menjaga kestabilan nilai uang.",
 "perdagangan internasional memungkinkan negara saling bertukar barang dan jasa.",
 "ekonomi mikro fokus pada perilaku individu dan perusahaan, makro pada ekonomi secara keseluruhan.",
 "tabungan dan investasi membantu mempersiapkan kebutuhan di masa depan.",
]

D["logika_matematika"] = [
 "logika matematika menggunakan simbol dan aturan formal untuk menyatakan penalaran.",
 "pernyataan adalah kalimat yang bernilai benar atau salah, tapi tidak keduanya.",
 "konjungsi berarti dan, bernilai benar hanya jika kedua pernyataan benar.",
 "disjungsi berarti atau, bernilai benar jika salah satu atau keduanya benar.",
 "implikasi jika p maka q bernilai salah hanya jika p benar dan q salah.",
 "negasi membalik nilai kebenaran suatu pernyataan.",
 "bi-implikasi berarti jika dan hanya jika, benar bila keduanya bernilai sama.",
 "tabel kebenaran menunjukkan semua kemungkinan nilai dari suatu pernyataan majemuk.",
 "penarikan kesimpulan yang valid menjamin kebenaran jika premisnya benar.",
 "modus ponens: jika p maka q, dan p benar, maka q benar.",
]

D["aljabar"] = [
 "aljabar adalah cabang matematika yang memakai simbol untuk menyatakan bilangan yang belum diketahui.",
 "variabel adalah huruf yang mewakili suatu nilai yang bisa berubah-ubah.",
 "persamaan linear memiliki variabel berpangkat satu dan grafiknya berupa garis lurus.",
 "untuk menyelesaikan persamaan, lakukan operasi yang sama pada kedua sisi.",
 "koefisien adalah angka yang menempel pada variabel, seperti 3 pada 3x.",
 "konstanta adalah bilangan tetap yang tidak memiliki variabel.",
 "sistem persamaan diselesaikan dengan metode substitusi atau eliminasi.",
 "pertidaksamaan menyatakan hubungan lebih besar atau lebih kecil, bukan sama dengan.",
 "pemfaktoran mengubah bentuk penjumlahan menjadi perkalian faktor-faktor.",
 "fungsi memetakan setiap input ke tepat satu output.",
]

D["geometri"] = [
 "geometri adalah cabang matematika yang mempelajari bentuk, ukuran, dan posisi.",
 "segitiga punya tiga sisi dengan jumlah sudut dalamnya 180 derajat.",
 "lingkaran adalah himpunan titik yang berjarak sama dari satu titik pusat.",
 "luas lingkaran adalah phi kali jari-jari kuadrat.",
 "sudut siku-siku besarnya 90 derajat.",
 "bangun datar seperti persegi, persegi panjang, dan segitiga punya rumus luas masing-masing.",
 "bangun ruang seperti kubus dan balok memiliki volume.",
 "garis sejajar tidak akan pernah bertemu meski diperpanjang.",
 "teorema pythagoras menghubungkan sisi-sisi segitiga siku-siku.",
 "simetri berarti bentuk yang sama di kedua sisi suatu garis atau titik.",
]

D["kalkulus"] = [
 "kalkulus adalah cabang matematika yang mempelajari perubahan dan akumulasi.",
 "limit menggambarkan nilai yang didekati suatu fungsi saat input mendekati titik tertentu.",
 "turunan mengukur laju perubahan sesaat dari suatu fungsi.",
 "turunan posisi terhadap waktu adalah kecepatan.",
 "integral adalah kebalikan dari turunan dan menghitung luas di bawah kurva.",
 "integral tentu menghasilkan nilai luas pada selang tertentu.",
 "kalkulus banyak dipakai di fisika, teknik, dan ekonomi.",
 "titik maksimum dan minimum dicari dengan menyamakan turunan dengan nol.",
 "aturan rantai digunakan untuk menurunkan fungsi bersusun.",
 "konsep dasar kalkulus dikembangkan oleh newton dan leibniz.",
]

D["statistika"] = [
 "statistika adalah ilmu mengumpulkan, mengolah, dan menafsirkan data.",
 "rata-rata atau mean dihitung dengan menjumlahkan semua data lalu dibagi banyaknya.",
 "median adalah nilai tengah dari data yang sudah diurutkan.",
 "modus adalah nilai yang paling sering muncul dalam data.",
 "data bisa disajikan dalam tabel, diagram batang, atau grafik.",
 "standar deviasi mengukur seberapa tersebar data dari rata-ratanya.",
 "peluang menyatakan kemungkinan terjadinya suatu peristiwa.",
 "sampel adalah sebagian dari populasi yang diambil untuk diteliti.",
 "korelasi menunjukkan hubungan antara dua variabel.",
 "statistika membantu mengambil keputusan berdasarkan data, bukan sekadar tebakan.",
]

D["metodologi_riset"] = [
 "metodologi riset adalah cara sistematis untuk menjawab pertanyaan penelitian.",
 "rumusan masalah adalah pertanyaan inti yang ingin dijawab lewat penelitian.",
 "hipotesis adalah dugaan sementara yang akan diuji kebenarannya.",
 "penelitian kuantitatif mengolah data berupa angka dengan analisis statistik.",
 "penelitian kualitatif menggali makna lewat wawancara dan observasi mendalam.",
 "variabel bebas adalah yang memengaruhi, variabel terikat adalah yang dipengaruhi.",
 "validitas menunjukkan apakah alat ukur benar-benar mengukur yang dimaksud.",
 "reliabilitas menunjukkan konsistensi hasil pengukuran.",
 "studi pustaka mengumpulkan teori dari sumber-sumber ilmiah terdahulu.",
 "kesimpulan harus menjawab rumusan masalah berdasarkan hasil analisis.",
 "etika penelitian mengharuskan kejujuran data dan penghormatan pada responden.",
]

D["filsafat_ilmu"] = [
 "filsafat ilmu mempertanyakan dasar, metode, dan batasan dari ilmu pengetahuan.",
 "epistemologi adalah cabang filsafat yang membahas tentang pengetahuan dan kebenarannya.",
 "metode ilmiah mengandalkan observasi, hipotesis, eksperimen, dan verifikasi.",
 "falsifikasi menurut karl popper: teori ilmiah harus bisa dibuktikan salah.",
 "paradigma adalah kerangka berpikir yang dianut komunitas ilmiah pada suatu masa.",
 "sains berbeda dari opini karena berbasis bukti yang bisa diuji.",
 "objektivitas berarti berusaha menilai berdasarkan fakta, bukan perasaan.",
 "teori ilmiah adalah penjelasan yang didukung banyak bukti, bukan sekadar tebakan.",
 "perkembangan ilmu terjadi lewat pengujian dan penyempurnaan terus-menerus.",
 "kerendahan hati ilmiah berarti siap merevisi keyakinan jika ada bukti baru.",
]

D["empati"] = [
 "empati adalah kemampuan memahami dan merasakan apa yang dialami orang lain.",
 "berempati berarti menempatkan diri di posisi orang lain sebelum menghakimi.",
 "mendengarkan tanpa memotong adalah bentuk empati yang paling sederhana.",
 "empati berbeda dari simpati: empati ikut merasakan, simpati sekadar kasihan.",
 "validasi perasaan orang lain membuat mereka merasa didengar dan dihargai.",
 "empati membantu menyelesaikan konflik karena kita memahami sudut pandang lawan.",
 "terlalu larut dalam emosi orang lain bisa melelahkan, jaga juga kesehatan mental sendiri.",
 "empati bisa dilatih dengan membayangkan bagaimana rasanya berada di situasi orang lain.",
 "bahasa tubuh yang terbuka menunjukkan bahwa kita benar-benar hadir untuk orang lain.",
 "empati adalah fondasi dari hubungan yang hangat dan saling percaya.",
]

D["komunikasi"] = [
 "komunikasi adalah proses menyampaikan pesan agar dipahami oleh orang lain.",
 "komunikasi yang efektif butuh kejelasan pesan dan pendengar yang memperhatikan.",
 "komunikasi verbal lewat kata-kata, nonverbal lewat gestur dan ekspresi.",
 "aktif listening berarti benar-benar menyimak, bukan sekadar menunggu giliran bicara.",
 "feedback yang membangun disampaikan dengan jujur tapi tetap menghargai.",
 "pesan yang baik mempertimbangkan siapa penerimanya dan bagaimana cara menyampaikannya.",
 "miskomunikasi sering terjadi karena asumsi, jadi selalu klarifikasi bila ragu.",
 "nada bicara bisa mengubah makna kata, perhatikan intonasi saat berbicara.",
 "komunikasi asertif menyampaikan kebutuhan dengan tegas tanpa menyerang orang lain.",
 "di era digital, komunikasi tertulis juga perlu jelas agar tidak salah paham.",
]

D["psikologi_massa"] = [
 "psikologi massa mempelajari perilaku individu ketika berada dalam kerumunan.",
 "di dalam kerumunan, orang cenderung mengikuti emosi dan tindakan mayoritas.",
 "deindividuasi membuat seseorang merasa anonim sehingga bertindak di luar kebiasaan.",
 "penularan emosi terjadi cepat dalam kelompok besar.",
 "konformitas adalah kecenderungan menyesuaikan diri dengan norma kelompok.",
 "tekanan kelompok bisa membuat orang menyetujui hal yang sebenarnya ia ragukan.",
 "pemimpin yang karismatik bisa mengarahkan massa dengan kuat.",
 "fenomena bystander: semakin banyak orang, semakin kecil kemungkinan ada yang menolong.",
 "memahami psikologi massa membantu kita tidak mudah terbawa arus.",
 "berpikir mandiri penting agar tidak ikut-ikutan tanpa pertimbangan.",
]

D["kepercayaan_diri"] = [
 "kepercayaan diri adalah keyakinan pada kemampuan diri sendiri untuk menghadapi situasi.",
 "kepercayaan diri tumbuh dari pengalaman berhasil yang dikumpulkan sedikit demi sedikit.",
 "mengubah self-talk negatif jadi positif membantu membangun rasa percaya diri.",
 "persiapan yang matang membuat kita lebih tenang dan yakin saat tampil.",
 "membandingkan diri dengan orang lain terus-menerus justru mengikis percaya diri.",
 "terima kegagalan sebagai pelajaran, bukan vonis atas kemampuanmu.",
 "postur tubuh tegak dan kontak mata memancarkan kepercayaan diri.",
 "fokus pada kemajuan diri sendiri, bukan pada kesempurnaan.",
 "setiap orang punya kelebihan, temukan dan asah milikmu.",
 "kepercayaan diri yang sehat bukan berarti sombong, tapi nyaman menjadi diri sendiri.",
]

D["manajemen_stres"] = [
 "stres adalah respons tubuh dan pikiran terhadap tekanan atau tuntutan.",
 "stres ringan bisa memotivasi, tapi stres berkepanjangan merusak kesehatan.",
 "olahraga teratur membantu melepas ketegangan dan memperbaiki suasana hati.",
 "tidur cukup penting agar pikiran pulih dan emosi lebih stabil.",
 "teknik pernapasan dalam bisa menenangkan sistem saraf saat cemas.",
 "membagi tugas besar jadi bagian kecil membuatnya terasa lebih ringan.",
 "bercerita pada orang yang dipercaya membantu melegakan beban pikiran.",
 "belajar berkata tidak untuk hal yang melebihi kapasitas adalah bentuk menjaga diri.",
 "hobi dan waktu santai bukan pemborosan, tapi kebutuhan untuk keseimbangan.",
 "jika stres terasa berat dan lama, tidak ada salahnya mencari bantuan profesional.",
]

D["hubungan"] = [
 "hubungan yang sehat dibangun di atas kepercayaan, komunikasi, dan saling menghargai.",
 "komunikasi terbuka mencegah salah paham yang bisa merusak hubungan.",
 "setiap orang butuh ruang pribadi meski dalam hubungan yang dekat.",
 "konflik dalam hubungan itu wajar, yang penting cara menyelesaikannya.",
 "mendengarkan pasangan dengan tulus adalah bentuk cinta yang nyata.",
 "hubungan yang baik membuat kedua pihak tumbuh, bukan saling mengekang.",
 "meminta maaf dengan tulus dan memaafkan memperkuat ikatan.",
 "perhatian kecil yang konsisten lebih bermakna dari kejutan besar sesekali.",
 "kenali tanda hubungan yang tidak sehat agar bisa mengambil sikap.",
 "cinta yang dewasa adalah memilih untuk saling menjaga setiap hari.",
]

D["kepemimpinan"] = [
 "kepemimpinan adalah kemampuan mengarahkan dan menginspirasi orang menuju tujuan bersama.",
 "pemimpin yang baik memberi contoh, bukan sekadar memberi perintah.",
 "mendengarkan masukan tim membuat keputusan lebih matang dan anggota merasa dihargai.",
 "pemimpin bertanggung jawab atas kegagalan dan berbagi pujian saat berhasil.",
 "delegasi yang tepat mempercayai anggota dan mengembangkan kemampuan mereka.",
 "keputusan yang adil dan konsisten membangun kepercayaan tim.",
 "pemimpin yang visioner melihat jauh ke depan tapi tetap membumi dalam eksekusi.",
 "kecerdasan emosional penting bagi pemimpin untuk memahami anggota timnya.",
 "kritik yang membangun disampaikan untuk memperbaiki, bukan menjatuhkan.",
 "kepemimpinan adalah keterampilan yang terus diasah lewat pengalaman.",
]

D["blockchain"] = [
 "blockchain adalah teknologi pencatatan data terdistribusi yang sulit diubah.",
 "setiap blok berisi transaksi dan terhubung dengan blok sebelumnya membentuk rantai.",
 "desentralisasi membuat data tersimpan di banyak komputer sekaligus.",
 "transparansi blockchain memungkinkan siapa pun memverifikasi transaksi.",
 "konsensus adalah mekanisme agar semua pihak setuju pada keadaan data yang sama.",
 "proof of work dan proof of stake adalah dua mekanisme konsensus yang umum.",
 "blockchain dipakai tidak hanya untuk crypto, tapi juga logistik dan identitas digital.",
 "sekali data tercatat di blockchain, sangat sulit untuk diubah atau dihapus.",
 "smart contract mengeksekusi perjanjian secara otomatis tanpa perantara.",
 "keamanan blockchain bergantung pada kriptografi dan jaringan yang tersebar.",
]

D["konten_kreator"] = [
 "konten kreator adalah orang yang membuat karya untuk dibagikan ke audiens.",
 "temukan gaya unikmu agar konten berbeda dari yang lain.",
 "pahami siapa audiensmu dan apa yang mereka butuhkan.",
 "kualitas cerita seringkali lebih penting daripada alat yang mahal.",
 "jadwal yang konsisten membantu audiens tahu kapan menunggumu.",
 "belajar dari analitik untuk tahu konten mana yang paling disukai.",
 "kolaborasi dengan kreator lain membuka jangkauan audiens baru.",
 "jaga keaslian, audiens bisa merasakan mana yang tulus dan mana yang dibuat-buat.",
 "komentar negatif adalah bagian dari perjalanan, jangan biarkan menghentikanmu.",
 "nikmati prosesnya, karena konsistensi lahir dari kecintaan pada apa yang dibuat.",
]

D["media_sosial"] = [
 "media sosial adalah platform untuk berbagi dan berinteraksi secara daring.",
 "gunakan media sosial dengan bijak dan jaga jejak digitalmu.",
 "tidak semua yang viral itu benar, selalu cek fakta sebelum membagikan.",
 "bandingkan dirimu dengan standar media sosial hanya akan membuat tidak bahagia.",
 "algoritma menampilkan konten berdasarkan apa yang sering kamu lihat dan sukai.",
 "privasi itu penting, hati-hati membagikan data pribadi.",
 "media sosial bisa jadi alat belajar dan berkarya kalau dipakai dengan tepat.",
 "istirahat sejenak dari layar membantu menjaga kesehatan mental.",
 "berinteraksilah dengan positif, dunia maya tetap dihuni manusia nyata.",
 "manfaatkan media sosial untuk membangun sesuatu, bukan sekadar menghabiskan waktu.",
]

D["trading"] = [
 "trading adalah kegiatan jual beli aset untuk mendapat keuntungan dari selisih harga.",
 "analisis teknikal membaca pola grafik harga untuk memperkirakan arah pasar.",
 "analisis fundamental menilai nilai intrinsik berdasarkan kondisi bisnis atau ekonomi.",
 "manajemen risiko adalah kunci: tentukan batas kerugian sebelum masuk posisi.",
 "jangan gunakan uang kebutuhan pokok untuk trading.",
 "emosi seperti serakah dan takut sering jadi penyebab kerugian trader.",
 "diversifikasi mengurangi risiko dengan menyebar dana ke beberapa aset.",
 "trading butuh disiplin pada rencana yang sudah dibuat.",
 "pasar bisa bergerak tidak rasional, selalu siap dengan skenario terburuk.",
 "belajar terus dan catat setiap transaksi sebagai bahan evaluasi.",
]

D["investasi_saham"] = [
 "saham adalah bukti kepemilikan sebagian dari suatu perusahaan.",
 "investasi saham cocok untuk tujuan jangka panjang.",
 "keuntungan saham berasal dari kenaikan harga dan dividen.",
 "laporan keuangan membantu menilai kesehatan suatu perusahaan.",
 "investasi rutin dalam jumlah kecil lebih baik daripada menunggu modal besar.",
 "jangan menaruh semua dana di satu saham saja.",
 "saham blue chip adalah saham perusahaan besar yang relatif stabil.",
 "fluktuasi harga jangka pendek adalah hal biasa dalam investasi saham.",
 "pahami profil risikomu sebelum memilih instrumen investasi.",
 "investasi terbaik dimulai dengan ilmu, bukan ikut-ikutan.",
]

D["penulisan_kreatif"] = [
 "penulisan kreatif adalah seni menuangkan imajinasi dan gagasan ke dalam kata-kata.",
 "ide bisa datang dari mana saja, catat segera sebelum hilang.",
 "membaca berbagai genre memperkaya gaya dan wawasan menulis.",
 "tulis draf pertama tanpa terlalu banyak mengedit agar ide mengalir.",
 "revisi adalah tempat tulisan biasa menjadi luar biasa.",
 "deskripsi yang melibatkan pancaindera membuat tulisan lebih hidup.",
 "temukan suaramu sendiri, jangan hanya meniru penulis lain.",
 "menulis setiap hari, walau sedikit, membangun kebiasaan dan keterampilan.",
 "kritik yang membangun membantu penulis berkembang.",
 "cerita yang baik menyentuh perasaan pembacanya.",
]

D["storytelling"] = [
 "storytelling adalah seni menyampaikan cerita agar pendengar terlibat dan tergerak.",
 "cerita yang kuat punya tokoh, tujuan, rintangan, dan perubahan.",
 "pembukaan yang memikat menentukan apakah pendengar mau melanjutkan.",
 "konflik menciptakan ketegangan yang membuat cerita menarik diikuti.",
 "detail spesifik lebih membekas daripada gambaran umum.",
 "jeda dan intonasi saat bercerita membangun suasana.",
 "cerita personal yang jujur lebih mudah menyentuh hati.",
 "akhir cerita yang berkesan sering kali mengandung kejutan atau pelajaran.",
 "storytelling dipakai di presentasi, pemasaran, dan pengajaran.",
 "cerita lebih mudah diingat daripada sekadar daftar fakta.",
]

D["pengembangan_karakter"] = [
 "karakter yang kuat adalah fondasi karya fiksi yang hidup.",
 "beri karakter tujuan yang jelas dan alasan di balik tindakannya.",
 "kelemahan membuat karakter terasa manusiawi dan dekat dengan pembaca.",
 "perkembangan karakter terjadi ketika ia berubah akibat pengalaman dalam cerita.",
 "latar belakang karakter menjelaskan mengapa ia bersikap tertentu.",
 "dialog yang khas membedakan satu karakter dengan karakter lain.",
 "antagonis yang baik punya motivasi yang bisa dipahami, bukan sekadar jahat.",
 "tunjukkan sifat karakter lewat tindakan, bukan hanya deskripsi.",
 "konflik internal membuat karakter lebih dalam dan menarik.",
 "karakter pendukung yang kuat memperkaya dunia cerita.",
]

D["plot"] = [
 "plot adalah rangkaian peristiwa yang disusun membentuk suatu cerita.",
 "struktur tiga babak: pengenalan, konfrontasi, dan penyelesaian.",
 "inciting incident adalah peristiwa yang memicu perjalanan tokoh utama.",
 "klimaks adalah puncak ketegangan dari seluruh konflik cerita.",
 "foreshadowing memberi petunjuk halus tentang kejadian mendatang.",
 "plot twist yang baik mengejutkan tapi tetap masuk akal saat ditinjau ulang.",
 "pacing mengatur cepat lambatnya alur agar pembaca tetap terlibat.",
 "subplot menambah kedalaman tanpa mengaburkan cerita utama.",
 "resolusi menjawab konflik utama dan memberi penutup yang memuaskan.",
 "plot hole adalah lubang logika yang harus dihindari penulis.",
]

D["dialog_penulisan"] = [
 "dialog yang baik menggerakkan cerita dan mengungkap karakter sekaligus.",
 "setiap tokoh sebaiknya punya cara bicara yang khas dan konsisten.",
 "hindari dialog yang hanya berisi informasi tanpa emosi atau tujuan.",
 "subtext adalah makna tersembunyi di balik kata-kata yang diucapkan.",
 "dialog terasa natural jika dibaca keras-keras tanpa terasa janggal.",
 "tag ucapan seperti katanya jangan berlebihan agar tidak mengganggu.",
 "konflik kecil dalam dialog membuat percakapan lebih hidup.",
 "orang nyata sering tidak menjawab langsung, dialog bisa meniru itu.",
 "dialog yang terlalu sempurna justru terasa palsu.",
 "gunakan aksi di sela dialog untuk memperkaya adegan.",
]

D["filsafat_timur"] = [
 "filsafat timur mencakup pemikiran dari asia seperti konfusianisme, taoisme, dan buddhisme.",
 "konfusius menekankan pentingnya moral, keluarga, dan harmoni sosial.",
 "taoisme mengajarkan keselarasan dengan alam dan jalan kehidupan.",
 "buddhisme membahas tentang penderitaan dan jalan menuju kebebasan batin.",
 "konsep wu wei berarti bertindak selaras dengan aliran alami tanpa memaksakan.",
 "meditasi adalah praktik melatih kesadaran dan ketenangan pikiran.",
 "filsafat timur sering menekankan keseimbangan dan jalan tengah.",
 "zen menekankan pengalaman langsung di atas penjelasan konseptual.",
 "penghormatan pada leluhur dan tradisi adalah nilai penting di banyak budaya timur.",
 "filsafat timur mengajak manusia hidup selaras dengan diri, sesama, dan alam.",
]

D["psikologi_kepribadian"] = [
 "psikologi kepribadian mempelajari pola pikir, rasa, dan perilaku yang khas pada tiap orang.",
 "kepribadian terbentuk dari perpaduan bawaan dan pengalaman hidup.",
 "model big five menggambarkan kepribadian lewat keterbukaan, kehati-hatian, ekstraversi, keramahan, dan kestabilan emosi.",
 "introvert mengisi energi dari kesendirian, ekstrovert dari interaksi sosial.",
 "tidak ada kepribadian yang lebih baik, masing-masing punya kekuatan.",
 "memahami kepribadian sendiri membantu memilih lingkungan yang tepat.",
 "kepribadian bisa berkembang seiring waktu dan pengalaman.",
 "temperamen adalah kecenderungan bawaan yang terlihat sejak kecil.",
 "mengenali kepribadian orang lain memperbaiki cara kita berkomunikasi.",
 "kepribadian yang sehat ditandai kemampuan beradaptasi dan menjalin hubungan baik.",
]

D["bahasa_gaul"] = [
 "bahasa gaul adalah ragam bahasa santai yang dipakai dalam pergaulan sehari-hari.",
 "bahasa gaul terus berkembang mengikuti tren dan kreativitas anak muda.",
 "memakai bahasa gaul membuat obrolan terasa akrab dan cair.",
 "gunakan bahasa gaul pada situasi yang tepat, hindari di situasi formal.",
 "banyak bahasa gaul berasal dari serapan, singkatan, atau plesetan.",
 "bahasa gaul menunjukkan identitas dan kedekatan dalam suatu komunitas.",
 "walau santai, tetap jaga agar bahasa tidak menyakiti orang lain.",
 "memahami bahasa gaul membantu lebih nyambung saat mengobrol.",
 "bahasa gaul indonesia sangat kreatif dan cepat menyebar lewat media sosial.",
 "casper bisa memakai bahasa gaul supaya obrolan terasa hangat dan akrab.",
]

D["debat"] = [
 "debat adalah adu argumen terstruktur untuk mempertahankan pendapat.",
 "argumen yang kuat didukung bukti dan penalaran yang logis.",
 "dengarkan argumen lawan dengan saksama sebelum memberi tanggapan.",
 "rebuttal adalah sanggahan terhadap poin yang disampaikan lawan.",
 "sampaikan argumen dengan jelas, runtut, dan percaya diri.",
 "hindari menyerang pribadi, fokus pada isi argumennya.",
 "data dan contoh konkret memperkuat posisi yang kamu bela.",
 "antisipasi bantahan lawan dan siapkan jawabannya.",
 "debat yang sehat bertujuan mencari kebenaran, bukan sekadar menang.",
 "penutup yang kuat merangkum poin utama dan meninggalkan kesan.",
]

D["negosiasi"] = [
 "negosiasi adalah proses mencapai kesepakatan antara pihak dengan kepentingan berbeda.",
 "persiapan yang matang menentukan keberhasilan negosiasi.",
 "pahami kebutuhan dan batasan kedua belah pihak.",
 "fokus pada kepentingan, bukan sekadar posisi yang kaku.",
 "mendengarkan aktif membantu menemukan celah kesepakatan.",
 "tawar-menawar yang baik mencari solusi yang menguntungkan semua pihak.",
 "jangan terburu-buru, jeda bisa jadi alat yang efektif.",
 "kenali kapan harus berkompromi dan kapan harus bertahan.",
 "hubungan baik seringkali lebih berharga dari kemenangan sesaat.",
 "kesepakatan yang baik adalah yang ditaati dengan rela oleh semua pihak.",
]

D["public_speaking"] = [
 "public speaking adalah keterampilan berbicara di depan banyak orang.",
 "persiapan dan latihan adalah kunci tampil percaya diri.",
 "pembukaan yang kuat menarik perhatian sejak awal.",
 "kontak mata membuat audiens merasa dilibatkan.",
 "atur tempo bicara, jangan terlalu cepat agar pesan tersampaikan.",
 "gunakan cerita dan contoh agar pesan lebih mudah diingat.",
 "demam panggung itu wajar, ubah jadi energi dengan persiapan matang.",
 "bahasa tubuh yang terbuka memperkuat penyampaian pesan.",
 "tutup dengan pesan yang kuat dan mudah diingat.",
 "semakin sering tampil, semakin terampil dan tenang kamu.",
]

D["parenting"] = [
 "parenting adalah seni mendampingi dan mendidik anak dengan penuh kasih.",
 "anak belajar banyak dari mencontoh perilaku orang tuanya.",
 "komunikasi yang hangat membangun rasa aman pada anak.",
 "tetapkan aturan yang jelas dan konsisten dengan penuh pengertian.",
 "puji usaha anak, bukan hanya hasilnya, agar ia tumbuh tangguh.",
 "dengarkan perasaan anak tanpa langsung menghakimi.",
 "waktu berkualitas lebih berharga daripada hadiah mahal.",
 "setiap anak unik, kenali dan hargai keunikan masing-masing.",
 "orang tua juga perlu menjaga kesehatan mentalnya sendiri.",
 "kasih sayang yang konsisten adalah fondasi tumbuh kembang anak.",
]

D["karir"] = [
 "karir adalah perjalanan pekerjaan dan pengembangan diri seseorang.",
 "kenali minat dan kekuatanmu untuk memilih arah karir yang tepat.",
 "keterampilan terus diasah agar tetap relevan di dunia kerja.",
 "jejaring profesional membuka banyak peluang yang tak terduga.",
 "cv yang baik menonjolkan pencapaian, bukan hanya daftar tugas.",
 "persiapan wawancara meningkatkan peluang diterima kerja.",
 "jangan takut memulai dari bawah, yang penting terus berkembang.",
 "keseimbangan antara kerja dan hidup pribadi menjaga kesehatan jangka panjang.",
 "umpan balik adalah bahan bakar untuk berkembang lebih baik.",
 "karir yang memuaskan sejalan dengan nilai dan passion diri.",
]

D["wirausaha"] = [
 "wirausaha adalah kegiatan membangun usaha sendiri dengan keberanian dan kreativitas.",
 "ide bisnis lahir dari masalah yang butuh solusi.",
 "riset pasar membantu memahami apa yang benar-benar dibutuhkan pelanggan.",
 "mulai dari yang kecil dan validasi ide sebelum mengembangkan besar.",
 "manajemen keuangan yang rapi adalah napas sebuah usaha.",
 "kegagalan adalah pelajaran berharga bagi seorang wirausahawan.",
 "konsistensi dan ketekunan sering mengalahkan bakat semata.",
 "bangun hubungan baik dengan pelanggan dan mitra.",
 "adaptasi terhadap perubahan pasar menentukan kelangsungan usaha.",
 "wirausaha bukan hanya soal uang, tapi menciptakan nilai dan lapangan kerja.",
]

D["astronomi"] = [
 "astronomi adalah ilmu yang mempelajari benda-benda langit dan alam semesta.",
 "tata surya kita terdiri dari matahari dan planet-planet yang mengitarinya.",
 "bumi berputar pada porosnya menyebabkan siang dan malam.",
 "revolusi bumi mengelilingi matahari menyebabkan pergantian musim.",
 "galaksi bimasakti adalah rumah bagi tata surya kita.",
 "bintang adalah bola gas raksasa yang memancarkan cahaya dan panas.",
 "teleskop membantu manusia mengamati benda langit yang jauh.",
 "lubang hitam adalah wilayah dengan gravitasi sangat kuat.",
 "bulan adalah satelit alami bumi yang memengaruhi pasang surut.",
 "alam semesta terus mengembang sejak peristiwa dentuman besar.",
 "menjelajah antariksa membantu manusia memahami asal-usul dan masa depan.",
]

D["filsafat_hidup"] = [
 "makna hidup adalah sesuatu yang kita ciptakan lewat pilihan dan tindakan setiap hari.",
 "kebahagiaan sejati sering ditemukan dalam hal-hal sederhana dan hubungan yang hangat.",
 "hidup yang bermakna bukan yang tanpa masalah, tapi yang terus bertumbuh melewatinya.",
 "mensyukuri apa yang ada membuat hati lebih tenang dan cukup.",
 "tujuan hidup bisa berubah seiring waktu, dan itu hal yang wajar.",
 "menolong orang lain memberi rasa berarti yang mendalam.",
 "waktu adalah hal paling berharga, gunakan untuk yang benar-benar penting.",
 "menerima ketidaksempurnaan diri adalah awal dari kedamaian batin.",
 "hidup di saat ini lebih menenangkan daripada terus mencemaskan masa depan.",
 "warisan terbaik adalah kebaikan yang kita tanam pada orang lain.",
]

D["kesehatan_mental"] = [
 "kesehatan mental sama pentingnya dengan kesehatan fisik.",
 "tidak apa-apa untuk tidak baik-baik saja, yang penting mau mencari pertolongan.",
 "stres yang dikelola dengan baik menjaga pikiran tetap jernih.",
 "tidur, olahraga, dan nutrisi memengaruhi kondisi mental secara signifikan.",
 "berbicara dengan orang yang dipercaya membantu melegakan beban pikiran.",
 "mengenali tanda kelelahan mental adalah bentuk peduli pada diri sendiri.",
 "istirahat bukan kemalasan, tapi kebutuhan untuk pulih.",
 "membatasi perbandingan sosial menjaga kesehatan pikiran.",
 "jika terasa berat dan berkepanjangan, bantuan profesional adalah langkah berani.",
 "merawat kesehatan mental adalah investasi jangka panjang untuk hidup yang lebih baik.",
]

D["produktivitas"] = [
 "produktivitas adalah tentang menyelesaikan hal yang tepat, bukan sekadar sibuk.",
 "menentukan prioritas membantu fokus pada yang paling berdampak.",
 "memecah tugas besar jadi langkah kecil membuatnya lebih mudah dimulai.",
 "teknik pomodoro memakai fokus 25 menit diselingi istirahat singkat.",
 "menghindari multitasking berlebihan meningkatkan kualitas kerja.",
 "menetapkan batas waktu menciptakan dorongan untuk menyelesaikan.",
 "istirahat yang cukup justru menjaga produktivitas jangka panjang.",
 "menghilangkan distraksi seperti notifikasi membantu masuk ke fokus mendalam.",
 "meninjau kembali capaian di akhir hari memberi rasa progres.",
 "konsistensi kecil setiap hari mengalahkan ledakan usaha sesekali.",
]

# ===== bangun korpus =====
def buat_korpus(nama, kalimat_list, target=45000):
    blok=[]
    # format pernyataan
    for k in kalimat_list:
        blok.append(k)
    # format tanya-jawab
    for k in kalimat_list:
        q = k.split(" adalah ")[0].strip() if " adalah " in k else k.split(".")[0].strip()
        blok.append(f"tanya: apa itu {q.lower()}?\njawab: {k}")
    # format fakta
    for k in kalimat_list:
        blok.append(f"fakta: {k}")
    out=[]; total=0; i=0
    while total < target:
        b = blok[i % len(blok)]
        out.append(b); total += len(b)+2; i+=1
        if i > len(blok)*50: break
    random.shuffle(out)
    path=os.path.join(OUT,f"{nama}.txt")
    open(path,"w",encoding="utf-8").write("\n\n".join(out))
    return path, total

print(f"{'domain':22s} {'char':>8s}")
print("-"*32)
for nama, kalimat in D.items():
    path, tot = buat_korpus(nama, kalimat)
    print(f"{nama:22s} {tot:>8,d}")
print(f"\ntotal domain: {len(D)}")
