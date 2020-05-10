#  中华英才网


import requests
import execjs


def zhyc_login(u, p):
    with open('./zhyc.js', encoding='utf-8') as f:
        js_code = f.read()
    c = execjs.compile(js_code)
    getpwd = "getFormValue('{}')".format(p)
    pwd = c.eval(getpwd)
    data = {
        "password": pwd,
        "isremember": "",
        "callback": "window.CL.AsyncModules.successFun",
        "fingerprint": "7F04EFD9521141CFE2F3D7C0A26F66443B123682DF155BDA_010",
        "finger2": "zh-CN|24|1.100000023841858|8|1920_1080|1920_1040|-480|1|1|1|undefined|1|unknown|Win32|unknown|3|true|false|false|false|false|0_false_false|d41d8cd98f00b204e9800998ecf8427e|1f5031da533fbff76940b6b5d700cf0d",
        "token": "kdyQRzsg0aCCLkBJACZzSNK6H0fS2yOB",
        "source": "chinahrzp-pc",
        "path": "https://www.chinahr.com/",
        "username": u,
        "passwordInputEmpty": "",
        "passwordInput": "",
        "validcode": "",
        "vcodekey": "",
        "btnSubmit": "登录中...",
    }
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Cookie": "gid=; blockid=; check_e=AQAB; check_n=twNcEC1rt4lf%2fno5uD7D0VgqJBMKnk4VJnSbHLcVKRw%2fpqzoYit0QXTg07ZeFYWuJPZUN5Kmy2cQvaWRcA6rH6iYQdK9OUTK66UzrbwfqQ9r%2bOYShcbQrxmptxyUSpw23hdayOu0dQBenUvapAgXxuz%2fHSgVl7v8eyeJq6I7wFU%3d; verify_type=SEA; VERIFY_KEY=6B7C9B1FE69EFAA093CB4ACA593BAF6C",
        "Host": "ilogin.kankan.com",
        "Pragma": "no-cache",
        "Referer": "http://www.kankan.com/",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
    }
    url = "https://passport.58.com/login/pc/dologin?"
    res = requests.post(url, headers=headers, data=data, timeout=3)
    print(res.text)


zhyc_login('111', '111111')