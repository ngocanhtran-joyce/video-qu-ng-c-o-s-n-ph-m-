"""QA: kiểm tra từng khung đồ hoạ có đè lên mặt người không.
usage: python3 check_faces.py <work_dir> <edl.txt> <số cảnh có người, vd 1,10,14>
In các khung có > 2% diện tích mặt bị đồ hoạ (alpha > 40) che."""
import sys, json, glob
import numpy as np
from PIL import Image
W, edl, people = sys.argv[1], sys.argv[2], {int(x) for x in sys.argv[3].split(",")}
F = json.load(open(f"{W}/faces.json")); C = [0.0]
for l in open(edl):
    if l.strip() and not l.startswith("#"): C.append(C[-1] + float(l.split()[3]))
frames = sorted(glob.glob(f"{W}/frames/f_*.png")); bad = []; checked = 0
for i, f in enumerate(frames):
    t = i / 30; k = next((j + 1 for j in range(len(C) - 1) if C[j] <= t < C[j + 1]), None)
    if k not in people: continue
    fi = min(int(t * F["fps"]), len(F["boxes"]) - 1); boxes = F["boxes"][fi]
    if not boxes: continue
    a = np.asarray(Image.open(f).getchannel("A")); checked += 1
    for x, y, w, h in boxes:
        reg = a[y:y + h, x:x + w]
        if reg.size and (reg > 40).mean() > 0.02: bad.append((i, round(t, 2), k, round(float((reg > 40).mean()), 3)))
print(f"đã kiểm {checked} khung có mặt người; {len(bad)} khung bị che")
for b in bad[:40]: print("  khung", b[0], "t=", b[1], "cảnh", b[2], "che", b[3])
