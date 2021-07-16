""" -*- coding: utf-8 -*-  
 @Author : life-0 
 @File : JD.py 
 @Time : 2021/1/7 14:21
 TODO @desc: 2.京东商城多页爬取
                
"""

# 1. 导入web驱动模块

import time
import json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
from selenium.webdriver.common.by import By


# 封装一个函数，用来判断属性值是否存在
def isElementPresent(driver, value):
    """
    用来判断元素标签是否存在，
    :param driver: 标签对象
    :param value: class类名
    :return:
    """
    try:
        driver.find_element_by_class_name(value)
    # 原文是except NoSuchElementException, e:
    except exceptions.NoSuchElementException:
        # 发生了NoSuchElementException异常，说明页面中未找到该元素，返回False
        return False
    else:
        # 没有发生异常，表示在页面中找到了该元素，返回True
        return True


def loadElement(driver, timing, xpath):
    """
    显式加载此元素
        :param driver: 驱动器
        :param timing: 时间 int
        :param xpath: xpath 标签路径
        :return: class or False
        """
    try:
        label = WebDriverWait(driver, timing).until(
            EC.presence_of_element_located((By.XPATH, xpath)))
    except exceptions:
        return False
    return label


# 2. 创建一个浏览器驱动 使用chrome
option = webdriver.ChromeOptions()

option.add_experimental_option('excludeSwitches', ['enable-automation'])
# 设置无头浏览 :无头浏览器主要目的是打开浏览器但用户看不到 下两行
# option.add_argument('--headless')
# option.add_argument('--disable-gpu')

browser = webdriver.Chrome(options=option)
browser.maximize_window()
# 3. 访问京东商城
browser.get("https://www.jd.com")
# 4. 获取到京东商城首页的输入框和搜索按钮
inputFrame = browser.find_element_by_xpath("//input")
inputFrame.send_keys("python")  # 设置输入框的值
submit_button = browser.find_element_by_xpath("//button[@class='button']")
browser.execute_script('arguments[0].click();', submit_button)  # 常用的提交方式

# 5. 因为打开了新的页面, 需要切换到新页面上
windows = browser.window_handles  # 获取所有窗口编号,窗口编号排序按照浏览器窗口从左到右进行排序
time.sleep(1)  # 休眠一下 等待网页数据加载完成
browser.switch_to.window(windows[-1])  # 选择最新的窗口编号

# 6. 获取总页数
page_total = browser.find_element_by_xpath("//span[@class='p-skip']/em/b")
print("共", page_total.text, "页")
# 设置一个暂存的爬取数据   最多可存储 1152921504606846975 个元素
list_info = []
# 设置临时的数据字典
dic_temp = {}
# 7.循环遍历前4页的数据
for count in range(1, 5):
    # 因为这个JD商城页面必须滚轮滚到底端 数据才能加载完成,因此使用显式或隐式等待没用
    # browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # 将进度条一点点下拉到最底部
    # time.sleep(3)
    # 当前线程被挂起1.5秒 (主要是让页面数据加载完成) 显示加载和隐式加载都没用
    # for y in range(3):
    browser.execute_script("window.scrollTo(0,(document.body.scrollHeight)*0.43)")
    time.sleep(1)
    # js = "window.scrollTo(0,(document.body.scrollHeight)*0.76)"
    browser.execute_script("window.scrollTo(0,(document.body.scrollHeight)*0.76)")
    time.sleep(0.5)

    list_modes = browser.find_elements_by_xpath("//div[@id='J_goodsList']/ul/li/div")
    for li in list_modes:
        dic_temp['书名'] = li.find_element_by_class_name('p-name').text
        # print('书名:', dic_temp['书名'])
        dic_temp['链接'] = li.find_element_by_xpath(".//div[@class='p-img']/a").get_attribute('href')
        # print('链接:', dic_temp['链接'])
        price = li.find_element_by_class_name('p-price')  # 获得价格标签对象
        if isElementPresent(price, 'price-plus-1'):  # 判断有无此标签
            dic_temp['价格'] = li.find_element_by_tag_name('strong').text
            plus_price = li.find_element_by_class_name('price-plus-1')  # 获得plus标签
            dic_temp[plus_price.get_attribute('title')] = plus_price.text
            # print('plus价格:', dic_temp[plus_price.get_attribute('title')])
        else:
            dic_temp['价格'] = price.text
        # print('价格:', dic_temp['价格'])
        dic_temp["书店"] = li.find_element_by_class_name('p-shopnum').text
        # print('书店', dic_temp["书店"])
        list_info.append(dic_temp.copy())
        dic_temp.clear()
    print("当前共爬取", len(list_info), "条数据")

    next_page = browser.find_element_by_xpath("//a[@class='pn-next']")  # 进行翻页
    browser.execute_script('arguments[0].click();', next_page)  # 常用的提交方式

# 8.持久化存储
fp = open("./JD.json", "w+", encoding="utf-8")
json.dump(list_info, fp=fp, ensure_ascii=False, indent=1)
print("finish")

# 9. 关闭窗口
# browser.close()  # 关闭当前窗口
browser.quit()  # 退出驱动并关闭所有关联的窗口。
