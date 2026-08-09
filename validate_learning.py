"""VALIDASI SELF-LEARNING — cek akurasi sebelum/sesudah belajar_online +
catastrophic forgetting pada pengetahuan lama.
Jalankan: python3 validate_learning.py
"""
import subprocess, sys, os, re
import casperverse as cv

HERE=os.path.dirname(os.path.abspath(__file__))
PROBES=[  # pengetahuan lama (harus tetap benar sesudah belajar)
 ("Apa fungsi firewall?",["menyaring","lalu lintas"]),
 ("Siapa pencipta Bitcoin?",["satoshi"]),
 ("Apa itu fotosintesis?",["cahaya"]),
]
def akurasi(items):
    ok=0
    for q,kws in items:
        r,n,s=cv.tanya(q)
        if any(k in r.lower() for k in kws): ok+=1
    return ok,len(items)

CAND=["Kolintang","Tifa","Rebab","Saluang","Kecapi","Gendang","Seruling","Bonang"]
def _ada(top):
    import rag
    return rag.jawab_fakta(f"apa itu {top}?") is not None
NEW=next((c for c in CAND if not _ada(c)), CAND[0])
q_new=f"Apa itu {NEW}?"

print("== SEBELUM belajar ==")
old_ok,old_n=akurasi(PROBES)
print(f"  pengetahuan lama: {old_ok}/{old_n}")
r,n,s=cv.tanya(q_new); before_new = (s=="rag")
print(f"  topik baru dipilih: {NEW} (sebelumnya belum ada: {not before_new})")
print(f"  topik baru ({NEW}) terjawab RAG: {before_new}")

print("== menjalankan belajar_online.py (fetch+retrain) ==")
subprocess.run([sys.executable,os.path.join(HERE,"belajar_online.py"),"belajar","id",NEW],
               capture_output=True,text=True)

import importlib, rag
importlib.reload(rag); rag._idx=None   # refresh index corpus
cv2=cv; 
print("== SESUDAH belajar ==")
new_ok,new_n=akurasi(PROBES)
print(f"  pengetahuan lama: {new_ok}/{new_n}  (catastrophic forgetting: {'TIDAK' if new_ok>=old_ok else 'YA'})")
r,n,s=cv.tanya(q_new); after_new=(s=="rag")
print(f"  topik baru ({NEW}) terjawab RAG: {after_new}  conf={rag.LAST['conf']} sumber={rag.LAST['sumber']}")
print("\nKESIMPULAN:", "self-learning menambah pengetahuan TANPA merusak yang lama ✅"
      if (after_new and not before_new and new_ok>=old_ok) else "perlu peninjauan ⚠️")
