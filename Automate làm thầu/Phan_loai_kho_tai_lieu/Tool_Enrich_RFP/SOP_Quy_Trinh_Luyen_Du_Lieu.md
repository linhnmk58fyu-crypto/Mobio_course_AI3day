# QUY TRÌNH HƯỚNG DẪN LÀM GIÀU DỮ LIỆU RFP (SOP)

Tài liệu này hướng dẫn chị cách chạy hệ thống tự động `Tool_Enrich_RFP`. Bất cứ khi nào phòng ban trúng hoặc fail một cái thầu, chị lấy file Phản hồi RFP cuối cùng bỏ vào đây để làm giàu kho dữ liệu tri thức của công ty.

## Bước 1: Copy file Excel mới vào Pipeline
1. Chép tất cả các file Excel RFP mới tải về.
2. Dán file vào thư mục: `Tool_Enrich_RFP/Input_New_RFP/`.
*(Hệ thống sẽ giữ lại tên Ngân hàng làm mốc truy vết, chị ghi tên file có chứa chữ như `MBBank - Response.xlsx` thì càng tốt).*

## Bước 2: Thiết lập Tọa độ (Mapping Config)
Hệ thống không tự biết đọc cột nào. Chị phải mở file Excel `rfp_mapping_config.csv` (Mở bằng Excel cực kì dễ dàng) và cập nhật cấu trúc:

| FileName_Keyword | SheetName_Keyword | Col_Requirement | Col_Response | Start_Row | Tag_Hint |
| --- | --- | --- | --- | --- | --- |
| MBBank | Nghiệp vụ | C | F | 6 | nghiệp vụ |
| .* | Non Functional | A | B | 1 | kỹ thuật |

**Giải thích thông số:**
- `FileName_Keyword`: Tên Ngân hàng (chỉ cần nhập `MBBank`, nó sẽ tự khớp chuỗi). Nếu áp dụng cho mọi file, nhập `.*`.
- `SheetName_Keyword`: Chữ nhận diện trong tên Sheet (Tab). Ví dụ ở MB có "Nghiệp vụ" thì gõ `Nghiệp vụ`, nó sẽ quét mọi tab chứa chữ đó. Để trống hoặc `.*` là chạy ở toàn bộ tab.
- `Col_Requirement`: Cột chứa **Yêu cầu của Khách Hàng**. VD: cột `D`.
- `Col_Response`: Cột chứa **Câu trả lời Tuyên bố Đáp ứng / Diễn giải**. VD: cột `G`.
- `Start_Row`: Dữ liệu bắt đầu từ dòng bao nhiêu? (Tránh Header làm rác hệ thống). VD: dòng `4`.
- `Tag_Hint` (Không bắt buộc): Gợi ý thêm hệ thống đây là tài liệu loại gì (ghi chữ `kỹ thuật` hoặc `nghiệp vụ` hoặc `pháp lý`).

## Bước 3: Click Chạy Pipeline (Chỉ tốn 10 giây)
- Sau khi điền xong CSV, lưu bảng đó lại.
- Trở về thư mục `Tool_Enrich_RFP`. Khỏi cần mở gõ code phức tạp, chị chỉ cần bấm **kích đúp chuột vào file `run_pipeline.bat`**. 
- Hệ thống sẽ tự động bật cửa sổ hiển thị tiến độ quét file. Khi chữ chạy xong, tức là thư viện đã được nhồi Data thành công!

> *(Dành cho dân IT: Hoặc mở Terminal gõ `python enrich_rfp_library.py`)*

## Bước 4: Kiểm tra Thành quả (Check Output)
- Khi chạy xong, Tool sẽ thông báo nạp thành công bao nhiêu Row. (Đừng lo nếu chạy trùng, Tool có tích hợp cơ chế chống rác Duplicate xịn nhất).
- Toàn bộ kết quả đã được gộp lại, thêm mới khéo léo vào phía cuối dòng của các file tại thẻ nhớ lớn:
  `Automate làm thầu/Phan_loai_kho_tai_lieu/Kho_Tai_Lieu/RFP_Library/`
- Bây giờ, thư viện của bạn vừa được cộng dồn thêm data để cho bọn AI xài sau này rồi nhé!

---
*Lưu ý: Nếu cần thay đổi luật tự động chuẩn hóa dấu, tự thay tên Ngân Hàng để giấu thông tin, hãy nhờ đội DEV thay đổi trong logic `clean_text` của `enrich_rfp_library.py`.*
