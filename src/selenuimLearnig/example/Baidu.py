""" -*- coding: utf-8 -*-  
 @Author : life-0 
 @File : Baidu.py 
 @Time : 2021/1/11 9:37
 TODO @desc: 3.爬取百度指数关键词热度
                
"""

import time
import json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
from selenium.webdriver.common.by import By


def loadElement(driver, timing, xpath):
    """
    显式加载此元素
        :param driver: 驱动器
        :param timing: 时间 int
        :param xpath: xpath标签
        :return: class or False
        """
    try:
        label = WebDriverWait(driver, timing).until(
            EC.presence_of_element_located((By.XPATH, xpath)))
    except exceptions:
        return False
    return label


# 1. 创建一个浏览器驱动 使用chrome
option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
browser = webdriver.Chrome(options=option)
browser.maximize_window()
browser.get("http://index.baidu.com/v2/main/index.html#/trend/海贼王?words=海贼王")
browser.implicitly_wait(10)
# # 找到登录输入框,登录按钮
# userName = loadElement(browser, 10, "//input[@name='userName']")
# userName.send_keys(18376809811)
#
# userPassword = loadElement(browser, 10, "//input[@name='password']")
# # userPassword = browser.find_element_by_name("password")
# userPassword.send_keys(input("输入密码: "))
current_url = browser.current_url.copy()
next_url = ''
while current_url != next_url:
    getUserPhoneDom = browser.find_element_by_id('TANGRAM__PSP_4__userName')
    getUserPassDom = browser.find_element_by_id('TANGRAM__PSP_4__password')
    phone = "18376809811"
    password = "838674308220"
    userName = loadElement(browser, 10, "//input[@name='userName']")
    # userName.send_keys(phone)
    userPassword = browser.find_element_by_name("password")
    # userPassword.send_keys(password)
    # 模拟人为方式一点点输入数据
    for i in phone:
        getUserPhoneDom.send_keys(i)
        time.sleep(0.4)
    for j in password:
        getUserPassDom.send_keys(j)
        time.sleep(0.4)
    login = loadElement(browser, 10, "//input[@class='pass-button pass-button-submit']")
    browser.execute_script('arguments[0].click();', login)  # 常用的提交方式

    # 登陆结束后,输入值进行查询
    time.sleep(4)
    search_input = browser.find_element_by_class_name('search-input')
    search_input.send_keys('海贼王')
    button = browser.find_element_by_class_name("search-input-cancle")
    browser.execute_script('arguments[0].click();', button)  # 常用的提交方式
    next_url = browser.current_url

# 滚动滚轮
browser.execute_script("window.scrollTo(0,(document.body.scrollHeight)/2)")  # 将进度条一点点下拉到最底部
time.sleep(1)
# 锁定鼠标的起始点并且移动到指定的位置
action = webdriver.ActionChains(browser)
action.move_by_offset(150, 576).perform()
chart = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div[3]/div[1]/div[3]/div[1]/div[1]/div")
while True:
    action = webdriver.ActionChains(browser)
    action.move_by_offset(20, 0).perform()
    time.sleep(0.3)
    print(chart.text())

# browser.quit()
