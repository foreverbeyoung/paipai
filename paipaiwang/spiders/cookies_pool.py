# -*- coding:utf-8 -*-
import json

from selenium.webdriver.chrome.options import Options
from scrapy import signals
import random

from redis import StrictRedis,ConnectionPool
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 配置终端运行
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import logging
import threading
import random
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
# from Utils.get_proxy import get_proxies
from paipaiwang.Utils.connect_redis import RedisClient
from paipaiwang.Utils.config import HOST_REDIS, PORT_REDIS, DB_REDIS_COOKIES, PASSWORD_REDIS
import time
from paipaiwang.Utils.mk_log import Logger



# def get_proxy():
#     while True:
#         proxy = get_proxies()
#         if ':' in proxy:
#             return proxy
#         else:
#             print('获取代理出错')
#             print(proxy)
#             time.sleep(0.2)





redis_client = RedisClient(host=HOST_REDIS, port=PORT_REDIS, db=DB_REDIS_COOKIES, password=PASSWORD_REDIS)


class GetCookies(object):

    def __init__(self):
        # {"phone": 15623826751, "password": "123456789"},
        self.account_list = [
                             {"phone": 18236283353, "password": "18236283353lnr"},
                             {"phone": 17683905943, "password": "123456789"} ]
        self.redis_client = redis_client
        # self.logger =Logger("./../Logs/cookies_pool.log")
        # driver = webdriver.Chrome()
        # super(GetCookies, self).__init__()



    def get_cookies_from_chrome(self,phone,password):
        phone =phone
        password = password
        seleniumCookies =''
        # driver =webdriver.Chrome()
        # opt = webdriver.ChromeOptions()
        # opt.add_argument('--headless')
        # # proxy = proxy
        # # opt.add_argument('--proxy-server={}'.format(proxy))
        # driver = webdriver.Chrome(options=opt)


        chrome_options = Options()
        # # # chrome_options.add_argument('--headless')

        chrome_options.add_argument('--proxy-server={}'.format('http://116.17.236.248:32898'))
        driver = webdriver.Chrome(chrome_options=chrome_options)
        # driver = webdriver.Chrome()
        try:

            driver.get("https://dc.simuwang.com/")
            # driver.get("https://baidu.com/")
            # time.sleep(10)
            usernameInput =  WebDriverWait(driver,120).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="登录注册首页-输入手机/用户名"]'))
            )
            time.sleep(2)
            usernameInput.clear()
            usernameInput.send_keys(phone)  # 输入用户名
            driver.find_element_by_xpath('//*[@id="登录注册首页-下一步"]').click()
            time.sleep(3)


            passWordElem =  WebDriverWait(driver,30).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="密码登录-输入密码2"]'))
            )


            # passWordElem = driver.find_element_by_xpath("//div[@id='messagelogin']//input[@name='password']")
            time.sleep(2)
            passWordElem.clear()
            passWordElem.send_keys(password)  # 输入密码

        # captchaElem = driver.find_element_by_xpath('//*[@id="密码登录-确认2"]')
            time.sleep(2)
        # captchaElem.clear()

        # 点击登录按钮
            loginButtonElem = driver.find_element_by_xpath('//*[@id="密码登录-确认2"]')
            time.sleep(2)
            loginButtonElem.click()
            time.sleep(1)
            seleniumCookies = driver.get_cookies()
            print(seleniumCookies)


            driver.close()

                    # # 查看搜索结果是否出现
            # searchRes = spider.wait.until(
            #     EC.presence_of_element_located((By.XPATH, "//div[@id='resultsCol']"))
            # )

        except Exception as e:
            print("chrome user login handle error, Exception = {e}")
            return

        else:
            # time.sleep(3)
            # # 登录成功之后，获取到selenium的cookie
            # cookie = [item["name"] + ":" + item["value"] for item in seleniumCookies]
            # cookMap = {}
            # for elem in cookie:
            #     str = elem.split(':')
            #     cookMap[str[0]] = str[1]
            # print(f"cookMap = {cookMap}")
            # # 中间件，对Request进行加工
            # # 开始用这个转换后的cookie重新构造Request，从源码中来看Request构造的原型
            # # E:\Miniconda\Lib\site-packages\scrapy\http\request\__init__.py
            # cookies = cookMap  # 让这个带有登录后cookie的Request继续爬取
            # return cookies
            time.sleep(3)
            driver.close()
            if seleniumCookies:
                return seleniumCookies
            else:
                driver.close()
                self.get_cookies_from_chrome(phone,password)


    def get_selenium_cookie(self):
        account_lists =self.account_list
        for li in account_lists:
            seleniumCookies_str = self.get_cookies_from_chrome(li["phone"], li["password"])

            if seleniumCookies_str:
                # self.redis_client.insert_cookies(seleniumCookies_str)
                print(seleniumCookies_str)
                print(type(seleniumCookies_str))
            # else:
            #     account_lists.remove(li)
            #
get_cookies = GetCookies()
get_cookies.get_selenium_cookie()

