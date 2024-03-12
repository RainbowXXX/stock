from sys import stderr
from spyder import do_spyder;

if __name__ == '__main__':
    stock_id = '000008'
    if(do_spyder(stock_id= stock_id) == False):
        print(f'Fail to work with {stock_id=}',file=stderr)