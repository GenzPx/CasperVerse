import numpy as np, time, pickle, sys, re, zlib
from collections import Counter
OUT=sys.argv[1] if len(sys.argv)>1 else "otak_raksasa.brain"
EPOCHS=int(sys.argv[2]) if len(sys.argv)>2 else 1
D,H1,H2,VMAX=96,640,320,30000
rng=np.random.default_rng(zlib.crc32(OUT.encode())%100000)
txt=open("regular.txt",encoding="utf-8").read().lower()
cnt=Counter(re.findall(r"\w+",txt))
vocab_words=[w for w,c in cnt.most_common(VMAX)]
t2i={w:i+1 for i,w in enumerate(vocab_words)}; t2i["<unk>"]=0
i2t={i:w for w,i in t2i.items()}; V=len(t2i)
toks=np.array([t2i.get(w,0) for w in re.findall(r"\w+",txt)],dtype=np.int32)
L=16; N=len(toks)-L
E=rng.normal(0,0.05,(V,D)).astype(np.float32)
W1=rng.normal(0,0.03,(L*D,H1)).astype(np.float32); b1=np.zeros(H1,np.float32)
W2=rng.normal(0,0.03,(H1,H2)).astype(np.float32); b2=np.zeros(H2,np.float32)
W3=rng.normal(0,0.03,(H2,V)).astype(np.float32); b3=np.zeros(V,np.float32)
SUB=min(60000,N); BATCH=256
win=np.stack([toks[i:i+L] for i in range(0,N-L,max(1,(N-L)//SUB))])[:SUB]
yall=np.array([toks[i+L] for i in range(0,N-L,max(1,(N-L)//SUB))])[:SUB]
t0=time.time()
for ep in range(EPOCHS):
    perm=rng.permutation(SUB); tot,seen=0,0
    for s in range(0,SUB-BATCH,BATCH):
        bi=perm[s:s+BATCH]; ctx=win[bi]; y=yall[bi]
        X=E[ctx].reshape(BATCH,L*D)
        h1=np.tanh(X@W1+b1); h2=np.tanh(h1@W2+b2); lo=h2@W3+b3
        ex=np.exp(lo-lo.max(1,keepdims=True)); p=ex/ex.sum(1,keepdims=True)
        loss=-np.log(p[np.arange(BATCH),y]+1e-9).mean()
        dl=p; dl[np.arange(BATCH),y]-=1; dl/=BATCH
        gW3=h2.T@dl; gb3=dl.sum(0); dh2=(dl@W3.T)*(1-h2*h2)
        gW2=h1.T@dh2; gb2=dh2.sum(0); dh1=(dh2@W2.T)*(1-h1*h1)
        gW1=X.T@dh1; gb1=dh1.sum(0)
        dE=np.zeros_like(E); np.add.at(dE,ctx,(dh1@W1.T).reshape(BATCH,L,D))
        lr=0.001
        E-=lr*dE; W1-=lr*gW1; b1-=lr*gb1; W2-=lr*gW2; b2-=lr*gb2; W3-=lr*gW3; b3-=lr*gb3
        tot+=loss*BATCH; seen+=BATCH
    print(f"ep {ep+1}/{EPOCHS} loss {tot/seen:.4f} {time.time()-t0:.0f}s",flush=True)
pickle.dump({"type":"token","D":D,"L":L,"t2i":t2i,"i2t":i2t,
 "E":E,"W1":W1,"b1":b1,"W2":W2,"b2":b2,"W3":W3,"b3":b3},open(OUT,"wb"))
tot=sum(x.size for x in (E,W1,b1,W2,b2,W3,b3))
print(f"saved {OUT} | params {tot:,}")
