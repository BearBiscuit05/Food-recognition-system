#!  conda env
# -*- coding:utf-8 -*-
# Time:2021/2/22 下午6:19
# Author : nishizzma
# File : getIngredinetList.py

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



def ResearchFood(tables_name,FoodName,NUM=3,Ingredient = None):
    """
    id:             唯一标签
    FoodName:       食物名称
    Url:            菜品来源
    Ingredients:    材料需求
    Mainpicture:    步骤对应图片
    Steps:          制作步骤
    StepPicture:    制作步骤对应图片
    """
    global cursor
    lists = []

    # 使用execute()方法执行SQL查询
    # cursor.execute("select * from %s WHERE FoodName LIKE '%%%s%%' and Ingredients LIKE '%%%s%%' limit %d" % \
    #                (tables_name, FoodName,Ingredient,NUM))

    cursor.execute("select * from %s " % (tables_name, FoodName,Ingredient,NUM))

    # 使用 fetchone() 方法获取单条数据.
    # data = cursor.fetchone()
    #选择所有数据
    data = cursor.fetchall()
    for d in data:
        id = d[0]
        FoodName = d[1]
        Url  = d[2]
        Ingredients = CleanData(d[3])
        Mainpicture = d[4]
        Steps = d[5]
        StepPicture  = d[6]
        list = [id, FoodName, Url, Ingredients, Mainpicture, Steps, StepPicture]
        lists.append(list)

    # 关闭数据库连接
    db.close()
    return lists

#清洗数据标签
def CleanData(str):
    str = str.replace('||||||','\n')
    str = str.replace('|||||', '\n')
    str = str.replace('||||', ' ')
    str = str.replace('|||', ',')
    str = str.replace('||', '')
    str = str.replace('|', '')
    str = str[1:]
    return str

def CleanIngredient(list):
    Ingredient = []
    str = ''
    for i in range(len(list)):
        if list[i] not in  [',',' ','0','1','2','3','4','5','6','7','8','9', '','\n','-','一','两','半','ml','适量']:
           str = str + list[i]
        else:
            if len(str) > 1:
                Ingredient.append(str)
            str = ''
    return Ingredient

if __name__ == '__main__':
    tables_name = 'food'
    FoodName = '酸菜'
    Ingredient = '辣椒'
    NUM = 4
    Foodlists = ResearchFood(tables_name,FoodName,NUM,Ingredient)
    if len(Foodlists) == 0:
        print("未在数据库中搜索到结果！")
        exit()
    for foodlist in Foodlists:
        print(CleanIngredient(list(foodlist[3])))

import numpy as np
numpy_array = np.array([1,2,3])
np.save('WordList/log.npy', numpy_array)

import numpy as np
numpy_array = np.load('WordList/log.npy')