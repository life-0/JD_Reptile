""" -*- coding: utf-8 -*-  
 @Author : life-0 
 @File : test_trash_5.py 
 @Time : 2021/1/11 10:39
 TODO @desc: 
                
"""
# -*- coding: utf-8 -*-
import urllib3
from selenium import webdriver
import random
from time import sleep
# import execjs
import requests


# 定义解密函数
def decrypt(key, data, js_string):
    js_handler = execjs.compile(js_string)
    strdata = js_handler.call('decrypt', key, data)
    return strdata


def getcookie():
    option = webdriver.ChromeOptions()
    option.add_argument('--start-maximized')
    drive = webdriver.Chrome(options=option)
    drive.get('http://www.baidu.com')

    login = drive.find_elements_by_css_selector('#u1>a.lb')[0]
    login.click()
    sleep(3)
    namelogin = drive.find_elements_by_css_selector('p.tang-pass-footerBarULogin')[0]
    namelogin.click()
    sleep(3)
    username = ''
    passwd = ''

    sleep(random.randint(0, 2))
    for i in username:
        randomInt = random.random()
        drive.find_element_by_id("TANGRAM__PSP_10__userName").send_keys(i)
        sleep(randomInt)
    sleep(random.randint(0, 2))
    for j in passwd:
        randomInt = random.random()
        drive.find_element_by_id("TANGRAM__PSP_10__password").send_keys(j)
        sleep(randomInt)

    submit = drive.find_element_by_id('TANGRAM__PSP_10__submit')
    submit.click()
    sleep(3)
    drive.find_element_by_id('kw').send_keys('百度指数')
    drive.find_element_by_id('su').click()
    sleep(2)
    drive.switch_to.window(drive.window_handles[-1])  # 新增，用于使用lcbin@163.com账号时获得弹出新窗口的焦点
    drive.find_element_by_xpath("//div//h3[@class='t']//a//em").click()
    sleep(2)
    drive.switch_to.window(drive.window_handles[-1])  # 新增，用于使用lcbin@163.com账号时获得弹出新窗口的焦点
    now_handle = drive.current_window_handle
    cookie = '; '.join(item for item in [item["name"] + "=" + item["value"] for item in drive.get_cookies()])
    print(cookie)
    return cookie


cookie = getcookie()
# 禁用警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

js_string = '''
function decrypt(t, e) {
    for (var n = t.split(""), i = e.split(""), a = {}, r = [], o = 0; o < n.length / 2; o++)
        a[n[o]] = n[n.length / 2 + o];
    for (var s = 0; s < e.length; s++)
        r.push(a[i[s]]);
    return r.join("")
}
'''
headers = {
    "Cookie": cookie,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/75.0.3770.142 Safari/537.36"
}
data_url = 'http://index.baidu.com/api/FeedSearchApi/getFeedIndex?word={}&area=0&days=30'
uniq_id_url = 'http://index.baidu.com/Interface/ptbk?uniqid={}'


class BDIndex(object):

    def __init__(self):
        self.session = self.get_session()

    @staticmethod
    def get_session():
        session = requests.session()
        session.headers = headers
        session.verify = False
        return session

    @staticmethod
    def decrypt(key, data):
        js_handler = execjs.compile(js_string)
        return js_handler.call('decrypt', key, data)

    def get_bd_index(self, key_word):
        response = self.session.get(data_url.format(key_word)).json()
        uniq_id = self.session.get(uniq_id_url.format(response.get("data").get("uniqid"))).json().get("data")
        data_dict = response['data']['index'][0]['data']

        decrypt_data = self.decrypt(uniq_id, data_dict)
        return decrypt_data


if __name__ == '__main__':
    bd = BDIndex()
    data = bd.get_bd_index("肺炎")
    print(data)
