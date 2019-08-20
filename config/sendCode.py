#!/usr/bin/python

import requests
import datetime


def sendCode():
    today = datetime.date.today()
    formatted_today = today.strftime('%Y%m%d')

    # print(formatted_today)
    # 激活万能验证码
    url = "https:xxx=xxxx&key="+formatted_today+"xxx"

    # print(url)
    r = requests.get(url)
    print(r.status_code)
    # print(r.content)