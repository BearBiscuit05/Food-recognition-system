#!  conda env
# -*- coding:utf-8 -*-
# Time:2021/2/22 下午7:48
# Author : nishizzma
# File : Test.py
from  Dao.query import ResearchFood
from Dao.update import UpdateFood


if __name__ == '__main__':
    tables_name = 'food'
    # FoodName = '酸菜'
    # Ingredient = '辣椒'
    # NUM = 4
    # Foodlists = ResearchFood(tables_name, FoodName, NUM, Ingredient)
    # if len(Foodlists) == 0:
    #     print("未在数据库中搜索到结果！")
    #     exit()
    # for foodlist in Foodlists:
    #     print(foodlist[3])
    str = '可乐鸡翅根'
    UpdateFood(49,str)
