from datetime import datetime, timedelta
import os
import pandas as pd

class MyAPI:


    @staticmethod
    def is_csv_empty(file_path: str) -> bool:
        return os.path.exists(file_path) and os.path.getsize(file_path) == 0
    

    @staticmethod
    def mana_csv(data: list) -> any:
        # data.append("0.82")
        l_name = MyAPI.read_excel('./data.xlsx')
        dates = pd.date_range(start='2019-01-01', end='2019-12-31')
        df = pd.DataFrame(columns=['code', 'name'] + [date.strftime('%Y-%m-%d') for date in dates])


        df[['code', 'name']] = pd.DataFrame(l_name)
        
        tem = data[0]

        for i, row in enumerate(data):
            df.iloc[0, i+2] = row


        df = df.astype(str)
        df.replace('nan', '', inplace=True)

        tem = data[0]
        if tem in df.iloc[0:, 1].values:
            cur_time = df.columns[df.iloc[1:, 2] == tem].tolist()
            print(cur_time)

        df.to_csv("./result.csv", mode='a',encoding="gbk", index=False, header=not os.path.exists("./result.csv"))

    @staticmethod
    def get_data(data: list[str], index: int) -> any:
        res = []
        start_date = datetime.strptime('2019-1-1', '%Y-%m-%d')
        end_date = datetime.strptime('2019-12-31', '%Y-%m-%d')
        for row in data:
            new_data = row.split(",")
            cur_time = new_data[0]
            cur_time = datetime.strptime(cur_time, '%Y-%m-%d')
            if start_date <= cur_time <= end_date:
            # cur_time = 
                fall = new_data[2]
                res.append(fall)
        MyAPI.mana_csv(res)

    @staticmethod
    def read_excel(file_name: str) -> list:
        df = pd.read_excel(file_name, dtype=str, index_col=False)
        tem = df.iloc[:, :2].values.tolist()
        return tem
        



if __name__ == "__main__":
    MyAPI.get_data(["1992-05-07,0.80,0.82,0.82,0.80,1590,3283350.00,5.71,134.29,0.47,1.40", "1993-02-24,1.00,0.98,1.05,0.97,8635,21457976.00,8.00,-2.00,-0.02,7.58"])
    # MyAPI.read_excel('./data.xlsx')