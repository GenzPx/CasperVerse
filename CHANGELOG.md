# Changelog

All notable changes to CasperAI are documented in this file.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and
versioning follows [Semantic Versioning](https://semver.org/).

## [4.2.0] — 2026-08-09

### Added
- 80 new personas (total: 200): higher education (UNPAD, Harvard, thesis,
  scholarships), games (Harvest Moon, God of War, farming sim, RPG, esports),
  language & communication (grammar, speaking, interviewing, CV & cover-letter
  writing, professional email, presentation), web development (website
  building, free hosting, HTML/CSS, JavaScript, WordPress, SEO, GitHub Pages),
  career (LinkedIn, networking, salary negotiation, remote work, freelancing,
  portfolio), productivity, personal finance, digital literacy, creative
  fields (photography, videography, design, music production, podcasting),
  and Indonesian culture (cuisine, tourism, traditions, regional languages).

### Changed
- Parameter count: 19.33M → 24.15M.
- Persona count: 120 → 200.

---

## [4.1.0] — 2026-08-09

### Added
- 20 new personas (total: 120):
  - Cybersecurity (defensive/educational): `white_hat`, `grey_hat`,
    `keamanan_siber`, `pengatasi_jailbreak`, `kriptografi`, `keamanan_data`,
    `etika_hacking`, `keamanan_jaringan`, `kesadaran_keamanan`,
    `keamanan_password`, `social_engineering_defense`, `privasi_digital`,
    `detektif_siber`, `bug_bounty`, `osint_edukasi`, `ctf`.
  - Personal development: `stoikisme`, `mindfulness`, `rasa_syukur`,
    `resiliensi`.
- Refined routing: disambiguated overlapping security keywords
  (password → `keamanan_password`, encryption → `kriptografi`,
  firewall → `keamanan_jaringan`).

### Changed
- Parameter count: 18.07M → 19.33M.
- Security content scoped to defense, ethics, and awareness.

---

## [4.0.0] — 2026-08-09

### Added
- 52 new personas (total: 100): formal logic, emotions, collective
  consciousness, speaking style, social interaction, crypto, blockchain,
  YouTube, novelist & creative writing, school-to-university subjects
  (physics, chemistry, biology, algebra, geometry, calculus, statistics,
  economics), research methodology, Eastern philosophy, mental health,
  productivity, leadership, and more.
- `train_cepat.py`: lightweight word-level trainer for rapid iteration.
- `gen_brains.py`: educational corpus generator for mass persona creation.
- Token throughput indicator (`*N token/s*`) displayed per response.

### Changed
- Persona count: 48 → 100.
- Parameter count: 8.4M → 18.07M.

---

## [3.0.0] — 2026-08-09

### Changed
- Consolidated all 42 personas into a single artifact (`otak_casper.brain`).
- Consolidated 62 corpus files into a single training corpus (`regular.txt`).
- Reduced 19 scripts to 5 core modules.
- Rewrote `evaluasi.py` as a per-domain health check over the merged corpus.

### Removed
- Superseded phase scripts (`nano1.py`, `sekolah.py`, `kuliah_*.py`,
  `chat.py`, `ngobrol.py`, `train_specialist.py`, one-off generators,
  legacy fetchers).

### Documentation
- Professional README rewrite; this changelog introduced.

---

## [2.3.0] — 2026-08-09

### Added
- `identitas` persona: self-knowledge and creator attribution.
- Personality traits and behavioral rules (honesty, politeness, safety).
- `belajar_online.py`: autonomous Wikipedia acquisition with self-training.
- `online` persona trained on self-collected data (LLM, neural networks,
  machine learning, Indonesian culture).

### Data
- `indo_extra3`, `inggris_extra3`, `korpus_online` (+390K characters).

---

## [2.2.0] — 2026-08-08

### Added
- `train_token.py`: word-level architecture with 64-d embeddings.
- Conversational personas upgraded to token generation
  (`bicara`, `curhat`, `motivasi`, `jokes`, `gombal`).
- Terminal streaming output.
- Word-boundary matching in the router to prevent short-keyword collisions.

### Fixed
- Eliminated character truncation in conversational output.
- Joke generation now terminates after the punchline.

---

## [2.1.0] — 2026-08-08

### Changed
- Weak knowledge personas upgraded to large capacity (context 16,
  hidden 384×192).
- Corpus expansion: +935K characters (Indonesian culture, world history,
  philosophy).

### Results
- Notable loss reductions: `tanaman` 0.65 → 0.028, `sejarah` 0.76 → 0.045,
  `kode` 0.80 → 0.15, `catur` 0.77 → 0.31, `filsafat` 0.77 → 0.44.
- Ensemble mean loss: 0.55 → 0.25.

---

## [2.0.0] — 2026-08-08

### Added
- Split the single model into specialist personas (ensemble architecture).
- Automatic context router (keyword scoring, arithmetic detection,
  proverb detection).
- Tool use: internal calculator for arithmetic queries.
- Dozens of personas: anime, code, ethical hacking, chess, cooking,
  emotional support, folklore, and more.

---

## [1.0.0] — 2026-08-08

### Added
- Progressive single-model training: general knowledge, anime, coding,
  ethical hacking, chess, creative arts.
- Seed formatting mechanism for clean Q&A output.
- Alphabet-coverage fix for small-capacity models.

---

## [0.1.0] — 2026-08-08

### Added
- Initial character-level neural network implemented from scratch in NumPy:
  one-hot input, two hidden layers (tanh), softmax output, manual Adam.
- Initial release at 109,000 parameters.
