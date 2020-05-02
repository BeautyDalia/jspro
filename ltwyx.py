# 联通沃邮箱


# coding:utf-8


import requests
import execjs
import uuid


def login(u, p):
    with open('./ltwyx.js', encoding='utf-8') as f:
        js_code = f.read()
    c = execjs.compile(js_code)
    getpwd = "getPwd('{}')".format(p)
    pwd = c.eval(getpwd)
    uid = uuid.uuid4()
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "mail.wo.cn",
        "Origin": "https://mail.wo.cn",
        "Pragma": "no-cache",
        "Referer": "https://mail.wo.cn/login",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
    }

    data = {
        "username": u,
        "password": pwd,
        "verifyCode": "0397",  # 验证码
        "isAutoLogin": "0",
        "domain": "wo.cn",
        "actionType": "submit",
        "ran": uid,  # 随机的uuid
        "ran1": "",
    }
    url = "https://mail.wo.cn/login"
    res = requests.post(url, headers=headers, data=data, timeout=3, verify=False)
    print(res.text)


login('13111131131', '111111')
