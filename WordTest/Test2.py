#!  conda env
# -*- coding:utf-8 -*-
# Time:2021/2/22 下午8:02
# Author : nishizzma
# File : Test2.py
'''
获得食材单词，并且去除多余项,已经更新
'''
import numpy as np

# numpy_array = np.load('../WordList/log.npy')

numpy_array1 = np.load('../WordList/Ingredients.npy')
print(len(numpy_array1))


# print(len(numpy_array1))
num = set(numpy_array1)
num = list(num)

print(type(num))
print(len(num))
# numpy_array = np.array(num)
np.save('../WordList/Ingredients.npy', num)
# print(len(num))

# for i in range(len(numpy_array1)):
#     if i >= 200 and i<300:
#         print(numpy_array1[i])
#     if i == 300:
#         break
