# coding:utf-8

import requests
import execjs


def login_xl(u, p):
    with open('xl.js', encoding='utf-8') as f:
        js_code = f.read()

    c = execjs.compile(js_code)
    code = "RSA('{}', '{}', '{}')".format('', '', p)
    pwd = c.eval(code)
    print(pwd)

    url = "http://j.esf.leju.com/ucenter/login?curcity=bj"
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Length": "338",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Host": "j.esf.leju.com",
        "Origin": "http://j.esf.leju.com",
        "Pragma": "no-cache",
        "Referer": "http://j.esf.leju.com/ucenter/login?curcity=bj",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }

    data = {
        "password": pwd,
        "username": u,
        "ckey": "4af1cd577f4630edaa53dc6182526f236819cad3",
        "imgcode": "",
    }

    s = requests.session()

    res = s.post(url, data=data, headers=headers, timeout=5)

    print(res.text)


login_xl(13711111111, 111111)