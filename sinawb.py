# coding:utf-8


import requests
import execjs
import time
import json


def sinawb_login(u, p):
    with open('sinawb.js', encoding="utf-8") as f:
        js_code = f.read()

    c = execjs.compile(js_code)
    get_su = "getSu('{}')".format(u)
    su = c.eval(get_su)

    s = requests.session()
    url = 'https://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su=MTMzODg0OTU4Nzk%3D&rsakt=mod&checkpin=1&client=ssologin.js(v1.4.19)&_=1583755357277'
    headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Pragma": "no-cache",
            "Referer": "https://weibo.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
        }
    data_time = str(int(time.time())*1000)
    data = {
        "entry": "weibo",
        "callback": "sinaSSOController.preloginCallBack",
        "su": su,
        "rsakt": "mod",
        "checkpin": "1",
        "client": "ssologin.js(v1.4.19)",
        "_": data_time,
    }

    res = s.get(url, headers=headers, params=data, timeout=3)

    # print(res.text)
    url2 = "https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.19)"
    headers2 = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        # "Content-Length": "760",
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "login.sina.com.cn",
        "Origin": "https://weibo.com",
        "Pragma": "no-cache",
        "Referer": "https://weibo.com/",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
    }
    servertime = str(int(time.time()))
    data_from_prelogin = res.text.split('(')[-1].split(')')[0]
    data_from_prelogin_json = json.loads(data_from_prelogin)
    print(data_from_prelogin_json)
    get_sp = "getPwd('{}', '{}', '{}')".format(p, data_from_prelogin_json['servertime'], data_from_prelogin_json['nonce'])
    sp = c.eval(get_sp)
    print(sp)
    data2 = {
        "entry": "weibo",
        "gateway": "1",
        "from": "",
        "savestate": "7",
        "qrcode_flag": "false",
        "useticket": "1",
        "pagerefer": "https://passport.weibo.com/visitor/visitor?entry=miniblog&a=enter&url=https%3A%2F%2Fweibo.com%2F&domain=.weibo.com&sudaref=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dbf01GVcQUCKNpuNPaIJdcN_z-NIHMs_-vrwc3pmjCNu%26wd%3D%26eqid%3De206952b001a738a000000035e6623a5&ua=php-sso_sdk_client-0.6.28&_rand=1583761184.6671",
        "vsnf": "1",
        "su": su,
        "service": "miniblog",
        "servertime": servertime,
        "nonce": data_from_prelogin_json["nonce"],
        "pwencode": "rsa2",
        "rsakv": data_from_prelogin_json["rsakv"],
        "sp": sp,
        "sr": "1920*1080",
        "encoding": "UTF-8",
        "prelt": "56",
        "url": "https://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack",
        "returntype": "META",
    }

    login_res = s.post(url2, headers=headers2, data=data2, timeout=30)
    print(login_res.status_code)
    print(login_res.text)


sinawb_login('18518987852', '4daohaosiquanjia')
