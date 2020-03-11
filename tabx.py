# coding:utf-8

import requests
import execjs
import time


"""
AES 直接用CryptoJS.js 这个库
"""


def login_tabx(u, p):
    with open('tabx.js', encoding='utf-8') as f:
        js_code = f.read()

    c = execjs.compile(js_code)
    transtime = int(time.time()*1000)
    s = {"body": {"loginMethod": "1", "name": u, "password": p}, "head": {"userCode": "null", "channelCode": "101",
                                                                          "transTime": transtime, "transToken": "",
                                                                          "customerId": "null", "transSerialNumber": ""}}
    code = 'Encrypt("{}")'.format(s)
    print(code)
    pwd = c.eval(code)
    print(pwd)

    url = "https://tianaw.95505.cn/tacpc/tiananapp/customer_login/taPcLogin?" \
          "jsonKey=NBLetNAD6tHSqG1kmgP12SFiv6oyyRDdvklJemP%" \
          "2BPaVi5k9LvIGQXwxa8MeGAhG8Y2O40RF%2FaYFELFMZMQD2D%" \
          "2BWxidZ6BMJyoEC2iG5Awrk4vGuxJjJwiOkW6V7O17PImCaw8jZ" \
          "v1lT1Ch6EKCU3b4wOTOxwfTZGWCOZEulNmfwfxMJfnaR9zpsKajM9" \
          "Bf6q3CbebDpo3t%2Ftkzu5xEZX%2FByYukeYkaFo2DgRIFk96eRwhtcjZREoYOi0HaS7vaG0XzHOcASLHVHl6tuIbJ4%2Fyw%3D%3D"

    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Host": "tianaw.95505.cn",
        "Origin": "https://tianaw.95505.cn",
        "Pragma": "no-cache",
        "Referer": "https://tianaw.95505.cn/tacpc/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
    }

    data = {
        "jsonKey": pwd
    }

    s = requests.session()

    res = s.post(url, data=data, headers=headers, timeout=5)

    print(res.text)


login_tabx(13178945612, 123456789)
