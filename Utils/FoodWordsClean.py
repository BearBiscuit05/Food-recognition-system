#!  conda env
# -*- coding:utf-8 -*-
# Time:2021/2/22 下午7:54
# Author : nishizzma
# File : FoodWordsClean.py
import numpy as np

def CleanIngredient(FoodList):
    FoodList = list(FoodList)
    Ingredient = []
    DeleteWord = np.load('WordList/DeleteWord.npy')
    str = ''
    for i in range(len(FoodList)):
        if FoodList[i] not in DeleteWord:
           str = str + FoodList[i]
        else:
            if len(str) > 1 and len(str) < 6:
                Ingredient.append(str)
            str = ''
    return Ingredient

def CleanData(str):
    str = str.replace('||||||','\n')
    str = str.replace('|||||', '\n')
    str = str.replace('||||', ' ')
    str = str.replace('|||', ',')
    str = str.replace('||', '')
    str = str.replace('|', '')
    str = str[1:]
    return str