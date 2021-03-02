#!  conda env
# -*- coding:utf-8 -*-
# Time:2021/3/2 下午8:36
# Author : nishizzma
# File : Test3.py
import numpy as np
numpy_array1 = np.load('../WordList/IngredientsNameList.npy')

for word in numpy_array1:
    print(word)