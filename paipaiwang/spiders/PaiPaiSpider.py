from decimal import Decimal

from scrapy.spiders import CrawlSpider
from paipaiwang.items import PaipaiwangItem,FundItem,CompanyItem,EmployItem,Fund_worthItem
from scrapy import Request, FormRequest
from scrapy.selector import Selector
import json
import requests
from urllib import parse
from lxml import etree
import re
from copy import deepcopy
import time
import scrapy
import logging
from scrapy.spiders import Spider
from scrapy.conf import settings
from selenium import webdriver
import datetime
# from paipaiwang.py_bloomfilter import PyBloomFilter
from selenium.webdriver.chrome.options import Options
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher
from scrapy.http import TextResponse
from paipaiwang.Utils.proxy import get_proxy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from paipaiwang.settings import DEFAULT_REQUEST_HEADERS
logger=logging.getLogger(__name__)
chrome_options = Options()
# chrome_options.add_argument('--headless')

chrome_options.add_argument('--proxy-server={}'.format('http://116.17.236.248:32898'))
class PaiPaiSpider(scrapy.Spider):
    name = 'PaiPaiSpider'
    allow_domain = ["dc.simuwang.com"]
    start_urls = ['https://dc.simuwang.com']
    proxy_mode = True  # 没有代理队列会停止pop
    cookie = settings["COOKIE"] # 带着Cookie向网页发请求
    # listCookies = [{'domain': '.simuwang.com', 'httpOnly': False, 'name': 'autologin_status', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.simuwang.com', 'httpOnly': False, 'name': 'Hm_lpvt_c3f6328a1a952e922e996c667234cdae', 'path': '/', 'secure': False, 'value': '1539064558'}, {'domain': 'dc.simuwang.com', 'expiry': 1539066333, 'httpOnly': False, 'name': 'fyr_ssid_n5776', 'path': '/', 'secure': False, 'value': 'fyr_n5776_jn1ba3y7'}, {'domain': '.simuwang.com', 'expiry': 1539669332, 'httpOnly': False, 'name': 'smppw_tz_auth', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.simuwang.com', 'expiry': 1539928531.998647, 'httpOnly': False, 'name': 'rz_u_p', 'path': '/', 'secure': False, 'value': 'd41d8cd98f00b204e9800998ecf8427e%3Du7053690600037'}, {'domain': '.simuwang.com', 'expiry': 7846264558, 'httpOnly': False, 'name': 'sensorsdata2015jssdkcross', 'path': '/', 'secure': False, 'value': '%7B%22distinct_id%22%3A%22582653%22%2C%22%24device_id%22%3A%221665764efde108-0c438b67462f5b-346d7809-2073600-1665764efdf8c1%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22582653%22%7D'}, {'domain': '.simuwang.com', 'expiry': 1539928531.998816, 'httpOnly': False, 'name': 'evaluation_result', 'path': '/', 'secure': False, 'value': '5'}, {'domain': '.simuwang.com', 'expiry': 1539928531.998761, 'httpOnly': False, 'name': 'qualified_investor', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.simuwang.com', 'expiry': 1539928531.998849, 'httpOnly': False, 'name': 'focus-certification-pop', 'path': '/', 'secure': False, 'value': '-1'}, {'domain': '.simuwang.com', 'httpOnly': False, 'name': 'sensro_profile_has_set', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.simuwang.com', 'expiry': 1539928525, 'httpOnly': False, 'name': 'regsms', 'path': '/', 'secure': False, 'value': '1539064525000'}, {'domain': '.simuwang.com', 'expiry': 1539928531.998627, 'httpOnly': False, 'name': 'passport', 'path': '/', 'secure': False, 'value': '582653%09u7053690600037%09UFAAAFNUCwRRAgsDUgZRCV0BUQEAXQRTVQcGBgwFBQc%3D80c9900986'}, {'domain': 'dc.simuwang.com', 'httpOnly': False, 'name': 'PHPSESSID', 'path': '/', 'secure': False, 'value': '2vgdjadfctrmf4t9mujlsbth27'}, {'domain': '.simuwang.com', 'expiry': 1539928531.998432, 'httpOnly': False, 'name': 'cur_ck_time', 'path': '/', 'secure': False, 'value': '1539064534'}, {'domain': '.simuwang.com', 'expiry': 1539065965, 'httpOnly': False, 'name': 'rz_token_6658', 'path': '/', 'secure': False, 'value': 'e61c2f089574254dc2b6d90e107cde5f.1539064525'}, {'domain': '.simuwang.com', 'expiry': 1539928531.998559, 'httpOnly': False, 'name': 'http_tK_cache', 'path': '/', 'secure': False, 'value': '0442c0ee23cf7f4e9de748f0647ad93fc8273fad'}, {'domain': 'dc.simuwang.com', 'expiry': 1696745428, 'httpOnly': False, 'name': '_9755xjdesxxd_', 'path': '/', 'secure': False, 'value': '32'}, {'domain': '.simuwang.com', 'expiry': 1539928531.998484, 'httpOnly': False, 'name': 'ck_request_key', 'path': '/', 'secure': False, 'value': 'zmKNxhPB%2BKhme%2BTXsI613QIUopZ%2B2VsRwNTIM%2F0Vx9g%3D'}, {'domain': '.simuwang.com', 'expiry': 1539100799, 'httpOnly': False, 'name': 'sajssdk_2015_cross_new_user', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.simuwang.com', 'expiry': 1539928531.998726, 'httpOnly': False, 'name': 'certification', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.simuwang.com', 'expiry': 1570600558, 'httpOnly': False, 'name': 'Hm_lvt_c3f6328a1a952e922e996c667234cdae', 'path': '/', 'secure': False, 'value': '1539064525'}, {'domain': '.simuwang.com', 'httpOnly': False, 'name': 'stat_sessid', 'path': '/', 'secure': False, 'value': '0s1c65pag19lvjqhgj19untiq6'}, {'domain': '.simuwang.com', 'expiry': 1539928531.998671, 'httpOnly': False, 'name': 'rz_rem_u_p', 'path': '/', 'secure': False, 'value': 'wfBnseEHc9Bhh%2FiLr8OhpcqlSGnMhrXjWpPqR5GJ7n4%3D%24Yf8XTznM89ixhCXODURjAtBjU6gI6w2owrLbuQYZ7bI%3D'}, {'domain': 'dc.simuwang.com', 'expiry': 1696745428, 'httpOnly': False, 'name': 'gdxidpyhxdE', 'path': '/', 'secure': False, 'value': 'UfXmPr3706QVzsV%5CzLo013%2FS%2BL%2FpV2%5CGJKSToZ3nSdmi3%2B7PjQuwIS5LJB0BKIfMZn0ej7%5Cr2vqtSqIqxRc%2B%2Btn6%2F3vA86mwEUYL9%5CT6w9bkGwCOtn8dYyqxuOvInLviYBcaU9D6Yga%2B9AkgiE8eXqADzJZ5IvRw0iqU%2BC%5CQx%5CxnZ3Kc%3A1539065428599'}, {'domain': '.simuwang.com', 'expiry': 1570600524.495628, 'httpOnly': False, 'name': 'guest_id', 'path': '/', 'secure': False, 'value': '1526711257'}]


    # headers = {
    #      'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13.',
    #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    #     'Accept-Encoding': 'gzip, deflate',
    #     'Accept - Language': 'zh - CN, zh;q = 0.8',
    #     'Host': 'dc.simuwang.com',
    #     'Referer': 'http://dc.simuwang.com',
    #     'X - Requested - With': 'XMLHttpRequest',
    # }
    def __init__(self):

        # self.headers = {
        #     'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13.',
        #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        #     'Accept-Encoding': 'gzip, deflate',
        #     'Accept - Language': 'zh - CN, zh;q = 0.8',
        #     'Host': 'dc.simuwang.com',
        #     'Referer': 'https://dc.simuwang.com',
        #     'X - Requested - With': 'XMLHttpRequest',
        # }
        # self.driver =webdriver.Chrome(chrome_options=chrome_options)   #无头浏览器
        # self.cookies = {'domain': '.simuwang.com', 'httpOnly': False, 'name': 'autologin_status', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.simuwang.com', 'httpOnly': False, 'name': 'Hm_lpvt_c3f6328a1a952e922e996c667234cdae', 'path': '/', 'secure': False, 'value': '1539064558'}, {'domain': 'dc.simuwang.com', 'expiry': 1539066333, 'httpOnly': False, 'name': 'fyr_ssid_n5776', 'path': '/', 'secure': False, 'value': 'fyr_n5776_jn1ba3y7'}, {'domain': '.simuwang.com', 'expiry': 1539669332, 'httpOnly': False, 'name': 'smppw_tz_auth', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.simuwang.com', 'expiry': 1539928531.998647, 'httpOnly': False, 'name': 'rz_u_p', 'path': '/', 'secure': False, 'value': 'd41d8cd98f00b204e9800998ecf8427e%3Du7053690600037'}, {'domain': '.simuwang.com', 'expiry': 7846264558, 'httpOnly': False, 'name': 'sensorsdata2015jssdkcross', 'path': '/', 'secure': False, 'value': '%7B%22distinct_id%22%3A%22582653%22%2C%22%24device_id%22%3A%221665764efde108-0c438b67462f5b-346d7809-2073600-1665764efdf8c1%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22582653%22%7D'}, {'domain': '.simuwang.com', 'expiry': 1539928531.998816, 'httpOnly': False, 'name': 'evaluation_result', 'path': '/', 'secure': False, 'value': '5'}, {'domain': '.simuwang.com', 'expiry': 1539928531.998761, 'httpOnly': False, 'name': 'qualified_investor', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.simuwang.com', 'expiry': 1539928531.998849, 'httpOnly': False, 'name': 'focus-certification-pop', 'path': '/', 'secure': False, 'value': '-1'}, {'domain': '.simuwang.com', 'httpOnly': False, 'name': 'sensro_profile_has_set', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.simuwang.com', 'expiry': 1539928525, 'httpOnly': False, 'name': 'regsms', 'path': '/', 'secure': False, 'value': '1539064525000'}, {'domain': '.simuwang.com', 'expiry': 1539928531.998627, 'httpOnly': False, 'name': 'passport', 'path': '/', 'secure': False, 'value': '582653%09u7053690600037%09UFAAAFNUCwRRAgsDUgZRCV0BUQEAXQRTVQcGBgwFBQc%3D80c9900986'}, {'domain': 'dc.simuwang.com', 'httpOnly': False, 'name': 'PHPSESSID', 'path': '/', 'secure': False, 'value': '2vgdjadfctrmf4t9mujlsbth27'}, {'domain': '.simuwang.com', 'expiry': 1539928531.998432, 'httpOnly': False, 'name': 'cur_ck_time', 'path': '/', 'secure': False, 'value': '1539064534'}, {'domain': '.simuwang.com', 'expiry': 1539065965, 'httpOnly': False, 'name': 'rz_token_6658', 'path': '/', 'secure': False, 'value': 'e61c2f089574254dc2b6d90e107cde5f.1539064525'}, {'domain': '.simuwang.com', 'expiry': 1539928531.998559, 'httpOnly': False, 'name': 'http_tK_cache', 'path': '/', 'secure': False, 'value': '0442c0ee23cf7f4e9de748f0647ad93fc8273fad'}, {'domain': 'dc.simuwang.com', 'expiry': 1696745428, 'httpOnly': False, 'name': '_9755xjdesxxd_', 'path': '/', 'secure': False, 'value': '32'}, {'domain': '.simuwang.com', 'expiry': 1539928531.998484, 'httpOnly': False, 'name': 'ck_request_key', 'path': '/', 'secure': False, 'value': 'zmKNxhPB%2BKhme%2BTXsI613QIUopZ%2B2VsRwNTIM%2F0Vx9g%3D'}, {'domain': '.simuwang.com', 'expiry': 1539100799, 'httpOnly': False, 'name': 'sajssdk_2015_cross_new_user', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.simuwang.com', 'expiry': 1539928531.998726, 'httpOnly': False, 'name': 'certification', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.simuwang.com', 'expiry': 1570600558, 'httpOnly': False, 'name': 'Hm_lvt_c3f6328a1a952e922e996c667234cdae', 'path': '/', 'secure': False, 'value': '1539064525'}, {'domain': '.simuwang.com', 'httpOnly': False, 'name': 'stat_sessid', 'path': '/', 'secure': False, 'value': '0s1c65pag19lvjqhgj19untiq6'}, {'domain': '.simuwang.com', 'expiry': 1539928531.998671, 'httpOnly': False, 'name': 'rz_rem_u_p', 'path': '/', 'secure': False, 'value': 'wfBnseEHc9Bhh%2FiLr8OhpcqlSGnMhrXjWpPqR5GJ7n4%3D%24Yf8XTznM89ixhCXODURjAtBjU6gI6w2owrLbuQYZ7bI%3D'}, {'domain': 'dc.simuwang.com', 'expiry': 1696745428, 'httpOnly': False, 'name': 'gdxidpyhxdE', 'path': '/', 'secure': False, 'value': 'UfXmPr3706QVzsV%5CzLo013%2FS%2BL%2FpV2%5CGJKSToZ3nSdmi3%2B7PjQuwIS5LJB0BKIfMZn0ej7%5Cr2vqtSqIqxRc%2B%2Btn6%2F3vA86mwEUYL9%5CT6w9bkGwCOtn8dYyqxuOvInLviYBcaU9D6Yga%2B9AkgiE8eXqADzJZ5IvRw0iqU%2BC%5CQx%5CxnZ3Kc%3A1539065428599'}, {'domain': '.simuwang.com', 'expiry': 1570600524.495628, 'httpOnly': False, 'name': 'guest_id', 'path': '/', 'secure': False, 'value': '1526711257'}
        # self.cookies = {'guest_id':1525751430 ,'_9755xjdesxxd_':32, 'gdxidpyhxdE':'L65QW%2F9x%5CNMfIgwrr9%5CPCeAP6JiXys33b%2BgMIxUi6invds%2BE%2FHA44xt%2FzeUQeXGuqbbZkItEJI1Plafgkqg3K%5C0awLqcQLl830tyLr1cjnqRi29ny1QwOjLOHaNcRR9Aw3V59V2pqLscz%2FoMHvwi9Pauicme0nZPEGnb4ckWr3REiPqt%3A1538272775074', 'certification':1, 'qualified_investor':1, 'evaluation_result':5, 'focus-certification-pop':-1, 'PHPSESSID':'u3pgn8qnl3akdhmdr1gu9da3k0', 'sensro_profile_has_set':1, 'Hm_lvt_c3f6328a1a952e922e996c667234cdae':'1538212651,1538270493,1538275688', 'stat_sessid':'jh9n5j8gha1tg12fjom5c3pmg4', 'regsms':1538977237000, 'sensorsdata2015jssdkcross':'%7B%22distinct_id%22%3A%22582653%22%2C%22%24device_id%22%3A%22166249e61a4c78-053fac6ad761df-346d7809-2073600-166249e61a58b7%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22582653%22%7D', 'rz_token_6658':'3b62890de15a2e170219d48b79d62345.1539050196', 'http_tK_cache':'f2974e07c2c384b563dd1be8370c794ffce4c0e0', 'cur_ck_time':1539050198, 'ck_request_key':'si9lkzlY3ti6ao9gMFvm%2B71tVf6Zuy7kfdY%2FebBmyoU%3D', 'passport':'582653%09u7053690600037%09UFAAAFNUCwRRAgsDUgZRCV0BUQEAXQRTVQcGBgwFBQc%3D80c9900986', 'rz_u_p':'d41d8cd98f00b204e9800998ecf8427e%3Du7053690600037', 'rz_rem_u_p':'wfBnseEHc9Bhh%2FiLr8OhpcqlSGnMhrXjWpPqR5GJ7n4%3D%24Yf8XTznM89ixhCXODURjAtBjU6gI6w2owrLbuQYZ7bI%3D', 'autologin_status':0, 'Hm_lpvt_c3f6328a1a952e922e996c667234cdae':1539050233}

        # self.driver = webdriver.Chrome()
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.set_page_load_timeout(60)
        self.listCookies = settings["LIST_COOKIES"]
        super(PaiPaiSpider,self).__init__()
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    def spider_closed(self,spider):
    #     request = scrapy.Request(url=self.driver.current_url,callback=self.parse())
    #     yield request
        self.driver.quit()


    #进入基金首页列表页取数据
    def parse(self, response):

        # driver.implicitly_wait(30)

        #不限的  先拿三心的做测试

        first_url = 'http://dc.simuwang.com/ranking/get?page=1&condition=fund_type%3A1%2C6%2C4%2C3%2C8%2C2%3Bret%3A1%3Brating_year%3A1%3Bsort_name%3Aprofit_col2%3Bsort_asc%3Adesc%3Bkeyword%3A'
        # first_url = 'https://dc.simuwang.com/ranking/get?page=1&condition=fund_type%3A1%2C6%2C4%2C3%2C8%2C2%3Bret%3A1%3Brating_year%3A1%3Brating%3A3%3Bstrategy%3A1%3Bistiered%3A0%3Bcompany_type%3A1%3Bsort_name%3Aprofit_col2%3Bsort_asc%3Adesc%3Bkeyword%3A'

        r = requests.get(url=first_url,headers=DEFAULT_REQUEST_HEADERS).json()
        page_count = r['pager']['pagecount']

        print(page_count)

        url_str = "https://dc.simuwang.com/ranking/get?page={}&condition=fund_type%3A1%2C6%2C4%2C3%2C8%2C2%3Bret%3A1%3Brating_year%3A1%3Bsort_name%3Aprofit_col2%3Bsort_asc%3Adesc%3Bkeyword%3A"
        for index in range(1, page_count+1):
            next_url = url_str.format(str(index))
            
            yield Request(url=next_url, callback=self.parse_list)

    #基金列表页翻页,并提取基金url和company的url
    def parse_list(self,response):

        sel = Selector(response)
        objs = json.loads(sel.response.body_as_unicode())['data']
        for j in range(len(objs)):
            item = PaipaiwangItem()
            item["company_id"] = objs[j]['company_id']
            item["company_gsjc"] = objs[j]['company_short_name']

            item["fund_id"] = objs[j]['fund_id']
            # print(item)
            fund_url = 'https://dc.simuwang.com/product/' + str(item['fund_id']) + '.html'
            company_url = 'https://dc.simuwang.com/company/' + str(item['company_id']) + '.html'


            yield Request(url=fund_url,cookies=self.cookie,callback=self.parse_fund,meta={'item':deepcopy(item)})
            # yield Request(url=company_url,cookies=self.cookie,callback=self.parse_company,meta={'item':deepcopy(item)})

    #进入基金详情页面
    def parse_fund(self,response):

        item = FundItem()
        item["fund_id"]=response.meta["item"]['fund_id']
        fund_id = item['fund_id']
        item["company_id"] = response.meta["item"]['company_id']

        datas = json.loads(response.body.decode())  #详情页所有界面
        data_index = datas[0]
        # print(data_index)

        html_index = etree.HTML(data_index)

        item["fund_name"] = html_index.xpath("//*[@id='fund-detail-box']/div[1]/div[1]/span/text()")[0] if len(html_index.xpath("//*[@id='fund-detail-box']/div[1]/div[1]/span/text()"))>0 else None

        item["rzpj"] = len(html_index.xpath('//*[@id="fund-detail-box"]/div[1]/div[1]/div[6]/div[3]/div/i')) if len(html_index.xpath('//*[@id="fund-detail-box"]/div[1]/div[1]/div[6]/div[3]/div/i'))>0 else None
        item["jjjl"] = html_index.xpath('//*[@id="fund-detail-box"]/div[1]/div[1]/div[6]/div[4]/div/a/span/text()') if len(html_index.xpath('//*[@id="fund-detail-box"]/div[1]/div[1]/div[6]/div[4]/div/a/span/text()'))>0 else None #有问题的地方

        item["manager_id"] = re.findall(r'<a href="/manager/(.*?).html',data_index)[0] if len(re.findall(r'<a href="/manager/(.*?).html',data_index))>0 else None

        # item["manager_id"] = item["manager_id"] if len(item["manager_id"]) > 0 else None

        item["paiming"] = html_index.xpath('//*[@id="fund-detail-box"]/div[1]/div[1]/div[6]/div[7]/span/text()')[0] if len(html_index.xpath('//*[@id="fund-detail-box"]/div[1]/div[1]/div[6]/div[7]/span/text()'))>0 else None

        item["company_name"] =html_index.xpath('//*[@id="fund-detail-box"]/div[1]/div[1]/div[6]/div[8]/a/span/text()')[0] if len(html_index.xpath('//*[@id="fund-detail-box"]/div[1]/div[1]/div[6]/div[8]/a/span/text()'))>0 else None

        item["cpmc"] = html_index.xpath('//*[@id="product-detail-table"]/tr[1]/td[2]/text()')[0] if len(html_index.xpath('//*[@id="product-detail-table"]/tr[1]/td[2]/text()'))>0 else None

        item["tzgw"] = html_index.xpath('//*[@id="product-detail-table"]/tr[2]/td[2]/span/text()')[0] if len(html_index.xpath('//*[@id="product-detail-table"]/tr[2]/td[2]/span/text()'))>0 else None

        item["jjglr"] = html_index.xpath('//*[@id="product-detail-table"]/tr[3]/td[2]/text()')[0] if len(html_index.xpath('//*[@id="product-detail-table"]/tr[3]/td[2]/text()'))>0 else None

        item["jjtgr"] = html_index.xpath('//*[@id="product-detail-table"]/tr[4]/td[2]/text()')[0] if len(html_index.xpath('//*[@id="product-detail-table"]/tr[4]/td[2]/text()'))>0 else None

        item["wbjgf"] = html_index.xpath('//*[@id="product-detail-table"]/tr[5]/td[2]/text()')[0] if len(html_index.xpath('//*[@id="product-detail-table"]/tr[5]/td[2]/text()'))>0 else None

        item["zqjjs"] = html_index.xpath('//*[@id="product-detail-table"]/tr[6]/td[2]/text()')[0] if len(html_index.xpath('//*[@id="product-detail-table"]/tr[6]/td[2]/text()'))>0 else None

        item["qhjjs"] = html_index.xpath('//*[@id="product-detail-table"]/tr[7]/td[2]/text()')[0] if len(html_index.xpath('//*[@id="product-detail-table"]/tr[7]/td[2]/text()'))>0 else None
        item["birthday"] = html_index.xpath('//*[@id="product-detail-table"]/tr[8]/td[2]/text()')[0] if len(html_index.xpath('//*[@id="product-detail-table"]/tr[8]/td[2]/text()'))>0 else None
        item["yxzt"] = html_index.xpath('//*[@id="product-detail-table"]/tr[9]/td[2]/text()')[0] if len(html_index.xpath('//*[@id="product-detail-table"]/tr[9]/td[2]/text()'))>0 else None
        item["cplx"] = html_index.xpath('//*[@id="product-detail-table"]/tr[10]/td[2]/text()')[0] if len(html_index.xpath('//*[@id="product-detail-table"]/tr[10]/td[2]/text()'))>0 else None
        item["csgm"] = html_index.xpath('//*[@id="product-detail-table"]/tr[11]/td[2]/text()')[0] if len(html_index.xpath('//*[@id="product-detail-table"]/tr[11]/td[2]/text()'))>0 else None
        item["tzcl"] = html_index.xpath('//*[@id="product-detail-table"]/tr[12]/td[2]/text()')[0] if len(html_index.xpath('//*[@id="product-detail-table"]/tr[12]/td[2]/text()'))>0 else None
        item["sffj"] = html_index.xpath('//*[@id="product-detail-table"]/tr[13]/td[2]/text()')[0] if len(html_index.xpath('//*[@id="product-detail-table"]/tr[13]/td[2]/text()'))>0 else None
        item["sfsx"] = html_index.xpath('//*[@id="product-detail-table"]/tr[14]/td[2]/text()')[0] if len(html_index.xpath('//*[@id="product-detail-table"]/tr[14]/td[2]/text()'))>0 else None
        item["rgqd"] = html_index.xpath('//*[@id="product-detail-table"]/tr[1]/td[4]/text()')[0] if len(html_index.xpath('//*[@id="product-detail-table"]/tr[1]/td[4]/text()'))>0 else None
        item["zjqd"] = html_index.xpath('//*[@id="product-detail-table"]/tr[2]/td[4]/text()')[0] if len(html_index.xpath('//*[@id="product-detail-table"]/tr[2]/td[4]/text()'))>0 else None
        item["fbq"] = html_index.xpath('//*[@id="product-detail-table"]/tr[3]/td[4]/text()')[0] if len(html_index.xpath('//*[@id="product-detail-table"]/tr[3]/td[4]/text()'))>0 else None
        item["kfr"] = html_index.xpath('//*[@id="product-detail-table"]/tr[4]/td[4]/text()')[0] if len(html_index.xpath('//*[@id="product-detail-table"]/tr[4]/td[4]/text()'))>0 else None  #有问题
        item["rgfl"] = html_index.xpath('//*[@id="product-detail-table"]/tr[5]/td[4]/text()')[0] if len(html_index.xpath('//*[@id="product-detail-table"]/tr[5]/td[4]/text()'))>0 else None#有问题
        item["shfl"] = html_index.xpath('//*[@id="product-detail-table"]/tr[6]/td[4]/text()')[0] if len(html_index.xpath('//*[@id="product-detail-table"]/tr[6]/td[4]/text()'))>0 else None
        item["shflsm"] = html_index.xpath('//*[@id="product-detail-table"]/tr[7]/td[4]/text()')[0] if len(html_index.xpath('//*[@id="product-detail-table"]/tr[7]/td[4]/text()'))>0 else None
        item["glfl"] = html_index.xpath('//*[@id="product-detail-table"]/tr[8]/td[4]/text()')[0] if len(html_index.xpath('//*[@id="product-detail-table"]/tr[8]/td[4]/text()'))>0 else None
        item["yjx"] = html_index.xpath('//*[@id="product-detail-table"]/tr[9]/td[4]/text()')[0] if len(html_index.xpath('//*[@id="product-detail-table"]/tr[9]/td[4]/text()'))>0 else None
        item["zsx"] = html_index.xpath('//*[@id="product-detail-table"]/tr[10]/td[4]/text()')[0] if len(html_index.xpath('//*[@id="product-detail-table"]/tr[10]/td[4]/text()'))>0 else None
        item["yjbc"] = html_index.xpath('//*[@id="product-detail-table"]/tr[11]/td[4]/text()')[0] if len(html_index.xpath('//*[@id="product-detail-table"]/tr[11]/td[4]/text()'))>0 else None
        item["cxqx"] = html_index.xpath('//*[@id="product-detail-table"]/tr[12]/td[4]/text()')[0].strip() if len(html_index.xpath('//*[@id="product-detail-table"]/tr[12]/td[4]/text()'))>0 else None
        item["babh"] = html_index.xpath('//*[@id="product-detail-table"]/tr[13]/td[4]/text()')[0] if len(html_index.xpath('//*[@id="product-detail-table"]/tr[13]/td[4]/text()'))>0 else None
        item["plbs"] = html_index.xpath('//*[@id="product-detail-table"]/tr[14]/td[4]/text()')[0] if len(html_index.xpath('//*[@id="product-detail-table"]/tr[14]/td[4]/text()'))>0 else None

        # print(item)
        yield item    #提取详情页的fund信息完成

        for data in datas:
            data = etree.HTML(data)
            fund_worth_item = Fund_worthItem()
            fund_worth_item["fund_id"] = fund_id
            tr = data.xpath("//*[@id='networth-table']/tbody/tr")
            #提取fund_worth数据
            for i in range(1,len(tr)+1):
                try:#
                    fund_worth_item["date"] = data.xpath("//*[@id='networth-table']/tbody/tr[%s]/td[1]/text()" %i)[0] if len(data.xpath("//*[@id='networth-table']/tbody/tr[%s]/td[1]/text()" %i))>0 else None
                    fund_worth_item["unit"] = data.xpath("//*[@id='networth-table']/tbody/tr[%s]/td[2]/text()" %i)[0] if len(data.xpath("//*[@id='networth-table']/tbody/tr[%s]/td[2]/text()" %i))>0 else None
                    fund_worth_item["unit"] = Decimal(fund_worth_item["unit"])
                    # print(fund_worth_item["unit"])

                    fund_worth_item["ljjz"] = data.xpath("//*[@id='networth-table']/tbody/tr[%s]/td[3]/text()" %i)[0] if len(data.xpath("//*[@id='networth-table']/tbody/tr[%s]/td[3]/text()" %i))>0 else None
                    fund_worth_item["ljjz"] = Decimal(fund_worth_item["ljjz"])
                    # print(fund_worth_item["ljjz"])

                    fund_worth_item["ljjz1"] = data.xpath("//*[@id='networth-table']/tbody/tr[%s]/td[4]/text()" %i)[0] if len(data.xpath("//*[@id='networth-table']/tbody/tr[%s]/td[4]/text()" %i))>0 else None
                    fund_worth_item["ljjz1"] = Decimal(fund_worth_item["ljjz1"])
                    # print(fund_worth_item["ljjz1"])

                    fund_worth_item["jzbd"] = data.xpath("//*[@id='networth-table']/tbody/tr[%s]/td[5]/span/text()" %i)[0] if len(data.xpath("//*[@id='networth-table']/tbody/tr[%s]/td[5]/span/text()" %i))>0 else None
                    fund_worth_item["jzbd"] = Decimal(fund_worth_item["jzbd"].strip("%"))/100
                    # print(fund_worth_item["jzbd"])
                    # print(fund_worth_item)
                except Exception as e:
                    self.logger.debug("数据有误 %s" %e)

                else:
                    # print(fund_worth_item)
                    yield fund_worth_item


    #进入到公司详情页面
    def parse_company(self, response):
        # print(3)
        item = CompanyItem()
        item["company_id"] = response.meta["item"]['company_id']
        item["company_gsjc"] = response.meta["item"]["company_gsjc"]  #公司简称

        sel = Selector(response)

        item["company_name"] = sel.xpath("/html/body/div[5]/div[1]/div[1]/span/text()").extract()[0] if len(sel.xpath("/html/body/div[5]/div[1]/div[1]/span/text()").extract())>0 else None
        item["company_ljsy"] = sel.xpath("/html/body/div[5]/div[1]/div[1]/div[1]/div[1]/span/text()").extract()[0] if len(sel.xpath("/html/body/div[5]/div[1]/div[1]/div[1]/div[1]/span/text()").extract())>0 else None
        #代表产品id 后缀字段
        #有问题
        item["company_dbcp"] = re.findall(r'<a href="/product/(.*?).html',response.body.decode())[0]  if len(re.findall(r'<a href="/product/(.*?).html',response.body.decode())) > 0 else None
        
        item["company_birthday"] = sel.xpath("/html/body/div[5]/div[1]/div[1]/div[1]/div[3]/span/text()").extract()[0] if len(sel.xpath("/html/body/div[5]/div[1]/div[1]/div[1]/div[3]/span/text()").extract())>0 else None
        item["company_szdq"] = sel.xpath("/html/body/div[5]/div[1]/div[1]/div[1]/div[4]/span/text()").extract()[0] if len(sel.xpath("/html/body/div[5]/div[1]/div[1]/div[1]/div[4]/span/text()").extract())>0 else None
        item["company_jnsy"] = sel.xpath("/html/body/div[5]/div[1]/div[1]/div[1]/div[5]/span/text()").extract()[0] if len(sel.xpath("/html/body/div[5]/div[1]/div[1]/div[1]/div[5]/span/text()").extract())>0 else None
        item["company_qxjj"] = sel.xpath("/html/body/div[5]/div[1]/div[1]/div[1]/div[6]/span/text()").extract()[0] if len(sel.xpath("/html/body/div[5]/div[1]/div[1]/div[1]/div[6]/span/text()").extract())>0 else None
        item["company_babh"] = sel.xpath("/html/body/div[5]/div[1]/div[1]/div[1]/div[7]/span/text()").extract()[0] if len(sel.xpath("/html/body/div[5]/div[1]/div[1]/div[1]/div[7]/span/text()").extract())>0 else None
        item["company_hxrw"] = sel.xpath("/html/body/div[5]/div[1]/div[1]/div[1]/div[8]/div/a/text()").extract()
        item["company_hxrw"] = ",".join(item["company_hxrw"]).strip()

        item["company_gsjs"] = sel.xpath("//*[@id='tab-1-1']/div[3]/p//text()").extract()  #重点检查
        item["company_gsjs"] = "".join(item["company_gsjs"]).strip().replace("\n","").replace('space',"")
        # print(item["company_gsjs"])
       #投资理念
        item["company_tzln"] = sel.xpath("//*[@id='tab-1-3']/div/p//text()").extract() if len(sel.xpath("//*[@id='tab-1-3']/div/p/text()").extract())>0 else None  #有问题
        if item["company_tzln"]:
            item["company_tzln"] = [i.strip() for i in item["company_tzln"]]
            item["company_tzln"] = "".join(item["company_tzln"]).replace(" ","")
            # print("投资理念：%s" %item["company_tzln"])

        item["company_employ"] = sel.xpath("//*[@id='tab-1-2']/div[3]/div[1]/a/@href").extract()
        item["company_employ"] = item["company_employ"] if len(item["company_employ"]) > 0 else None
        # print(item)
        if item["company_employ"] is not None:
            for employ in item["company_employ"]:
                employ_url= "http://dc.simuwang.com" +str(employ)
                item["employ_id"] = str(employ).strip("/manager/").strip(".html")
