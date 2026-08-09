import sys, subprocess, os
domains = sys.argv[1:]
for d in domains:
    k = f"korpus_baru/{d}.txt"
    o = f"korpus_baru/{d}.brain"
    if not os.path.exists(k): print(f"!! {k} nggak ada"); continue
    r = subprocess.run([sys.executable,"train_cepat.py",k,o,"60"],capture_output=True,text=True)
    print(r.stdout.strip() or r.stderr.strip()[:200])
print("BATCH SELESAI")
