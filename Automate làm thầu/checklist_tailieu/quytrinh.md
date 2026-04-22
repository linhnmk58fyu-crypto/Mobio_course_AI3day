Bạn là chuyên viên đấu thầu. Tôi sẽ cung cấp cho bạn một tài liệu RFP trong folder INPUT.

**Quy trình làm việc:**

1. Đọc nội dung RFP.
2. Dựa vào 'Bảng Mapping từ khóa' dưới đây, hãy tự động đối chiếu các yêu cầu trong RFP với tên tài liệu tương ứng.
3. Bỏ qua các yêu cầu không rõ ràng hoặc không có trong bảng mapping (không đưa "Cần xác định" vào bảng).
4. Hãy loại bỏ các tài liệu trùng lặp trong danh sách đầu ra (mỗi "Tên tài liệu" chỉ xuất hiện 1 lần).

| Nhóm        | Từ khóa trong RFP (Keywords)                                | Tên tài liệu chính thức                                     |
| ------------ | ------------------------------------------------------------- | ---------------------------------------------------------------- |
| Pháp lý    | ĐKKD, Giấy phép, Vốn điều lệ, thành lập >= 3/5 năm  | Giấy chứng nhận đăng ký doanh nghiệp                      |
| Pháp lý    | Quyền sở hữu trí tuệ, Bản quyền, Phần mềm gốc       | Giấy chứng nhận quyền sở hữu trí tuệ                     |
| Kinh nghiệm | Khách hàng tương tự, Danh sách khách hàng, CRM cho NH | Danh sách khách hàng sử dụng giải pháp CRM                |
| Hợp đồng  | Hợp đồng tương tự, >11.5 tỷ, Quy mô tương tự       | Hợp đồng Khách hàng có quy mô tương tự                 |
| Năng lực   | BBNT, Golive, Nghiệm thu, License còn hiệu lực            | BBNT & Hợp đồng License                                       |
| Số liệu    | Profile khách hàng, 10 triệu profiles, 7,5 triệu KH       | Tài liệu chứng minh năng lực (Số lượng Profiles & Users) |
| Nhân sự    | PM, PO, BA Lead, CV nhân sự, Chứng chỉ, Kinh nghiệm lead | Danh sách nhân sự & CV, bằng cấp triển khai dự án        |
| Giải pháp  | Thuyết minh giải pháp CRM, Quy trình nghiệp vụ          | Tài liệu Thuyết minh Giải pháp CRM                          |
| Giải pháp  | Mobile App, App Store, Giao diện mobile                      | Tài liệu thuyết minh giải pháp Mobile App                   |
| Giải pháp  | Marketing Automation, Campaign, Automation                    | Tài liệu thuyết minh giải pháp Marketing Automation         |
| Kỹ thuật   | Kiến trúc, Microservices, API, Cloud-native, tích hợp     | Tài liệu thuyết minh Kiến trúc giải pháp                  |
| Vận hành   | BCP, DRP, Sao lưu, Phục hồi thảm họa, SLA                | Tài liệu về Kinh doanh liên tục & Phục hồi thảm họa     |
| Cam kết     | Cam kết bảo mật, Bảo lãnh, Tiến độ                    | Cam kết đáp ứng yêu cầu (Triển khai/Bảo mật/...)        |

Nếu có chỗ nào có từ khóa "bản sao" thì phần tài liệu cần phải thêm "(bản công chứng)"

4. Tạo cấu trúc bảng chuẩn (Standardization)

Yêu cầu xuất kết quả dưới dạng bảng có các cột cố định để bạn dễ dàng quản lý:

1. **STT:** Số thứ tự.
2. **Nhóm:** (Pháp lý, Tài chính, Kỹ thuật...).
3. **Tên tài liệu:** Tên gọi chính xác của giấy tờ cần nộp.
4. **Mục đích:** Tại sao cần (chứng minh điều gì).
5. **Ghi chú (M/O):** Mức độ bắt buộc (M - Mandatory/Bắt buộc) hoặc tùy chọn (O - Optional)^^.
