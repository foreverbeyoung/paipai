from scrapy import cmdline
# from paipaiwang.spiders.cookies_pool import GetCookies,redis_client
# import time
cmdline.execute("scrapy crawl PaiPaiSpider".split())

# import multiprocessing
#
# def cookies_get():
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
#
#
#
# def spider_paipai():
#
#     cmdline.execute("scrapy crawl PaiPaiSpider".split())
#
#
# if __name__ == "__main__":
#     p1 = multiprocessing.Process(target= cookies_get())
#     p2 = multiprocessing.Process(target=spider_paipai())
#
#     p1.start()
#     p2.start()