#            print('fund_url', fund_url)
#            yield Request(company_url, callback=self.parse_company_detail)
                yield Request(url=employ_url,cookies=self.cookie, callback=self.parse_employ,meta={'item':deepcopy(item)})
        # print(item)
        yield item

    #进入经理详情页面
    def parse_employ(self,response):
        # print(4)
        item = EmployItem()
        item["company_id"] = response.meta["item"]["company_id"]
        item['employ_id'] = response.meta["item"]["employ_id"]
        sel = Selector(response)
        item["employ_name"] = sel.xpath("/html/body/div[5]/div[1]/div[1]/div[1]/span/text()").extract()[0] if len(sel.xpath("/html/body/div[5]/div[1]/div[1]/div[1]/span/text()"))>0 else None
        item["rwjs"] = sel.xpath('//*[@id="tab-1-1"]/div[3]/p//text()').extract()  #问题很大
        item["rwjs"] = "".join(item["rwjs"]).strip().replace("\n","").replace("space","")
        item["gszw"] = sel.xpath("/html/body/div[5]/div[1]/div[1]/div[2]/div[8]/span/text()").extract()[0] if len(sel.xpath("/html/body/div[5]/div[1]/div[1]/div[2]/div[8]/span/text()"))>0 else None
        item["cynx"] = sel.xpath("/html/body/div[5]/div[1]/div[1]/div[2]/div[10]/span/text()").extract()[0] if len(sel.xpath("/html/body/div[5]/div[1]/div[1]/div[2]/div[10]/span/text()"))>0 else None
        item["qxjj"] = sel.xpath("/html/body/div[5]/div[1]/div[1]/div[2]/div[11]/span/text()").extract()[0] if len(sel.xpath("/html/body/div[5]/div[1]/div[1]/div[2]/div[11]/span/text()"))>0 else None
        item["zybj"] = sel.xpath("/html/body/div[5]/div[1]/div[1]/div[2]/div[13]/span/text()").extract()[0] if len(sel.xpath("/html/body/div[5]/div[1]/div[1]/div[2]/div[13]/span/text()").extract())>0 else None
        #下面是代表产品url的后缀，需要拼接
        # item["dbcp_url"] = sel.xpath("/html/body/div[5]/div[1]/div[1]/div[2]/div[3]/a/@href").extract()[0] if len(sel.xpath("/html/body/div[5]/div[1]/div[1]/div[2]/div[3]/a/@href").extract())>0 else None

        item['dbcp'] =sel.xpath("/html/body/div[5]/div[1]/div[1]/div[2]/div[3]/a/span/text()").extract()[0] if len(sel.xpath("/html/body/div[5]/div[1]/div[1]/div[2]/div[3]/a/@href").extract())>0 else None

        # item["dbcp"] = item["dbcp"].replace("/product/","").replace(".html","")

        #item["zgxl"] = sel.xpath("/html/body/div[5]/div[1]/div[1]/div[2]/div[12]/span").extract()

        # print(item)
        yield item



