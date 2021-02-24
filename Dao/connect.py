#!  conda env
# -*- coding:utf-8 -*-
# Time:2021/2/16 下午7:04
# Author : nishizzma
# File : connect.py

'''
连接MySQL数据库
'''

import pymysql
import re

def connect():
    '''
    :return:    数据库(db)，游标对象(cursor)
    '''

    db = pymysql.connect(
             host='rm-bp14l6dz98z1rzk95mo.mysql.rds.aliyuncs.com',
             port=3306,
             user='bearbiscuit_root',
             passwd='Xiangyongan05',
             db ='ifood',
             # charset='utf8'
             )

    # 使用cursor()方法创建一个游标对象cursor
    cursor = db.cursor()
    return db,cursor

def close(db):
    '''
    :param db:  待关闭数据库
    '''
    db.close()











