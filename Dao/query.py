#!  conda env
# -*- coding:utf-8 -*-
# Time:2021/2/22 下午7:36
# Author : nishizzma
# File : query.py
'''
对数据库内容进行查询
'''

from Dao.connect import connect,close
def ResearchFood(tables_name='food',id = None,FoodName = None, NUM=3, Ingredients=None):
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

    # 使用execute()方法执行SQL查询,根据传输参数不同，获得不同参数结果
    if FoodName != None and Ingredients != None:
        cursor.execute("select * from %s WHERE FoodName LIKE '%%%s%%' and Ingredients LIKE '%%%s%%' limit %d" % \
                    (tables_name, FoodName, Ingredients, NUM))

    elif id != None:
        cursor.execute("select * from %s WHERE id = '%s'" % \
                       (tables_name, id))
    elif FoodName != None:
        cursor.execute("select * from %s WHERE FoodName LIKE '%%%s%%' limit %d" % \
                       (tables_name, FoodName, NUM))
    elif Ingredients != None:
        cursor.execute("select * from %s WHERE  Ingredients LIKE '%%%s%%' limit %d" % \
                       (tables_name,Ingredients, NUM))
    else:
        print("所提供参数不足以查询数据库！")
        return -1;


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





