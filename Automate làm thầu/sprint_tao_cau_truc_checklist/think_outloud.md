User yêu cầu: Tạo các file và folder cần thiết để thực hiện quy trình được mô tả trong file `quytrinh.md` vào folder `checklist_tailieu`.

1. **Phân tích file `quytrinh.md`:**
- Input: folder `INPUT`.
- Resource: Bảng mapping từ khóa.
- Process: Đọc RFP, đối chiếu theo Rule, xử lý ngoại lệ (thêm "bản công chứng", đánh dấu "Cần xác định").
- Output: Bảng chuẩn gồm 5 cột.

2. **Dự kiến cấu trúc:**
- Khởi tạo thư mục `INPUT` và `OUTPUT`.
- Khởi tạo file `mapping_tu_khoa.csv` để lưu trữ file cấu hình từ khóa.
- Cần có 1 script `extract_checklist.py` (cùng file `run_extract.bat`) tự động hóa quy trình đọc file trong INPUT, đối chiếu bằng Regex hoặc string match thông thường, và xuất CSV table ra OUTPUT.

3. **Kế hoạch hành động:**
- Viết file log sprint.
- Chạy lệnh mkDir cho INPUT, OUTPUT.
- Viết file mapping_tu_khoa.csv.
- Viết file extract_checklist.py để hoàn thiện toàn bộ luồng IPO (Input - Process - Output).
- Viết file run_extract.bat để dễ sử dụng.
