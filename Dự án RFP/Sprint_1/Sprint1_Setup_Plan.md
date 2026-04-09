# Kế hoạch & Sprint thiết lập hệ thống tự động hóa Phản hồi RFP

Dựa trên tài liệu "Use case Phản hồi RFP", mục tiêu của chúng ta là cung cấp đủ thông tin và môi trường để cả Nhân sự mới và AI Agent (Antigravity/GEM) có thể phối hợp nhịp nhàng, giúp giảm 50-80% thời gian xử lý thủ công. 

Kế hoạch này (Sprint 1) sẽ tập trung vào việc thu thập các đầu vào cốt lõi dựa trên một bộ quy tắc quản lý chặt chẽ.

---

## Nguyên Tắc Vận Hành (Working Rules)
Toàn bộ quá trình làm việc cần tuân thủ 5 nguyên tắc đã được thống nhất:
1. **Quản lý theo Sprint Folder:** Các đầu việc đang thực thi phải được nằm gọn trong một thư mục Sprint riêng biệt (như `Sprint_1`). Chỉ sau khi xử lý xong, chốt OK mới được chuyển vào folder dự án chung.
2. **Single Source of Truth (Nguồn chân lý duy nhất):** Mọi quy định, quyết định hay biểu mẫu chỉ lưu trữ ở một nguồn duy nhất và mọi thành viên/AI đều đối chiếu vào nguồn đó.
3. **Trạng thái Task rõ ràng (Todolist):** Bắt buộc duy trì cập nhật một `todolist.md` để quản lý tiến độ thực hiện (Đang làm/Đã xong/Tồn đọng).
4. **Nhật ký Công việc (Work log):** Cần ghi lại nhật ký để mô tả tiến trình phát triển và các thay đổi trong cách làm.
5. **Think out loud (Suy nghĩ ra giấy):** Không "nghĩ ngầm" các logic hay cấu trúc. Tất cả quá trình phân tích, nguyên nhân chọn giải pháp đều sẽ phải được viết xuống thành văn bản lưu lại dự án.

---

## 1. Thiết lập Bối cảnh làm việc (Context)

**Mục đích:** Đảm bảo AI Agent và nhân sự biết tìm kiếm dữ liệu ở đâu, hỏi ai, và phạm vi công việc là gì.

### Template Thu thập bối cảnh

| STT | Câu hỏi / Yêu cầu Cung cấp                                                                                                                                                   | Phản hồi từ anh [Cần anh điền]          |
| :-- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------- |
| 1   | **Kho tài liệu thầu (Knowledge Base):** Cung cấp đường dẫn (Google Drive/Local Folder) tới các bộ hồ sơ thầu cũ.                                             | `[Điền link/đường dẫn tại đây]`    |
| 2   | **Danh sách các GEM đã train:** Tên hoặc định danh của các công cụ/GEM nội bộ hỗ trợ đọc email/chat và chấm điểm thầu (như nhắc đến trong file). | `[Liệt kê danh sách GEM/AI]`             |
| 3   | **Thông tin nhân sự tham gia (PIC):** Danh sách email hoặc thông liên lạc của các Role (PO, SA, AM, PD) để AI biết cách tag/phân quyền.                     | `[Điền thông tin liên hệ hoặc nhóm]` |
| 4   | **Danh mục Domain/Industry:** Danh sách các domain/tập khách hàng ưu tiên phục vụ việc tra cứu độ tương thích.                                             | `[Điền danh sách domain]`                |

---

## 2. Thiết lập Quy trình làm việc (Workflow)

**Mục đích:** Làm rõ các công cụ sẽ sử dụng trong các bước rẽ nhánh và điểm tiếp xúc (touchpoints) giữa con người và AI.

### Checklist Chốt Workflow

| STT | Câu hỏi / Yêu cầu Cung cấp                                                                                                                                                                    | Phản hồi từ anh [Cần anh điền]         |
| :-- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------- |
| 1   | **Điểm kích hoạt (Trigger):** AI sẽ tự động bắt đầu quét khi có file RFP thả vào thư mục hay khi nhận được Email/Thông báo?                                           | `[Cách thức kích hoạt]`                |
| 2   | **Nền tảng làm việc:** Quá trình "Review 1st Draft/2nd Draft" của con người sẽ diễn ra trên nền tảng nào? (Google Sheets chia sẻ, File Excel local, hệ thống nội bộ...?) | `[Tên nền tảng/công cụ]`              |
| 3   | **Bộ Rule phân nhóm (Category Rule):** Anh có sẵn danh sách các Nhóm Tính năng (Module), Nhóm Kỹ thuật (Kiến trúc, bảo mật...) chưa? Nếu có, vui lòng cung cấp.        | `[Link tài liệu Rule phân nhóm]`       |
| 4   | **Định dạng dữ liệu JSON:** Việc lưu trữ vào kho tài liệu dưới dạng JSON sẽ do hệ thống nào quản lý lưu trữ (Database nội bộ, MongoDB, hay lưu thành file text)?   | `[Hệ thống lưu trữ cơ sở dữ liệu]` |

---

## 3. Thiết lập Template Input / Output

**Mục đích:** Số hoá các bảng biểu được mô tả trong file word thành dạng file để AI fill dữ liệu hoặc người dùng dễ dàng cung cấp dữ liệu đầu vào.

### Yêu cầu Cung cấp Template Mẫu

*(Anh vui lòng đính kèm file hoặc cung cấp link tải các file gốc có sẵn định dạng xlsx/docx)*

| STT | Tài liệu Mẫu (Template) cần cung cấp                                                                                                                              | Phản hồi từ anh [Cần anh điền]            |
| :-- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------- |
| 1   | **File "Mẫu Thông tin gói thầu":** Bản Word hoặc Excel đã chứa sẵn cấu trúc tiêu đề.                                                              | `[Link/Bản đính kèm]`                     |
| 2   | **File "Checklist hồ sơ dự thầu":** Bản Excel cần cung cấp sẵn các List option dropdown (VD: Cột Status có To do / To review...).                     | `[Link/Bản đính kèm]`                     |
| 3   | **File "Mẫu bảng phản hồi RFP":** Bản Excel hoàn chỉnh với các cột (như PIC, Trạng thái, Phân loại, Hình ảnh tham chiếu...) và Format chuẩn. | `[Link/Bản đính kèm]`                     |
| 4   | **Thiết lập "Ma trận tuyên bố đáp ứng":** Các rule vượt trội / một phần đã rõ ở file doc, nhưng anh có bảng excel mẫu cụ thể không?     | `[Có / Không / Dùng theo file tài liệu]` |
| 5   | **Bộ tiêu chí Chấm điểm:** Cần cung cấp bộ các tiêu chí để AI dựa vào đó chấm điểm phản hồi thầu trên thang từ 1-10.                   | `[Link/Bản đính kèm]`                     |

---

## Các Bước Triển Khai Sau Khi Nhận Được Thông Tin
Để bắt đầu Sprint 1 tuân thủ các quy tắc trên, công việc tiếp theo sẽ là:
1. **Khởi tạo thư mục và file quản lý:** Sẽ tạo ra folder dự án `Sprint_1`, khởi tạo các file `todolist.md` (để tracking list công việc của em và anh), `work_log.md` (Ghi lại tiến trình hàng ngày) và file `think_out_loud.md` để ghi nhận các logic luồng suy nghĩ.
2. **Khởi tạo Code / Agent (làm việc trong Sprint_1):** Bắt đầu lập trình kịch bản xử lý thông tin.
3. **Mô hình hóa dữ liệu (Single Source of Truth):** Gom các mapping, rules về 1 file config duy nhất.
