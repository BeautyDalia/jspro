#  哔哩哔哩


import requests
import execjs
import json


def get_login_params():
    url = "https://passport.bilibili.com/login?act=getkey&r=0.8823285677377048"
    headers = {
            "authority": "passport.bilibili.com",
            "method": "GET",
            "path": "/login?act=getkey&r=0.8823285677377048",
            "scheme": "https",
            "accept": "*/*",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "no-cache",
            "pragma": "no-cache",
            "referer": "https://passport.bilibili.com/login",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
            "x-requested-with": "XMLHttpRequest",
    }

    res = requests.get(url, headers=headers, timeout=3)
    return res.text


def login(u, p):
    t = get_login_params()
    with open('./blbl.js', encoding='utf-8') as f:
        js_code = f.read()
    c = execjs.compile(js_code)
    getpwd = """encryptPassword('{}','{}')""".format(p, t)
    print(getpwd)
    pwd = c.eval(getpwd)
    print(pwd)


login('123', '111111')