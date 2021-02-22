#!  conda env
# -*- coding:utf-8 -*-
# Time:2021/2/20 下午3:20
# Author : nishizzma
# File : PageRank.py
import pandas as pd

filepath = "./Ifood_food.csv"
df_recipes = pd.read_csv(filepath, encoding="utf_8")

# # drop rows where cuisine, ingregients are NA
# df_recipes.dropna(subset=['cuisine', 'ingredients'], inplace=True)
print(df_recipes['Ingredients'])