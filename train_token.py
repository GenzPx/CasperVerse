"""
TRAIN_TOKEN — latih otak berbasis TOKEN (word-level) seperti LLM sungguhan.
Arsitektur: embedding layer -> 2 hidden layer (tanh) -> softmax.
Satu langkah generasi = satu token utuh (bukan per karakter).

Pakai: python3 train_token.py file1+file2 output.brain [epoch] [lanjut]
"""
import numpy as np, time, pickle, sys, os, re, zlib
from collections import Counter

CORPUS = sys.argv[1].split("+")
OUT = sys.argv[2]
EPOCHS = int(sys.argv[3]) if len(sys.argv) > 3 else 60
LANJUT = len(sys.argv) > 4 and sys.argv[4] == "lanjut"

# hyperparameter
D = 64          # dimensi embedding
H1, H2 = 256, 128
L = 8           # konteks (jumlah token)
BATCH = 512
LR0 = 0.002

rng = np.random.default_rng(zlib.crc32(OUT.encode())%100000)
mix = "\n".join(open(f, encoding="utf-8").read() for f in CORPUS if os.path.exists(f))

# ---- tokenisasi ----
tokens = re.findall(r"\w+|[^\w\s]", mix.lower())
cnt = Counter(tokens)
threshold = 5 if len(tokens) < 100_000 else 10
vocab_words = sorted([w for w, c in cnt.items() if c >= threshold])
token2id = {"<unk>": 0}
for i, w in enumerate(vocab_words, 1):
    token2id[w] = i
id2token = {i: w for w, i in token2id.items()}
V = len(token2id)

ids = np.array([token2id.get(t, 0) for t in tokens], dtype=np.int32)
N = len(ids) - L
print(f"[{OUT}] token={len(tokens):,} | vocab={V:,} | konteks={L} kata | embed={D}", flush=True)

# ---- inisialisasi bobot ----
E  = rng.normal(0, 0.1, (V, D)).astype(np.float32)
W1 = rng.normal(0, 0.08, (L*D, H1)).astype(np.float32); b1 = np.zeros(H1, dtype=np.float32)
W2 = rng.normal(0, 0.08, (H1, H2)).astype(np.float32);  b2 = np.zeros(H2, dtype=np.float32)
W3 = rng.normal(0, 0.08, (H2, V)).astype(np.float32);    b3 = np.zeros(V, dtype=np.float32)

if LANJUT and os.path.exists(OUT):
    lama = pickle.load(open(OUT, "rb"))
    if isinstance(lama, dict) and lama.get("type") == "token" and len(lama["token2id"]) == V:
        E,W1,b1,W2,b2,W3,b3 = lama["E"],lama["W1"],lama["b1"],lama["W2"],lama["b2"],lama["W3"],lama["b3"]
        print(f"[{OUT}] LANJUT dari otak lama ✓", flush=True)
    else:
        print(f"[{OUT}] otak lama nggak kompatibel, mulai dari awal", flush=True)

# ---- adam ----
state = {k:(np.zeros_like(v),np.zeros_like(v)) for k,v in
         dict(E=E,W1=W1,b1=b1,W2=W2,b2=b2,W3=W3,b3=b3).items()}
t = 0
def adam(name, g, P, lr):
    global t
    m,v = state[name]
    m = 0.9*m + 0.1*g; v = 0.999*v + 0.001*g*g
    P -= lr*(m/(1-0.9**t))/(np.sqrt(v/(1-0.999**t))+1e-8)
    state[name] = (m,v); return P

SUB = min(250_000, N - BATCH)
idx = rng.integers(0, N, size=(SUB,))
win_ids = np.stack([ids[i:i+L] for i in range(0, N-L, max(1,(N-L)//SUB))])[:SUB]
y_all   = np.array([ids[i+L] for i in range(0, N-L, max(1,(N-L)//SUB))])[:SUB]

print(f"[{OUT}] mulai latihan {EPOCHS} epoch", flush=True)
t0 = time.time()
total_steps = EPOCHS * (SUB // BATCH)
for ep in range(EPOCHS):
    perm = rng.permutation(SUB)
    tot, seen = 0.0, 0
    for s in range(0, SUB-BATCH, BATCH):
        bi = perm[s:s+BATCH]
        ctx = win_ids[bi]                 # (B, L)
        y = y_all[bi]                     # (B,)
        Xemb = E[ctx]                     # (B, L, D)
        X = Xemb.reshape(BATCH, L*D)
        h1 = np.tanh(X@W1+b1); h2 = np.tanh(h1@W2+b2)
        logits = h2@W3+b3
        ex = np.exp(logits - logits.max(1,keepdims=True))
        p = ex/ex.sum(1,keepdims=True)
        loss = -np.log(p[np.arange(BATCH),y]+1e-9).mean()
        # backward
        dl = p.copy(); dl[np.arange(BATCH),y]-=1; dl/=BATCH
        gW3 = h2.T@dl; gb3 = dl.sum(0)
        dh2 = (dl@W3.T)*(1-h2*h2)
        gW2 = h1.T@dh2; gb2 = dh2.sum(0)
        dh1 = (dh2@W2.T)*(1-h1*h1)
        gW1 = X.T@dh1; gb1 = dh1.sum(0)
        dX = (dh1@W1.T).reshape(BATCH, L, D)
        dE = np.zeros_like(E); np.add.at(dE, ctx, dX)
        t += 1
        lr = LR0 * (0.25 + 0.75*(1 - t/total_steps))
        E=adam('E',dE,E,lr); W1=adam('W1',gW1,W1,lr); b1=adam('b1',gb1,b1,lr)
        W2=adam('W2',gW2,W2,lr); b2=adam('b2',gb2,b2,lr)
        W3=adam('W3',gW3,W3,lr); b3=adam('b3',gb3,b3,lr)
        tot += loss*BATCH; seen += BATCH
    print(f"  ep {ep+1:>3}/{EPOCHS} loss {tot/seen:.4f} | {time.time()-t0:.0f}s", flush=True)

pickle.dump({
 "type":"token","E":E,"W1":W1,"b1":b1,"W2":W2,"b2":b2,"W3":W3,"b3":b3,
 "token2id":token2id,"id2token":id2token,"L":L,"D":D,
}, open(OUT,"wb"))
print(f"[{OUT}] SELESAI | loss akhir {tot/seen:.4f} | vocab {V:,} token", flush=True)
