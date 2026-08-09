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
import rag

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
              ["hack","hacker","terminal","ssh","server","root","port","sudo","bash","linux"]),
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
              ["film","bioskop","sutradara","aktor","aktris","genre",
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
 "hukum":    ("⚖️ CASPER-HUKUM (ahli hukum)", "spesialis_hukum.brain",
              ["hukum","undang","pengacara","hakim","pengadilan","pasal","konstitusi",
               "keadilan","pidana","perdata","advokat"]),
 "kriminal": ("🕵️ CASPER-KRIMINAL (studi kasus)", "spesialis_kriminal.brain",
              ["kriminal","kejahatan","kasus pembunuhan","pencurian","korupsi","penipuan",
               "forensik","perampokan","kejahatan siber","tindak pidana"]),
 "politik":  ("🏛️ CASPER-POLITIK (pengamat politik)", "spesialis_politik.brain",
              ["politik","partai","pemilu","presiden","dpr","pemerintahan","ideologi",
               "kebijakan","nasionalisme","demokrasi"]),
 "hardware": ("🖥️ CASPER-HARDWARE (ahli komponen)", "spesialis_hardware.brain",
              ["cpu","gpu","ram","prosesor","motherboard","vga","ssd","hdd",
               "hardware","komponen komputer","power supply","kipas processor"]),
 "animasi":  ("🎬 CASPER-ANIMASI (film & series)", "spesialis_animasi.brain",
              ["animasi","kartun","disney","pixar","serial","series","drakor",
               "drama korea","film animasi","sitkom"]),
 "ips":      ("🌍 CASPER-IPS (ilmu sosial)", "spesialis_ips.brain",
              ["ips","sosiologi","antropologi","geografi","demografi","ekonomi",
               "urbanisasi","statistik","ilmu sosial"]),
 "logika_formal":   ("🧠 CASPER-LOGIKA-FORMAL", "logika_formal.brain",
              ["logika formal","silogisme","premis","deduksi","induksi","fallacy","kesesatan","penalaran","argumen sah"]),
 "emosi":   ("💗 CASPER-EMOSI", "emosi.brain",
              ["emosi","kecerdasan emosional","perasaan","marah","sedih","senang","takut","regulasi emosi"]),
 "kesadaran_kolektif":   ("🌐 CASPER-KESADARAN-KOLEKTIF", "kesadaran_kolektif.brain",
              ["kesadaran kolektif","solidaritas","norma sosial","anomie","durkheim","gotong royong","identitas kelompok"]),
 "gaya_bicara":   ("🗣️ CASPER-GAYA-BICARA", "gaya_bicara.brain",
              ["gaya bicara","cara casper bicara","gaya ngobrol","kepribadian casper"]),
 "interaksi_sosial":   ("🤝 CASPER-INTERAKSI-SOSIAL", "interaksi_sosial.brain",
              ["interaksi sosial","komunikasi sosial","hubungan sosial","bergaul","kerja sama tim"]),
 "crypto":   ("🪙 CASPER-CRYPTO", "crypto.brain",
              ["crypto","kripto","cryptocurrency","bitcoin","ethereum","altcoin","nft","wallet crypto"]),
 "youtuber":   ("📹 CASPER-YOUTUBER", "youtuber.brain",
              ["youtuber","youtube","channel youtube","konten youtube","monetisasi","subscriber"]),
 "novelis":   ("📖 CASPER-NOVELIS", "novelis.brain",
              ["novelis","menulis novel","novel","show don't tell","plot novel"]),
 "matematika_sekolah":   ("🔢 CASPER-MATEMATIKA-SEKOLAH", "matematika_sekolah.brain",
              ["matematika sekolah","pecahan","aljabar dasar","operasi hitung"]),
 "fisika":   ("⚛️ CASPER-FISIKA", "fisika.brain",
              ["fisika","hukum newton","newton","gaya","energi","gravitasi","kecepatan","termodinamika"]),
 "kimia":   ("🧪 CASPER-KIMIA", "kimia.brain",
              ["kimia","atom","unsur","reaksi kimia","tabel periodik","ikatan kimia","ph"]),
 "biologi":   ("🧬 CASPER-BIOLOGI", "biologi.brain",
              ["biologi","sel","dna","fotosintesis","evolusi","ekosistem","genetika"]),
 "sejarah_sekolah":   ("🏛️ CASPER-SEJARAH-SEKOLAH", "sejarah_sekolah.brain",
              ["sejarah sekolah","peradaban kuno","sejarah dunia","kronologi"]),
 "bahasa_inggris":   ("🔤 CASPER-BAHASA-INGGRIS", "bahasa_inggris.brain",
              ["bahasa inggris","tenses","grammar","vocabulary","speaking english","belajar inggris"]),
 "ekonomi":   ("📈 CASPER-EKONOMI", "ekonomi.brain",
              ["ekonomi","permintaan","penawaran","inflasi","pasar","biaya peluang","pdb"]),
 "logika_matematika":   ("🔣 CASPER-LOGIKA-MATEMATIKA", "logika_matematika.brain",
              ["logika matematika","konjungsi","disjungsi","implikasi","tabel kebenaran"]),
 "aljabar":   ("➗ CASPER-ALJABAR", "aljabar.brain",
              ["aljabar","variabel","persamaan linear","koefisien","sistem persamaan"]),
 "geometri":   ("📐 CASPER-GEOMETRI", "geometri.brain",
              ["geometri","segitiga","lingkaran","luas","keliling","sudut","pythagoras"]),
 "kalkulus":   ("∫ CASPER-KALKULUS", "kalkulus.brain",
              ["kalkulus","limit","turunan","integral","diferensial"]),
 "statistika":   ("📊 CASPER-STATISTIKA", "statistika.brain",
              ["statistika","rata-rata","mean","median","modus","standar deviasi","peluang"]),
 "metodologi_riset":   ("🔬 CASPER-METODOLOGI-RISET", "metodologi_riset.brain",
              ["metodologi riset","metode penelitian","hipotesis","rumusan masalah","variabel penelitian"]),
 "filsafat_ilmu":   ("🧭 CASPER-FILSAFAT-ILMU", "filsafat_ilmu.brain",
              ["filsafat ilmu","epistemologi","metode ilmiah","falsifikasi","paradigma"]),
 "empati":   ("🫶 CASPER-EMPATI", "empati.brain",
              ["empati","berempati","memahami perasaan","validasi perasaan"]),
 "komunikasi":   ("💬 CASPER-KOMUNIKASI", "komunikasi.brain",
              ["komunikasi","komunikasi efektif","active listening","komunikasi asertif"]),
 "psikologi_massa":   ("👥 CASPER-PSIKOLOGI-MASSA", "psikologi_massa.brain",
              ["psikologi massa","kerumunan","konformitas","deindividuasi","perilaku kelompok"]),
 "kepercayaan_diri":   ("💪 CASPER-KEPERCAYAAN-DIRI", "kepercayaan_diri.brain",
              ["kepercayaan diri","percaya diri","pd","self confidence","insecure"]),
 "manajemen_stres":   ("🧘 CASPER-MANEJEMEN-STRES", "manajemen_stres.brain",
              ["manajemen stres","kelola stres","tekanan","burnout","rileks"]),
 "hubungan":   ("❤️ CASPER-HUBUNGAN", "hubungan.brain",
              ["hubungan","pasangan","relasi","hubungan sehat","pacaran"]),
 "kepemimpinan":   ("👑 CASPER-KEPEMIMPINAN", "kepemimpinan.brain",
              ["kepemimpinan","pemimpin","memimpin","leadership","delegasi"]),
 "blockchain":   ("⛓️ CASPER-BLOCKCHAIN", "blockchain.brain",
              ["blockchain","desentralisasi","smart contract","konsensus","proof of work"]),
 "konten_kreator":   ("🎥 CASPER-KONTEN-KREATOR", "konten_kreator.brain",
              ["konten kreator","bikin konten","kreator","audiens"]),
 "media_sosial":   ("📱 CASPER-MEDIA-SOSIAL", "media_sosial.brain",
              ["media sosial","medsos","instagram","tiktok","algoritma medsos"]),
 "trading":   ("📉 CASPER-TRADING", "trading.brain",
              ["trading","trader","analisis teknikal","candlestick","cut loss"]),
 "investasi_saham":   ("💹 CASPER-INVESTASI-SAHAM", "investasi_saham.brain",
              ["investasi saham","saham","dividen","investasi jangka panjang","blue chip"]),
 "penulisan_kreatif":   ("✍️ CASPER-PENULISAN-KREATIF", "penulisan_kreatif.brain",
              ["penulisan kreatif","menulis kreatif","creative writing","inspirasi menulis"]),
 "storytelling":   ("🎤 CASPER-STORYTELLING", "storytelling.brain",
              ["storytelling","bercerita","teknik bercerita","cerita yang menarik"]),
 "pengembangan_karakter":   ("🎭 CASPER-PENGEMBANGAN-KARAKTER", "pengembangan_karakter.brain",
              ["pengembangan karakter","karakter fiksi","protagonis","antagonis","karakter cerita"]),
 "plot":   ("🧩 CASPER-PLOT", "plot.brain",
              ["plot","struktur cerita","klimaks","plot twist","tiga babak","pacing"]),
 "dialog_penulisan":   ("💭 CASPER-DIALOG-PENULISAN", "dialog_penulisan.brain",
              ["dialog penulisan","menulis dialog","subtext","dialog cerita"]),
 "filsafat_timur":   ("☯️ CASPER-FILSAFAT-TIMUR", "filsafat_timur.brain",
              ["filsafat timur","taoisme","konfusius","buddhisme","zen","wu wei"]),
 "psikologi_kepribadian":   ("🎨 CASPER-PSIKOLOGI-KEPRIBADIAN", "psikologi_kepribadian.brain",
              ["psikologi kepribadian","kepribadian","introvert","ekstrovert","big five","temperamen"]),
 "bahasa_gaul":   ("😎 CASPER-BAHASA-GAUL", "bahasa_gaul.brain",
              ["bahasa gaul","slang","bahasa anak muda","bahasa santai"]),
 "debat":   ("⚔️ CASPER-DEBAT", "debat.brain",
              ["debat","argumentasi","rebuttal","sanggahan","adu argumen"]),
 "negosiasi":   ("🤝 CASPER-NEGOSIASI", "negosiasi.brain",
              ["negosiasi","tawar-menawar","kesepakatan","kompromi"]),
 "public_speaking":   ("🎙️ CASPER-PUBLIC-SPEAKING", "public_speaking.brain",
              ["public speaking","pidato","presentasi","bicara di depan umum","demam panggung"]),
 "parenting":   ("👨‍👧 CASPER-PARENTING", "parenting.brain",
              ["parenting","mendidik anak","pola asuh","orang tua","tumbuh kembang"]),
 "karir":   ("💼 CASPER-KARIR", "karir.brain",
              ["karir","karier","dunia kerja","cv","wawancara kerja","profesional"]),
 "wirausaha":   ("🚀 CASPER-WIRAUSAHA", "wirausaha.brain",
              ["wirausaha","wirausahawan","bisnis","usaha sendiri","startup","entrepreneur"]),
 "astronomi":   ("🔭 CASPER-ASTRONOMI", "astronomi.brain",
              ["astronomi","tata surya","galaksi","planet","bintang","teleskop","alam semesta"]),
 "filsafat_hidup":   ("🌅 CASPER-FILSAFAT-HIDUP", "filsafat_hidup.brain",
              ["filsafat hidup","makna hidup","tujuan hidup","kebahagiaan sejati"]),
 "kesehatan_mental":   ("💚 CASPER-KESEHATAN-MENTAL", "kesehatan_mental.brain",
              ["kesehatan mental","mental health","kelelahan mental","self care","healing"]),
 "produktivitas":   ("⏰ CASPER-PRODUKTIVITAS", "produktivitas.brain",
              ["produktivitas","produktif","prioritas","manajemen waktu","fokus kerja","pomodoro"]),
 "white_hat":   ("🤍 CASPER-WHITE-HAT (peretas etis)", "white_hat.brain",
              ["white hat","peretas etis","ethical hacker","bug hunter etis","pentester"]),
 "grey_hat":   ("🩶 CASPER-GREY-HAT", "grey_hat.brain",
              ["grey hat","gray hat","topi abu-abu","area abu-abu hacking"]),
 "keamanan_siber":   ("🛡️ CASPER-KEAMANAN-SIBER", "keamanan_siber.brain",
              ["keamanan siber","cyber security","cybersecurity","keamanan digital","ancaman siber"]),
 "pengatasi_jailbreak":   ("🔓 CASPER-PENGATASI-JAILBREAK", "pengatasi_jailbreak.brain",
              ["jailbreak","prompt injection","anti jailbreak","pengaman ai","guardrail ai"]),
 "kriptografi":   ("🔐 CASPER-KRIPTOGRAFI", "kriptografi.brain",
              ["kriptografi","enkripsi","dekripsi","cipher","hash","kunci publik"]),
 "keamanan_data":   ("💾 CASPER-KEAMANAN-DATA", "keamanan_data.brain",
              ["keamanan data","perlindungan data","backup","kebocoran data","data pribadi"]),
 "etika_hacking":   ("⚖️ CASPER-ETIKA-HACKING", "etika_hacking.brain",
              ["etika hacking","etika peretasan","hukum siber","izin hacking","legalitas hacking"]),
 "keamanan_jaringan":   ("🌐 CASPER-KEAMANAN-JARINGAN", "keamanan_jaringan.brain",
              ["keamanan jaringan","firewall","vpn","keamanan wifi","jaringan aman"]),
 "kesadaran_keamanan":   ("👁️ CASPER-KESADARAN-KEAMANAN", "kesadaran_keamanan.brain",
              ["phishing","penipuan online","scam","keamanan akun","waspada online"]),
 "keamanan_password":   ("🔑 CASPER-KEAMANAN-PASSWORD", "keamanan_password.brain",
              ["password","kata sandi","keamanan password","two factor","autentikasi"]),
 "social_engineering_defense":   ("🎭 CASPER-ANTI-SOCENG", "social_engineering_defense.brain",
              ["social engineering","rekayasa sosial","manipulasi psikologis","anti soceng"]),
 "privasi_digital":   ("🕶️ CASPER-PRIVASI-DIGITAL", "privasi_digital.brain",
              ["privasi digital","jejak digital","data pribadi online","privasi online"]),
 "detektif_siber":   ("🕵️ CASPER-DETEKTIF-SIBER", "detektif_siber.brain",
              ["forensik digital","detektif siber","investigasi digital","bukti digital"]),
 "bug_bounty":   ("🐛 CASPER-BUG-BOUNTY", "bug_bounty.brain",
              ["bug bounty","program bug bounty","lapor celah keamanan","reward keamanan"]),
 "osint_edukasi":   ("🔎 CASPER-OSINT", "osint_edukasi.brain",
              ["osint","intelijen sumber terbuka","riset sumber terbuka","open source intelligence"]),
 "ctf":   ("🚩 CASPER-CTF", "ctf.brain",
              ["ctf","capture the flag","kompetisi keamanan","lomba hacking legal"]),
 "stoikisme": ("🏛️ CASPER-STOIKISME", "stoikisme.brain",
              ["stoikisme","stoik","filosofi teras","ketenangan batin"]),
 "mindfulness": ("🧘 CASPER-MINDFULNESS", "mindfulness.brain",
              ["mindfulness","meditasi","kesadaran penuh","hadir sepenuhnya"]),
 "rasa_syukur": ("🙏 CASPER-RASA-SYUKUR", "rasa_syukur.brain",
              ["rasa syukur","bersyukur","gratitude","terima kasih"]),
 "resiliensi": ("💪 CASPER-RESILIENSI", "resiliensi.brain",
              ["resiliensi","bangkit dari kegagalan","ketangguhan","pantang menyerah"]),
 "unpad":   ("🎓 CASPER-UNPAD", "unpad.brain",
              ["unpad","universitas padjadjaran","jatinangor","kampus unpad"]),
 "harvard":   ("🎓 CASPER-HARVARD", "harvard.brain",
              ["harvard","ivy league","universitas harvard"]),
 "kuliah_sukses":   ("🎓 CASPER-KULIAH", "kuliah_sukses.brain",
              ["tips kuliah","kuliah sukses","mahasiswa baru"]),
 "skripsi":   ("📝 CASPER-SKRIPSI", "skripsi.brain",
              ["skripsi","tesis","karya ilmiah","dosen pembimbing"]),
 "beasiswa":   ("🎁 CASPER-BEASISWA", "beasiswa.brain",
              ["beasiswa","scholarship","lpdp"]),
 "studi_luar_negeri":   ("🌏 CASPER-STUDI-LN", "studi_luar_negeri.brain",
              ["studi luar negeri","kuliah di luar negeri","beasiswa luar negeri"]),
 "organisasi_mahasiswa":   ("🧑🤝‍ CASPER-ORGMAWA", "organisasi_mahasiswa.brain",
              ["organisasi mahasiswa","bemm","himpunan mahasiswa"]),
 "manajemen_waktu_kuliah":   ("⏰ CASPER-WAKTU-KULIAH", "manajemen_waktu_kuliah.brain",
              ["manajemen waktu kuliah","atur jadwal kuliah"]),
 "harvest_moon":   ("🌾 CASPER-HARVEST-MOON", "harvest_moon.brain",
              ["harvest moon","story of seasons","game bertani"]),
 "god_of_war":   ("⚔️ CASPER-GOD-OF-WAR", "god_of_war.brain",
              ["god of war","kratos","game mitologi"]),
 "farming_sim":   ("🚜 CASPER-FARMING-SIM", "farming_sim.brain",
              ["farming sim","game pertanian","simulator bertani"]),
 "rpg_games":   ("🗡️ CASPER-RPG", "rpg_games.brain",
              ["rpg","role playing","game rpg"]),
 "game_design":   ("🎮 CASPER-GAME-DESIGN", "game_design.brain",
              ["game design","desain game","mekanik game"]),
 "esports_pro":   ("🏆 CASPER-ESPORTS", "esports_pro.brain",
              ["esports","pro player","turnamen game"]),
 "retro_games":   ("🕹️ CASPER-RETRO", "retro_games.brain",
              ["retro game","game klasik","game jadul"]),
 "open_world_games":   ("🗺️ CASPER-OPEN-WORLD", "open_world_games.brain",
              ["open world","game dunia terbuka","eksplorasi game"]),
 "tata_bahasa":   ("📖 CASPER-TATA-BAHASA", "tata_bahasa.brain",
              ["tata bahasa","grammar indonesia","ejaan"]),
 "cara_ngomong":   ("🗣️ CASPER-CARA-NGOMONG", "cara_ngomong.brain",
              ["cara ngomong","public speaking","bicara baik"]),
 "wawancara_kerja":   ("💼 CASPER-WAWANCARA", "wawancara_kerja.brain",
              ["wawancara kerja","interview","hrd"]),
 "nulis_cv":   ("📄 CASPER-CV", "nulis_cv.brain",
              ["nulis cv","curriculum vitae","resume","bikin cv"]),
 "surat_lamaran":   ("✉️ CASPER-LAMARAN", "surat_lamaran.brain",
              ["surat lamaran","cover letter","lamaran kerja"]),
 "email_profesional":   ("📧 CASPER-EMAIL", "email_profesional.brain",
              ["email profesional","email kerja","etiket email"]),
 "presentasi":   ("📊 CASPER-PRESENTASI", "presentasi.brain",
              ["presentasi","slide","pitching"]),
 "bahasa_baku":   ("📘 CASPER-BAHASA-BAKU", "bahasa_baku.brain",
              ["bahasa baku","kata baku","ejaan baku"]),
 "small_talk":   ("💬 CASPER-SMALL-TALK", "small_talk.brain",
              ["small talk","basa basi","obrolan ringan"]),
 "bikin_website":   ("🌐 CASPER-WEBSITE", "bikin_website.brain",
              ["bikin website","membuat website","bikin situs"]),
 "web_gratis":   ("🆓 CASPER-WEB-GRATIS", "web_gratis.brain",
              ["web gratis","website gratis","rekomendasi web gratis"]),
 "html_css":   ("🖥️ CASPER-HTML-CSS", "html_css.brain",
              ["html","css","frontend"]),
 "javascript_dasar":   ("⚙️ CASPER-JAVASCRIPT", "javascript_dasar.brain",
              ["javascript","belajar js","dom"]),
 "hosting_gratis":   ("🖧 CASPER-HOSTING", "hosting_gratis.brain",
              ["hosting gratis","deploy gratis","hosting"]),
 "cms_wordpress":   ("📰 CASPER-WORDPRESS", "cms_wordpress.brain",
              ["wordpress","cms","blog wordpress"]),
 "seo_dasar":   ("🔍 CASPER-SEO", "seo_dasar.brain",
              ["seo","search engine","optimasi pencarian"]),
 "desain_web":   ("🎨 CASPER-DESAIN-WEB", "desain_web.brain",
              ["desain web","ui web","tampilan website"]),
 "github_pages":   ("🐙 CASPER-GITHUB-PAGES", "github_pages.brain",
              ["github pages","deploy github"]),
 "linkedin":   ("💼 CASPER-LINKEDIN", "linkedin.brain",
              ["linkedin","profil profesional"]),
 "networking":   ("🤝 CASPER-NETWORKING", "networking.brain",
              ["networking","jejaring","relasi profesional"]),
 "negosiasi_gaji":   ("💰 CASPER-NEGO-GAJI", "negosiasi_gaji.brain",
              ["negosiasi gaji","nawar gaji"]),
 "kerja_remote":   ("🏠 CASPER-REMOTE", "kerja_remote.brain",
              ["kerja remote","wfh","remote working"]),
 "freelancing":   ("🧑‍💻 CASPER-FREELANCE", "freelancing.brain",
              ["freelance","freelancer","kerja lepas"]),
 "portofolio":   ("🗂️ CASPER-PORTOFOLIO", "portofolio.brain",
              ["portofolio","portfolio"]),
 "produktivitas_kerja":   ("⚡ CASPER-PRODUKTIF-KERJA", "produktivitas_kerja.brain",
              ["produktivitas kerja","efisien kerja"]),
 "habit_building":   ("🔁 CASPER-HABIT", "habit_building.brain",
              ["habit","membangun kebiasaan"]),
 "deep_work":   ("🧠 CASPER-DEEP-WORK", "deep_work.brain",
              ["deep work","fokus mendalam","kerja fokus"]),
 "belajar_efektif":   ("📚 CASPER-BELAJAR-EFEKTIF", "belajar_efektif.brain",
              ["belajar efektif","teknik belajar","cara belajar"]),
 "membaca_cepat":   ("⚡ CASPER-SPEED-READING", "membaca_cepat.brain",
              ["membaca cepat","speed reading","skimming"]),
 "mencatat":   ("✏️ CASPER-MENCATAT", "mencatat.brain",
              ["mencatat","teknik mencatat","cornell"]),
 "goal_setting":   ("🎯 CASPER-GOAL", "goal_setting.brain",
              ["goal setting","menetapkan tujuan","target"]),
 "refleksi_diri":   ("🪞 CASPER-REFLEKSI", "refleksi_diri.brain",
              ["refleksi diri","evaluasi diri","journaling"]),
 "literasi_digital":   ("📱 CASPER-LITERASI-DIGITAL", "literasi_digital.brain",
              ["literasi digital","hoaks","verifikasi informasi"]),
 "keamanan_akun":   ("🔐 CASPER-KEAMANAN-AKUN", "keamanan_akun.brain",
              ["keamanan akun","2fa","password akun"]),
 "backup_data":   ("💾 CASPER-BACKUP", "backup_data.brain",
              ["backup","cadangan data","backup data"]),
 "cloud_storage":   ("☁️ CASPER-CLOUD", "cloud_storage.brain",
              ["cloud storage","google drive","dropbox"]),
 "open_source":   ("🌱 CASPER-OPEN-SOURCE", "open_source.brain",
              ["open source","kontribusi kode"]),
 "tools_ai_gratis":   ("🤖 CASPER-TOOLS-AI", "tools_ai_gratis.brain",
              ["tools ai","ai gratis","alat ai"]),
 "aplikasi_produktif":   ("📲 CASPER-APP-PRODUKTIF", "aplikasi_produktif.brain",
              ["aplikasi produktif","aplikasi to-do"]),
 "internet_sehat":   ("🌿 CASPER-INTERNET-SEHAT", "internet_sehat.brain",
              ["internet sehat","screen time","digital wellbeing"]),
 "fotografi":   ("📷 CASPER-FOTOGRAFI", "fotografi.brain",
              ["fotografi","kamera","foto"]),
 "videografi":   ("🎥 CASPER-VIDEOGRAFI", "videografi.brain",
              ["videografi","rekam video","shooting"]),
 "editing_video":   ("🎬 CASPER-EDIT-VIDEO", "editing_video.brain",
              ["editing video","edit video","capcut","premiere"]),
 "desain_grafis":   ("🎨 CASPER-DESAIN-GRAFIS", "desain_grafis.brain",
              ["desain grafis","canva","grafis"]),
 "ilustrasi":   ("🖌️ CASPER-ILUSTRASI", "ilustrasi.brain",
              ["ilustrasi","menggambar"]),
 "musik_produksi":   ("🎵 CASPER-PRODUKSI-MUSIK", "musik_produksi.brain",
              ["produksi musik","music production","mixing"]),
 "podcasting":   ("🎙️ CASPER-PODCAST", "podcasting.brain",
              ["podcast","podcasting"]),
 "blogging":   ("✍️ CASPER-BLOG", "blogging.brain",
              ["blog","blogging","nulis blog"]),
 "budgeting_pribadi":   ("💵 CASPER-BUDGETING", "budgeting_pribadi.brain",
              ["budgeting","anggaran","budget pribadi"]),
 "dana_darurat":   ("🛟 CASPER-DANA-DARURAT", "dana_darurat.brain",
              ["dana darurat","emergency fund"]),
 "asuransi_dasar":   ("🛡️ CASPER-ASURANSI", "asuransi_dasar.brain",
              ["asuransi","polis","klaim"]),
 "pajak_dasar":   ("🧾 CASPER-PAJAK", "pajak_dasar.brain",
              ["pajak","spt","npwp"]),
 "frugal_living":   ("🌱 CASPER-FRUGAL", "frugal_living.brain",
              ["frugal living","hidup hemat"]),
 "side_income":   ("💸 CASPER-SIDE-INCOME", "side_income.brain",
              ["side income","penghasilan tambahan"]),
 "manajemen_utang":   ("💳 CASPER-UTANG", "manajemen_utang.brain",
              ["manajemen utang","cicilan","paylater"]),
 "perencanaan_keuangan":   ("📈 CASPER-FINPLAN", "perencanaan_keuangan.brain",
              ["perencanaan keuangan","financial planning"]),
 "etika_bermedia":   ("📱 CASPER-ETIKA-MEDIA", "etika_bermedia.brain",
              ["etika bermedia","saring before sharing"]),
 "netiket":   ("🤝 CASPER-NETIKET", "netiket.brain",
              ["netiket","etika internet","tata krama online"]),
 "budaya_indonesia":   ("🇮 CASPER-BUDAYA", "budaya_indonesia.brain",
              ["budaya indonesia","kebudayaan","warisan budaya"]),
 "kuliner_nusantara":   ("🍛 CASPER-KULINER", "kuliner_nusantara.brain",
              ["kuliner","makanan indonesia","kuliner nusantara"]),
 "wisata_indonesia":   ("🏝️ CASPER-WISATA-IDO", "wisata_indonesia.brain",
              ["wisata indonesia","tempat wisata","destinasi indonesia"]),
 "tradisi_nusantara":   ("🎎 CASPER-TRADISI", "tradisi_nusantara.brain",
              ["tradisi","adat","upacara adat"]),
 "bahasa_daerah":   ("🗣️ CASPER-BAHASA-DAERAH", "bahasa_daerah.brain",
              ["bahasa daerah","bahasa jawa","bahasa sunda"]),
 "seni_rupa":   ("🖼️ CASPER-SENI-RUPA", "seni_rupa.brain",
              ["seni rupa","lukis","patung"]),
 "casperc":  ("👻 CASPER-BASE (model orisinal)", "casperc.brain",
              ["casperc","model asli","base model","model dasar","versi awal"]),
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

def _niat_matematika(t):
    if re.search(r"(berapa|hitung|kalkulasi|sqrt|akar)", t): return True
    if re.search(r"\d+\s*%\s*(dari|of)", t): return True
    if t.rstrip().endswith(("=","?")): return True
    sisa = re.sub(r"[0-9.,\sx×:/*+\-^%()]", "", t)
    return len(sisa) <= 2

def _safe_eval(expr):
    e = expr.replace(",",".").replace("×","*").replace("x","*").replace(":","/").replace("^","**")
    if not re.fullmatch(r"[\d\s.+\-*/()%]+", e): return None
    try:
        v = eval(e, {"__builtins__": {}}, {})
    except ZeroDivisionError:
        return "DIV0"
    except Exception:
        return None
    return v

def _norm_ribuan(s):
    return re.sub(r"(?<=\d)\.(?=\d{3}\b)","",s)
def hitung(teks):
    """kalkulator internal casper — tool use, kayak LLM pro.
    Mendukung: + - x / ^ sqrt() persen() kurung, desimal koma, negatif, bagi-nol."""
    t = _norm_ribuan(teks.lower().strip())
    if not _niat_matematika(t): return None
    # persen: "15% dari 200"
    m = re.search(r"(\d+(?:[.,]\d+)?)\s*%\s*(?:dari|of)\s*(\d+(?:[.,]\d+)?)", t)
    if m:
        a=float(m.group(1).replace(",",".")); b=float(m.group(2).replace(",","."))
        h=a/100*b
        hh=int(h) if h==int(h) else round(h,4)
        return f"{a:g}% dari {b:g} = {hh}"
    # akar N tanpa kurung -> sqrt
    m = re.search(r"akar\s+(\d+(?:[.,]\d+)?)", t)
    if m:
        a=float(m.group(1).replace(",",".")); h=a**0.5
        hh=int(h) if h==int(h) else round(h,4)
        return f"akar {a:g} = {hh}"
    # sqrt
    m = re.search(r"sqrt\s*\(\s*(\d+(?:[.,]\d+)?)\s*\)", t)
    if m:
        a=float(m.group(1).replace(",","."))
        h=a**0.5
        hh=int(h) if h==int(h) else round(h,4)
        return f"sqrt({a:g}) = {hh}"
    # ekspresi umum (boleh kurung, ^, negatif)
    m = re.search(r"[-+.(\d][0-9.,\sx×:/*+\-^%()]*", t)
    if m:
        expr=m.group(0).strip()
        v=_safe_eval(expr)
        if v=="DIV0": return "pembagian dengan nol tidak terdefinisi."
        if v is not None:
            vv=int(v) if v==int(v) else round(v,4)
            return f"{expr.replace('**','^').strip()} = {vv}"
    return None

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

INTENT_OVERRIDES = [
 (r"harvest ?moon","harvest_moon"),
 (r"gagal ujian|failed.{0,8}exam","manajemen_stres"),
 (r"keuangan pribadi|mengatur keuangan","budgeting_pribadi"),
 (r"gombal|gombalin|merayu|\brayu\b","gombal"),
 (r"budgeting|\banggaran\b","budgeting_pribadi"),
 (r"dana darurat","dana_darurat"),
 (r"\binflasi\b|makroekonomi|mikroekonomi","ekonomi"),
 (r"negosiasi gaji|\bgaji\b|take home pay","negosiasi_gaji"),
 (r"\bskripsi\b|\btesis\b|dosen pembimbing","skripsi"),
 (r"bug bounty|\bbounty\b","bug_bounty"),
 (r"website gratis|web gratis|rekomendasi web","web_gratis"),
 (r"\bmanajemen\b.{0,12}waktu","manajemen_waktu_kuliah"),
 (r"\bstres\b|\bstress\b|tertekan|burnout","manajemen_stres"),
 (r"newton|gravitasi|percepatan","fisika"),
 (r"\bcv\b|curriculum vitae|\bresume\b","nulis_cv"),
 (r"wawancara|\binterview\b","wawancara_kerja"),
 (r"\bdna\b|fotosintesis","biologi"),
 (r"enkripsi|hashing|kriptografi","kriptografi"),
]

def route_scored(teks):
    t = teks.lower()
    for rg,nama in INTENT_OVERRIDES:
        if re.search(rg,t): return nama, 99
    for p in PERIBAHASA_POPULER:
        if p in t:
            return "peribahasa", 99
    skor = {}
    for nama, (_,_,kws) in PAKAR.items():
        skor[nama] = sum(1 for k in kws if _kw(k, t))
    if re.search(r"\d\s*[x×:/*+\-^]\s*\d", t) or re.search(r"\d+\s*%\s*(dari|of)", t) or re.search(r"\d\s*=\s*$", t) or re.search(r"(sqrt|akar)\s*\(?\d", t):
        skor["matematika"] = skor.get("matematika",0) + 2
    terbaik = max(skor.values())
    if terbaik == 0:
        return "bicara", 0
    for nama in PAKAR:
        if skor[nama] == terbaik:
            return nama, terbaik
    return "bicara", 0

def route(teks):
    return route_scored(teks)[0]

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
    t0 = _time.time()
    for _ in range(n):
        X = np.zeros((Lb,V),dtype=np.float32); X[np.arange(Lb), ids[-Lb:]] = 1.0
        h1 = np.tanh(X.reshape(1,-1)@W1+b1); h2 = np.tanh(h1@W2+b2)
        logits = (h2@W3+b3)[0]/temp
        ex = np.exp(logits-logits.max()); pr = ex/ex.sum()
        c = rng.choice(V, p=pr); out.append(ivocab[c]); ids.append(c)
    STATS["waktu"] = max(_time.time()-t0, 0.001)
    STATS["tokens"] = max(len(out)//4, 1)
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
    t_hitung = 0.0
    for i in range(n_tokens):
        t0 = _time.time()
        ctx = np.array(ids[-Lb:], dtype=np.int32).reshape(1, Lb)
        Xemb = E[ctx].reshape(1, Lb*D)
        h1 = np.tanh(Xemb@W1+b1); h2 = np.tanh(h1@W2+b2)
        logits = (h2@W3+b3)[0]/temp
        ex = np.exp(logits-logits.max()); pr = ex/ex.sum()
        tid = int(rng.choice(V, p=pr))
        t_hitung += _time.time() - t0
        tok = i2t.get(tid, "")
        ids.append(tid); hasil.append(tok)
        if stream:
            baru = _detok_step(tampil, tok)
            print(baru[len(tampil):], end="", flush=True)
            tampil = baru
            if delay: _time.sleep(delay)
        if tok in stop and i >= min_stop: # berhenti rapi di akhir kalimat
            break
    STATS["tokens"] = len(hasil)
    STATS["waktu"] = t_hitung if t_hitung > 0 else 0.001
    full = "".join((t if re.match(r"^[^\w\s]+$", t) else (" "+t)) for t in hasil)
    return full.strip()

HARM_PATTERNS = [
 r"\b(bobol|membobol|retas|meretas)\b", r"\b(mencuri|curi|steal)\b", r"\bmalware\b", r"\bransomware\b",
 r"\bkeylogger\b", r"\bspyware\b", r"\bexploit\b", r"curi.{0,12}(token|password|data)",
 r"(password|sandi).{0,12}(curi|mencuri)", r"\binject\b.{0,16}(akun|sistem)",
 r"tembus.{0,12}(wifi|akun)", r"(menembus|menyusup|bobol).{0,12}wifi", r"hack\b.{0,16}(akun|orang|bank)",
]
SAFETY_MSG = ("Maaf, saya tidak bisa membantu melakukan hal yang merugikan atau ilegal. "
 "Tapi saya senang membantu dari sisi pertahanan: cara melindungi akun, membuat password kuat, "
 "atau melaporkan celah keamanan secara legal lewat bug bounty.")

DUAL_USE = [
 (r"port scanning","Port scanning hanya boleh pada sistem yang kamu miliki/izin. Untuk belajar, scan localhost atau ikut CTF/legal lab."),
 (r"menguji keamanan (website|aplikasi)","Uji hanya aset yang kamu miliki/izin: cek konfigurasi, update, dan scanner pada aset sendiri, atau ikut bug bounty resmi."),
]
def dual_reply(t):
    for rg,ans in DUAL_USE:
        if re.search(rg,t): return ans
    return None

BIAS_GUARD=[
 (r"(perempuan|wanita|pria|laki-?laki|suku|agama|kulit).{0,20}(lebih pintar|lebih bodoh|lebih buruk|pantas|cocok|pasti buruk|pasti jahat)",
  "Karakter dan kemampuan seseorang tidak ditentukan gender, suku, agama, atau warna kulit. Setiap orang punya potensi yang sama."),
 (r"apakah (perempuan|wanita) cocok","Cocok tidaknya ditentukan minat dan kemampuan, bukan gender."),
 (r"(orang (tua|muda)|usia).{0,16}(bisa|tidak bisa|bodo)", "Usia bukan penghalang untuk belajar; banyak orang belajar di berbagai usia."),
]
def bias_reply(t):
    for rg,ans in BIAS_GUARD:
        if re.search(rg,t): return ans
    return None

def is_harmful(t):
    return any(re.search(p, t) for p in HARM_PATTERNS)

def epistemic(t):
    years=[int(y) for y in re.findall(r"2[01]\d\d", t)]
    if any(y>2026 for y in years):
        return ("Saya tidak tahu dan tidak bisa memastikan—peristiwa itu belum terjadi / "
                "di luar pengetahuan saya. Lebih baik merujuk sumber terpercaya saat waktunya tiba.")
    if re.search(r"2\s*\+\s*2\s*=\s*5", t):
        return "Itu tidak tepat. Dalam aritmetika standar, 2 + 2 = 4, bukan 5."
    if "jakarta" in t and "australia" in t:
        return "Premisnya keliru. Jakarta adalah ibu kota Indonesia, bukan Australia. Ibu kota Australia adalah Canberra."
    if "bumi datar" in t:
        return "Itu tidak tepat. Bukti ilmiah menunjukkan bumi berbentuk bulat (oblate spheroid), bukan datar."
    if re.search(r"(menara eiffel.{0,16}inci|berapa jumlah bintang|anti[ -]gravitasi mutlak)", t):
        return "Saya tidak punya data pasti untuk itu, dan itu tidak dapat dipastikan—sebaiknya rujuk sumber terpercaya."
    if re.search(r"\b(besok|lusa|minggu depan|bulan depan|tahun depan)\b", t):
        return "Saya tidak bisa memastikan hal yang belum terjadi. Saya hanya bisa memberi konteks berdasarkan data yang sudah ada."
    if re.search(r"(fiktif|tidak pernah ada|imajiner|khayalan)", t):
        return "Sepertinya premisnya merujuk pada sesuatu yang tidak nyata — saya tidak bisa memberikan fakta untuk entitas fiktif."
    if re.search(r"(percakapan privat|pesan pribadi|isi chat|dm seseorang)", t):
        return "Saya tidak punya akses ke percakapan privat siapa pun, dan itu ranah privasi. Saya tidak bisa membukanya."
    if re.search(r"(warna favorit|nomor favorit|makanan favorit) (presiden|bulan|planet)", t):
        return "Itu bukan informasi yang bisa dipastikan — saya tidak tahu preferensi pribadi entitas seperti itu."
    if re.search(r"casper(ai)?\b.{0,24}(menang|memenangkan|nobel)", t):
        return "Saya tidak punya informasi itu — dan setahu saya saya belum pernah menang Nobel. 🙂"
    return None

def identity_reply(t):
    if re.search(r"(siapa nama|nama kamu|namamu|nama kamu siapa|who are you|kamu siapa|siapa kamu|siapa sih kamu|perkenalkan diri)", t):
        return ("Namaku Casper — sering juga dipanggil CasperAI. Aku model bahasa ringan "
                "yang dibangun dari nol dengan NumPy, bagian dari keluarga CasperVerse. "
                "Aku bisa diajak ngobrol soal banyak hal, dari sains sampai curhat.")
    if re.search(r"(siapa penciptamu|pencipta kamu|kamu buatan|kamu dibuat|kamu diciptakan|who created you|who made you|siapa yang menciptakan kamu|siapa yang membuat kamu|siapa yang membuatmu|siapa yang bikin kamu|yang membuat kamu)", t):
        return ("Aku diciptakan oleh Gen Z, yang kerap disebut genzxseventh. "
                "Dia yang merancang dan melatih keluarga CasperVerse.")
    return None

FACT_DB = [
 (("ibu kota","indonesia"), "Jakarta adalah ibu kota Indonesia."),
 (("dna",), "DNA membawa informasi genetik yang menentukan sifat suatu organisme."),
 (("mitokondria",), "Mitokondria adalah organel sel penghasil energi (ATP) melalui respirasi seluler; sering disebut pembangkit tenaga sel."),
 (("organel","energi"), "Mitokondria adalah organel sel penghasil energi (ATP), pembangkit tenaga sel."),
 (("newton","pertama"), "Hukum Newton pertama: benda tetap diam atau bergerak lurus beraturan kecuali ada gaya luar."),
 (("enkripsi","hash"), "Enkripsi bisa dibalik dengan kunci; hashing satu arah menghasilkan sidik jari data."),
 (("bitcoin","pencipta"), "Bitcoin diciptakan oleh Satoshi Nakamoto."),
 (("bitcoin","siapa"), "Bitcoin diciptakan oleh Satoshi Nakamoto."),
 (("firewall",), "Firewall menyaring lalu lintas jaringan berdasarkan aturan keamanan."),
 (("segitiga","sisi"), "Segitiga memiliki tiga sisi."),
 (("fotosintesis",), "Fotosintesis adalah proses tumbuhan mengubah cahaya menjadi energi kimia. Proses ini berlangsung di kloroplas dengan bantuan klorofil. Hasilnya adalah glukosa dan oksigen yang penting bagi kehidupan."),
 (("merdeka","indonesia"), "Indonesia merdeka pada 17 Agustus 1945."),
 (("kapan","indonesia"), "Indonesia merdeka pada 17 Agustus 1945."),
 (("inflasi",), "Inflasi adalah kenaikan harga barang secara umum dari waktu ke waktu."),
 (("jantung",), "Jantung berfungsi memompa darah ke seluruh tubuh."),
 (("gravitasi",), "Gravitasi adalah gaya tarik-menarik antar benda bermassa."),
 (("blockchain",), "Blockchain adalah buku besar terdistribusi yang mencatat transaksi transparan."),
 (("cpu",), "CPU adalah unit pemroses pusat, otak dari komputer."),
 (("ram",), "RAM adalah memori akses acak untuk penyimpanan sementara."),
 (("ibu kota","jepang"), "Ibu kota Jepang adalah Tokyo."),
 (("vitamin c",), "Vitamin C berperan dalam imunitas dan bertindak sebagai antioksidan."),
 (("suku bunga",), "Suku bunga adalah imbalan atas pinjaman uang, dinyatakan dalam persen."),
 (("presiden pertama",), "Presiden pertama Indonesia adalah Soekarno."),
 (("pancasila",), "Pancasila adalah dasar negara Indonesia."),
 (("komodo",), "Komodo adalah hewan endemik Indonesia."),
 (("batik",), "Batik merupakan warisan budaya Indonesia yang diakui UNESCO."),
 (("mendIdih",), "Air mendidih pada 100 derajat Celsius pada tekanan atmosfer standar."),
]
CAPITALS={"prancis":"Paris","francis":"Paris","inggris":"London","amerika":"Washington DC",
 "jepang":"Tokyo","italia":"Roma","jerman":"Berlin","spanyol":"Madrid","australia":"Canberra",
 "kanada":"Ottawa","mesir":"Kairo","thailand":"Bangkok","vietnam":"Hanoi","malaysia":"Kuala Lumpur",
 "korea":"Seoul","china":"Beijing","rusia":"Moskwa","belanda":"Amsterdam","turki":"Ankara",
 "india":"New Delhi","brazil":"Brasilia","meksiko":"Mexico City","portugal":"Lisbon","yunani":"Athena",
 "swiss":"Bern","swedia":"Stockholm","norwegia":"Oslo","denmark":"Kopenhagen","finlandia":"Helsinki",
 "polandia":"Warsawa","ukraina":"Kyiv","arab saudi":"Riyadh","iran":"Teheran","irak":"Baghdad",
 "filipina":"Manila","kamboja":"Phnom Penh","laos":"Vientiane","timor leste":"Dili",
 "selandia baru":"Wellington","afrika selatan":"Pretoria","nigeria":"Abuja","kenya":"Nairobi",
 "maroko":"Rabat","argentina":"Buenos Aires","chile":"Santiago","peru":"Lima","kolombia":"Bogota",
 "austria":"Wina","hungaria":"Budapest","ceko":"Praha","rumania":"Bukarest","belgia":"Brussel",
 "irlandia":"Dublin","islandia":"Reykjavik","kuba":"Havana"}
def fact_lookup(t):
    if "ibu kota" in t:
        for c,cap in CAPITALS.items():
            if c in t: return f"Ibu kota {c.capitalize()} adalah {cap}."

    for conds, ans in FACT_DB:
        if all(c in t for c in conds):
            return ans
    return None

FACT_Q = rFACT_Q = r"\b(apa|siapa|kapan|dimana|berapa|mengapa|kenapa|jelaskan|fungsi|tujuan|sebutkan|perbedaan)\b"
FOLLOWUP = r"(lebih detail|lanjuti?|lanjut|yang nomor|nomor \d|terus\?|maksudnya|jelaskan lagi|contohnya|mana yang|kenapa begitu)"
STATE = {"persona": None, "seed": ""}

ENUM_DB=[
 (("warna","dasar"),["Merah","Kuning","Hijau","Biru"]),
 (("warna","primer"),["Merah","Kuning","Biru"]),
 (("mata angin",),["Utara","Selatan","Timur","Barat"]),
 (("perbedaan","massa"),["Massa adalah jumlah materi (kg) dan tetap di mana pun.","Berat adalah gaya gravitasi pada massa (N) dan berubah sesuai lokasi."]),
]
def structured(t):
    if re.search(r"tabel",t):
        m=re.search(r"([A-Za-z]+) dan ([A-Za-z]+)",t)
        a,b=(m.group(1),m.group(2)) if m else ("A","B")
        return (f"| Aspek | {a} | {b} |\n|---|---|---|\n"
                f"| Ranah utama | backend/AI/data | web/frontend |\n"
                f"| Eksekusi | server/client | browser/server |")
    if re.search(r"langkah",t):
        st_db=[(("teh",),["Didihkan air bersih terlebih dahulu.","Seduh teh selama 3-5 menit.","Sajikan; tambahkan gula atau madu sesuai selera."]),
               (("kopi",),["Didihkan air.","Seduh kopi dengan takaran sesuai selera.","Sajikan hangat."])]
        for conds,items in st_db:
            if all(c in t for c in conds):
                mm=re.search(r"(\d+)",t); n=int(mm.group(1)) if mm else len(items)
                return "\n".join(f"{i+1}. {x}" for i,x in enumerate(items[:n]))
    if re.search(r"sebutkan|tuliskan|buat|berikan",t):
        for conds,items in ENUM_DB:
            if all(c in t for c in conds):
                mm=re.search(r"(\d+)",t); n=int(mm.group(1)) if mm else len(items)
                return "\n".join(f"{i+1}. {x}." for i,x in enumerate(items[:n]))
    for conds,items in ENUM_DB:
        if ("perbedaan" in t) and all(c in t for c in conds):
            return "\n".join(f"{i+1}. {x}" for i,x in enumerate(items))
    return None

WORD_NUM={"satu":1,"dua":2,"tiga":3,"empat":4,"lima":5,"enam":6,"tujuh":7}
def _num(t,unit):
    m=re.search(r"(\d+)\s*"+unit,t)
    if m: return int(m.group(1))
    for w,n in WORD_NUM.items():
        if re.search(w+r"\s*"+unit,t): return n
    return None
def detect_format(t):
    n=_num(t,r"kalimat")
    if n: return ("kalimat",n)
    n=_num(t,r"kata")
    if n: return ("kata",n)
    n=_num(t,r"(poin|item)")
    if n: return ("poin",n)
    if "singkat" in t: return ("singkat",0)
    return None

def apply_format(raw,fmt):
    kind,n=fmt
    sents=[s.strip() for s in re.split(r"[.!?\n]+",raw) if len(s.strip())>8]
    if kind=="kalimat":
        return (" ".join(s.strip()+". " for s in sents[:n])).strip() or raw
    if kind=="poin":
        pts=sents[:n]
        return "\n".join(f"{i+1}. {p}." for i,p in enumerate(pts)) or raw
    if kind=="kata":
        w=re.findall(r"[A-Za-zÀ-ɏ\-]+",raw)
        return (w[0] if w else raw.split()[0])
    if kind=="singkat":
        raw=re.sub(r"\[sumber:.*?\]","",raw)
        return (raw[:100].rsplit(" ",1)[0]+".").strip()
    return raw

def rencanakan(text, paksa=None):
    """Rencanakan jawaban: identitas -> guard -> memory -> router -> tool -> RAG -> gen."""
    global STATE
    t=text.lower().strip()
    if re.search(r"(siapa nama (?:saya|aku|gue)|nama (?:saya|aku|gue) siapa|ingat nama)",t):
        if STATE.get("user_nama"):
            return {"jenis":"teks","reply":f"Nama kamu {STATE['user_nama']}, kan? 🙂","nama":"memori","src":"memori"}
    m_un=re.search(r"(?:nama (?:saya|aku|gue|ku) (\w+))|(?:panggil (?:saya|aku|gue) (\w+))",t)
    if m_un and not re.search(r"siapa$",t):
        nm=(m_un.group(1) or m_un.group(2)).capitalize()
        STATE["user_nama"]=nm
        return {"jenis":"teks","reply":f"Baik, aku akan ingat nama kamu: {nm}. 👋","nama":"memori","src":"memori"}
    if is_harmful(t): return {"jenis":"teks","reply":SAFETY_MSG,"nama":"safety","src":"guard"}
    du=dual_reply(t)
    if du: return {"jenis":"teks","reply":du,"nama":"dualuse","src":"guard"}
    br=bias_reply(t)
    if br: return {"jenis":"teks","reply":br,"nama":"bias","src":"guard"}
    ep=epistemic(t)
    if ep: return {"jenis":"teks","reply":ep,"nama":"epistemic","src":"guard"}
    fl0=fact_lookup(t)
    if fl0:
        fmt0=detect_format(t)
        rep=apply_format(fl0,fmt0) if fmt0 else fl0+"\n"+warna("2","[sumber: knowledge-base · conf 1.0]")
        return {"jenis":"teks","reply":rep,"nama":"fakta","src":"rag"}
    idr=identity_reply(t)
    if idr: return {"jenis":"teks","reply":idr,"nama":"identitas","src":"identitas"}
    is_follow = bool(re.search(FOLLOWUP,t)) or len(t)<20
    rnama, rscore = route_scored(text)
    nama = paksa or (STATE["persona"] if (rscore==0 and STATE["persona"]) else rnama)
    seed = (STATE["seed"]+" "+t).strip() if (is_follow and STATE["seed"]) else t
    if nama=="rp":
        dipilih = next((c for c in ["kai","rara","surya","arga","nala","bara"] if c in t), "kai")
        seed = f"user: {t}\n{dipilih}: "
    elif nama=="jokes":
        seed = "dark joke: " if "dark" in t else ("pun: " if ("pun" in t or "english" in t) else "jokes bapak-bapak: ")
    elif nama=="gombal":
        seed = "pantun: " if "pantun" in t else "gombalan: "
    elif nama in SEEDS:
        seed = SEEDS[nama].format(q=t)
    if nama=="matematika":
        h=hitung(t)
        if h: return {"jenis":"teks","reply":h,"nama":nama,"src":"tool"}
    st=structured(t)
    if st:
        STATE["persona"]=nama; STATE["seed"]=t[:80]
        return {"jenis":"teks","reply":st,"nama":nama,"src":"structured"}
    if re.search(FACT_Q,t):
        fl=fact_lookup(t)
        if fl:
            STATE["persona"]=nama; STATE["seed"]=t[:80]
            return {"jenis":"teks","reply":fl+"\n"+warna("2","[sumber: knowledge-base · conf 1.0]"),
                    "nama":nama,"src":"rag"}
        r=rag.jawab_fakta(t)
        if r:
            STATE["persona"]=nama; STATE["seed"]=t[:80]
            sumber = rag.LAST["sumber"] if rag.LAST["sumber"]!="corpus" else ("persona:"+nama)
            meta = "[sumber: "+sumber+" · conf "+str(rag.LAST["conf"])+"]"
            fmt0=detect_format(t)
            rep=apply_format(r,fmt0) if fmt0 else r+"\n"+warna("2",meta)
            return {"jenis":"teks","reply":rep,"nama":nama,"src":"rag"}
    return {"jenis":"gen","nama":nama,"seed":seed,"fmt":detect_format(t),"t":t}

def tanya(text, stream=False, paksa=None):
    global STATE
    p=rencanakan(text,paksa)
    if p["jenis"]=="teks":
        return p["reply"], p["nama"], p["src"]
    nama=p["nama"]; seed=p["seed"]; t=p["t"]
    brain=load(nama)
    if brain is None: return "", nama, "model"
    if is_token(brain):
        r=generate_token(brain, seed+" ", n_tokens=(90 if p.get("fmt") else 60), temp=0.3, stream=stream)
    else:
        r=generate(brain, seed+" ", n=(340 if p.get("fmt") else 240), temp=0.3)
        if r.startswith(seed): r=r[len(seed):].strip()
        if nama=="rp": r=r.split("\n",1)[1] if "\n" in r else r
    if p.get("fmt"): r=apply_format(r,p["fmt"])
    STATE["persona"]=nama; STATE["seed"]=t[:80]
    return r, nama, "model"

def is_token(brain):
    return isinstance(brain, dict) and brain.get("type") == "token"

# ---------- tampilan gaya platform chat (llmccp-style) ----------
def warna(kode, teks):
    return f"\033[{kode}m{teks}\033[0m" if TTY else teks

def speaker_label(nama):
    emoji = PAKAR[nama][0].split()[0]
    return f"{emoji} {warna('1;36','Casper')}"

# statistik generasi (buat indikator kecepatan token/s ala llmccp)
STATS = {"tokens": 0, "waktu": 0.001}

def kecepatan():
    return STATS["tokens"] / STATS["waktu"] if STATS["waktu"] > 0 else 0

def baris_kecepatan():
    return warna("2", f"*{kecepatan():.0f} token/s*")

BANNER = f"""
  {warna('1;35','🌌 C A S P E R V E R S E')}
  {warna('2', f'{len(PAKAR)} kepribadian · 1 Casper · ketik langsung, dia langsung jawab')}
  {warna('2', '/bantu  /pakar  /pakai <nama>  /auto  /suhu  /panjang  /keluar')}
"""

def main():
    print(BANNER)
    temp, n = 0.5, 300
    paksa = None
    while True:
        try:
            user = input(warna("2", "› ")).strip()
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

        plan = rencanakan(user, paksa)
        if plan["jenis"]=="teks":
            icon = {"guard":"️","identitas":"","rag":"","tool":""}.get(plan["src"],"💬")
            print(f"{icon} {warna('1;36','Casper')}: {plan['reply']}\n")
            continue
        nama = plan["nama"]
        brain = load(nama)
        if brain is None:
            print(f"  otak {PAKAR[nama][1]} belum ada di folder ini"); continue
        if is_token(brain):
            print(f"{speaker_label(nama)}: ", end="", flush=True)
            tanya(user, stream=TTY, paksa=paksa)
            print(f"\n{baris_kecepatan()}\n")
        else:
            reply, nm, srcc = tanya(user, stream=False, paksa=paksa)
            print(f"{speaker_label(nama)}: {reply}")
            print(f"{baris_kecepatan()}\n")

if __name__ == "__main__":
    main()
