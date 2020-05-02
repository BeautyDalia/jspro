# 电信欢乐go

# coding:utf-8

import requests
import execjs


def dx_login(u, p):
    with open('./dxhlg.js', encoding='utf-8') as f:
        js_code = f.read()
    c = execjs.compile(js_code)
    getpwd = "aesEncrypt('{}')".format(p)
    pwd = c.eval(getpwd)
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Host": "login.189.cn",
        "Origin": "https://login.189.cn",
        "Pragma": "no-cache",
        "Referer": "https://login.189.cn/web/login",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }
    data = {
        "uName": u,
        "uType": "203",
        "uPwd": pwd,
        "isRandomPwd": "false",
    }
    url = "https://login.189.cn/web/pwd/validate"
    res = requests.post(url, headers=headers, data=data, timeout=3)
    print(res.text)


dx_login('13111311131', '111111')