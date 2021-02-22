#!  conda env
# -*- coding:utf-8 -*-
# Time:2021/2/22 下午7:36
# Author : nishizzma
# File : query.py
from connect import connect,close


def ResearchFood(tables_name, FoodName, NUM=3, Ingredient=None):
    """
    id:             唯一标签
    FoodName:       食物名称
    Url:            菜品来源
    Ingredients:    材料需求
    Mainpicture:    步骤对应图片
    Steps:          制作步骤
    StepPicture:    制作步骤对应图片
    """

    lists = []
    db,cursor = connect()

    # 使用execute()方法执行SQL查询
    cursor.execute("select * from %s WHERE FoodName LIKE '%%%s%%' and Ingredients LIKE '%%%s%%' limit %d" % \
                   (tables_name, FoodName, Ingredient, NUM))
    # 使用 fetchone() 方法获取单条数据.
    # data = cursor.fetchone()
    # 选择所有数据
    data = cursor.fetchall()
    for d in data:
        id = d[0]
        FoodName = d[1]
        Url = d[2]
        Ingredients = CleanData(d[3])
        Mainpicture = d[4]
        Steps = d[5]
        StepPicture = d[6]
        list = [id, FoodName, Url, Ingredients, Mainpicture, Steps, StepPicture]
        lists.append(list)

    # 关闭数据库连接
    close(db)
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