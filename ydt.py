# coding:utf-8


# 易贷通

import requests
import execjs


def login_ydt(u, p):
    with open('ydt.js', encoding='utf-8') as f:
        js_code = f.read()

    c = execjs.compile(js_code)
    getpwd = 'toMd5("{}")'.format(p)
    pwd = c.eval(getpwd)

    url = "https://app.etongdai.com/login/verifylogin"
    headers = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Host": "app.etongdai.com",
        "Origin": "https://app.etongdai.com",
        "Pragma": "no-cache",
        "Referer": "https://app.etongdai.com/login/index",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }

    data = {
        "loginName": u,
        "password": pwd,
        "check": "on",
        "next": "null",
    }

    s = requests.session()
    res = s.post(url, headers=headers, data=data, timeout=3)

    print(res.text)


login_ydt(13719887897, 111111)
