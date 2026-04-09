# Tài Liệu Ghi Nhận Suy Nghĩ & Phân Tích (Think Out Loud)

*Theo nguyên tắc "không nghĩ ngầm", mọi đánh giá ưu nhược điểm, quyết định kiến trúc và logic luồng làm việc sẽ được cập nhật vào đây.*

---

### Ngày 04/04/2026
- **Vấn đề vị trí lưu trữ file theo dõi:** Thay vì để các file theo dõi (`todolist.md`, `work_log.md`) vào trong một folder con như `Sprint_1` khiến khó theo dõi toàn bộ tiến trình lớn, quyết định là sẽ đặt 3 file này ra thư mục gốc (`Dự án RFP`).
- **Logic Quản trị:** Việc lưu ngoài gốc giúp chúng ta có góc nhìn "Bird-eye-view". Bất kỳ sprint con nào (Sprint 1, Sprint 2...) cũng đều cập nhật tiến độ về `todolist` chung và ghi log vào `work_log.md` chung này để có *Single Source of Truth* cho công tác quản lý đầu việc. Khi code hay bóc tách dữ liệu mới thực sự cho vào `Sprint_1` folder.
- **Phân tích độ tin cậy của Use Case Document:** Khi làm động tác chạy nhẩm luồng IPO trong đầu (Mock simulation), nhận thấy Use Case được vẽ ra ở viễn cảnh rất lý tưởng (Happy Case). Nếu đưa thẳng cho AI automate, hệ thống sẽ gãy ngay điểm chạm với con người (làm sao AI biết con người đã review xong trên excel để mà chạy tiếp bước sau?), và lỗ hổng nguy hiểm nhất là cơ chế phê duyệt dữ liệu để Train lại vòng đời 2 (Approve to Train) chưa được mảy may tính đến. Sẽ tốn nhiều effort xử lý cơ chế rẽ nhánh nếu Go/No-go tạch ở bước 1.
- **Phân định Ranh giới Hệ thống (Man vs. Machine):** Việc tách bạch rõ "Người làm trực giác phi cấu trúc" và "Máy làm chỉnh sửa cấu trúc" là nền tảng cốt lõi của Human-in-the-loop (HITL). Tuy nhiên, điểm G của hệ thống nằm ở 3 nốt thắt: Cổng Data đầu vào (giấy/quang học), Cổng Nhập liệu Draft (Google Sheet vs. UI/UX custom) và Cổng Ghi đè Quyết định (Override). Nếu không chốt được 3 cổng này bằng các logic rẽ nhánh, hệ gen AI sẽ không tự trigger được. Đã đẩy câu hỏi ra cho người quyết định.
- **Tái cấu trúc thiết kế Foundation (Kiến trúc Nền tảng):** Khi nhận được yêu cầu nâng cấp từ người dùng (reference kiến trúc), phải từ bỏ tư thế "thợ code" lao vào viết script băm nhỏ dữ liệu ngay. Việc định hình lại thành 5 Tầng: (1) Checkpoint Ranh giới, (2) Tổ chức Database (Approve mechanism), (3) Vòng lặp feedback, (4) Rule-based Matrix và (5) Cơ chế QC chéo, sẽ giúp hệ thống này có thể scale lên làm một App chuẩn. Đã hoàn thiện draft lên Kế hoạch Thực thi (Implementation Plan).
