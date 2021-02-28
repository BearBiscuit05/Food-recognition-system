#!  conda env
# -*- coding:utf-8 -*-
# Time:2021/2/28 下午2:56
# Author : nishizzma
# File : ChangePd.py
"""
修改密码
"""
from Dao.update import UpdateUserInfmation
from Utils.md5Use import get_md5

def ChangePasswd(UID,Passwd):
    Passwd = get_md5(Passwd)
    UpdateUserInfmation(UID,Passwd = Passwd)
