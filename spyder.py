import json
import time
import requests;
from api import MyAPI;
from states import globalStates;

class Spyder:
    url = 'https://push2his.eastmoney.com/api/qt/stock/kline/get'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }
    param : dict[str,str] = {
        'cb': 'jQuery35107966420494187909_1710204122023',
        'secid': '',
        'ut': 'fa5fd1943c7b386f172d6893dbfba10b',
        'fields1': 'f1,f2,f3,f4,f5,f6',
        'fields2': 'f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61',
        'klt': '101',
        'fqt': '1',
        'end': '20500101',
        'lmt': '1000000',
        '_': '',
    }

    def RefreshParam(self, secid: str) -> dict[str,str]:
        self.param['secid'] = secid
        self.param['_'] = str(int(time.time()*1000))
        return self.param
    
    def Work(self) -> requests.Response:
        return requests.get(url=self.url, headers=self.headers, params=self.param)

    def GetInfo(self, response: requests.Response, name: str) -> tuple[bool, list[str]]:
        response_text = response.text
        callback_name = self.param['cb']

        if response_text[:len(callback_name)] == callback_name and response_text.endswith(');'):
            response_text = response_text[len(callback_name)+1:]
            response_text = response_text[:-2]
        else:
            raise RuntimeError('Response is not invalid')
        
        try:
            response_json = json.loads(response_text)
            tmp = str(response_json['data']['name']).replace(' ','')
            if tmp[0] != name[0]:
                return False, []
            response_data = response_json['data']['klines']

            ret_data = response_data
        except:
            raise
        
        return True, ret_data

def do_spyder(idx: int, stock_id: str, name: str) -> bool:
    if stock_id in globalStates['processed_list']:
        return True
    
    spyder = Spyder()
    is_failed = stock_id in globalStates['fail_list']
    for prefix in {'0.','1.'}:

        secid = prefix + stock_id
        globalStates['cur_states']['cur_id'] = secid

        try:
            spyder.RefreshParam(secid)
            response = spyder.Work()
            globalStates['cur_states']['cur_respons'] = response.text
            status, data = spyder.GetInfo(response=response, name=name)

            if status:
                MyAPI.get_data(data, idx)
                globalStates['processed_list'].append(stock_id)

                return True
            else:
                continue
        except BaseException as e:
            # print(e)
            continue
    
    if not is_failed:
        globalStates['fail_list'].append(stock_id)
        
    return False