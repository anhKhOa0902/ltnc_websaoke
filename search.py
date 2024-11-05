import pandas as pd

# Đọc file CSV vào DataFrame
df = pd.read_csv('chuyen_khoan.csv')

# Hiển thị dữ liệu để xem qua cấu trúc
print(df.head())

# Ví dụ 1: Tìm tất cả các giao dịch có chi tiết chứa từ "chuyen tien"
ket_qua_chuyen_tien = df[df['detail'].str.contains('chuyen tien', case=False, na=False)]
print("Các giao dịch có chứa 'chuyen tien' trong chi tiết:")
print(ket_qua_chuyen_tien)

# Ví dụ 2: Tìm các giao dịch có credit trên 10000
ket_qua_credit_tren_10000 = df[df['credit'].astype(float) > 10000]
print("Các giao dịch có credit lớn hơn 10000:")
print(ket_qua_credit_tren_10000)

# Ví dụ 3: Tìm các giao dịch vào ngày "02/09/2024"
ket_qua_ngay_02_09 = df[df['date_time'].str.contains('02/09/2024')]
print("Các giao dịch vào ngày 02/09/2024:")
print(ket_qua_ngay_02_09)

# Ví dụ 4: Tìm các giao dịch có tên người nhận là "NGUYEN THI LAN HANH"
ket_qua_ten = df[df['detail'].str.contains('NGUYEN THI LAN HANH', case=False, na=False)]
print("Các giao dịch có người nhận là 'NGUYEN THI LAN HANH':")
print(ket_qua_ten)
