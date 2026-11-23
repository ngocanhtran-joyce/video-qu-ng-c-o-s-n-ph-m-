"""Tìm mặt người trên video đã ghép (base.mp4) để đồ hoạ + phụ đề né mặt.
usage: python3 faces.py <base.mp4> <faces.json>
Ra: {"fps": 10, "boxes": [[[x,y,w,h], ...] cho mỗi khung 0.1s]} — toạ độ khung 1080x1920, đã nới rộng
phủ cả tóc/cằm. Bước đồ hoạ gộp mọi khung trong cùng một cảnh để không lọt khung nhận dạng hụt."""
import sys, json, os, subprocess
import numpy as np, cv2

FPS = 10
MODEL = os.path.join(os.path.dirname(__file__), "..", ".cache", "models", "yunet.onnx")
if not os.path.exists(MODEL):
    subprocess.run(["curl", "-sSL", "-m", "60", "-o", MODEL, "--create-dirs",
                    "https://media.githubusercontent.com/media/opencv/opencv_zoo/main/models/face_detection_yunet/face_detection_yunet_2023mar.onnx"], check=True)

src, out = sys.argv[1], sys.argv[2]
SW, SH = 540, 960
det = cv2.FaceDetectorYN.create(MODEL, "", (SW, SH), score_threshold=0.8, nms_threshold=0.3, top_k=20)
p = subprocess.Popen(["ffmpeg", "-v", "error", "-i", src, "-vf", f"fps={FPS},scale={SW}:{SH}", "-f", "rawvideo",
                      "-pix_fmt", "bgr24", "-"], stdout=subprocess.PIPE)
raw = []
while True:
    buf = p.stdout.read(SW * SH * 3)
    if len(buf) < SW * SH * 3:
        break
    img = np.frombuffer(buf, np.uint8).reshape(SH, SW, 3)
    _, faces = det.detect(img)
    boxes = []
    for f in (faces if faces is not None else []):
        x, y, w, h = [v * 2 for v in f[:4]]           # về khung 1080x1920
        if w < 70:                                     # quá nhỏ: thường là nhận nhầm (hoa, logo, phản chiếu kính)
            continue
        bx, by = x - 0.40 * w, y - 0.60 * h            # nới: tóc, tai, cằm
        bw, bh = w * 1.8, h * 2.0
        boxes.append([round(max(0, bx)), round(max(0, by)), round(min(1080, bx + bw) - max(0, bx)), round(min(1920, by + bh) - max(0, by))])
    raw.append(boxes)
merged = raw  # gộp theo từng cảnh ở bước đồ hoạ (mọi khung trong cảnh)
json.dump({"fps": FPS, "boxes": merged}, open(out, "w"))
hit = sum(1 for b in raw if b)
print(f"{len(raw)} khung, {hit} khung có mặt người -> {out}")
