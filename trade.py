# -*- coding:utf-8 -*-
import requests
import csv
import json
from method import handle_pub_key,encrypt,md5,plus,token


proxies = {'http': 'http://localhost:8888', 'https':'http://localhost:8888'}

class User:
    #获取公钥
    def getPublicKey(self):
        url = 'hhttp://192xxxxxxxxxxx/user/user/rsa/getPublicKey'
        data = {}
        response = requests.get(url,params=data)
        print(response.json())
        a = response.json()['data']['code']
        b = response.json()['data']['value']
        S = [a,b]
        return S

    #非登录发送短信
    def sendcode(self):
        url = 'http://192xxxxxxxxxxx/notice/service/msg/sendcode'
        headers = {'Device-Type':'web','Content-Type':'application/json'}
        data ={'contact':'13719657675','shortCode':'+86','type':2}
        response = requests.post(url, headers=headers,data=json.dumps(data))
        print(response.json())

    #登录发送短信
    def SendCodeNormal(self):
        url = 'http://192xxxxxxxxxxx/notice/service/msg/SendCodeNormal'
        headers = {'Device-Type':'app','Content-Type':'application/json'}
        data ={'contact':'13719657675','shortCode':'+86','type':2}
        response = requests.post(url, proxies=proxies, headers=headers,data=json.dumps(data))
        print(response.json())

    #注册
    def register(self):
        self.sendcode()
        url = 'http://192xxxxxxxxxxx/user/user/register'
        headers = {'Device-Type':'app','Content-Type':'application/json'}
        password = 'ab123456'
        l = self.getPublicKey()
        print(l[1])
        word = encrypt(l[1],password)
        print(word)
        data = {'mobile':'13719657675','msgCode':'666666','password':word,'publicCode':l[0],'registerType':1,'shortCode':'+86','username':'rayun118'}
        response = requests.post(url,proxies=proxies,headers=headers,data=json.dumps(data))
        print(response.json())

    #登录
    def login(self):
        self.sendcode()
        url = 'http://192xxxxxxxxxxx/user/user/login'
        headers = {'Device-Type':'web','Content-Type':'application/json'}
        password = 'ab123456'
        l = self.getPublicKey()
        print(l[1])
        word = encrypt(l[1],password)
        print(word)
        data = {'loginType':1,'mobile':'13719657675','mobileCode':'666666','password':word,'publicCode':l[1],'shortCode':'+86','username':'rayun118'}
        response = requests.post(url,headers=headers,data=json.dumps(data))
        print(response.json())
        return response.json()['data']['token']

    #登出
    def logout(self):
        url = 'http://192xxxxxxxxxxx/user/user/logout'
        headers = {'Device-Type':'app','Content-Type':'application/json'}
        data ={}
        response = requests.post(url,headers=headers,data=json.dumps(data))
        print(response.json())

    def checkLogin(self):
        url = 'http://192xxxxxxxxxxx/user/user/checkLogin'
        headers = {'Device-Type': 'app', 'Content-Type': 'application/json','Api-Token':self.login()}
        data ={'userid':'1202'}
        response = requests.post(url, headers=headers, data=json.dumps(data))
        print(response.json())

    def findPwd(self):
        self.sendcode()
        password = 'ab123456'
        l = self.getPublicKey()
        print(l[1])
        word = encrypt(l[1], password)
        url = 'http://192xxxxxxxxxxx/user/user/findPwd'
        headers = {'Content-Type': 'application/json'}
        data ={'findType':1,'mobile':'13719657675','mobileCode':'666666','password':word,'publicCode':l[1],'shortCode':'+86','username':'rayun118'}
        response = requests.post(url, headers=headers, data=json.dumps(data))
        print(response.json())




class Quotation:
    def __init__(self):
        self.url = 'http://192xxxxxxxxxxx'
        self.headers ={'Content-Type':'application/json'}


    def getAssistPrice(self,Splicing):
        url = self.url+'/quotations/quotation/buss/%s'%Splicing
        print(url)
        data ={}
        try:
            response = requests.post(url,headers=self.headers,data=json.dumps(data)).json()
            print(response)
        except Exception as e:
            print(e)








if __name__ == '__main__':
    user = User()
    user.findPwd()
    # user.login()
    # user.checkLogin()
    # user.logout()
    # p = Quotation()
    # s = ['getAssistPrice','getMainCurrencyTapeStatistic','getNotices']
    # try:
    #     for i in s:
    #         p.getAssistPrice(i)
    # except Exception as e:
    #     proxies (e)



