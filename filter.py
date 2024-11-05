import pandas as pd

# Lọc nhóm
def segment(df, segment):
    return df[df['segment'] == segment]

# Lọc ngày 
def date(df, start_date, end_date):
    # Kiểm tra tính hợp lệ
    if start_date > end_date:
        print("Lỗi: Ngày bắt đầu lớn hơn ngày kết thúc")
        return None

    # Chuyển định dạng thành date_time
    df['date'] = pd.to_datetime(df['date'], dayfirst=True)

    mask = (df['date'] >= start_date) & (df['date'] <= end_date)
    return df[mask]
