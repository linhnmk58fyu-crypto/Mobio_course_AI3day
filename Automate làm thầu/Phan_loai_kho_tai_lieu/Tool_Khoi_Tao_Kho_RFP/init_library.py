import pandas as pd
import re
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Relative paths to ensure portability across accounts/computers
script_dir = os.path.dirname(os.path.abspath(__file__))
input_dir = os.path.join(script_dir, "..", "Kho_Tai_Lieu", "Customer_Specific", "RFP_Response")
pub_dir = os.path.join(script_dir, "..", "Kho_Tai_Lieu", "RFP_Library")

# Thư mục lưu log (không bắt buộc)
output_dir = os.path.join(script_dir, "logs_khoi_tao")

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

if not os.path.exists(pub_dir):
    os.makedirs(pub_dir)

def clean_text(text):
    if pd.isna(text): return "[MISSING_DATA]"
    text = str(text)
    # Xử lý format theo Rule: Đổi tên Ngân hàng thành [BANK_NAME]
    text = re.sub(r'(?i)(LPBank|OCB|SeABank)', '[BANK_NAME]', text)
    # Lược bỏ các ký tự xuống dòng chèn trong Excel
    text = re.sub(r'\n+', ' ', text).strip()
    if not text:
        return "[MISSING_DATA]"
    return text

def categorize(req_text, sheet_hint=""):
    # Phân loại dựa trên keyword mapping
    text = str(req_text).lower() + " " + sheet_hint.lower()
    
    if any(k in text for k in ['api', 'microservices', 'mã hóa', 'bảo mật', 'security', 'kafka', 'k8s', 'cloud', 'tích hợp', 'database', 'công nghệ', 'non functional', 'kiến trúc']):
        return "2. Kỹ thuật (Technical)"
    
    if any(k in text for k in ['vốn điều lệ', 'báo cáo tài chính kiểm toán', 'báo cáo tài chính năm', 'gpđkkd', 'bảo lãnh dự thầu', 'bảo lãnh bảo hành', 'bảo lãnh thực hiện hợp đồng', 'bảo lãnh tạm ứng', 'nda', 'giấy phép đăng ký kinh doanh']):
        return "3. Tài chính & Pháp lý"
    
    if any(k in text for k in ['hợp đồng tương tự', 'kinh nghiệm nhà thầu', 'kinh nghiệm triển khai', 'biên bản nghiệm thu', 'bbnt', ' cv ', ' pm ', ' ba ', 'thời gian triển khai dự án', 'project plan', 'năng lực triển khai', 'kế hoạch triển khai dự án']):
        return "4. Năng lực triển khai"
    
    if any(k in text for k in ['tài liệu hướng dẫn', 'tài liệu kỹ thuật', 'đào tạo', 'vận hành hệ thống', 'bảo trì', 'cam kết sla', 'sla hỗ trợ', 'sla xử lý sự cố', 'support', 'chuyển giao', 'bảo hành']):
        return "5. Chuyển giao & Đào tạo"
    
    return "1. Nghiệp vụ (Functional)"

all_data = []

def process_sheet(file_name, sheet_name, df, req_col, resp_col, start_row, sheet_hint=""):
    print(f"   Processing: {file_name} -> {sheet_name}")
    # Convert row limit: 1-based index to 0-based
    df = df.iloc[start_row-1:]
    
    if req_col < len(df.columns):
        df.iloc[:, req_col] = df.iloc[:, req_col].ffill() # forward fill for merged cells
        
    count = 0
    for index, row in df.iterrows():
        if req_col >= len(row) or resp_col >= len(row): continue
        req_val = row.iloc[req_col]
        resp_val = row.iloc[resp_col]
        
        if pd.isna(req_val) or str(req_val).strip() == "":
            continue
            
        req_clean = clean_text(req_val)
        resp_clean = clean_text(resp_val)
        
        cat = categorize(req_clean, sheet_hint)
        
        all_data.append({
            "Ngân hàng": file_name.split(' ')[0],
            "Tab": sheet_name,
            "Nhóm": cat,
            "Yêu cầu": req_clean,
            "Diễn giải đáp ứng": resp_clean
        })
        count += 1
    print(f"     => Found {count} lines.")

print("=======================================================")
print("      KHOI TAO KHO TRI THUC THAU TU DU LIEU CU")
print("=======================================================\n")
print("Dang quet muc:", input_dir, "\n")

