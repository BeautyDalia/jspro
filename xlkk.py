# coding:utf-8


import requests
import execjs
from retrying import retry


@retry(stop_max_attempt_number=5)
def get_login_params(u):
    s = requests.session()
    url = "https://ilogin.kankan.com/check/?u={}&v=100".format(u)
    print(url)
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Host": "ilogin.kankan.com",
        "Pragma": "no-cache",
        "Referer": "http://www.kankan.com/",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
    }

    res = s.get(url, headers=headers)
    print(res.status_code)
    return s.cookies.get_dict()


def login(u, p):
    check = get_login_params(u)
    check_e = check['check_e']
    check_n = check['check_n']
    with open('./xlkk.js', encoding='utf-8') as f:
        js_code = f.read()

    c = execjs.compile(js_code)
    getpwd = "getPwd('{}','{}','')".format(u, p)
    pwd = c.eval(getpwd)
    print(pwd)
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "ilogin.kankan.com",
        "Origin": "http://www.kankan.com",
        "Pragma": "no-cache",
        "Referer": "http://www.kankan.com/",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
    }
    data = {
        "p": pwd,
        "u": u,
        "n": check_n,
        "e": check_e,
        "v": "100",
        "verifycode": "!Pfx",
        "login_enable": "0",
        "business_type": "107",
    }
    # res = requests.post()
login('123123123', '111111')