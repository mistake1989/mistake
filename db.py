# -*- coding:utf-8 -*-
import pymysql

def mysql():
    try:
        conn = pymysql.connect(host = '',user='',port=3306,password='',database='t',charset='utf8')
        return conn
    except Exception as e:
        print(e)


def select(sql):
    db = mysql()
    cur = db.cursor()
    cur.execute(sql)
    results = cur.fetchall()
    print(results)
    return results





if __name__ == '__main__':
    sql='SELECT * FROM exx_main_new.pay_user LIMIT 10'
    select(sql)














