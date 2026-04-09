# TIÊU CHÍ ĐÁNH GIÁ ĐẦU RA BƯỚC 1 (EVALUATION CRITERIA & DoD)

*Tài liệu này là chốt chặn cuối cùng. Để dán nhãn "HOÀN THÀNH BƯỚC 1" và cho phép luồng dữ liệu trôi sang Bước 2, bộ phận QA hoặc AI QC phải chấm điểm và check đạt yêu cầu các tiêu chí khắt khe dưới đây.*

---

## 1. Definition of Done (DoD - Điều Kiện Hoàn Thành)
*Công việc chỉ được coi là xong (Done) khi đáp ứng toàn bộ các gạch đầu dòng sau:*
- [ ] Dữ liệu Mời Thầu (RFP) đã được dọn sạch rác, lưu ở định dạng Machine-Readable (Docx/PDF chuẩn text/Txt). Tuyệt đối không còn file ảnh scan nhòe.
- [ ] Bảng Form "Thông tin tóm tắt gói thầu" đã được điền đủ 100% các trường căn bản (Tên, Chủ thầu, Đích nộp).
- [ ] Báo cáo rủi ro (Risk Assessment) đã đối chiếu qua thư viện Blacklist và Rule Pháp lý để gửi đến Lãnh đạo.
- [ ] Lãnh đạo đã tick chọn "GO" (Quyết định triển khai) bằng văn bản/tin nhắn.

---

## 2. Checklist Đánh Giá Đầu Ra (Output Checklist)
*File output sinh ra phải cầm nắm được. Bộ phận kiểm duyệt đánh dấu (x) khi đã nhận đủ vệt tài liệu vật lý sau đưa sang Bước 2:*
- [ ] Có file `RFP_Goc_Da_Lam_Sach.pdf` (Tài liệu gốc).
- [ ] Có Form Tóm tắt gói thầu (Đã điền).
- [ ] Có Báo Cáo Yếu tố Vi phạm rủi ro (Danh sách bãi mìn).

---

## 3. Thang Chấm Điểm Thẩm Định Khả Thi (Scoring Matrix)
*Dành cho AI hoặc Quản lý tự chấm nhanh độ "ngon" của dự án thầu. Giúp đưa ra quyết định có đáng để dồn sức kỹ thuật cho Bước 3 hay không.*

| Tiêu chí Thẩm định | Trọng số | Điểm 1-4 (Yếu/Nguy Hiểm) | Điểm 5-7 (Tạm ổn/Sửa được) | Điểm 8-10 (Tuyệt vời) | Chốt Action Của AI |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Độ Sạch Của Đầu Vào (Readable)** | 30% | File ảnh chụp nghiêng, nhòe mờ, không thể OCR. | PDF text xen lẫn hình decor, cần tỉa tót rác. | Văn bản Docx chuẩn, cấu trúc heading rõ ràng 1-2-3. | Trả <5đ -> Ngừng máy, Đòi AM gõ lại. |
| **Độ Rủi Ro Thương Mại (Risk Level)**| 50% | Dính vào Tiêu chí Tử huyệt (Bắt giao source code, ngân sách < 50tr). | Có yêu cầu hơi quá đáng ngốn nguồn lực (Bắt code tool free). | Đề bài bám cực sát năng lực lõi của cty. Ít customize. | Trả <5đ -> Đề xuất NO-GO. |
| **Tính Kiên Quyết Mốc Deadline** | 20% | Yêu cầu thời gian mập mờ "Sớm nhất có thể". | Có mốc ngày nhưng lại không ghi cụ thể gửi tới email nào. | Rõ ràng Ngày-Giờ-Phút nộp bài, Tên/SĐT người nhận bản cứng. | Trả <5đ -> Gọi hỏi check Khách hàng. |

**> QUYẾT ĐỊNH PASS CỬA:** Điểm tổng trung bình có trọng số > **6.0 điểm** VÀ đặc biệt không có tiêu chí nào vấp phải **Khung Mức Rủi Ro (1-4)**. Nếu dính 1 điểm Yếu là tự động bật đèn đỏ chờ người phân xử.