# if __name__ == '__main__':
#     '''
#     1. 检测redis数据库中cookies剩余量，如果小于10，则启动
#     '''
#     while True:
#         result = redis_client.get_keys()
#         if len(result) < 6:
#             get_cookies = GetCookies()
#             get_cookies.get_selenium_cookie()
#             time.sleep(10)
#         time.sleep(3600*6)
#         result_delete = redis_client.get_keys()
#         for i in result_delete[1:]:      #为防止redis数据库中取得时候没有cookie，从第二个开始删除
#             redis_client.delete(i)




#  排排网 罗兰账号： 18236283353   密码：18236283353lnr

# import json
# seleniumCookies = [{'domain': '.simuwang.com', 'expiry': 1539768267, 'httpOnly': False, 'name': 'smppw_tz_auth', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.simuwang.com', 'expiry': 7846363467, 'httpOnly': False, 'name': 'sensorsdata2015jssdkcross', 'path': '/', 'secure': False, 'value': '%7B%22distinct_id%22%3A%22582653%22%2C%22%24device_id%22%3A%221665d4a7c8a1e7-08f81ae7ea13b7-346d7809-2073600-1665d4a7c8c8ce%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22582653%22%7D'}, {'domain': '.simuwang.com', 'expiry': 1540027467.551419, 'httpOnly': False, 'name': 'evaluation_result', 'path': '/', 'secure': False, 'value': '5'}, {'domain': '.simuwang.com', 'expiry': 1540027467.551365, 'httpOnly': False, 'name': 'qualified_investor', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.simuwang.com', 'expiry': 1540027467.55144, 'httpOnly': False, 'name': 'focus-certification-pop', 'path': '/', 'secure': False, 'value': '-1'}, {'domain': '.simuwang.com', 'expiry': 1540027467.551233, 'httpOnly': False, 'name': 'rz_u_p', 'path': '/', 'secure': False, 'value': 'd41d8cd98f00b204e9800998ecf8427e%3Du7053690600037'}, {'domain': '.simuwang.com', 'expiry': 1540027467.551176, 'httpOnly': False, 'name': 'passport', 'path': '/', 'secure': False, 'value': '582653%09u7053690600037%09UFAAAFNUCwRRAgsDUgZRCV0BUQEAXQRTVQcGBgwFBQc%3D80c9900986'}, {'domain': '.simuwang.com', 'expiry': 1540027467.551018, 'httpOnly': False, 'name': 'cur_ck_time', 'path': '/', 'secure': False, 'value': '1539163469'}, {'domain': '.simuwang.com', 'expiry': 1540027467.551127, 'httpOnly': False, 'name': 'http_tK_cache', 'path': '/', 'secure': False, 'value': '2aa0b0c4f49c81aea9699cbc4ba9f5916a136178'}, {'domain': 'dc.simuwang.com', 'httpOnly': False, 'name': 'PHPSESSID', 'path': '/', 'secure': False, 'value': '3958g2hhiv6865kv0h0lunadr1'}, {'domain': '.simuwang.com', 'httpOnly': False, 'name': 'Hm_lpvt_c3f6328a1a952e922e996c667234cdae', 'path': '/', 'secure': False, 'value': '1539163455'}, {'domain': 'dc.simuwang.com', 'expiry': 1696844360, 'httpOnly': False, 'name': '_9755xjdesxxd_', 'path': '/', 'secure': False, 'value': '32'}, {'domain': '.simuwang.com', 'expiry': 1540027467.551292, 'httpOnly': False, 'name': 'certification', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.simuwang.com', 'expiry': 1570699455, 'httpOnly': False, 'name': 'Hm_lvt_c3f6328a1a952e922e996c667234cdae', 'path': '/', 'secure': False, 'value': '1539163455'}, {'domain': '.simuwang.com', 'httpOnly': False, 'name': 'stat_sessid', 'path': '/', 'secure': False, 'value': 'o4d29ni3ipmjsp51fbosla04h7'}, {'domain': '.simuwang.com', 'expiry': 1540027455, 'httpOnly': False, 'name': 'regsms', 'path': '/', 'secure': False, 'value': '1539163455000'}, {'domain': '.simuwang.com', 'expiry': 1540027467.551261, 'httpOnly': False, 'name': 'rz_rem_u_p', 'path': '/', 'secure': False, 'value': 'wfBnseEHc9Bhh%2FiLr8OhpcqlSGnMhrXjWpPqR5GJ7n4%3D%24Yf8XTznM89ixhCXODURjAtBjU6gI6w2owrLbuQYZ7bI%3D'}, {'domain': '.simuwang.com', 'expiry': 1539164895, 'httpOnly': False, 'name': 'rz_token_6658', 'path': '/', 'secure': False, 'value': 'ca82a2c953d9a475e6fdcd7801664f7c.1539163455'}, {'domain': 'dc.simuwang.com', 'expiry': 1696844360, 'httpOnly': False, 'name': 'gdxidpyhxdE', 'path': '/', 'secure': False, 'value': 'kYJlpCTuV94XG%2BUgvv7uwupjBd9YmghO0vQYKL862d26lwZ0RHkG%2FqoDg%2BIytUlQXWWQz96VQPML6p2OajMTUyO9NNmDj2%2B0z97RT6H5Mw7cmH%5CHOW7tiIfp9CEzhlvfS1ldjgse6il24CsI1t7ICCCfKtokueSAASOOnLBo7zK3W21U%3A1539164360213'}, {'domain': '.simuwang.com', 'expiry': 1539187199, 'httpOnly': False, 'name': 'sajssdk_2015_cross_new_user', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.simuwang.com', 'expiry': 1540027467.551064, 'httpOnly': False, 'name': 'ck_request_key', 'path': '/', 'secure': False, 'value': 'hg4EPjnwaWZ%2BWcd5ov4Zel9k8DaXaJd2msvZh8u5Ox4%3D'}, {'domain': '.simuwang.com', 'expiry': 1570699454.566084, 'httpOnly': False, 'name': 'guest_id', 'path': '/', 'secure': False, 'value': '1526767495'}]

