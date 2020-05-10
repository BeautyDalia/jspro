#   39健康


import requests
import execjs
import time
from retrying import retry


@retry(stop_max_attempt_number=5)
def login(u, p):
    with open('./39jk.js', encoding='utf-8') as f:
        js_code = f.read()
    c = execjs.compile(js_code)
    getpwd = "f0('{}')".format(p)
    getuser = "f0('{}')".format(u)
    pwd = c.eval(getpwd)
    user = c.eval(getuser)
    url = "https://my.39.net/post.ashx"
    headers = {
        "authority": "my.39.net",
        "method": "GET",
        # "path": "/post.ashx?callback=jQuery17202819085444361529_1588827999781&action=jsonploginf0&uname=454b4b020847494b020a45&pwd=45494b020845&safecode=&app=29&_=1588828009403",
        "scheme": "https",
        "accept": "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "referer": "https://my.39.net/passport/Login.aspx?usertype=1&regauto=1&backurl=http://www.39.net/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
        "x-requested-with": "XMLHttpRequest",
    }
    t = int(time.time()*1000)
    data = {
        "callback": "jQuery17202819085444361529_{}".format(t),
        "action": "jsonploginf0",
        "uname": user,
        "pwd": pwd,
        "safecode": "",
        "app": "29",
        "_": t,
    }
    s = requests.session()
    res = s.get(url, headers=headers, params=data, timeout=3)
    print(res.text)


login('13113111311', '111111')
