# -*- coding:utf-8 -*-
import rsa
from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.PublicKey import RSA
import base64
import hashlib
import requests
import time
import threading
import json
from method import handle_pub_key,encrypt,md5,plus,token
import csv
proxies = {'http': 'http://localhost:8888', 'https':'http://localhost:8888'}
appSecret = 'pxxxxxxxxxxCnADwg9qXLf3OIykcc0UG9J8mJVdhotwCBJBNbjHQlZPaOj3dtjjxTwtsWThxpIq7NScTeQuWVRmtb'
appKey = 'xxxxxxxxxxxL1OTL7enygUJCVu3W4I2qyXPkSN13DY0PFDjyWStxIKvl3oVnAkZVUNKO4uO0tP4GHrZ85E8rBxT'
key = 'xxxxxxxxxxxxxxxxxxx89b8aY8wcnvd4UdnO054znkYoRhxUtFXAqVqlE6BuXYJOAMtu+bmCzy0/slncW9i7PezMCBZhl0BaLm4XCLqKTmxaSDSgbdr9wKhe5s5RURGbhSqon3fxmXuniyiMVzLQOMSkYDsOILyyCh18IBw/NbeBe5TbYphZecztM1QIDAQAB'

# #rsa加密
# def handle_pub_key(key):
#     """
#     处理公钥
#     公钥格式pem，处理成以-----BEGIN PUBLIC KEY-----开头，-----END PUBLIC KEY-----结尾的格式
#     :param key:pem格式的公钥，无-----BEGIN PUBLIC KEY-----开头，-----END PUBLIC KEY-----结尾
#     :return:
#     """
#     start = '-----BEGIN PUBLIC KEY-----\n'
#     end = '-----END PUBLIC KEY-----'
#     result = ''
#     # 分割key，每64位长度换一行
#     divide = int(len(key) / 64)
#     divide = divide if (divide > 0) else divide+1
#     line = divide if (len(key) % 64 == 0) else divide+1
#     for i in range(line):
#         result += key[i*64:(i+1)*64] + '\n'
#     result = start + result + end
#     # print(result)
#     return result
#
# def encrypt(key, content):
#     """
#     ras 加密[公钥加密]
#     :param key: 无BEGIN PUBLIC KEY头END PUBLIC KEY尾的pem格式key
#     :param content:待加密内容
#     :return:
#     """
#     pub_key = handle_pub_key(key)
#     pub = RSA.import_key(pub_key)
#     cipher = Cipher_pkcs1_v1_5.new(pub)
#     encrypt_bytes = cipher.encrypt(content.encode(encoding='utf-8'))
#     result = base64.b64encode(encrypt_bytes)
#     result = str(result, encoding='utf-8')
#     # print(result)
#     return result
#
# def md5(dat):
#     m = hashlib.md5()
#     m.update(dat.encode())
#     res = m.hexdigest()
#     print("md5:", res)
#     return res
#
# def plus(**kwargs):
#     s = sorted(kwargs.items(), key=lambda x: x[0])
#     c=[]
#     for i in s:
#         b = str(i[0])+str(i[1])
#         c.append(b)
#     # print(''.join(c))
#     return ''.join(c)




    # print(s)
    # print(''.join(s))
    # b = ""
    # for key,vaule in s.items():
    #     b = b+str(key) + str(vaule)
    # print(b)
    # return b

#APP登录
def login(username):
    content = 'ab123456'
    headers = {'User-Agent':'Exx_pro/4.3.6 (com.exx.pro; build:4.3.61; iOS 12.4.0) Alamofire/4.7.3','Content-Type':'application/x-www-form-urlencoded'}
    uri = 'http://tmaxxxxx/api/m/V2_0/login'
    password = encrypt(key, content)
    data1 = {'appKey':'sDbDoEiBVCfjL1OTL7enygUJCVu3W4I2qyXPkSN13DY0PFDjyWStxIKvl3oVnAkZVUNKO4uO0tP4GHrZ85E8rBxT','countryCode': '+86',
            'dynamicCode': '', 'googleCode': '', 'lang': 1, 'osType': 1, 'password':password,
            'token': '', 'userId': '', 'userName': username}
    # print(plus(**data1))
    # print(appSecret+plus(**data1)+appKey)
    # print(password)
    sig = md5(appSecret+md5(plus(**data1))+appKey).lower()
    # print(sig)
    data = {'appKey':'sDbDoEiBVCfjL1OTL7enygUJCVu3W4I2qyXPkSN13DY0PFDjyWStxIKvl3oVnAkZVUNKO4uO0tP4GHrZ85E8rBxT','countryCode':'+86',
            'dynamicCode':'','googleCode':'','lang':1,'osType':1,'password':password,'sign':sig,
            'token':'','userId':'','userName':username}
    response = requests.post(uri,data=data)
    print(response.json())
    print(response.json()['datas']['token'])
    return response.json()['datas']['token']


#批量存token
# def token():
#     n = -1
#     A = ['13537548267', '13719657675', '13537548268']
#     B = []
#     while n < len(A) - 1:
#         n += 1
#         B.append(login(A[n]).split())
#         print(B)
#         csvFile = open('token.csv', 'w', newline='')
#         writer = csv.writer(csvFile)
#         writer.writerows(B)


# token = login()
# print(token)
def snatchbuy():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
        }
    uri = 'http://tmaiwweew/et/m/snatch/SnatchController/buy'
    data = {"userId": 1133,'buyNum':100.6599887,'snatchId':1}
    response = requests.post(uri, headers=headers, params=data)
    print(response.json())
    # if response.status_code in range(200, 300):
    #     print (u"线程" + str(threadNum) + u"状态码：" + str(response.status_code))

# def run(threadNum,internTime,duration):
#     # 创建数组存放线程
#     threads = []
#     try:
#         # 创建线程
#         for i in range(1, threadNum):
#             # 针对函数创建线程
#             t = threading.Thread(target=snatchbuy(i),args=(i,))
#             # 把创建的线程加入线程组
#             threads.append(t)
#     except Exception as e:
#         print (e)
#     try:
#         # 启动线程
#         for thread in threads:
#             thread.setDaemon(True)
#             thread.start()
#             time.sleep(internTime)
#         # 等待所有线程结束
#         for thread in threads:
#             thread.join(duration)
#     except Exception as e:
#         print (e)










if __name__ == '__main__':

    A = ['13537548267', '13719657675', '13537548268']
    token(login,*A)
    # S = {'a':1,'b':3,'d':6}
    # print(list(S.items()))
    # print(plus(**S))







    # snatchbuy()
    # threadNum = 10
    # startime = time.strftime("%Y%m%d%H%M%S")
    # print(startime)
    # now = time.strftime("%Y%m%d%H%M%S")
    # duratiion = input(u"输入持续运行时间:")
    # while (startime + str(duratiion)) != now:
    #     run(threadNum, 0.01, int(duratiion))
    #     now = time.strftime("%Y%m%d%H%M%S")
    # try:
    #     i = 0
    #     # 开启线程数目
    #     tasks_number = 20
    #     print('测试启动')
    #     time1 = time.process_time()
    #     while i < tasks_number:
    #         t = threading.Thread(target=snatchbuy())
    #         t.start()
    #         i += 1
    #         time2 = time.process_time()
    #         times = time2 - time1
    #         print(times / tasks_number)
    # except Exception as e:
    #     print(e)


















