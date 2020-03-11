# coding:utf-8

import execjs
import requests

"""
e = execjs.eval('a = new Array(1,2,3)')  # 获取js环境，直接执行js代码，适用于较简单的运算
c = execjs.compile('''                   # 用于复杂代码
    function add(x,y){
        return x+y;
    };
''')

print(e)
print(c)
print(c.call("add", "1", "2"))

房天下
"""


def login_ftx(u, p):
    with open('ftx.js', encoding='utf-8') as f:
        js_code = f.read()

    c = execjs.compile(js_code)
    code = "getPwd('{}')".format(p)
    pwd = c.eval(code)
    print(pwd)

    url = "https://passport.fang.com/login.api"
    headers = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Length": "316",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Host": "passport.fang.com",
        "Origin": "https://passport.fang.com",
        "Pragma": "no-cache",
        "Referer": "https://passport.fang.com/?backurl=https%3A%2F%2Fwww.fang.com%2F",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }

    data = {
        "uid": u,
        "pwd": pwd,
        "Service": "soufun-passport-web",
        "AutoLogin": "1",
    }

    s = requests.session()

    res = s.post(url, data=data, headers=headers, timeout=5)

    print(res.text)


login_ftx(13711111111, 111111)
