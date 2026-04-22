User yêu cầu: Loại bỏ các dòng "Cần xác định" hoặc "Chưa rõ" khỏi file output.

Phân tích:
- Trong hàm `process_text_content` của file `extract_checklist.py`, hiện tại đang có đoạn logic nếu vòng lặp không match được với `mapping_rules` nhưng câu có chứa các từ khóa như 'tài liệu', 'hồ sơ', thì sẽ tạo ra một dictionary với Nhóm là "Cần xác định".
- Mất khoảng 8 dòng code.

Hành động:
- Cập nhật file `extract_checklist.py` và xóa khối logic `not matched`.
- Ghi nhật ký vào `sprint_xoa_dong_undefined`.
