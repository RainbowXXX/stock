from datetime import datetime
import csv

class MyAPI:
    @staticmethod
    def mana_csv(data):
        with open("./result.csv", 'a', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['股票编号', '日期'])  # 写入标题行
            for row in data:
                print(row)
                csv_writer.writerow(row)

    @staticmethod
    def get_data(data):
        for row in data:
            new_data = row.split(",")
            date = datetime.strptime(new_data[0], '%Y-%m-%d')
            fall = new_data[2]
            res = []
            res.append([date.strftime('%Y-%m-%d'),fall])
            
            # print(res)
            MyAPI.mana_csv(res)
