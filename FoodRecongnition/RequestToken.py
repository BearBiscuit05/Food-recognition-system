#!  conda env
# -*- coding:utf-8 -*-
# Time:2021/2/23 下午3:57
# Author : nishizzma
# File : RequestToken.py
"""
获取百度API接口的Token令牌
"""

import requests
import configparser

# client_id 为官网获取的AK， client_secret 为官网获取的SK
CONFIG_PATH = '../config.ini'
config = configparser.ConfigParser()
config.read(CONFIG_PATH)
AK = config["Word_API"]["AK"]
SK = config["Word_API"]["SK"]
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id='+AK+'&client_secret='+SK
response = requests.get(host)
if response:
    print(response.json())