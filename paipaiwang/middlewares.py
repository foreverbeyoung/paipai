# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random
import re
from scrapy import signals
from scrapy.http import HtmlResponse
from fake_useragent import UserAgent
import time
import json
# from redis import StrictRedis
# from paipaiwang.settings import REDIS_HOST,REDIS_PORT
# from paipaiwang.Utils.mk_log import Logger
import logging
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
# from scrapy.exceptions import IgnoreRequest
from paipaiwang.Utils.proxy import get_proxy
# from paipaiwang.Utils import cookie_to_dict
from redis import StrictRedis
from paipaiwang.Utils.config import HOST_REDIS, PORT_REDIS, DB_REDIS_COOKIES, PASSWORD_REDIS
class RequestsChrometmiddware(object):              # 浏览器访问中间件

    def process_request(self, request, spider):     # 重写process_request请求方法
                    # if spider.name == 'PaiPaiSpider':                   # 判断爬虫名称为PaiPaiSpider时执行
        #
        if request.url == "https://dc.simuwang.com":
            spider.driver.get(request.url)
            spider.driver.implicitly_wait(40)
            time.sleep(5)
            spider.driver.delete_all_cookies()
            time.sleep(5)
            for cookie in spider.listCookies:
                spider.driver.add_cookie(cookie)
            time.sleep(3)
        #     spider.driver.maximize_window()
        #     spider.driver.get(request.url)         #用谷歌浏览器访问url
        #     spider.driver.implicitly_wait(60)
        #     user = spider.driver.find_element_by_xpath('//*[@id="登录注册首页-输入手机/用户名"]')
        #     user.send_keys(spider.phone_number)
        #     time.sleep(3)
        #     spider.driver.find_element_by_xpath('//*[@id="登录注册首页-下一步"]').click()
        #     # time.sleep(10)
        #     spider.driver.implicitly_wait(20)
        #     time.sleep(3)
        #     spider.driver.find_element_by_xpath('//*[@id="密码登录-输入密码2"]').send_keys(spider.password)
        #     time.sleep(3)
        #     spider.driver.find_element_by_xpath('//*[@id="密码登录-确认2"]').click()
        #     spider.driver.implicitly_wait(30)
        #     print('访问：{0}'.format(request.url))  # 打印访问网址
        #     #设置响应信息，由浏览器响应信息返回
        #     response = HtmlResponse(url=spider.driver.current_url, body=(spider.driver.page_source), encoding='utf-8', request=request)
        #     return response
            return HtmlResponse(url=spider.driver.current_url, body=(spider.driver.page_source), encoding='utf-8', request=request)
        #     # return HtmlResponse(url=spider.driver.current_url)
        #     # raise IgnoreRequest()
        if re.match(r'https://dc.simuwang.com/product/.*',request.url) is not None:
            # spider.driver.get(request.url)
            # spider.driver.implicitly_wait(40)
            #
            # spider.driver.delete_all_cookies()
            # for cookie in spider.listCookies:
            #     spider.driver.add_cookie(cookie)

            spider.driver.get(request.url)
            spider.driver.implicitly_wait(40)
            time.sleep(1)
            pages_source = []
            data_index = spider.driver.page_source
            pages_source.append(data_index)
            spider.driver.find_element_by_xpath('//*[@id="tab-1-1-one"]/div[1]/div[1]/a[2]').click()
            time.sleep(1)
            try:
                next_url = spider.driver.find_element_by_xpath('//*[@id="networth-table_pager"]/a[3]')
            except Exception as e:
                pass
            else:
                pages = spider.driver.find_element_by_xpath('//*[@id="networth-table_pager"]/a[4]').get_attribute("data-page")
                pages = int(pages)
                for i in range(pages-1):

                    spider.driver.find_element_by_xpath('//*[@id="networth-table_pager"]/a[3]').click()
                    spider.driver.implicitly_wait(10)
                    time.sleep(1)
                    data = spider.driver.page_source
                    pages_source.append(data)
            pages_source = json.dumps(pages_source)



            response = HtmlResponse(url=spider.driver.current_url, body= pages_source, encoding='utf-8',
                                    request=request)
            return response
class PaipaiwangSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self,response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self,response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self,response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self,start_requests,spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r
        pass
    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

class PaipaiwangDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
# class RandomUserAgentMiddleware(object):
#     # 随机跟换ua
#     def __init__(self, crawler):
#         super(RandomUserAgentMiddleware, self).__init__()
#         self.ua = UserAgent()
#         self.ua_type = crawler.settings.get("RANDOM_UA_TYPE", "random")
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         return cls(crawler)
#
#     def process_request(self, request, spider):
#         def get_ua():
#             return getattr(self.ua, self.ua_type)
#             request.headers.setdefault("User-Agent", get_ua())
#             # request.meta["proxy"] = proxies()
class RandomUserAgentMiddleware(UserAgentMiddleware):
    #随机跟换ua
    def __init__(self,user_agent):
        super().__init__()
        self.user_agent = user_agent

    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            user_agent=crawler.settings.get("USER_AGENT_LIST")
        )

    def process_request(self,request,spider):
        agent = random.choice(self.user_agent)
        request.headers["User-Agent"] =agent
        logging.debug("CURRENT_USER_AGENT: {}".format(agent))
        # request.headers["Authorization"] = get_auth()
        # cookies = ['guest_id=1525751430; _9755xjdesxxd_=32; gdxidpyhxdE=L65QW%2F9x%5CNMfIgwrr9%5CPCeAP6JiXys33b%2BgMIxUi6invds%2BE%2FHA44xt%2FzeUQeXGuqbbZkItEJI1Plafgkqg3K%5C0awLqcQLl830tyLr1cjnqRi29ny1QwOjLOHaNcRR9Aw3V59V2pqLscz%2FoMHvwi9Pauicme0nZPEGnb4ckWr3REiPqt%3A1538272775074; certification=1; qualified_investor=1; evaluation_result=5; focus-certification-pop=-1; PHPSESSID=u3pgn8qnl3akdhmdr1gu9da3k0; sensro_profile_has_set=1; Hm_lvt_c3f6328a1a952e922e996c667234cdae=1538212651,1538270493,1538275688; stat_sessid=jh9n5j8gha1tg12fjom5c3pmg4; regsms=1538977237000; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22582653%22%2C%22%24device_id%22%3A%22166249e61a4c78-053fac6ad761df-346d7809-2073600-166249e61a58b7%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22582653%22%7D; rz_token_6658=3b62890de15a2e170219d48b79d62345.1539050196; http_tK_cache=f2974e07c2c384b563dd1be8370c794ffce4c0e0; cur_ck_time=1539050198; ck_request_key=si9lkzlY3ti6ao9gMFvm%2B71tVf6Zuy7kfdY%2FebBmyoU%3D; passport=582653%09u7053690600037%09UFAAAFNUCwRRAgsDUgZRCV0BUQEAXQRTVQcGBgwFBQc%3D80c9900986; rz_u_p=d41d8cd98f00b204e9800998ecf8427e%3Du7053690600037; rz_rem_u_p=wfBnseEHc9Bhh%2FiLr8OhpcqlSGnMhrXjWpPqR5GJ7n4%3D%24Yf8XTznM89ixhCXODURjAtBjU6gI6w2owrLbuQYZ7bI%3D; autologin_status=0; Hm_lpvt_c3f6328a1a952e922e996c667234cdae=1539050233']
        # cookie =random.choice(cookies)
        # cookie = 'guest_id=1525751430; _9755xjdesxxd_=32; gdxidpyhxdE=L65QW%2F9x%5CNMfIgwrr9%5CPCeAP6JiXys33b%2BgMIxUi6invds%2BE%2FHA44xt%2FzeUQeXGuqbbZkItEJI1Plafgkqg3K%5C0awLqcQLl830tyLr1cjnqRi29ny1QwOjLOHaNcRR9Aw3V59V2pqLscz%2FoMHvwi9Pauicme0nZPEGnb4ckWr3REiPqt%3A1538272775074; certification=1; qualified_investor=1; evaluation_result=5; focus-certification-pop=-1; PHPSESSID=u3pgn8qnl3akdhmdr1gu9da3k0; sensro_profile_has_set=1; Hm_lvt_c3f6328a1a952e922e996c667234cdae=1538212651,1538270493,1538275688; stat_sessid=jh9n5j8gha1tg12fjom5c3pmg4; regsms=1538977237000; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22582653%22%2C%22%24device_id%22%3A%22166249e61a4c78-053fac6ad761df-346d7809-2073600-166249e61a58b7%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22582653%22%7D; rz_token_6658=3b62890de15a2e170219d48b79d62345.1539050196; http_tK_cache=f2974e07c2c384b563dd1be8370c794ffce4c0e0; cur_ck_time=1539050198; ck_request_key=si9lkzlY3ti6ao9gMFvm%2B71tVf6Zuy7kfdY%2FebBmyoU%3D; passport=582653%09u7053690600037%09UFAAAFNUCwRRAgsDUgZRCV0BUQEAXQRTVQcGBgwFBQc%3D80c9900986; rz_u_p=d41d8cd98f00b204e9800998ecf8427e%3Du7053690600037; rz_rem_u_p=wfBnseEHc9Bhh%2FiLr8OhpcqlSGnMhrXjWpPqR5GJ7n4%3D%24Yf8XTznM89ixhCXODURjAtBjU6gI6w2owrLbuQYZ7bI%3D; autologin_status=0; Hm_lpvt_c3f6328a1a952e922e996c667234cdae=1539050233'
        #
        # request.cookies =cookie
