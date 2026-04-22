# Nhật ký hệ thống hóa cấu trúc tải RFP_Library

- **[2026-04-10]**: 
  - Khách hàng yêu cầu "cấu trúc lại các file để sau này thêm RFP mới vẫn tự động làm giàu thư viện" và "viết 1 file quy trình chuẩn".
  - Chuyển hướng tư duy: Script `extract.py` hiện tại đang bị hardcode 3 ngân hàng (LPBank, OCB, SeABank). Cần thay đổi cấu trúc thành một tool "Enrichment" với một file cấu hình Excel/CSV độc lập, cho phép định nghĩa toạ độ trích xuất mà không phải sửa code.
  - Tiến hành soạn Implementation Plan gửi khách hàng để duyệt kiến trúc Pipeline mới.
