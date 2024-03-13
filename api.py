from datetime import datetime, timedelta
import csv
import os
import pandas as pd

class MyAPI:

    @staticmethod
    def generate_dates(start_date, end_date):

        current_date = start_date
        while current_date <= end_date:
            yield current_date
            current_date += timedelta(days=1)

    @staticmethod
    def is_csv_empty(file_path):
        return os.path.exists(file_path) and os.path.getsize(file_path) == 0
    
    @staticmethod
    def mana_csv(data):
        start_date = datetime(2019, 1, 1)
        end_date = datetime(2019, 12, 31)
        dates = list(MyAPI.generate_dates(start_date, end_date))
        with open("./result.csv", 'a', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            if MyAPI.is_csv_empty('./result.csv'):
                csv_writer.writerow(['code'] + ['name'] + [date.strftime('%Y-%m-%d') for date in dates])
            for row in data:
                csv_writer.writerow([''] * 2 + row.split(',')[:2])

    @staticmethod
    def get_data(data):
        # excel_file = MyAPI.read_excel()
        res = []
        for row in data:
            new_data = row.split(",")
            fall = new_data[2]
            res.append(fall)
        MyAPI.mana_csv(res)

    @staticmethod
    def read_excel():
        tem = []
        df = pd.read_excel('data.xlsx',dtype=str)
        code = df['code']['name']
        print(code)
        # name = df['name']
        # tem.append(code)
        # tem.append(name)
        return tem
        



if __name__ == "__main__":
    MyAPI.get_data(["1992-05-07,0.80,0.82,0.82,0.80,1590,3283350.00,5.71,134.29,0.47,1.40", "1993-02-24,1.00,0.98,1.05,0.97,8635,21457976.00,8.00,-2.00,-0.02,7.58"])
    # MyAPI.read_excel()