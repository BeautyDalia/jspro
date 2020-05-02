# coding:utf-8

import requests
import execjs


def ayy_login(u, p):
    with open('./ayy.js', encoding='utf-8') as f:
        js_code = f.read()
    c = execjs.compile(js_code)
    getpwd = "getPwd('{}')".format(p)
    pwd = c.eval(getpwd)
    headers = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Host": "www.iappstoday.com",
        "Origin": "http://www.iappstoday.com",
        "Pragma": "no-cache",
        "Referer": "http://www.iappstoday.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }
    data = {
        "username": u,
        "password": pwd,
    }
    url = "http://www.iappstoday.com/ajax/login"
    res = requests.post(url, headers=headers, data=data, timeout=3)
    print(res.text)


ayy_login('13113311331', '111111')
