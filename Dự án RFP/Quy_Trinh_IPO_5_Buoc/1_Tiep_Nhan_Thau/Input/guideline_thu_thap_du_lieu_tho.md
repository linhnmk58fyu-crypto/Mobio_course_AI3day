# Hướng dẫn thu thập thông tin và xử lý dữ liệu thô (Bước 1)

**Mục tiêu:** Đảm bảo mọi Hồ sơ mời thầu (RFP) dù gửi qua đường nào (Email, Zalo, Bản cứng) đều được số hóa, làm sạch và gom về một nguồn chuẩn hóa trước khi quăng cho AI xử lý.

## 1. Nguồn thu thập
- Hồ sơ Mời thầu điện tử (Hệ thống thầu quốc gia / Email Khách hàng).
- File mềm rải rác qua Zalo cá nhân của bộ phận AM/Sales.
- Bản giấy đóng mộc (Gửi qua bưu điện).

## 2. Quy trình xử lý dữ liệu thô
### Dành cho Nhân sự (Người):
- **Bản giấy/Scan nhòe:** Sử dụng phần mềm OCR (như Adobe Scan, CamScanner hoặc FPT.AI Reader) để quét lại các trang có chứa text. **Tuyệt đối không đẩy file ảnh đuôi .JPEG/.PNG thẳng cho AI** ở hệ thống hiện tại.
- **Tập hợp file:** Gom toàn bộ file đính kèm, thư mời, phụ lục vào thành 1 cục Zip.

### Dành cho Hệ thống (AI):
- Chỉ tiếp nhận định dạng chuẩn: `.docx`, `.pdf` (có thể bôi đen text) hoặc `.xlsx`.
- Loại bỏ các trang rác (trang bìa trang trắng, hình ảnh decor) để tiết kiệm token khi đọc.

## 3. Tiêu chuẩn đầu ra của khâu tiền kỳ
Chỉ khi nào 1 bộ hồ sơ đạt đủ điều kiện "Readable" (Máy đọc được), nó mới được đặt vào thư mục `Input/mockup_data` để quy trình nhảy sang bước tiếp theo.
