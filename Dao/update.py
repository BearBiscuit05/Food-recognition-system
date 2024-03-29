#!  conda env
# -*- coding:utf-8 -*-
# Time:2021/2/22 下午7:42
# Author : nishizzma
# File : update.py
from Dao.connect import connect,close

"""
更新数据库中所包含数据
"""
def UpdateFood(id,FoodName =None,Url = None,Ingredients=None,\
               Mainpicture=None,Steps=None,StepPicture=None,\
               tables_name='food'):

    db, cursor = connect()
    cursor.execute("select * from %s WHERE id = %s" %(tables_name, id))
    datas = cursor.fetchall()
    for data in datas:
        id = data[0]
        new_FoodName = data[1] if FoodName == None else FoodName
        new_Url = data[2] if Url == None else  Url
        new_Ingredients = data[3] if Ingredients == None else  Ingredients
        new_Mainpicture = data[4] if Mainpicture == None else Mainpicture
        new_Steps = data[5] if Steps == None else  Steps
        new_StepPicture = data[6] if StepPicture == None else  StepPicture

    cursor.execute("update %s set FoodName = '%s',Url = '%s',Ingredients='%s',Mainpicture='%s', Steps='%s',StepPicture='%s' WHERE id = %s" % \
                   (tables_name, new_FoodName, new_Url,new_Ingredients,new_Mainpicture,new_Steps,new_StepPicture,id))

    db.commit()
    close(db)
    print("食物数据库中id={}更新成功".format(id))

def UpdateUserInfmation(UID,Name=None,Passwd=None,Region=None,Flavor=None,History=None):
    db, cursor = connect()
    tables_name = 'User'
    cursor.execute("select * from %s WHERE UID = %s" % (tables_name, UID))
    datas = cursor.fetchall()
    for data in datas:
        UID = data[0]
        new_Name = data[1] if Name == None else Name
        new_Passwd = data[2] if Passwd == None else  Passwd
        new_Region = data[3] if Region == None else  Region
        new_Flavor = data[4] if Flavor == None else Flavor
        new_History = data[5] if History == None else  History

    cursor.execute(
        "update %s set Name = '%s',Passwd = '%s',Region='%s',Flavor='%s', History='%s' WHERE UID = %s" % \
        (tables_name, new_Name, new_Passwd, new_Region, new_Flavor, new_History,  UID))

    db.commit()
    close(db)
    print("用户数据库中UID={}更新成功".format(id))