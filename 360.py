# coding:utf-8


import requests
import execjs
import time
import re


def get_login_params(u, p):
    url = "https://login.360.cn/"
    ts = int(time.time()*1000)
    func = "jQuery112406530374436532924_{}".format(ts)
    data = {
        "func": func,
        "src": "pcw_home",
        "from": "pcw_home",
        "charset": "UTF-8",
        "requestScema": "https",
        "quc_sdk_version": "6.8.4",
        "quc_sdk_name": "jssdk",
        "o": "sso",
        "m": "getToken",
        "userName": u,
        "_": ts,
    }
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "login.360.cn",
        "Origin": "https://i.360.cn",
        "Pragma": "no-cache",
        "Referer": "https://i.360.cn/login/?src=pcw_home&destUrl=https://www.360.cn/",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
    }
    res = requests.get(url, headers=headers, params=data, timeout=3)
    token = re.findall('token\":\"(.*)\"}', res.text)[0]
    return token


def login(u, p):
    token = get_login_params(u, p)
    with open('./360.js', encoding='utf-8') as f:
        js_code = f.read()
    c = execjs.compile(js_code)
    getpwd = "md5('{}','')".format(p)
    pwd = c.eval(getpwd)
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "login.360.cn",
        "Origin": "https://i.360.cn",
        "Pragma": "no-cache",
        "Referer": "https://i.360.cn/login/?src=pcw_home&destUrl=https://www.360.cn/",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
    }
    data = {
        "src": "pcw_home",
        "from": "pcw_home",
        "charset": "UTF-8",
        "requestScema": "https",
        "quc_sdk_version": "6.8.4",
        "quc_sdk_name": "jssdk",
        "o": "sso",
        "m": "login",
        "lm": "0",
        "captFlag": "1",
        "rtype": "data",
        "validatelm": "0",
        "isKeepAlive": "1",
        "captchaApp": "i360",
        "userName": u,
        "smDeviceId": "",
        "type": "normal",
        "account": u,
        "password": pwd,
        "captcha": "",
        "token": token,
        "proxy": "https://i.360.cn/psp_jump.html",
        "callback": "QiUserJsonp384509904",
        "func": "QiUserJsonp384509904",
    }
    url = "https://login.360.cn/"
    res = requests.post(url, headers=headers, data=data, timeout=3)
    print(res.text)


login('131113131313', '111111')
