#!  conda env
# -*- coding:utf-8 -*-
# Time:2021/2/28 上午11:17
# Author : nishizzma
# File : LogOut.py

from Dao.Delete import DeleteUserInformation

def DeleteUser(UID):
    DeleteUserInformation(UID)


if __name__ == '__main__':
    DeleteUser('1')