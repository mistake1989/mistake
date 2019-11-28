# -*- coding:utf-8 -*-
import requests
import csv
import json
import logging

proxies = {'http': 'http://localhost:8888', 'https':'http://localhost:8888'}
with open('data.csv', 'w',newline='') as f:
    B = [['col1'],['col2']]
    writer = csv.writer(f)
    writer.writerows(B)
    # for row in row_list:
    #     writer.writerow(row)
    # # 或直接调用
    # writer.writerows(row_list)


def login():
    try:
        url = 'http://tmaxxxxx/login/'
        header = {'Cookie': 'csrftoken=ti5QsF0FkYicPf7TFegj0r8JdRHmVyLC10j7ObOFSjFwiLxgkVU2VccGkSvY7ZqN'}
        data = {'username':'leiyunqing','password':'ab159753'}
        response = requests.post(url,headers=header,data=data,proxies=proxies)
        print(response.json())
        print(response.json()['data']['sessionid'])
        return response.json()['data']['sessionid']
    except Exception as e:
        proxies (e)


def add_roles():
    try:
        url = 'http://tmaxxxxx/rbac/user_info/'
        header = {'Cookie':'sessionid=%s'%(login())}
        data = {'user_id':'2'}
        response = requests.post(url,headers=header,data=data,proxies=proxies)
        print(response.text)
    except Exception as e:
        proxies (e)

#启动机器人
def startrobot():
    url = 'http://tmaxxxxx/deal/startrobot/'
    header = {'sessionid': (login())}
    data = {'robot_id':25,'flag':'0'}
    response = requests.post(url,headers=header,data=json.dumps(data),proxies=proxies)
    print(response.json())


# user = {'ray':'123','lei':456,'david':789}

# while True:
#     name = input('请输入您的用户名：')
#     if name in user:
#         break
#     else:
#         print('您输入的用户名不存在，请重新输入')
#         continue
#
# count = 5
# while count:
#     password = input('请输入您的密码：')
#     if user[name] == password:
#         print('进入系统')
#         break
#     elif count!=1:
#         count -= 1
#         print('您输入的密码不正确，还有{}次输入机会'.format(count))
#     else:
#         print('已登出')
#         break

def selectcurrency():
    try:
        url = 'http://tmaxxxxx/deal/selectcurrency/'
        header = {'Cookie': 'sessionid=%s' % (login())}
        data = {'currency':'ETH','currency':'BTC'}
        response = requests.post(url,headers=header,data=data,proxies=proxies)
        print(response.json())
    except Exception as e:
        print(e)

def showconfiginfo():
    try:
        url = 'http://tmaxxxxx/deal/showconfiginfo/'
        header = {'Cookie': 'sessionid=%s' % (login())}
        data = {'robot_id':2}
        response = requests.post(url,headers=header,data=data,proxies=proxies)
        print(response.json())
    except Exception as e:
        print(e)


def createrobot():
    try:
        url = 'http://tmaxxxxx/deal/createrobot/'
        header = {'sessionid': (login())}
        data = {'currency':'LTC','market':'USDT','trading_strategy':'网格交易V1.0','trading_account':'46','current_price':'45.35','orders_frequency':'10000','resistance':'50.68',
                'support_level':'38.63','girding_num':'20','procudere_fee':'0.1%','min_num':'10','max_num':'30','girding_porfit':'3','stop_price':'35.89','warning_price':'36.00'
                ,'warning_account':'13352916854','total_money':'100.00','float_profit':'100.00','realized_profit':'100.00','total_profit':'100.00','annual_yield':'0',
                'protection':'1','status':'0','girding_profit':'20.00','run_status':'0','currency_num':156,'market_num':15}
        response = requests.post(url,headers=header,data=json.dumps(data),proxies=proxies)
        print(response.json())
    except Exception as e:
        print(e)


def update_password():
    try:
        url = 'http://192.168.1.52:8030/rbac/update_password'
        header = {'Cookie': 'sessionid=%s' % (login()),'Content-Type':'multipart/form-data'}
        data = {'old_password':'lee123','password':'lei123'}
        response = requests.post(url,headers=header,data=data,proxies=proxies)
        print(response.text)
    except Exception as e:
        print(e)

def all_menus():
    try:
        url = 'http://tmaxxxxx/rbac/all_menus/'
        header = {'sessionid': (login())}
        data = {}
        response = requests.get(url,headers=header,data=data,proxies=proxies)
        print(response.text)
    except Exception as e:
        print(e)

# def func_callback(func1, args):
#     print("调用函数:")
#     func1(args)
#     print("____________________")
#
#
# def f1(x):
#     print("回调函数启动:", x)


def all_users():
    url = 'http://tmaxxxxx/rbac/all_users/'
    header = {'Cookie': 'sessionid=%s' % (login()),'Content-Type':'application/x-www-form-urlencoded'}
    data = {}
    response = requests.get(url,headers=header,data=data,proxies=proxies)
    print(response.status_code)

def accountlist():
    url = 'http://tmaxxxxx/deal/accountlist/'
    header = {'sessionid': (login()),'Content-Type':'application/x-www-form-urlencoded'}
    data = {'pageIndex':1}
    response = requests.get(url,headers=header,data=data,proxies=proxies)
    print(response.json())




def showassert():
    url = 'http://tmaxxxxx/deal/showassert/'
    header = {'sessionid': (login())}
    data = {'id':54}
    response = requests.post(url,headers=header,data=data,proxies=proxies)
    print(response.json())




if __name__ == '__main__':
    # all_menus()
    # accountlist()
    # createrobot()
    # accountlist()
    # login()
    # add_roles()
    # startrobot()
    # selectcurrency()
    # showconfiginfo()
    # createrobot()
    # all_users()
    # func_callback(f1, 100)
    # update_password()
    # startrobot()
    # createrobot()
    showassert()











