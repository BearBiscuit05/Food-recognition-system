#!  conda env
# -*- coding:utf-8 -*-
# Time:2021/2/27 下午3:15
# Author : nishizzma
# File : Add.py

from Dao.connect import connect,close

def addFoodInformation(FoodName, Url, Ingredients, Mainpicture, Steps, StepPicture):
    db, cursor = connect()
    tables_name = 'food'
    sql = ("insert into {} (FoodName, Url, Ingredients, Mainpicture, Steps, StepPicture) "\
           "values(%s,%s,%s,%s,%s,%s)".format(tables_name))


    cursor.execute(sql,(FoodName, Url, Ingredients, Mainpicture, Steps, StepPicture))
    db.commit()
    db.close()
    print("成功加入新菜谱")


def addUserInformation(Name,Passwd,Region,Flavor,History):
    db, cursor = connect()
    tables_name = 'User'
    sql = ("insert into {} (Name,Passwd,Region,Flavor,History) "\
           "values(%s,%s,%s,%s,%s)".format(tables_name))

    cursor.execute(sql,(Name,Passwd,Region,Flavor,History))
    db.commit()
    db.close()
    print("成功加入用户")

