# coding:utf-8

import requests
import execjs
import time
import json


class LoginSteam(object):
    def __init__(self, u, p):
        self.u = u
        self.p = p
        self.retry_time = 1

    def get_login_params(self):
        url = "https://store.steampowered.com/login/getrsakey/"
        headers = {
            "Accept": "*/*",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Host": "store.steampowered.com",
            "Origin": "https://store.steampowered.com",
            "Pragma": "no-cache",
            "Referer": "https://store.steampowered.com/login/?redir=&redir_ssl=1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
        }

        data = {
            "donotcache": int(time.time()*1000),
            "username": self.u
        }
        res = requests.post(url, headers=headers, data=data, timeout=3)
        results = res.text
        return results

    def login(self):
        results = self.get_login_params()
        with open('./steam.js', encoding='utf-8') as f:
            js_code = f.read()
        com = execjs.compile(js_code)
        getpwd = "getPwd('{}', '{}')".format(self.p, results)    # 单引号和双引号要注意，js中jsonparse只能转单引号包双引号
        do_getpwd = com.eval(getpwd)
        rsatimestamp = json.loads(results)['timestamp']
        url = 'https://store.steampowered.com/login/dologin/'
        headers = {
            "Accept": "*/*",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Host": "store.steampowered.com",
            "Origin": "https://store.steampowered.com",
            "Pragma": "no-cache",
            "Referer": "https://store.steampowered.com/login/?redir=&redir_ssl=1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
        }

        data = {
            "donotcache": int(time.time()*1000),
            "password": do_getpwd,
            "username": self.u,
            "twofactorcode": "",
            "emailauth": "",
            "loginfriendlyname": "",
            "captchagid": "-1",
            "captcha_text": "",
            "emailsteamid": "",
            "rsatimestamp": rsatimestamp,
            "remember_login": "false",
        }
        res = requests.post(url, headers=headers, data=data, timeout=3)
        print(res.text.encode('utf-8').decode('unicode_escape'))    # unicode转中文
        return res.text


a = LoginSteam('1111112', '111111')
a.login()
