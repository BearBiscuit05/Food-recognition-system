#!  conda env
# -*- coding:utf-8 -*-
# Time:2021/2/22 下午7:42
# Author : nishizzma
# File : update.py
from Dao.connect import connect,close

def UpdateFood(id,Ingredient,tables_name='food'):
    db, cursor = connect()
    cursor.execute("update %s set FoodName = '%s' WHERE id = %s" % \
                   (tables_name, Ingredient, id))

    # cursor.execute("select * from %s WHERE id= %s" % \
    #                (tables_name, id))
    # data = cursor.fetchall()
    # print(data)
    # close(db)

    print("数据库中id={}更新成功".format(id))