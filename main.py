import os
import pickle
import pandas

from sys import stderr
from spyder import do_spyder;
from states import globalStates;

xlsx_file_path = r'D:\Documents\VsCode\Python\project\spyder\stock\data.xlsx'
with open(file=xlsx_file_path, mode='rb') as xlsx_file:
    data = pandas.read_excel(xlsx_file, dtype={'code':str,'name':str})
    codes = data['code']

dump_file_path = globalStates['dump_file']

if os.path.exists(dump_file_path) and os.path.isfile(dump_file_path):
    with open(dump_file_path, 'rb') as dump_file:
        globalStates = pickle.load(dump_file)

try:
    if __name__ == '__main__':
        for stock_id in codes:
            if(do_spyder(stock_id= stock_id) == False):
                print(f'Fail to work with {stock_id=}',file=stderr)

except:
    with open(dump_file_path, 'wb') as dump_file:
        pickle.dump(globalStates, dump_file)
    
    print('异常退出!',file=stderr)