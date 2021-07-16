""" -*- coding: utf-8 -*-  
 @Author : life-0 
 @File : test_trash_2.py 
 @Time : 2021/1/7 15:02
 TODO @desc: 
                
"""
import time

from selenium import webdriver
from selenium.webdriver import ChromeOptions
option = ChromeOptions()
browser = webdriver.Chrome(options=option)   # 声明一个浏览器对象

option.add_experimental_option('excludeSwitches', ['enable-automation'])
browser.get("https://www.baidu.com")  # 打开Chrome

input = browser.find_element_by_id("kw")  # 通过id定位到input框
input.send_keys("爱奇艺")   # 在输入框内输入python
browser.find_element_by_id("su").click()
time.sleep(3)
browser.find_element_by_xpath('//*[@id="1"]/h3').click()
time.sleep(10)
browser.switch_to_window(browser.window_handles[1])  # 切换到新打开的选项卡定位爱奇艺的搜索框

search = browser.find_element_by_xpath("//input[@class='search-box-input']").send_keys("青春有你")

# browser.close()               # 关闭浏览器