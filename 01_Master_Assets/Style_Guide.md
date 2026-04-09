# Bidding Document Master Style Guide

## 1. Định hướng Hành văn (Tone & Mood)

- **Danh xưng:**
  - Tuyệt đối thay thế từ "Doanh nghiệp" thành "Ngân hàng" trong toàn bộ hồ sơ.
  - Sử dụng đúng chức danh đặc thù của từng ngân hàng (Ví dụ: RBO, SRBO, RM, CBB).

- **Định hướng chiến lược (Tùy theo đối thủ):**
  - **Khi đối đầu Hãng lớn (Salesforce/Pega):** Tập trung nhấn mạnh "Giải pháp thiết kế riêng cho người Việt", "Chi phí sở hữu thấp nhất", "Tốc độ triển khai nhanh nhất".
  - **Khi đối đầu SI Local (FPT/GMO):** Tập trung nhấn mạnh "Kiến trúc lõi tiêu chuẩn Enterprise (Microservices, Kafka, MongoDB)", "Khả năng xử lý hàng chục triệu Profile không độ trễ". Cung cấp tài liệu kỹ thuật, sơ đồ diagram phức tạp để tạo sự áp đảo.

- **Tính khách quan:** Không dùng văn phong Marketing sáo rỗng. Mọi tuyên bố phải dựa trên logic, bằng chứng và ngữ cảnh ngành BFSI.

## 2. Formatting (Quy tắc Định dạng)

1. **Highlight Keyword (Bôi đậm & Nhấn mạnh):**
   - Mọi keyword bán hàng mạnh, con số ấn tượng, tỷ lệ phần trăm (%), tên công nghệ lõi (Kafka, Microservices), cam kết SLA (thời gian) phải được **BÔI ĐẬM** hoặc đổi màu chữ.
   - Khi tính năng của Mobio xịn hơn yêu cầu CĐT, bắt buộc bôi đậm dòng chữ "**Đáp ứng vượt trội!**".

2. **Cấu trúc Heading (Tôn trọng File Template):**
   - Không được tự ý thay đổi định dạng. Dán nội dung vào File Master phải theo dạng **Paste as Plain Text** hoặc **Merge Formatting**.
   - **Heading 1:** Tên chương
   - **Heading 2:** Mục lớn
   - **Heading 3:** Mục con

3. **Quy chuẩn Hình ảnh & Bằng chứng:**
   - Mọi tuyên bố "Đáp ứng hoàn toàn" BẮT BUỘC có ảnh chụp màn hình/Figma đi kèm.
   - **Khoanh đỏ:** Phải đánh dấu/khoanh đỏ đúng khu vực tính năng trên ảnh. 
   - **Chất lượng & Vị trí:** Ảnh phải to, rõ, đặt in-cell và luôn có text diễn giải bên dưới. Bề rộng ảnh thường để Width 100%.
   - **Lỗi chú ý:** Tránh dùng ảnh KHCN để tham chiếu cho tính năng dành cho KHDN.

4. **Dẫn chiếu chi tiết:**
   - Cấm ghi chung chung kiểu "Xem tài liệu nộp kèm". 
   - Định dạng chuẩn: `Tên Tài liệu -> Chương -> Mục (Trang XX / Hình YY)`.
