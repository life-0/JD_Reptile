""" -*- coding: utf-8 -*-  
 @Author : life-0 
 @File : test_trash.py 
 @Time : 2021/1/7 10:01
 TODO @desc: 
                
"""
import time

from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://www.baidu.com")
browser.get("https://www.taobao.com")

js = 'window.open("https://www.jd.com");'  # 通过执行js，开启一个新的窗口
browser.execute_script(js)
list_window = browser.window_handles
print(list_window)
browser.back()  # 后退
print(browser.current_window_handle)
time.sleep(2)
browser.forward()  # 前进
print(browser.current_window_handle)
time.sleep(2)
browser.close()  # 关闭浏览器

# 连续访问三个页面
