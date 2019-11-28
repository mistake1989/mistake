# -*- coding:utf-8 -*-
import random
import requests
import json
import re
import hmac
import hashlib
import time
import hashlib
from APP import handle_pub_key,encrypt
import smtplib
from email.mime.text import MIMEText
from email.header import Header


proxies = {'http': 'http://localhost:8888', 'https':'http://localhost:8888'}


cookies = 'wlan=cn;webDomainName=exx.com;wbbsemail=false;wbbsSynchronization=;bbsenviroment=;user-info={};wExchangeMode=1;wTradeTheme=dark;winputPriceMode=0;wmname=cny;wJSESSIONID=8291B988BD02BF1F7D97D68B90FB12C4'
url = 'http://t/api/web/V1_0/getTargetUserAssetNew'
url2 = 'http://tn/login'
url3 = 'http:9000/darkcore/web/user/UserLogin/login'
url5 = 'http://t:9000/api/web/V1_0/getPubTag'
key = '+bmCzy0/slncW9i7PezMCBZhl0BaLm4XCLqKTmxaSDSgbdr9wKhe5s5RURGbhSqon3fxmXuniyiMVzLQOMSkYDsOILyyCh18IBw/NbeBe5TbYphZecztM1QIDAQAB'


def sha256hex(data):
    sha256 = hashlib.sha256()
    sha256.update(data.encode())
    res = sha256.hexdigest()
    print("sha256加密结果:", res)
    return res

def get_pub():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
        'Content-Type': 'application/json'}
    uri = url5
    # print(uri)
    data = {}
    response = requests.get(uri, headers=headers, params=data)
    print(response.json()['datas']['pubTag'])
    return response.json()['datas']['pubTag']







def login ():
    data = 'ab123456'
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8','Cookie':cookies}
    session = requests.session()
    session.headers = header
    password = encrypt(key,data)
    print(password)
    response = session.get(url2,headers=header)
    data1 = {'userType':1,'userName':13537548267,'password':password,'countryCode':'+86'}
    response1 = session.post(url3,data=data1,proxies=proxies,headers=header)
    print(response1.text)



#GET https://trade.exx.com/api/getBalance?accesskey=your_access_key&nonce=当前时间毫秒数&signature=请求加密签名串

def timestamp():
    timestamp = int(time.time()*1000)
    return timestamp

def sign(key,params):
    signature = hmac.new(bytes(key, 'utf-8'), bytes(params, 'utf-8'), digestmod=hashlib.sha512)
    return signature.hexdigest()



#GET https://trade.exx.com/api/getBalance?accesskey=your_access_key&nonce=当前时间毫秒数&signature=请求加密签名串
def getBalance ():
    key = 'c6b2ee35465dfddf535e8ddaeaaaf4ee8a90894e'
    url = 'http://192xxxxxxxxxxx/api/getBalance'
    t= timestamp()
    params = 'accesskey=3b56369d-8072-461e-91f6-243b6277af01&nonce=%d'%t
    print(params)
    # signature = hmac.new(bytes(key,'utf-8'),bytes(params,'utf-8'),digestmod=hashlib.sha512)
    # print(signature.hexdigest())
    try:
        data = {'accesskey':'3b56369d-8072-461e-91f6-243b6277af01', 'nonce':t, 'signature':sign(key,params)}
        # response = requests.get(url,proxies=proxies,verify=False,params=data)
        response = requests.get(url,params=data)
        print(response.json())
    except requests.exceptions.ConnectionError:
        response.status_code = "Connection refused"

#https://trade.exx.com/api/getOpenOrders 获取多个委托买单或卖单，每次请求返回10条记录

def getOpenOrders():
    key = '5706106ab1761acb276a905102be268f2c09502d'
    url = 'http://192xxxxxxxxxxx/api/getOpenOrders'
    params = 'accesskey=ed63b1a8-7906-4bfb-baec-9e01ff65742d&currency=ltc_usdt&nonce=%d&pageIndex=1&type=buy'%timestamp()
    print(params)
    data = {'accesskey': 'ed63b1a8-7906-4bfb-baec-9e01ff65742d', 'currency':'ltc_usdt','nonce':timestamp(),'pageIndex':1,'type':'buy','signature':sign(key,params)}
    response = requests.get(url,params=data)
    print(response.json())


#获取K线
def klines():
    url = 'http://192.168.4.171:9008/data/v1/klines'
    data = {'market':'ltc_usdt','type':'1day','size':30}
    response = requests.get(url,params=data)
    print(response.json()['datas']['data'])
    count = response.json()['datas']['data']
    a = []
    s = 0
    for i in count:
        a.append(i[3])
    for n in a:
        s+=n
    print(s/len(a))

#下单
def order():
    key = '5706106ab1761acb276a905102be268f2c09502d'
    url = 'http://192xxxxxxxxxxx/api/order'
    time = timestamp()
    params ='accesskey=ed63b1a8-7906-4bfb-baec-9e01ff65742d&amount=5&currency=ltc_usdt&nonce=%d&price=63.15&type=buy'%time
    print(params)
    try:
        data = {'accesskey': 'ed63b1a8-7906-4bfb-baec-9e01ff65742d','amount':'5','currency':'ltc_usdt','nonce':time,'price':'63.15','type':'buy','signature':sign(key,params)}
        # response = requests.get(url,proxies=proxies,verify=False,params=data)
        response = requests.get(url,params=data)
        print(response.json())
    except requests.exceptions.ConnectionError:
        response.status_code = "Connection refused"
    id = response.json()['id']
    return id

def getOrder():
    key = '5706106ab1761acb276a905102be268f2c09502d'
    url = 'http://192xxxxxxxxxxx/api/getOrder'
    params = 'accesskey=ed63b1a8-7906-4bfb-baec-9e01ff65742d&currency=ltc_usdt&id=76129653&nonce=%d'%timestamp()
    print(params)
    data = {'accesskey': 'ed63b1a8-7906-4bfb-baec-9e01ff65742d', 'currency':'ltc_usdt','nonce':timestamp(),'id':order(),'signature':sign(key,params)}
    response = requests.get(url,params=data)
    print(response.json())


#撤单
def cancel():
    id = int(order())
    print(id)
    key = '5706106ab1761acb276a905102be268f2c09502d'
    url = 'http://192xxxxxxxxxxx/api/cancel'
    params = 'accesskey=ed63b1a8-7906-4bfb-baec-9e01ff65742d&currency=ltc_usdt&id=%d&nonce=%d'%(id,timestamp())
    print(params)
    data = {'accesskey': 'ed63b1a8-7906-4bfb-baec-9e01ff65742d', 'currency':'ltc_usdt','id':id,'nonce':timestamp(),'signature':sign(key,params)}
    response = requests.get(url,params=data)
    print(response.json())
















#
#
if __name__ == '__main__':
    # startrobot()
    getBalance()
    # klines()
    # order()
    # login()
    # get_pub()

    # getOpenOrders()
    # cancel()
    # getOrder()
    # cancel()
    # ticker()



