"""RAG ringan untuk CasperAI — retrieval atas regular.txt biar jawaban factual
grounded (tidak mengarang). Index dibangun lazy & di-cache."""
import re, os, math
from collections import Counter

_HERE = os.path.dirname(os.path.abspath(__file__))
_CORPUS = os.path.join(_HERE, "regular.txt")
_idx = None

STOP = {"apa","siapa","kapan","dimana","berapa","mengapa","kenapa","adalah","itu","ini",
 "yang","dan","atau","di","ke","dari","pada","untuk","dengan","dalam","sebuah","adalah",
 "the","a","an","is","are","was","what","who","when","where","how","why","of","to","in","on"}

def _clean(b):
    b = re.sub(r"=== pelajaran dari:.*?===\n?", "", b)
    b = re.sub(r"judul:.*?\n", "", b)
    return b.strip()

JUNK = re.compile(r"(wayback|diarsipkan|https?://|isbn|pranala|referensi|diakses|\[\d+\])", re.I)
def _build():
    txt = open(_CORPUS, encoding="utf-8").read()
    blocks = [b for b in re.split(r"\n\n+", txt) if len(b) > 40]
    docs = []; df = Counter()
    for b in blocks:
        lab = re.search(r"=== pelajaran dari: (.*?) ===", b)
        label = lab.group(1) if lab else "corpus"
        b = _clean(b)
        if JUNK.search(b): continue
        toks = set(re.findall(r"[a-z0-9]+", b.lower())) - STOP
        if len(toks) < 2: continue
        docs.append((toks, b, label)); df.update(toks)
    N = len(docs)
    idf = {t: math.log((N+1)/(c+1)) + 1 for t, c in df.items()}
    return docs, idf

def retrieve(q, k=3):
    global _idx
    if _idx is None: _idx = _build()
    docs, idf = _idx
    qt = set(re.findall(r"[a-z0-9]+", q.lower())) - STOP
    if not qt: return []
    scored = []
    for toks, b, label in docs:
        ov = qt & toks
        if ov:
            idf_sum = sum(idf[t] for t in ov)
            coverage = len(ov)/max(len(qt),1)   # rerank: seberapa banyak query tercakup
            scored.append((idf_sum + 4.0*coverage, b, label))
    scored.sort(key=lambda x: (-x[0], len(x[1])))
    return scored[:k]

LAST = {"conf":0.0, "sumber":""}
def jawab_fakta(q, max_char=300):
    """Return jawaban grounded kalau retrieval yakin, else None. Set LAST (conf+sumber)."""
    global LAST
    res = retrieve(q, k=2)
    if not res: return None
    score, best, label = res[0]
    docs, idf = _idx
    qt = set(re.findall(r"[a-z0-9]+", q.lower())) - STOP
    ov = qt & set(re.findall(r"[a-z0-9]+", best.lower()))
    max_idf = max((idf.get(t,0) for t in ov), default=0)
    if len(ov) < 2 and not (len(ov)==1 and max_idf > 6): return None
    top2 = res[1][0] if len(res)>1 else 0
    conf = round(min(1.0, 0.35*len(ov)/max(len(qt),1) + 0.4 + (0.25 if (score-top2)>2 else 0.05)),2)
    LAST = {"conf":conf, "sumber":label}
    # pilih kalimat dalam blok yang paling relevan dgn pertanyaan
    qt = set(re.findall(r"[a-z0-9]+", q.lower())) - STOP
    sents = [s for s in re.split(r"(?<=[.!?])\s+", best) if len(s) > 15]
    if sents:
        def sk(s): return len(qt & set(re.findall(r"[a-z0-9]+", s.lower())))
        sents.sort(key=sk, reverse=True)
        ans = sents[0]
        # tambah kalimat pendamping bila ada
        if len(sents) > 1 and sk(sents[1]) >= 2: ans += " " + sents[1]
    else:
        ans = best
    return ans[:max_char]
