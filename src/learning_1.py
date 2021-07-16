""" -*- coding: utf-8 -*-  
 @Author : life-0 
 @File : learning_1.py 
 @Time : 2020/12/31 9:27
 TODO @desc: requests 四步走
                指定URL
                发送请求
                获取响应数据
                持久化存储
            实战学习一: 破解百度翻译
"""
import requests
import json

if __name__ == '__main__':
    # 1.指定url
    post_url = "https://fanyi.baidu.com/sug"
    # 2. 模拟UA伪装
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66"
    }
    # 3.post请求参数处理(同get请求一致)
    word = input("paramater:")
    data = {
        'kw': word
    }
    # 4.发送请求
    response = requests.post(url=post_url, data=data, headers=headers)
    # 5.获取响应数据:json()方法返回的是obj(如果确认响应数据的json类型的,才可以使用json())
    #   查看: content-type: application/json (看这个)
    dic_obj = response.json()

    # 6.持久化存储
    fp = open("./data.json", "a+", encoding="utf-8")
    json.dump(dic_obj, fp=fp, ensure_ascii=False, indent=1)
    print("finish")