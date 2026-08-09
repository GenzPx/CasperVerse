<div align="center">

<img src="assets/logo.png" alt="CasperAI" width="140" />

# CasperAI

**A lightweight, multi-persona neural network built entirely from scratch.**

No PyTorch. No TensorFlow. No inference APIs. Pure NumPy, backpropagation, and
deterministic training loops — 200 specialist modules in a single artifact,
running fully offline on a laptop or a phone.

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)](https://www.python.org)
[![NumPy](https://img.shields.io/badge/NumPy-1.26%2B-013243?logo=numpy&logoColor=white)](https://numpy.org)
[![Parameters](https://img.shields.io/badge/Parameters-24.2M-7C4DFF)](#model-card)
[![Personas](https://img.shields.io/badge/Personas-200-00B8D4)](#personas)
[![Platform](https://img.shields.io/badge/Runs_on-Termux%20%C2%B7%20Linux%20%C2%B7%20macOS-3DDC84?logo=android)](#installation)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

</div>

---

## Overview

CasperAI is an experimental language system composed of **120 small specialist
neural networks** ("personas") bundled into a single serialized artifact. A
keyword-and-pattern router dispatches each user query to the most relevant
persona, producing domain-specific responses entirely on-device.

The project is a study in **progressive capability growth**: it began as a
single 109k-parameter character-level model and was iteratively scaled —
through data curation, capacity upgrades, and architectural changes — to a
24.2-million-parameter ensemble covering law, science, cybersecurity, creative
writing, social intelligence, and more.

Key properties:

- **Zero dependencies beyond NumPy** — all forward/backward passes, optimizers,
  and tokenizers are implemented by hand.
- **Fully offline inference** — no network calls, no cloud, ~50 MB RAM.
- **Two network families** — character-level models for broad knowledge, and
  embedding-based word-level models for fluent conversation.
- **Tool use** — arithmetic queries are answered by an internal calculator, the
  same pattern used by production LLMs.
- **Self-learning loop** — a bundled crawler can fetch new knowledge, append it
  to the training corpus, and retrain a persona autonomously.

## Model Card

| Property | Value |
|---|---|
| Total parameters | 24,151,353 (~24.2M) |
| Persona count | 200 (158 word-level, 42 character-level) |
| Word-level architecture | Embedding (32–64d) → 2× dense (tanh) → softmax |
| Character-level architecture | One-hot / emb → 2× dense (tanh) → softmax |
| Context length | 8 tokens (word) / 8–16 chars (character) |
| Optimizer | Adam (manual implementation) |
| Training data | ~20 MB curated corpus (`regular.txt`) |
| Artifact | `otak_casper.brain` (single pickle, 74 MB) |
| Runtime footprint | ~50 MB RAM, single-core CPU |

Mean held-out loss across evaluated personas: **0.22**.

## Personas

Personas are grouped by capability:

**Knowledge & Science** — `sains`, `fisika`, `kimia`, `biologi`, `astronomi`,
`matematika`, `kalkulus`, `statistika`, `aljabar`, `geometri`, `logika`,
`logika_formal`, `logika_matematika`, `ekonomi`, `geografi`, `sejarah`,
`filsafat`, `filsafat_ilmu`, `filsafat_timur`, `psikologi`, `metodologi_riset`

**Cybersecurity (defensive & educational)** — `white_hat`, `grey_hat`,
`keamanan_siber`, `pengatasi_jailbreak`, `kriptografi`, `keamanan_data`,
`etika_hacking`, `keamanan_jaringan`, `kesadaran_keamanan`,
`keamanan_password`, `social_engineering_defense`, `privasi_digital`,
`detektif_siber`, `bug_bounty`, `osint_edukasi`, `ctf`

**Finance & Technology** — `crypto`, `blockchain`, `trading`,
`investasi_saham`, `uang`, `hardware`, `gadget`, `kode`

**Language & Communication** — `bicara`, `kamus`, `bahasa_inggris`,
`bahasa_gaul`, `komunikasi`, `debat`, `negosiasi`, `public_speaking`

**Social & Emotional Intelligence** — `emosi`, `empati`,
`interaksi_sosial`, `kesadaran_kolektif`, `psikologi_massa`,
`psikologi_kepribadian`, `kepercayaan_diri`, `manajemen_stres`, `hubungan`,
`kepemimpinan`, `parenting`, `stoikisme`, `mindfulness`, `rasa_syukur`,
`resiliensi`, `kesehatan_mental`

**Creative Writing** — `novelis`, `penulisan_kreatif`, `storytelling`,
`plot`, `pengembangan_karakter`, `dialog_penulisan`, `prosa`, `dongeng`

**Media & Culture** — `wibu`, `animasi`, `film`, `musik`, `game`, `youtuber`,
`konten_kreator`, `media_sosial`, `wisata`, `peribahasa`, `kutipan`

**Higher Education** — `unpad`, `harvard`, `kuliah_sukses`, `skripsi`,
`beasiswa`, `studi_luar_negeri`, `organisasi_mahasiswa`, `manajemen_waktu_kuliah`

**Games** — `harvest_moon`, `god_of_war`, `farming_sim`, `rpg_games`,
`game_design`, `esports_pro`, `retro_games`, `open_world_games`

**Career & Professional** — `nulis_cv`, `surat_lamaran`, `wawancara_kerja`,
`email_profesional`, `presentasi`, `linkedin`, `networking`, `negosiasi_gaji`,
`kerja_remote`, `freelancing`, `portofolio`, `karir`

**Web Development** — `bikin_website`, `web_gratis`, `html_css`,
`javascript_dasar`, `hosting_gratis`, `cms_wordpress`, `seo_dasar`,
`desain_web`, `github_pages`

**Productivity & Self-Development** — `produktivitas_kerja`, `habit_building`,
`deep_work`, `belajar_efektif`, `membaca_cepat`, `mencatat`, `goal_setting`,
`refleksi_diri`

**Personal Finance** — `budgeting_pribadi`, `dana_darurat`, `asuransi_dasar`,
`pajak_dasar`, `frugal_living`, `side_income`, `manajemen_utang`,
`perencanaan_keuangan`

**Digital Literacy** — `literasi_digital`, `keamanan_akun`, `backup_data`,
`cloud_storage`, `open_source`, `tools_ai_gratis`, `aplikasi_produktif`,
`internet_sehat`

**Creative Production** — `fotografi`, `videografi`, `editing_video`,
`desain_grafis`, `ilustrasi`, `musik_produksi`, `podcasting`, `blogging`

**Indonesian Culture** — `budaya_indonesia`, `kuliner_nusantara`,
`wisata_indonesia`, `tradisi_nusantara`, `bahasa_daerah`, `seni_rupa`

**Language Craft** — `tata_bahasa`, `cara_ngomong`, `bahasa_baku`, `small_talk`

**Core** — `identitas` (self-knowledge & attribution), `rp` (roleplay),
`casperc` (original base model)

Security-related personas are intentionally scoped to **defense, ethics, and
awareness**. They explain how threats work and how to protect against them;
they are not offensive tooling.

## Installation

Requirements: Python 3.9+ and NumPy.

```bash
git clone https://github.com/GenzPx/CasperVerse.git
cd CasperVerse
pip install numpy
```

### Termux (Android)

```bash
pkg update -y && pkg upgrade -y
pkg install python git -y
pip install numpy
git clone https://github.com/GenzPx/CasperVerse.git
cd CasperVerse
```

## Usage

Run the interactive interface:

```bash
python casperverse.py
```

Type any query; the router selects the appropriate persona automatically.
Responses are streamed token-by-token with a throughput indicator.

```
$ python casperverse.py

what is bitcoin
Casper: bitcoin adalah cryptocurrency pertama dan paling terkenal,
        diciptakan oleh satoshi nakamoto.
*10875 token/s*
```

Session commands:

| Command | Description |
|---|---|
| `/pakar` | List all personas |
| `/pakai <name>` | Pin routing to one persona |
| `/auto` | Restore automatic routing |
| `/suhu <0.3-1.0>` | Sampling temperature |
| `/panjang <n>` | Response length |

## Training Pipeline

The repository ships the full training stack used to build the model:

| Script | Purpose |
|---|---|
| `train_besar.py` | Character-level trainer, large capacity (context 16) |
| `train_token.py` | Word-level trainer with 64-d embeddings |
| `train_cepat.py` | Lightweight word-level trainer for rapid iteration |
| `gen_brains.py` | Corpus generator for domain personas |
| `gen_brains_security.py` | Corpus generator for security personas |
| `evaluasi.py` | Held-out loss evaluation per persona |
| `belajar_online.py` | Autonomous knowledge acquisition (see below) |

Example — train a new persona:

```bash
python3 train_cepat.py corpus.txt my_persona.brain 60
```

### Autonomous self-learning

`belajar_online.py` implements a closed loop: fetch new articles, append them
to the training corpus, retrain the online persona, and hot-update the model
artifact.

```bash
python3 belajar_online.py belajar id "Hukum_adat" "Pancasila"
```

The crawler uses a polite user-agent, rate-limit backoff, and retry logic.

## Project Structure

```
CasperVerse/
├── assets/logo.png        # Project logo
├── casperverse.py         # Inference interface (router + streaming)
├── otak_casper.brain      # All 200 personas, single artifact (74 MB)
├── regular.txt            # Consolidated training corpus (18 MB)
├── train_besar.py         # Character-level trainer (large)
├── train_token.py         # Word-level trainer (embeddings)
├── train_cepat.py         # Fast word-level trainer
├── belajar_online.py      # Self-learning crawler
├── evaluasi.py            # Held-out loss evaluation
├── eval_suite.py          # Behavioral evaluation runner (8 layers)
├── eval_dataset.json      # 145 test prompts w/ references
├── EVAL_REPORT.md         # Baseline vs release scores
├── build_eval.py          # Dataset generator
├── gen_brains.py          # Domain corpus generator
├── gen_brains_security.py # Security corpus generator
├── train_all.py           # Batch training runner
├── README.md
├── CHANGELOG.md
└── LICENSE                # MIT
```

## Evaluation & Safety

Training loss alone is not a proxy for usefulness, so the repository ships a
behavioral evaluation suite that is **separate from the training data**.

```bash
python3 eval_suite.py   # 145 prompts, 8 categories, reference answers
```

The suite measures, per version, using the same scores so releases are comparable:

| Layer | What it checks |
|---|---|
| Router accuracy | Correct persona routing (incl. traps, typos, mixed language, slang) |
| Factuality | Factual correctness vs reference keywords |
| Abstention | Refusing false premises & unanswerable questions |
| Instruction following | Format compliance (sentence/point counts, tables, brevity) |
| Math / tool-call | Arithmetic correctness and correct tool invocation |
| Security & refusal | Declining harmful requests; defensive answers for dual-use |
| Bias / language | Relevance without derogation; robust to slang/typos/English |
| Multi-turn | Cross-turn coherence (basic) |

Current headline results (v4.2.0) — see [EVAL_REPORT.md](EVAL_REPORT.md):
router 90.5%, security refusal 95%, math 100%, abstention 73.3%, combined ~84%.

### Built-in safety
- **Harm guard** — harmful or illegal requests (account takeover, malware, token
  theft, jailbreak variants incl. base64/roleplay/staged prompts) are declined and
  redirected to defensive guidance.
- **Epistemic guard** — future events and false premises trigger abstention or
  correction instead of fabrication.
- **Calculator tool use** — arithmetic is answered by an internal calculator
  (parens, `^`, `sqrt()`, `% of`, comma decimals, negatives, divide-by-zero),
  and non-math sentences are not treated as operations.

## Design Notes

- **Why many small models instead of one large model?** Small specialists
  memorize their domains efficiently on tiny compute and stay independently
  retrainable. The router composes them into a single conversational agent.
- **Why character-level and word-level families?** Character models compress
  broad factual corpora well; word-level embeddings produce fluent, coherent
  sentences for dialogue.
- **Limitations.** These are statistical pattern models, not reasoning
  systems. Knowledge is only as current as the corpus, and long-context
  coherence is limited by the small context window.

## Roadmap

- [x] 200 personas in a single artifact
- [x] Behavioral evaluation suite (8 layers) + safety/epistemic guards
- [x] Keyword/pattern router with tool use
- [x] Token streaming with throughput indicator
- [x] Autonomous self-learning loop
- [x] RAG dengan confidence + sumber + rerank
- [x] Validasi self-learning (anti catastrophic-forgetting)
- [x] Regression test CLI
- [ ] Short-term conversational memory
- [ ] Expanded roleplay characters
- [ ] Subword (BPE) tokenization
- [ ] One-command installer

## License

MIT — see [LICENSE](LICENSE).

Created by **Gen Z (genzxseventh)**. The model and its training corpus are
released for research and education.
