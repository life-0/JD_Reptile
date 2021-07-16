""" -*- coding: utf-8 -*-  
 @Author : life-0 
 @File : MongoDB.py 
 @Time : 2021/1/13 15:33
 TODO @desc: 将数据存储MongoDB中
                
"""
from pymongo import MongoClient
import json
# 8.2 持久化存储: MongoDB
fp = open("./JD.json", "r", encoding="utf-8")
JD_data = json.load(fp)
print(JD_data)
client = MongoClient('mongodb://localhost:27017/')
with client:
    db = client.testdb
    db.JD_data.insert_many(JD_data)

# data = db.cars.find()  # 查询得到数据集合必须要用游标遍历
# for i in data:
#     print(i, type(i))
