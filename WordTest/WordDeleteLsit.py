#!  conda env
# -*- coding:utf-8 -*-
# Time:2021/2/22 下午8:13
# Author : nishizzma
# File : WordDeleteLsit.py
'''
可删除词汇
'''

import numpy as np

list = [',',' ','0','1','2','3','4','5','6','7','8','9', '','\n','-','一','两','半','m','量','适','|','l','克'\
        ,'个','条','颗','三','四','包','g','勺','片','，','、']
numpy_array = np.array(list)
np.save('../WordList/DeleteWord.npy', numpy_array)
print("DeleteWord词汇库已经被更新修改！")