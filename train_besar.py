"""LATIH BESAR — otak kapasitas ganda (konteks 16, memori 384/192).
Pakai: python3 train_specialist.py file1+file2 otak.brain [epoch]
"""
import numpy as np, time, pickle, sys, os
from collections import Counter

CORPUS = sys.argv[1].split("+")
OUT = sys.argv[2]
EPOCHS = int(sys.argv[3]) if len(sys.argv) > 3 else 80
LANJUT = len(sys.argv) > 4 and sys.argv[4] == "lanjut"
BATCH = 1024
LR0 = 0.002
L = 16; H1, H2 = 384, 192

rng = np.random.default_rng(hash(OUT) % 10_000)
mix = "\n\n".join(open(f, encoding="utf-8").read() for f in CORPUS)
cnt = Counter(mix)
threshold = 100 if len(mix) > 100_000 else 5
chars = sorted([c for c, n in cnt.items() if n >= threshold])
vocab = {c: i for i, c in enumerate(chars)}
ivocab = {i: c for c, i in vocab.items()}
V = len(chars)
unk = vocab.get(" ", 0)
data = np.array([vocab.get(c, unk) for c in mix], dtype=np.int32)
win = np.lib.stride_tricks.sliding_window_view(data, L + 1)

W1 = rng.normal(0, 0.08, (L*V, H1)).astype(np.float32)
b1 = np.zeros(H1, dtype=np.float32)
W2 = rng.normal(0, 0.08, (H1, H2)).astype(np.float32)
b2 = np.zeros(H2, dtype=np.float32)
W3 = rng.normal(0, 0.08, (H2, V)).astype(np.float32)
b3 = np.zeros(V, dtype=np.float32)
if LANJUT and os.path.exists(OUT):
    W1,b1,W2,b2,W3,b3,v0,i0,L0 = pickle.load(open(OUT,"rb"))
    assert len(v0) == V, "vocab berubah, nggak bisa lanjut"
    print(f"[{OUT}] LANJUT dari otak lama ✓", flush=True)

state = {k:(np.zeros_like(v),np.zeros_like(v)) for k,v in
         dict(W1=W1,b1=b1,W2=W2,b2=b2,W3=W3,b3=b3).items()}
t = 0
def adam(name, g, P, lr):
    global t
    m,v = state[name]
    m = 0.9*m + 0.1*g; v = 0.999*v + 0.001*g*g
    P -= lr*(m/(1-0.9**t))/(np.sqrt(v/(1-0.999**t))+1e-8)
    state[name] = (m,v); return P

SUB = min(300_000, len(win) - BATCH)
OFF = (np.arange(L)*V).astype(np.int32)
rows = np.repeat(np.arange(BATCH)[:,None], L, axis=1)
def onehot(ctx):
    X = np.zeros((BATCH, L*V), dtype=np.float32)
    X[rows, ctx + OFF] = 1.0
    return X

print(f"[{OUT}] korpus {len(data):,} char | vocab {V} | {EPOCHS} epoch", flush=True)
t0 = time.time()
total_steps = EPOCHS * (SUB // BATCH)
for ep in range(EPOCHS):
    sel = rng.choice(len(win), SUB, replace=False)
    sub = win[sel]
    perm = rng.permutation(SUB)
    tot, seen = 0.0, 0
    for s in range(0, SUB-BATCH, BATCH):
        bi = perm[s:s+BATCH]
        ctx = sub[bi, :L]; y = sub[bi, L]
        X = onehot(ctx)
        h1 = np.tanh(X@W1+b1); h2 = np.tanh(h1@W2+b2)
        logits = h2@W3+b3
        ex = np.exp(logits - logits.max(1,keepdims=True))
        p = ex/ex.sum(1,keepdims=True)
        loss = -np.log(p[np.arange(BATCH),y]+1e-9).mean()
        dl = p; dl[np.arange(BATCH),y] -= 1; dl /= BATCH
        gW3 = h2.T@dl; gb3 = dl.sum(0)
        dh2 = (dl@W3.T)*(1-h2*h2)
        gW2 = h1.T@dh2; gb2 = dh2.sum(0)
        dh1 = (dh2@W2.T)*(1-h1*h1)
        gW1 = X.T@dh1; gb1 = dh1.sum(0)
        t += 1
        lr = LR0 * (0.25 + 0.75*(1 - t/total_steps))
        W1=adam('W1',gW1,W1,lr); b1=adam('b1',gb1,b1,lr)
        W2=adam('W2',gW2,W2,lr); b2=adam('b2',gb2,b2,lr)
        W3=adam('W3',gW3,W3,lr); b3=adam('b3',gb3,b3,lr)
        tot += loss*BATCH; seen += BATCH
    print(f"  ep {ep+1:>2}/{EPOCHS} loss {tot/seen:.4f} | {time.time()-t0:.0f}s", flush=True)

pickle.dump((W1,b1,W2,b2,W3,b3,vocab,ivocab,L), open(OUT,"wb"))
print(f"[{OUT}] SELESAI | loss akhir {tot/seen:.4f} | {time.time()-t0:.0f}s total", flush=True)
