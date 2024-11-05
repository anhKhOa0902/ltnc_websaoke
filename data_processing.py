import pandas as pd

# Đọc file CSV vào DataFrame
df = pd.read_csv('chuyen_khoan.csv')

# Tách cột date_time thành 2 cột: date và time
df[['date', 'ID']] = df['date_time'].str.split('_', expand=True)

# Xóa cột date_time ban đầu nếu không cần nữa
df = df.drop('date_time', axis=1)

# Số tiền ủng hộ/ chi 
df['amount'] = df['credit'] - df['debit']

# Xoá cột số thứ tự, credit và debit
df = df.drop('trans_no', axis=1)
df = df.drop('credit', axis=1)
df = df.drop('debit', axis=1)

# Phân nhóm số tiền
df['segment'] = pd.cut(df['amount'], bins=[-float('inf'), 0, 50000, 100000, 500000, 1000000, 10000000, 100000000, 500000000, 1000000000], labels=['Tien chi', '0-50K', '50K-100K', '100K-500K', '500K-1M', '1M-10M', '10M-100M', '10M-500M', '500M-1B'])

# Thay đổi thứ tự cột
df = df[['date', 'ID', 'amount', 'detail', 'segment']]

# Lưu DataFrame vào file Excel
df.to_excel('processed_data.xlsx', index=False)