# class ProxyMiddleware(object):
#     def process_request(self, request, spider):
#         request.meta['proxy'] = "https://" + get_peoxies()
class RandomProxyMiddleware(object):
    def __init__(self, crawler):
        # self.proxy_mode = getattr(crawler.spider, 'proxy_mode', False)
        # self.spider_name = crawler.spider.name
        self.first_time = -15
        self.proxy_list = []

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def process_request(self, request, spider):
        request.dont_filter = True
        # if self.proxy_mode:
        cur_time = time.time()
        span = cur_time - self.first_time
        if span > 10:
            self.first_time = cur_time

            self.proxy_list = get_proxy()
        if self.proxy_list:
            proxy = random.choice(self.proxy_list)
            request.meta.update({'proxy': proxy})
        else:
            print('IP池已空')

    def process_exception(self, request, exception, spider):
        exception_name = exception.__class__.__name__
        spider.logger.error('({}: {}) {}'.format(exception_name, request.url, exception))
        return request.replace(dont_filter=True)
#

class RandomCookiesMiddleware(object):
    def __init__(self, crawler):
        self.first_time = 0
        self.spider_name = crawler.spider.name
        self.cookies_enable = crawler.settings.getbool('COOKIES_ENABLED')
        self.conn = StrictRedis(host= HOST_REDIS, port=PORT_REDIS, db= DB_REDIS_COOKIES, decode_responses=True)  # cookie池
        self.cookies = self.conn.keys()

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def process_request(self, request, spider):
        if self.cookies_enable:
            cur_time = time.time()
            span = cur_time - self.first_time
            if span > 3600*6:
                self.first_time = cur_time
                self.cookies = self.conn.keys(self.spider_name)
            if self.cookies:
                selenium_cookie = random.choice(self.cookies)
                selenium_cookie =eval(selenium_cookie)
                # cookie = 'mds_u_s_cn=%5Cu5f7c%5Cu56fe%5Cu6069;_ga=GA1.2.2055015572.1522221785;unick=jiangxiaoping%40p2n-w.com;mds_u_cn=%5Cu6df1%5Cu5733%5Cu5e02%5Cu5f7c%5Cu56fe%5Cu6069%5Cu79d1%5Cu6280%5Cu6709%5Cu9650%5Cu516c%5Cu53f8;user_trace_token=20180328152259-a0f876ff-28e3-4f75-9929-886244584b79;LG_LOGIN_USER_ID=72c6bf03df259b3fc791436d4ce23e1694eab749dbee73c6;login=true;LGUID=20180328152310-deac44b6-3258-11e8-b652-5254005c3644;gray=resume;gate_login_token=a52d9889668bd1f1a06c03294380e12959d3026cfa82d632;_putrc=4113EEF5FBCD3C56;PRE_LAND=https%3A%2F%2Fpassport.lagou.com%2Flogin%2Flogin.html;PRE_SITE=;LGRID=20180328152310-deac444b-3258-11e8-b652-5254005c3644;_gid=GA1.2.579102704.1522221785;PRE_HOST=;mds_u_ci=90320;mds_login_authToken="OyvQy2B1eWDYArlGJ3Te2fUm57gKlMn3IBNHfr6/VrnfZ/7x43wmmQjQmdRtU1s0Nc7WKuRRuBrZDSWkG/ICGaEwCFr+7hyWcr2b8PwQlDtR+mHaL+7pIRRLu0+mfgIGPyo/kfiFHGjXQAPI9a/mXw4hHFG0KxxICAD3ZwYcj914rucJXOpldXhUiavxhcCELWDotJ+bmNVwmAvQCptcy5e7czUcjiQC32Lco44BMYXrQ+AIOfEccJKHpj0vJ+ngq/27aqj1hWq8tEPFFjdnxMSfKgAnjbIEAX3F9CIW8BSiMHYmPBt7FDDY0CCVFICHr2dp5gQVGvhfbqg7VzvNsw==";_gat=1;mds_u_n=%5Cu674e%5Cu7acb%5Cu5f3a;JSESSIONID=ABAAABAABIDABIC9635B0D69B8F51655DD00D4EC2AB66DC;Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1522221786;PRE_UTM=;Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1522221786;X_HTTP_TOKEN=7433e6166ce03d4b0beca0514952318e;LGSID=20180328152310-deac42c0-3258-11e8-b652-5254005c3644;'
                if re.match(r'https://dc.simuwang.com/product/.*',request.url) is not None:

                    spider.listCookies  = selenium_cookie

                else:
                    # request.cookies = cookie_to_dict(selenium_cookie)

                    cookie = [item["name"] + ":" + item["value"] for item in selenium_cookie]
                    cookies_dict = {}
                    for elem in cookie:
                        str = elem.split(':')
                        cookies_dict[str[0]] = str[1]
                request.cookies = cookies_dict
                logging.debug("CURRENT_COOKIE: {}".format(selenium_cookie))
            # else:
            #     print('cookies池为空')

