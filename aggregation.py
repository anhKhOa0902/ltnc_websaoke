import pandas as pd

# Đếm số giao dịch
def count(df):
    return len(df)

# Tính tổng số tiền của nhiều giao dịch 
def sum(df):
    return df['amount'].sum()

