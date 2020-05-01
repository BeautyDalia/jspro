# coding=utf-8


# 移动掌上门户

import requests
import execjs
import time


def yd_login(u, p):
    with open('yd.js', encoding='gbk', errors='ignore') as f:
        js_code = f.read()

    c = execjs.compile(js_code)
    getpwd = 'encrypt("{}")'.format(p)
    pwd = c.eval(getpwd)
    print(pwd)
    url = 'https://login.10086.cn/login.htm'
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Host": "login.10086.cn",
        "Pragma": "no-cache",
        "Referer": "https://login.10086.cn/html/login/touch.html?channelID=12022&backUrl=http://wap.10086.cn/bj/index_100_100.html",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }
    timestamp = str(int(time.time()*1000))
    data = {
        "accountType": "01",
        "pwdType": "02",
        "account": u,
        "password": pwd,
        "inputCode": "",
        "backUrl": "http://wap.10086.cn/bj/index_100_100.html",
        "rememberMe": "0",
        "channelID": "12022",
        "loginMode": "03",
        "protocol": "https:",
        "timestamp": timestamp,
    }

    s = requests.session()
    res = s.get(url, headers=headers, params=data, timeout=3)
    print(res.text)


yd_login(13111123432, 9999)
