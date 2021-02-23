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
    print("数据库中id={}更新成功".format(id))