User yêu cầu bổ sung 2 logic vào file `quytrinh.md` (không in dòng unmapped và phải lọc trùng lặp tài liệu) và chỉnh sửa lại file code xử lý cho đúng.

- Sprint folder: `sprint_loai_bo_trung_lap`
- Hành động:
  - Cập nhật file markdown để thay thế rule số 3 cũ thành luật bỏ qua dòng chưa rõ, chèn thêm luật lọc trùng lặp số 4.
  - Sửa `extract_checklist.py`: Tại bước xuất CSV, sẽ duyệt qua danh sách `all_results`, nếu cột "Tên tài liệu" đã tồn tại trong mảng Set `seen_docs` thì bỏ qua dòng đó. 
  - Test lại số dòng output.
