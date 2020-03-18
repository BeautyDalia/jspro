# coding:utf-8

# 37玩

import requests
import execjs
import time


def login_37w(u, p):
    with open('37w.js', encoding='utf-8') as f:
        js_code = f.read()

    c = execjs.compile(js_code)
    getpwd = 'td("{}")'.format(p)
    pwd = c.eval(getpwd)

    url = "https://my.37.com/api/login.php"
    headers = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Pragma": "no-cache",
        "Referer": "https://www.37.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }

    t = str(int(time.time()*1000))
    data = {
        "callback": "jQuery18302538687738033465_1584524505497",
        "action": "login",
        "login_account": u,
        "password": pwd,
        "ajax": "0",
        "remember_me": "1",
        "save_state": "1",
        "ltype": "1",
        "tj_from": "100",
        "s": "1",
        "tj_way": "1",
        "_": t,
    }

    s = requests.session()
    res = s.get(url, headers=headers, timeout=3, params=data)

    print(res.text)


login_37w(13719887897, 111111)