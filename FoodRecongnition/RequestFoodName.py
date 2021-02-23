#!  conda env
# -*- coding:utf-8 -*-
# Time:2021/2/23 下午4:01
# Author : nishizzma
# File : RequestFoodName.py

# encoding:utf-8

import requests
import base64

'''
菜品识别
'''

def FoodNameSearch(PicturePath):
    NameList = []

    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v2/dish"
    # 二进制方式打开图片文件
    #PicturePath = './FoodPicture/1.jpg'

    f = open(PicturePath, 'rb')
    img = base64.b64encode(f.read())

    #对照片进行上传，选取最高可能性的5个
    params = {"image":img,"top_num":5}

    #来源于RequestToken获得结果
    access_token = '24.3c5aaba95806d021a107c9176f8f6b0d.2592000.1616659137.282335-23693553'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        #列表
        FoodList = response.json()['result']
        for Food in FoodList:
            #{'probability': '0.61203', 'has_calorie': True, 'calorie': '194', 'name': '烤翅'}
            print(Food['name'])
            NameList.append(Food['name'])

    return NameList

if __name__ == '__main__':
    FoodNameSearch('./FoodPicture/1.jpg')