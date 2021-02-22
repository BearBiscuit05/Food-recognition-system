#!  conda env
# -*- coding:utf-8 -*-
# Time:2021/2/22 下午6:20
# Author : nishizzma
# File : Test.py
import numpy as np
numpy_array = np.array(['int','str','range'])
np.save('log.npy',numpy_array )

numpy_array1 = np.load('log.npy')
print(numpy_array1)