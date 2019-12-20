# -*- coding:utf-8 -*-
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.PublicKey import RSA
import base64
import hashlib
import requests
import csv

proxies = {'http': 'http://localhost:8888', 'https':'http://localhost:8888'}
appSecret = 'xxxxxLf3OIykcc0UG9J8mJVdhotwCBJBNbjHQlZPaOj3dtjjxTwtsWThxpIq7NScTeQuWVRmtb'
appKey = 'xxxxgUJC3W4I2qyXPkSN13DY0PFDjyWStxIKvl3oVnAkZVUNKO4uO0tP4GHrZ85E8rBxT'
key = 'BAQUAA4GNADCBiQKBgQCc0K89b8aY8wcnvd4UdnO054znkYoRhxUtFXAqVqlE6BuXYJOAMtu+bmCzy0/slncW9i7PezMCBZhl0BaLm4XCLqKTmxaSDSgbdr9wKhe5s5RURGbhSqon3fxmXuniyiMVzLQOMSkYDsOILyyCh18IBw/NbeBe5TbYphZecztM1QIDAQAB'

#rsa加密
def handle_pub_key(key):
    """
    处理公钥
    公钥格式pem，处理成以-----BEGIN PUBLIC KEY-----开头，-----END PUBLIC KEY-----结尾的格式
    :param key:pem格式的公钥，无-----BEGIN PUBLIC KEY-----开头，-----END PUBLIC KEY-----结尾
    :return:
    """
    start = '-----BEGIN PUBLIC KEY-----\n'
    end = '-----END PUBLIC KEY-----'
    result = ''
    # 分割key，每64位长度换一行
    divide = int(len(key) / 64)
    divide = divide if (divide > 0) else divide+1
    line = divide if (len(key) % 64 == 0) else divide+1
    for i in range(line):
        result += key[i*64:(i+1)*64] + '\n'
    result = start + result + end
    # print(result)
    return result

def encrypt(key, content):
    """
    ras 加密[公钥加密]
    :param key: 无BEGIN PUBLIC KEY头END PUBLIC KEY尾的pem格式key
    :param content:待加密内容
    :return:
    """
    pub_key = handle_pub_key(key)
    pub = RSA.import_key(pub_key)
    cipher = Cipher_pkcs1_v1_5.new(pub)
    encrypt_bytes = cipher.encrypt(content.encode(encoding='utf-8'))
    result = base64.b64encode(encrypt_bytes)
    result = str(result, encoding='utf-8')
    print(result)
    return result

def md5(dat):
    m = hashlib.md5()
    m.update(dat.encode())
    res = m.hexdigest()
    print("md5:", res)
    return res

#拼接排序参数
def plus(**kwargs):
    s = sorted(kwargs.items(), key=lambda x: x[0])
    print(list(kwargs.items()))
    print(s)
    c=[]
    for i in s:
        b = str(i[0])+str(i[1])
        c.append(b)
    # print(''.join(c))
    print(c)
    return ''.join(c)

#批量存token
def token(f,*args):
    n = -1
    B = []
    while n < len(args) - 1:
        n += 1
        B.append(f(args[n]).split())
        # print(B)
        csvFile = open('token.csv', 'w', newline='')
        writer = csv.writer(csvFile)
        writer.writerows(B)


#
# if __name__ == '__main__':
#     key = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCc0K89b8aY8wcnvd4UdnO054znkYoRhxUtFXAqVqlE6BuXYJOAMtu+bmCzy0/slncW9i7PezMCBZhl0BaLm4XCLqKTmxaSDSgbdr9wKhe5s5RURGbhSqon3fxmXuniyiMVzLQOMSkYDsOILyyCh18IBw/NbeBe5TbYphZecztM1QIDAQAB'
#
#     encrypt(key,'5555')
