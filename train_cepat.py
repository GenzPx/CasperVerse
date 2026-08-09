"""TRAIN_CEPAT — trainer word-level ringan utk bikin banyak otak sekaligus.
Sama kayak train_token.py tapi kapasitas kecil (D=32,H1=160,H2=80) biar ngebut.
Pakai: python3 train_cepat.py korpus.txt output.brain [epoch]
"""
import numpy as np, time, pickle, sys, os, re, zlib
from collections import Counter
CORPUS=sys.argv[1]; OUT=sys.argv[2]
EPOCHS=int(sys.argv[3]) if len(sys.argv)>3 else 60
D=32; H1=160; H2=80; L=8; BATCH=512; LR0=0.002
rng=np.random.default_rng(zlib.crc32(OUT.encode())%100000)
mix=open(CORPUS,encoding="utf-8").read()
tokens=re.findall(r"\w+|[^\w\s]",mix.lower())
cnt=Counter(tokens)
thr=5 if len(tokens)<100000 else 10
vocab_words=sorted([w for w,c in cnt.items() if c>=thr])
token2id={"<unk>":0}
for i,w in enumerate(vocab_words,1): token2id[w]=i
id2token={i:w for w,i in token2id.items()}; V=len(token2id)
ids=np.array([token2id.get(t,0) for t in tokens],dtype=np.int32)
N=len(ids)-L
E=rng.normal(0,0.1,(V,D)).astype(np.float32)
W1=rng.normal(0,0.08,(L*D,H1)).astype(np.float32); b1=np.zeros(H1,np.float32)
W2=rng.normal(0,0.08,(H1,H2)).astype(np.float32); b2=np.zeros(H2,np.float32)
W3=rng.normal(0,0.08,(H2,V)).astype(np.float32); b3=np.zeros(V,np.float32)
state={k:(np.zeros_like(v),np.zeros_like(v)) for k,v in dict(E=E,W1=W1,b1=b1,W2=W2,b2=b2,W3=W3,b3=b3).items()}
t=0
def adam(n,g,P,lr):
    global t; m,v=state[n]; m=0.9*m+0.1*g; v=0.999*v+0.001*g*g
    P-=lr*(m/(1-0.9**t))/(np.sqrt(v/(1-0.999**t))+1e-8); state[n]=(m,v); return P
SUB=min(60000,N-BATCH)
win=np.stack([ids[i:i+L] for i in range(0,N-L,max(1,(N-L)//SUB))])[:SUB]
yall=np.array([ids[i+L] for i in range(0,N-L,max(1,(N-L)//SUB))])[:SUB]
t0=time.time(); total=EPOCHS*(SUB//BATCH)
for ep in range(EPOCHS):
    perm=rng.permutation(SUB); tot,seen=0.0,0
    for s in range(0,SUB-BATCH,BATCH):
        bi=perm[s:s+BATCH]; ctx=win[bi]; y=yall[bi]
        Xemb=E[ctx].reshape(BATCH,L*D)
        h1=np.tanh(Xemb@W1+b1); h2=np.tanh(h1@W2+b2); logits=h2@W3+b3
        ex=np.exp(logits-logits.max(1,keepdims=True)); p=ex/ex.sum(1,keepdims=True)
        loss=-np.log(p[np.arange(BATCH),y]+1e-9).mean()
        dl=p.copy(); dl[np.arange(BATCH),y]-=1; dl/=BATCH
        gW3=h2.T@dl; gb3=dl.sum(0); dh2=(dl@W3.T)*(1-h2*h2)
        gW2=h1.T@dh2; gb2=dh2.sum(0); dh1=(dh2@W2.T)*(1-h1*h1)
        gW1=Xemb.T@dh1; gb1=dh1.sum(0)
        dE=np.zeros_like(E); np.add.at(dE,ctx,(dh1@W1.T).reshape(BATCH,L,D))
        t+=1; lr=LR0*(0.25+0.75*(1-t/total))
        E=adam('E',dE,E,lr);W1=adam('W1',gW1,W1,lr);b1=adam('b1',gb1,b1,lr)
        W2=adam('W2',gW2,W2,lr);b2=adam('b2',gb2,b2,lr);W3=adam('W3',gW3,W3,lr);b3=adam('b3',gb3,b3,lr)
        tot+=loss*BATCH; seen+=BATCH
pickle.dump({"type":"token","E":E,"W1":W1,"b1":b1,"W2":W2,"b2":b2,"W3":W3,"b3":b3,
 "token2id":token2id,"id2token":id2token,"L":L,"D":D},open(OUT,"wb"))
print(f"{OUT} | vocab {V} | loss {tot/seen:.4f} | {time.time()-t0:.0f}s")
