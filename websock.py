# -*- coding:utf-8 -*-

from ws4py.client.threadedclient import WebSocketClient
import json
import requests


# s1 = {'c':3,'b':2,'a':1}
# s = sorted(s1.items(), key=lambda x: x[0])
# print(s)
# # print(s1.keys())
# # print(list(s1.values()))
# # a = []
# # for i in s1.keys():
# #     a.append(s1[i])
# # print(sorted(a))
# # print(sorted(a,reverse=True))\


class DummyClient(WebSocketClient):
    def opened(self):
        self.send("{'eventName': 'chat_msg', 'data': {'messages':'789','room':'6583997720510337024','color':'#148700','sendTimes':1569747391612}}")  # 发送请求数据格式

    def closed(self, code, reason=None):
        print("Closed down", code, reason)

    # 服务器返回消息
    def received_message(self, message):
        print("recv:", message)


# if __name__ == '__main__':
#     try:
#         # 服务器连接地址wss://real.okex.com:10440/websocket/okexapi  (该地址需翻墙，测试可找其他地址)
#         ws = DummyClient('ws:///', protocols=['chat'])
#         ws.connect()
#         ws.send(json.dumps({"eventName":"chat_msg","data":{"messages":"789","room":"6583997720510337024","color":"#148700","sendTimes":1569747391612}}))
#
#         ws.close()
#
#
#
#     except KeyboardInterrupt:
#         ws.close()




