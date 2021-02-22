#!  conda env
# -*- coding:utf-8 -*-
# Time:2021/2/20 下午3:20
# Author : nishizzma
# File : PageRank.py
import pandas as pd
import numpy as np
from Utils.FoodWordsClean import CleanIngredient

filepath = "WordList/IFood_Food.csv"

df_recipes = pd.read_csv(filepath, encoding="utf_8")

Ingredients = []
for i in range(len(df_recipes['Ingredients'])):
    Ingredients = Ingredients + CleanIngredient(df_recipes['Ingredients'][i])
    if i == 10:
        break

set(Ingredients)
numpy_array = np.array(Ingredients)
np.save('WordList/Ingredients.npy', numpy_array)
print(numpy_array)
print("success!")