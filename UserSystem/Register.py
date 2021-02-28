#!  conda env
# -*- coding:utf-8 -*-
# Time:2021/2/27 下午2:54
# Author : nishizzma
# File : Register.py

from Dao.Add import addUserInformation

def addUser(Name, Passwd, Region, Flavor, History):
    addUserInformation(Name, Passwd, Region, Flavor, History)


if __name__ == '__main__':
    Name = 'zhangsan'
    Passwd = '123456'
    Region = 'huanan'
    Flavor = 'suan'
    History = 'meiyou'
    addUser(Name, Passwd, Region, Flavor, History)