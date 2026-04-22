# Think Outloud

- **Mục tiêu**: Tạo cấu trúc thư mục cho Kho tài liệu làm thầu với 3 tầng logic.
- **Tiến trình dự kiến**:
  1. Tạo toàn bộ cấu trúc thư mục bên trong thư mục `sprint_tao_cau_truc_thu_muc` để "cách ly" không làm rối file gốc trước khi hoàn thành.
  2. Các thư mục gồm: `Master_Knowledge_Base`, `RFP_Library`, `Customer_Specific` (cùng các thư mục con tương ứng cho ngân hàng `LPBank`, `OCB`, `SeABank`).
  3. Sau khi xác nhận cấu trúc tạo ra đã đúng và full, tiến hành move/merge chúng về thư mục chung (dự tính là trong `Phan_loai_kho_tai_lieu` gốc).
- **Lý luận**:
  - Yêu cầu của người dùng là tuân thủ việc xử lý trong folder sprint, có nghĩa là tất cả kết quả nháp phải nằm trong sprint này. Chỉ khi check xong xuôi mới đẩy lên hoặc ra ngoài.
  - Có các file hướng dẫn định dạng doc (.pdf, .xlsx), nhưng người dùng chỉ bảo là "tạo thư mục" theo hướng dẫn. Vậy tôi chỉ tạo directory, không tạo placeholder file unless requested, nhưng nếu file là giả định thì để rỗng hoặc tạo luôn placeholder file để tường minh? Không, "Hãy tạo thư mục theo hướng dẫn sau", nên chỉ tạo thư mục.
