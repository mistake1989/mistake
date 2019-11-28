# -*- coding:utf-8 -*-
import requests
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def ticker():
    url = 'https://api.exxvip.com/data/v1/ticker'
    data = {'currency':'noa_krwt'}
    response = requests.get(url,params=data)
    # print(response.json())
    print(response.json()['ticker']['last'])
    return response.json()['ticker']['last']


def stmp():
    # 第三方 SMTP 服务
    mail_host = "smtp.qq.com"  # 设置服务器
    mail_user = "412476173@qq.com"  # 用户名
    mail_pass = "dbhi"  # 口令

    sender = '412476173@qq.com'
    receivers = ['rayunqing@163.com','linz.com','46.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    message = MIMEText('eth当前价格已浮动10%，请注意风险', 'plain', 'utf-8')
    message['From'] = Header("行情监控", 'utf-8')
    message['To'] = Header("量化行情监控", 'utf-8')

    subject = '量化行情监控'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print('邮件发送成功')
    except Exception as e:
        print(e)



#监控
def Monitor():
    while True:
        time.sleep(5)
        price = float(ticker())
        time.sleep(10)
        price1 = float(ticker())
        if (price1 - price)/price>= 0.1:
            stmp()
            print('当前价格涨幅达到10%，请注意风险')
        elif(price1 - price)/price <= -0.1:
            stmp()
            print('当前价格跌幅达到10%，请注意风险')
        else:
            print('正常运行')




if __name__ == '__main__':
    Monitor()
