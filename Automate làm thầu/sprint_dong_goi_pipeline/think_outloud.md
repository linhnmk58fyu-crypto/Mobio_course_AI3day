# Think Outloud

- **Phân tích vấn đề:** Script Python lần trước tuy chạy tốt trên 3 file Excel khách đưa, nhưng điểm yếu chết người của tự động hóa này là nó **hardcode**. Nếu ngày mai có RFP từ MBBank vào, khách sẽ không biết chèn code Python thế nào.
- **Giải pháp:** Cần tách rời phần "Logic bóc tách" và "Tọa độ cấu hình".
  - **Tọa độ cấu hình:** Dùng 1 file CSV tên là `rfp_mapping_config.csv`. Khách chỉ cần điền: Tên file, Tên sheet, Cột Yêu Cầu, Cột Diễn giải, Dòng bắt đầu, Tag Gợi ý.
  - **Logic bóc tách:** Script `enrich_library.py` sẽ đọc CSV này, chạy trên RFP Excel, và thay vì TẠO MỚI (overwrite), nó sẽ MỞ các file `01_Functional_Answers.xlsx` có sẵn trong RFP_Library và APPEND thêm vào cuối file. Cuối cùng deduplicate (xóa dòng trùng) nếu khách nhỡ chạy 2 lần.
- **Hệ thống hóa:** Soạn `quy_trinh_enrich.md` (Quy trình vận hành chuẩn SOP) để giải thích tường tận cách điền CSV và chạy script.
- **Tiến trình:** Đẩy lên Artifact cho khách duyệt trước vì thay vì tạo 1 file, ta đang tái cấu trúc thành nguyên bộ Pipeline Appender.
