#!  conda env
# -*- coding:utf-8 -*-
# Time:2021/2/24 上午11:40
# Author : nishizzma
# File : config_test.py

import os
import configparser

CONFIG_PATH = '../config.ini'
# try:
#     CONFIG_PATH = os.environ['CONFIG_PATH']
# except Exception:
#     raise ValueError

config = configparser.ConfigParser()
config.read(CONFIG_PATH)

host = config["DATABASE"]["HOST"]
print(host)
