| Ngân hàng | File / Tab (Sheet)                                         | Cột "Yêu cầu" (Input)            | Cột "Diễn giải" (Output)      | Ghi chú cho AI                                             |
| ----------- | ---------------------------------------------------------- | ----------------------------------- | -------------------------------- | ----------------------------------------------------------- |
| LPBank      | Tất cả các Tab (Nghiệp vụ, Kỹ thuật, Đính chính) | Cột D (Nội dung chi tiết)        | Cột G (Diễn giải đáp ứng)  | Dữ liệu bắt đầu từ dòng 4. Cột E là mức độ M/O. |
| OCB         | Yêu cầu tính năng                                      | Cột D (Mô tả tính năng)        | Cột J (Giải thích đáp ứng) | Header phức tạp, bắt đầu nhặt từ dòng 6.            |
|             | Yêu cầu kỹ thuật                                       | Cột C (Mô tả yêu cầu)          | Cột E (Giải thích đáp ứng) | Cột D là trạng thái Full/Partial.                       |
|             | Yêu cầu Non Functional                                   | Cột C (Mức yêu cầu tối thiểu) | Cột F (Giải thích đáp ứng) | Tập trung vào Hiệu năng/Security.                       |
|             | Các yêu cầu khác                                       | Cột B (Nội dung yêu cầu)        | Cột E (Giải thích đáp ứng) | Chứa Năng lực/Pháp lý.                                 |
|             | EST MD                                                     | Cột C (Tính năng)                | Cột I (Tuyên bố đáp ứng)   | Dùng để đối chiếu khối lượng công việc.          |
| SeABank     | KPI                                                        | Cột C (Nội dung chi tiết)        | Cột G (Diễn giải đáp ứng)  | Gắn tag "Nghiệp vụ".                                     |
|             | Nghiệp vụ (Tab C, D, E)                                  | Cột C (Nội dung chi tiết)        | Cột G (Diễn giải đáp ứng)  | Gắn tag "Nghiệp vụ".                                     |
|             | F. Yêu cầu công nghệ                                   | Cột B (Nội dung chi tiết)        | Cột E (Diễn giải đáp ứng)  | Gắn tag "Kỹ thuật".                                      |
|             | A. Năng lực kinh nghiệm                                 | Cột C (Mô tả yêu cầu)          | Cột F (Diễn giải đáp ứng)  | Gắn tag "Pháp lý/Tài chính".                           |
|             | B. Năng lực triển khai                                  | Cột C (Mô tả yêu cầu)          | Cột F (Diễn giải đáp ứng)  | Gắn tag "Kinh nghiệm triển khai".                        |

Hướng dẫn lấy dữ liệu:

* **Skip Headers:** Bỏ qua các dòng tiêu đề (thường là 1-4 dòng đầu tùy file).
* **Context Carry-over:** Nếu cột "Yêu cầu" ở dòng hiện tại trống, hãy lấy nội dung của "Yêu cầu" ở dòng gần nhất phía trên (xử lý vấn đề merge cell/grouping).
* **Data Cleaning:** Loại bỏ các ký tự xuống dòng thừa trong ô Diễn giải để giữ định dạng bảng phẳng cho Tầng 2.
