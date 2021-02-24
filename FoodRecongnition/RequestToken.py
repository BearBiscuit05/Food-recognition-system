#!  conda env
# -*- coding:utf-8 -*-
# Time:2021/2/23 下午3:57
# Author : nishizzma
# File : RequestToken.py
"""
获取百度API接口的Token令牌
"""

import requests

# client_id 为官网获取的AK， client_secret 为官网获取的SK
AK = '3TXW7FsmKrgTgEuGac0mn0GL'
SK = 'gSrNb8TS6O3mTLBbvoy1pGimGG9ttGNu'
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id='+AK+'&client_secret='+SK
response = requests.get(host)
if response:
    print(response.json())