### Nhật ký công việc

* **Thời gian bắt đầu**: 2026-04-21 16:50:00
* **Công việc**: Cập nhật file `quytrinh.md` theo 2 rule mới, và triển khai tính năng deduplicate (xóa lặp) trong mã nguồn.
* **Diễn biến**:
  - Tạo `sprint_loai_bo_trung_lap`.
  - Cập nhật dòng số 3, 4 trong file `quytrinh.md` đúng với tinh thần gạt bỏ file không rõ ràng và lọc trùng.
  - Sửa logic hàm `main()` trong `extract_checklist.py` để sử dụng cấu trúc dữ liệu `Set` lưu trữ `seen_docs` (những tên tài liệu đã gặp), qua đó bỏ qua nếu văn bản lặp lại yêu cầu.
  - Test chạy lệnh lại. Kết quả giảm từ 211 mục gộp xuống còn vỏn vẹn **15 loại tài liệu** duy nhất.
* **Kết quả**: Output đã được cô đọng triệt để. Code đã tích hợp. Sprint hoàn thành.
