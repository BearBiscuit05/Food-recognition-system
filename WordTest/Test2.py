#!  conda env
# -*- coding:utf-8 -*-
# Time:2021/2/22 下午8:02
# Author : nishizzma
# File : Test2.py
'''
获得食材单词，并且去除多余项,已经更新
'''
import numpy as np
from  FoodRecongnition.WordRecongnition import FoodNameSearch
# numpy_array = np.load('../WordList/log.npy')

numpy_array1 = np.load('../WordList/Ingredients.npy')
str = ''
dict = {}
for i in range(len(numpy_array1)):
    print("已经进行到{}".format(i))
    if len(str) < 130:
        str = str + numpy_array1[i]
    else:
        words = FoodNameSearch(str)
        for word in words:
            if word not in dict:
                dict[word] = 1
            else:
                dict[word] += 1
        str = ''

NameList = []

for d in dict:
    if dict[d] > 1:
        NameList.append(d)



# print(len(numpy_array1))
# num = set(numpy_array1)
# num = list(num)
#
# print(type(num))
# print(len(num))
# numpy_array = np.array(num)
np.save('../WordList/IngredientsNameList.npy', NameList)
# print(len(num))

# for i in range(len(numpy_array1)):
#     if i >= 200 and i<300:
#         print(numpy_array1[i])
#     if i == 300:
#         break
