""" -*- coding: utf-8 -*-  
 @Author : life-0 
 @File : test_1.py 
 @Time : 2021/1/5 14:18
 TODO @desc: 
                
"""
# 导入web驱动模块
from selenium import webdriver

# 创建一个Chrome驱动
driver = webdriver.Chrome()

# 有了实例之后相当于我们有了Chrome浏览器了，接着使用get方法打开百度
driver.get("https://www.baidu.com")

# 打开百度之后，我们获取到输入框
# 获取到输入框之后我们就往里面写入我们要搜索的内容
input = driver.find_element_by_css_selector("#kw")
input.send_keys("照片")

# 输入完了之后呢，我们就获取到搜索这个按钮，然后点击
button = driver.find_element_by_css_selector("#su")
button.click()
# driver.quit()
