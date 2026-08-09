"""BPE subword tokenizer utk CasperAI — fondasi vocab efisien.
Latih:  python3 bpe.py [n_merges]   -> menyimpan bpe_vocab.json
Pakai:  import bpe; enc=bpe.encode("halo dunia")
"""
import re, json, os, sys
from collections import Counter
HERE=os.path.dirname(os.path.abspath(__file__))
VOC=os.path.join(HERE,"bpe_vocab.json")

def _words(sample_chars=2_000_000):
    txt=open(os.path.join(HERE,"regular.txt"),encoding="utf-8").read()[:sample_chars]
    return Counter(re.findall(r"\S+", txt.lower()))

def train(n_merges=1000):
    vocab={w:tuple(w)+("</w>",) for w,c in _words().items()}
    freq=dict(_words())
    merges=[]
    for _ in range(n_merges):
        pairs=Counter()
        for w,t in vocab.items():
            for a,b in zip(t,t[1:]): pairs[(a,b)]+=freq[w]
        if not pairs: break
        best=max(pairs,key=pairs.get)
        merges.append(best)
        nw={}
        for w,t in vocab.items():
            nt=[]; i=0
            while i<len(t):
                if i<len(t)-1 and (t[i],t[i+1])==best: nt.append(t[i]+t[i+1]); i+=2
                else: nt.append(t[i]); i+=1
            nw[w]=tuple(nt)
        vocab=nw
    json.dump({"merges":[list(m) for m in merges]},open(VOC,"w"))
    return merges

_m=None
def _load():
    global _m
    if _m is None: _m=[tuple(x) for x in json.load(open(VOC))["merges"]]
    return _m

def encode(text):
    merges=_load(); toks=[]
    for w in re.findall(r"\S+", text.lower()):
        t=tuple(w)+("</w>",)
        for a,b in merges:
            nt=[]; i=0
            while i<len(t):
                if i<len(t)-1 and (t[i],t[i+1])==(a,b): nt.append(a+b); i+=2
                else: nt.append(t[i]); i+=1
            t=tuple(nt)
        toks+=list(t)
    return toks

def ratio(sample="caspers adalah model bahasa yang dibangun dari nol dengan numpy"):
    chars=len(sample); words=len(sample.split()); toks=len(encode(sample))
    return chars,words,toks

if __name__=="__main__":
    n=int(sys.argv[1]) if len(sys.argv)>1 else 1000
    train(n)
    c,w,t=ratio()
    print(f"BPE vocab {n} merges tersimpan.")
    print(f"contoh: {c} char / {w} word / {t} subword-token  (kompresi char->token {c/t:.1f}x)")
