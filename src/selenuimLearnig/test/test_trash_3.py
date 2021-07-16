""" -*- coding: utf-8 -*-  
 @Author : life-0 
 @File : test_trash_3.py
 @Time : 2021/1/7 22:03
 TODO @desc: 
                
"""
import time
import re
import json
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def loadElement(driver, timing, xpath):
    """
    显式加载此元素
        :param driver: 驱动器
        :param timing: 时间 int
        :param xpath: xpath标签
        :return:
        """
    try:

        label = WebDriverWait(driver, timing).until(
            EC.presence_of_element_located((By.XPATH, xpath)))
    except NoSuchElementException as e:
        return False
    return label


# 2. 创建一个浏览器驱动 使用chrome
option = webdriver.ChromeOptions()  #
option.add_experimental_option('excludeSwitches', ['enable-automation'])
browser = webdriver.Chrome(options=option)
# browser.maximize_window()   # 是窗口最大化
# 3. 访问京东商城
browser.get("https://www.jd.com")
# 4. 获取到京东商城首页的输入框和搜索按钮
inputFrame = browser.find_element_by_xpath("//input")
inputFrame.send_keys("java")  # 设置输入框的值
submit_button = browser.find_element_by_xpath("//button[@class='button']")
browser.execute_script('arguments[0].click();', submit_button)  # 常用的提交方法

for i in range(1, 5):
    # 因为这个JD商城页面必须滚轮滚到底端 数据才能加载完成,因此使用显式或隐式等待没用
    for y in range(3):
        js = 'window.scrollBy(0,330)'
        browser.execute_script(js)
        time.sleep(0.5)
    # browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # 将进度条下拉到最底部
    # time.sleep(1.5)  # 当前线程被挂起1.5秒 (主要是让数据加载完成) 显示加载和隐式加载都没用
    # loadElement(browser, 10, "//div[@id='footer-2017']")
    # current_page = loadElement(browser, 10, "//span[@class='p-num']//a[@class='curr']")

    current_page = browser.find_element_by_xpath("//span[@class='p-num']//a[@class='curr']")
    print("页号:", current_page.text)

    next_page = browser.find_element_by_xpath("//a[@class='pn-next']")
    browser.execute_script('arguments[0].click();', next_page)  # 常用的提交方式
    # next_button = loadElement(browser, 10, "//a[@class='pn-next']")
    # browser.execute_script('arguments[0].click();', next_button)  # 常用的提交方式
    # next_button.click()

browser.quit()  # 退出驱动并关闭所有关联的窗口。
