# Xử lý Dữ liệu RFP Response Dựa Trên Master Knowledge Base

Dựa trên yêu cầu của anh và các file có trong `Master_Knowledge_Base`, kịch bản triển khai được xác định là:

## Hướng 1: Viết Script Tự Động Hóa Bằng Python

Sử dụng `pandas` để xử lý hàng loạt thay vì làm tay.
- **Đầu vào (Input):** 3 file Excel trong `Customer_Specific/RFP_Response`.
- **Thực thi:** 
  1. Script đọc file `huongdanlaydulieu.md` để tự động map cột tương ứng cho LPBank, OCB, SeABank (bỏ qua header rác, nối các ô merge cell content).
  2. Áp dụng các keyword từ `keyword_phanloai.md` để tự động dán nhãn 5 nhóm.
  3. Áp dụng chuẩn hóa theo `quytrinhtonghop.md`: Đổi tên Ngân hàng thành `[BANK_NAME]`, thay dòng trống là `[MISSING_DATA]`, lược bỏ ký tự xuống dòng thừa.
- **Đầu ra (Output):** Xuất dữ liệu đã phân nhóm thành danh sách phẳng (CSV hoặc Excel gộp) rồi đẩy vào thư mục `Tầng 2: RFP_Library` - như một Data Lake sạch để sau này phục vụ các luồng thầu khác.

*Kế hoạch đã được người dùng chốt phương án 1 vào ngày 2026-04-10.*
