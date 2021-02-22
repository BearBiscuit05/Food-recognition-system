#!  conda env
# -*- coding:utf-8 -*-
# Time:2021/2/22 下午7:42
# Author : nishizzma
# File : update.py
from Dao.connect import connect,close

def UpdateFood(tables_name,Ingredient,id):
    db, cursor = connect()
    cursor.execute("update * from %s set Ingredient = %s WHERE id = %d" % \
                   (tables_name,  Ingredient, id))
    close(db)