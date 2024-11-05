import aggregation
import export
import filter
import data_processing

if __name__ == '__main__': 
    df = data_processing.read_csv('chuyen_khoan.csv')
    df = filter.date(df, '2020-01-01', '2020-12-31')
    df = filter.segment(df, 'Tien chi')
    df = aggregation.sum(df)
    export.save_csv(df, 'chuyen_khoan.csv') 