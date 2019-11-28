# -*- coding:utf-8 -*-
from selenium import  webdriver
import time
import requests
import json


proxies = {'http': 'http://localhost:8888', 'https':'http://localhost:8888'}
def buycoin():
    url = 'http:/c2c/web/buyCoin'
    headers = {'User-Agent':'Exx_pro/4.3.6 (com.exx.pro; build:4.3.61; iOS 12.4.0) Alamofire/4.7.3','Content-Type':'application/json','Cookie':'wlan=cn; wmname=cny; webDomainName=exx.com; wJSESSIONID=DB44B10C1B4DBF1705DBF6B6F99B8439; wuid=1205; wuname=13537548268; wuon=1; wbbsemail=false; wbbsSynchronization=; bbsenviroment=w; __t=C62799FA6C312915C4531CA0BD383705; __uid=1205; user-info={"image":null,"user_status":1,"create_time":"2019-09-24 15:34:32","isCustomized":0,"enableTime":null,"security_level":0,"authInfo":null,"user_type":"1","phone":"13537548268","nickname":null,"id":269,"email":null,"country_id":236,"region_code":"+86","risk_evaluation":0,"account":"13537548268"}; otc-currentMoney=KRW; otc-currentMoneyId=7'}
    data = {'coinName':'krwt','amount':'100','legalcode':'krw','legal_currency_id':'7'}
    respose  = requests.post(url=url,data=json.dumps(data),headers=headers,proxies=proxies)
    print(respose.json())





if __name__ == '__main__':
    buycoin()
