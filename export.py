import pandas as pd

# Xuất JSON
def save_json(df, filename):
    df.to_json(filename, orient='records', lines=True)

# Xuất CSV
def save_csv(df, filename):
    df.to_csv(filename, index=False, encoding='utf-8')