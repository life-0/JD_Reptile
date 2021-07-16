""" -*- coding: utf-8 -*-  
 @Author : life-0 
 @File : BliBli.py 
 @Time : 2021/1/6 14:47
 TODO @desc: 1. 爬取B站关于python爬虫视频的相关数据 单页爬取
            参看文档: https://www.cnblogs.com/songzhixue/p/11270593.html
                
"""

# 1. 导入web驱动模块
from selenium import webdriver
import time
import re
import json

# 2. 创建一个浏览器驱动 使用chrome
browser = webdriver.Chrome()
# 3. 访问B站
browser.get("https://www.bilibili.com/")
# 4. 获取到b站首页的输入框和搜索按钮
inputFrame = browser.find_element_by_class_name("nav-search-keyword")
inputFrame.send_keys("python爬虫")  # 设置输入框的值
submit_button = browser.find_element_by_class_name("nav-search-submit")
# submit_button.click()  # 一般不推荐使用此点击方式
browser.execute_script('arguments[0].click();', submit_button)  # 常用得方式

# 5. 因为打开了新的页面, 需要切换到新页面上
windows = browser.window_handles  # 获取所有窗口编号,窗口编号排序按照浏览器窗口从左到右进行排序
# time.sleep(1) # 休眠一下
browser.switch_to.window(windows[-1])  # 选择最新的窗口编号

# 6. 爬取ul上的所有子标签li上的数据
# browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # 将进度条下拉到最底部
ul_video = browser.find_element_by_class_name('video-list')
li_module = ul_video.find_elements_by_tag_name('li')
print(len(li_module))  # 查看有多少个li标签
list_info = []  # 将每个视频的所有信息收集并且作为一个字典存储在列表中
dict_temp = {}  # 临时存储视频数据
for i in li_module:
    # print("视频标题:", i.find_element_by_class_name('title').get_attribute('title'))
    dict_temp['视频标题'] = i.find_element_by_class_name('title').get_attribute('title')
    dict_temp['网址连接'] = i.find_element_by_class_name('img-anchor').get_attribute('href')
    # print("视频时长:", i.find_element_by_class_name('img').find_element_by_class_name('so-imgTag_rb').text)
    dict_temp['视频时长'] = i.find_element_by_class_name('img').find_element_by_class_name('so-imgTag_rb').text
    tags = i.find_element_by_class_name('tags').find_elements_by_tag_name('span')
    for j in tags:
        if j.text == "":
            # 弹幕数量不显示,需要正则一下 re.findall(r,str)返回列表数据 选择索引值为0的元素
            # print(j.get_attribute("title"), re.findall(r'\d+', str(j.get_attribute("innerText")))[0])
            dict_temp[str(j.get_attribute("title"))] = re.findall(r'\d+', str(j.get_attribute("innerText")))[0]
        else:
            # print(j.get_attribute("title"), j.text)
            dict_temp[str(j.get_attribute("title"))] = j.text
    # 存入到列表中 因为字典和列表是可以修改(内存存储值)的,因此需要深拷贝,再放入列表中 dict_temp.copy()
    list_info.append(dict_temp.copy())
    # print(dict_temp)

# 7.持久化存储
fp = open("blibli.json", "w+", encoding="utf-8")
json.dump(list_info, fp=fp, ensure_ascii=False, indent=1)
print("finish")

# 8. 关闭窗口
# browser.close()  # 关闭当前窗口
browser.quit()  # 退出驱动并关闭所有关联的窗口。
