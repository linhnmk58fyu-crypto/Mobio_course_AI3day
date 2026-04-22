User yêu cầu: File excel input chưa được quét do script hiện tại chỉ đọc `*.txt`. Yêu cầu quét toàn bộ các sheet trong file Excel.

Kế hoạch giải quyết:
- Viết hàm `extract_sentences_from_excel(filepath)` sử dụng `pandas` để duyệt qua tất cả các sheets.
- Gộp nội dung string từ các cells và tách thành câu.
- Sửa lại hàm main trong `extract_checklist.py` để hỗ trợ duyệt cả `.txt` và `.xlsx`.
- Tránh cài thêm thư viện phức tạp nếu pandas đã có sẵn (môi trường user đã có pandas và openpyxl).
- Cập nhật checklist và nhật ký khi hoàn thành.
