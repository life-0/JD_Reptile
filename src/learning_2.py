""" -*- coding: utf-8 -*-  
 @Author : life-0 
 @File : learning_2.py 
 @Time : 2021/1/4 15:37
 TODO @desc: 
            爬取豆瓣信息
"""
import requests
import json

if __name__ == '__main__':
    # 1.url 请求路径
    url = "https://movie.douban.com/j/new_search_subjects"
    # 2.UA伪装
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66"
    }
    # 3.参数请求
    parameter = {
        'sort': 'S',  # 按照评分排序
        'range': "0, 10",
        'tags': "",
        'start': "40"  # 从数据库中第几部电影开始取数据
    }
    # 3.发送请求    post: 参数是data=  get: 参数是params=
    response = requests.get(url=url, params=parameter, headers=headers)
    data = response.json()  # 得到数据
    # 4.持久化存储
    fp = open("./doubao.json", 'w', encoding="utf-8")
    json.dump(data, fp=fp, ensure_ascii=False, indent=1)
    print("finish")
