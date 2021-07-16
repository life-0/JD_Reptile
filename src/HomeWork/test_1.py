""" -*- coding: utf-8 -*-  
 @Author : life-0 
 @File : test_1.py 
 @Time : 2021/1/4 17:29
 TODO @desc:    爬取ajax请求后的所有数据
                
"""
import requests
import re

if __name__ == '__main__':
    # 1.url请求路径  http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx
    url = "http://www.kfc.com.cn/kfccda/storelist/index.aspx?op=北京"
    # 2.伪装UA
    headers = {
        'Host': 'www.kfc.com.cn',  # application/x-www-form-urlencoded; charset=UTF-8
        # 'content-type': 'multipart/form-data;charset=UTF-8',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66"
    }
    # 3. 参数请求
    data = {
        # 'op': 'keyword',
        # 'cname': '',
        # 'pid': '',
        # 'keyword': '北京',
        'pageIndex': '1',
        'pageSize': '10'
    }
    # 4. 发送请求
    response = requests.post(url=url, data=data, headers=headers)  # 得到数据
    # Content-Type: text/plain
    print(response.content)  # 没办法,模块响应就是-1000