# # if __name__ == '__main__':
# #     '''
# #     1. 检测redis数据库中cookies剩余量，如果小于20，则启动
# #     '''
# #     while True:
# #         result = redis_client.get_keys()
# #         if len(result) < 20:
# #             get_cookies = GetCookies()
# #             proxy = get_proxy()
# #             for i in range(3):
# #                 t_1 = threading.Thread(target=get_cookies.get_cookies_from_firefox, args=(proxy,))
# #                 t_1.start()
# #                 t_2 = threading.Thread(target=get_cookies.get_cookies_from_chrome, args=(proxy,))
# #                 t_2.start()
# #         time.sleep(15)
# '''
# # _lxsdk=16618bc96a7c8-01bc7c9697c92f-347a6f2d-1fa400-16618bc96a7c8; _lxsdk_cuid=16618bc96a7c8-01bc7c9697c92f-347a6f2d-1fa400-16618bc96a7c8; _lxsdk_s=16618bc96a8-e40-3be-0d0%7C%7C42; logan_custom_report=; cityid=1; logan_session_token=enysg423n941117lqf31; default_ab=shopList%3AA%3A1; msource=default; _hc.v=6f45483d-b9a7-eec2-a0de-5fc20a040659.1538013299;
# # _lxsdk=16618bc95af70-0d9f3b7a39b8b4-347a6f2d-1fa400-16618bc95b0c8; _lxsdk_cuid=16618bc95af70-0d9f3b7a39b8b4-347a6f2d-1fa400-16618bc95b0c8; _lxsdk_s=16618bc95b1-f94-9e1-8e6%7C%7C42; logan_custom_report=; cityid=1; logan_session_token=p0iobiyszzvihs7qbana; default_ab=shopList%3AA%3A1; msource=default; _hc.v=a95377eb-1dad-8758-5e03-aa49bc73da2c.1538013300;
# # _lxsdk=16618e802e7c8-036ceb1f282014-347a6f2d-1fa400-16618e802e8c8; _lxsdk_cuid=16618e802e7c8-036ceb1f282014-347a6f2d-1fa400-16618e802e8c8; _lxsdk_s=16618e802ea-6bb-e21-a52%7C%7C42; logan_custom_report=; cityid=1; logan_session_token=j31bjj9azu5jjsm4lxjm; default_ab=shopList%3AA%3A1; msource=default; _hc.v=b38ee5fa-024c-d776-5ef2-489c79ac6a00.1538016146;
# # _lxsdk=16618e80a66c8-090899ee9f084a-4a506a-100200-16618e80a661e; _lxsdk_cuid=16618e80a66c8-090899ee9f084a-4a506a-100200-16618e80a661e; _lxsdk_s=16618e80a67-eb8-0fd-630%7C%7CNaN;  logan_custom_report=; cityid=1;  logan_session_token=wdk0o922cxfoelr4m4kv;  default_ab=shopList%3AA%3A1; msource=default; _hc.v=682b76dd-45ed-bb4c-3e0f-b3c2bf6388a6.1538016150;
# #
# #
# # _hc.v=a9039261-d763-0503-3039-1fcd94ef6ecc.1538029425; msource=default; default_ab=shopList%3AA%3A1; cityid=10; logan_session_token=u8xsrmpsi41d49dx9do7; logan_custom_report=; _lxsdk_cuid=16619b2ac8dc8-0035aa74bc7a02-4a506a-100200-16619b2ac8dc8; _lxsdk=16619b2ac8dc8-0035aa74bc7a02-4a506a-100200-16619b2ac8dc8; _lxsdk_s=16619b2ac8e-d50-244-23d%7C%7C1;
# # _lxsdk=16619b2eb58c8-02afc28e0ef9ef-347a6f2d-1fa400-16619b2eb59c8; _lxsdk_cuid=16619b2eb58c8-02afc28e0ef9ef-347a6f2d-1fa400-16619b2eb59c8; logan_session_token=bwl2tqa0xs4lojgug9ct; default_ab=shopList%3AA%3A1; msource=default; _hc.v=078c49e0-50d4-b0a5-75ee-a3554facd237.1538029439; _lxsdk_s=16619b2eb5a-4ba-aa8-ca7%7C%7C42; logan_custom_report=; cityid=110;
# #
# # '''