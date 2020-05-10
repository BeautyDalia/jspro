#  爱奇艺

# coding:utf-8

import requests
import execjs


def login(u, p):
    with open('./aqy.js', encoding='utf-8') as f:
        js_code = f.read()
    c = execjs.compile(js_code)
    getpwd = "rsaFun('{}')".format(p)
    pwd = c.eval(getpwd)
    s = requests.session()
    res = s.post()