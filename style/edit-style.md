# Style dựng video

> Mặc định: talking-head / b-roll + đồ hoạ scrapbook. Câu lệnh khởi tạo có thể đổi theo video mẫu của bạn.

## Yêu cầu của chủ kênh (ưu tiên cao nhất)
- **Tiêu đề hấp dẫn hiện đủ ngay từ 0s** (t0 âm, không hiệu ứng chạy chữ).
- **3 giây đầu phải có người** trong khung hình.
- **Cắt cảnh nhanh: đổi hành động / cảnh khoảng mỗi 3s** (2–4s), xen kẽ **zoom in** (`zoom 2`) và **zoom out** (`zoom 3`) trong `edl.txt`.
- **Không khung hình nào để đồ hoạ / phụ đề che mặt người**: chạy `python3 pipeline/faces.py work/<slug>/base.mp4 work/<slug>/faces.json`
  sau bước `seg`; trong `graphics.py` đặt danh sách cảnh có người thật (`PEOPLE`) và để code tự dời thẻ/phụ đề né vùng mặt
  (xem `projects/keo/graphics.py`). Kiểm tra lại bằng `pipeline/check_faces.py` trước khi giao.
- Video quảng cáo sản phẩm: được sắp cảnh theo nội dung lời nói (không bắt buộc theo thứ tự quay); chèn ảnh sản phẩm
  tách nền từ chính cảnh quay (không dùng ảnh trên mạng có watermark/hotline của bên khác).

## Khung hình
- 1080×1920, 30fps, dài đúng bằng voice.
- **Cảnh theo thứ tự thời gian quay** (xem `creation_time` bằng ffprobe): chạy hết clip này rồi mới sang clip khác,
  **không cắt xen kẽ**, không quay lại clip cũ. Chỉ cắt ở ranh giới câu (lấy từ `transcript.json`); bỏ bớt phần đầu/cuối clip nếu dư.
- Mỗi clip zoom chậm 7% suốt đoạn cho đỡ tĩnh.

## Màu
**Không làm đẹp mặt / chỉnh dáng tự động** (đã thử, kết quả không đẹp). Chủ kênh tự chỉnh source trước khi up nếu cần.
Toàn khung chỉ chỉnh nhẹ: brightness +0.015, saturation 1.06, contrast 1.03.

## Đồ hoạ (`pipeline/gfx/lib.py`)
- **Hook**: chữ viết tay (Dancing Script) + tiêu đề lớn Fraunces 800 màu kem `#f8eda0`. **Hiện đủ cả câu ngay từ 0s** (dùng `t0` âm, không reveal từng chữ) để người xem biết ngay nội dung.
- **Giấy ghi chú** dán băng keo, giấy xé (`paper(..., cls="paper torn")`), chữ tay Patrick Hand, chữ đánh máy IBM Plex Mono.
- **Nhãn highlight vàng** + **ngôi sao đánh số** cho từng ý (`star(n)` + `label lg`).
- **Gạch ngang** `S(t, text)` khi nói điều sai / kém hiệu quả; **highlight** `H(t, text)` cho từ khoá đúng.
- Số liệu to: `num red` / `num grey`.
- Giấy nhớ vàng có dòng kẻ cho danh sách N ý.
- Đặt đồ hoạ ở vùng **y 90–650** (trên đầu người), không che mặt. Xuất hiện đúng từ khoá (lấy mốc từ word timestamps).
- **Phụ đề**: Fraunces italic 58px, 1–3 chữ/cụm, góc trái y≈1240, ẩn trong lúc hook.

## Âm thanh
highpass 80Hz → khử ồn → compressor → loudnorm −14 LUFS. Chưa có nhạc nền (chờ chủ kênh gửi nhạc).
