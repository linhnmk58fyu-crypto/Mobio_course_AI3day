# Nhật Ký Công Việc

- **[2026-04-10]**: Bắt đầu sprint xử lý yêu cầu tạo input/output cho data RFP.
  - Đã list các file trong `Master_Knowledge_Base` và kiểm tra dung lượng các file `.xlsx` trong `Customer_Specific/RFP_Response`.
  - Các file rất lớn (từ 27MB đến 74MB), không thể xử lý nạp thô vào context của LLM mà phải dùng script Python.
  - Đã chốt theo Hướng 1 là viết script auto data pipeline.
  - Viết `extract.py` và chạy trên 3 file `Customer_Specific/RFP_Response`.
  - Kết quả: Đã trích xuất và phân loại thành công 2186 dòng yêu cầu vào đúng 5 file nhóm ở thư mục `RFP_Library` để làm input cho các Agent đấu thầu tiếp theo.