# --- Xử lý LPBank ---
lp_file = os.path.join(input_dir, "LPBank - RFP Response.xlsx")
if os.path.exists(lp_file):
    print("Reading LPBank...")
    try:
        xls = pd.ExcelFile(lp_file)
        for sheet in xls.sheet_names:
            df = pd.read_excel(xls, sheet_name=sheet, header=None)
            process_sheet("LPBank - RFP Response.xlsx", sheet, df, 3, 6, 4)
    except Exception as e:
        print(f"  -> Bo qua LPBank: {e}")

# --- Xử lý OCB ---
ocb_file = os.path.join(input_dir, "OCB - RFP Response.xlsx")
if os.path.exists(ocb_file):
    print("Reading OCB...")
    try:
        xls = pd.ExcelFile(ocb_file)
        for sheet in xls.sheet_names:
            df = pd.read_excel(xls, sheet_name=sheet, header=None)
            sheet_l = sheet.lower()
            if "tính năng" in sheet_l:
                process_sheet("OCB - RFP Response.xlsx", sheet, df, 3, 9, 6, sheet_hint="nghiệp vụ")
            elif "kỹ thuật" in sheet_l:
                process_sheet("OCB - RFP Response.xlsx", sheet, df, 2, 4, 6, sheet_hint="kỹ thuật")
            elif "non functional" in sheet_l:
                process_sheet("OCB - RFP Response.xlsx", sheet, df, 2, 5, 6, sheet_hint="kỹ thuật")
            elif "các yêu cầu khác" in sheet_l:
                process_sheet("OCB - RFP Response.xlsx", sheet, df, 1, 4, 6)
            elif "est md" in sheet_l:
                process_sheet("OCB - RFP Response.xlsx", sheet, df, 2, 8, 6)
    except Exception as e:
        print(f"  -> Bo qua OCB: {e}")

# --- Xử lý SeABank ---
sea_file = os.path.join(input_dir, "SeABank - RFP Response.xlsx")
if os.path.exists(sea_file):
    print("Reading SeABank...")
    try:
        xls = pd.ExcelFile(sea_file)
        for sheet in xls.sheet_names:
            df = pd.read_excel(xls, sheet_name=sheet, header=None)
            sheet_l = sheet.lower()
            if "kpi" in sheet_l or any(x in sheet_l for x in ["tab c", "tab d", "tab e", "nghiệp vụ"]):
                process_sheet("SeABank - RFP Response.xlsx", sheet, df, 2, 6, 4, sheet_hint="nghiệp vụ")
            elif "công nghệ" in sheet_l or "f." in sheet:
                process_sheet("SeABank - RFP Response.xlsx", sheet, df, 1, 4, 4, sheet_hint="kỹ thuật")
            elif "năng lực kinh nghiệm" in sheet_l or "a." in sheet:
                 process_sheet("SeABank - RFP Response.xlsx", sheet, df, 2, 5, 4, sheet_hint="pháp lý")
            elif "năng lực triển khai" in sheet_l or "b." in sheet:
                 process_sheet("SeABank - RFP Response.xlsx", sheet, df, 2, 5, 4, sheet_hint="triển khai")
    except Exception as e:
        print(f"  -> Bo qua SeABank: {e}")

if not all_data:
    print("\nKhong tim thay du lieu tu cac ngan hang muc tieu.")
    exit()

# Export Raw Backup to CSV
res_df = pd.DataFrame(all_data)
out_csv = os.path.join(output_dir, "RFP_Library_Initialization_Log.csv")
res_df.to_csv(out_csv, index=False, encoding='utf-8-sig')

# Generate Library Files
for group_name, group_df in res_df.groupby("Nhóm"):
    safe_name = re.sub(r'[^a-zA-Z0-9_\-\u00C0-\u1EF9]', '_', group_name.strip()).strip('_')
    
    if "1. Nghi" in group_name: target_file = "01_Functional_Answers.xlsx"
    elif "2. K" in group_name: target_file = "02_Technical_Answers.xlsx"
    elif "3. T" in group_name: target_file = "03_Legal_Answers.xlsx"
    elif "4. N" in group_name: target_file = "04_Deployment_Experience.xlsx"
    elif "5. Chuy" in group_name: target_file = "05_Training_Transfer.xlsx"
    else: target_file = f"{safe_name}.xlsx"
    
    target_path = os.path.join(pub_dir, target_file)
    
    # Neu dang khoi tao tu dau, ghi de hoac tao moi
    group_df.to_excel(target_path, index=False)

print(f"\n[DONE] Da khoi tao Library moi tao thanh cong {len(all_data)} dong du lieu.")
print(f"File duoc luu tai: {pub_dir}")
