#  一号店


import requests
import execjs
from retrying import retry


@retry(stop_max_attempt_number=5)
def login(u, p):
    pass
