# coding:utf-8

import requests
import execjs


def login_kyzg(u, p):
    with open('./kyzg.js', encoding='utf-8') as f:
        js_code = f.read()
    c = execjs.compile(js_code)
    getpwd = "CryptoJS.SHA1('{}').toString()".format(p)
    pwd = c.eval(getpwd)
    url = "https://www.oschina.net/action/user/hash_login?from="
    headers = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Host": "www.oschina.net",
        "Origin": "https://www.oschina.net",
        "Pragma": "no-cache",
        "Referer": "https://www.oschina.net/home/login?goto_page=https%3A%2F%2Fwww.oschina.net%2F",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }

    data = {
        "email": u,
        "pwd": pwd,
        "verifyCode": "",
        "save_login": "1",
        "google_code": "03AGdBq25z5JiJ1znAsIietQSR3aXcR8qtBm-MIJuvCMqIVfYXysGxhKQs6RxHaH0i7AQLSIxwO_2fsgZOpCLxw4tTd2izDOhDKBsnHfIg993dhtuumuBw3DaZRccrDzX6qs2GR-lq00MCFakI42wixgNV6vGyypDSuDT4s6kamQOt8-Hp2SZIMAnzoQaeKneFA5aEaYb6WBu4-5rCCgeWTm08Cb-b8nobmb0Q35rXp9NqWhd50YLc6jnm7F_6_7OeUNjtn5i-EdqwEfZsOdbDWf7Ypjps7bPrMsgEVaXKRmv4c0zjhFMnSfZ4omI7fO0QeoyWivRvn0EMBGiFi83xkANgHncb2NLsxHywjZdOGyRXJd8fKbOKQSc38DWPDgodjBDWlEzHbo6XLdPQu42KJ2Rkvtpo55kAKQ",
    }
    res = requests.post(url, headers=headers, data=data, timeout=3)
    print(res.text)


login_kyzg('111111', '111111')
