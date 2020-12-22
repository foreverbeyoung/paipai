# -*- coding: utf-8 -*-

# Scrapy settings for paipaiwang project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random
BOT_NAME = 'paipaiwang'

SPIDER_MODULES = ['paipaiwang.spiders']
NEWSPIDER_MODULE = 'paipaiwang.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13.'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32
LOG_LEVEL = 'DEBUG'
# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 1     #设置下载缓存时间
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16
# COOKIE ={'guest_id': '1525751430', '_9755xjdesxxd_': '32', 'gdxidpyhxdE': 'L65QW%2F9x%5CNMfIgwrr9%5CPCeAP6JiXys33b%2BgMIxUi6invds%2BE%2FHA44xt%2FzeUQeXGuqbbZkItEJI1Plafgkqg3K%5C0awLqcQLl830tyLr1cjnqRi29ny1QwOjLOHaNcRR9Aw3V59V2pqLscz%2FoMHvwi9Pauicme0nZPEGnb4ckWr3REiPqt%3A1538272775074', 'certification': '1', 'qualified_investor': '1', 'evaluation_result': '5', 'focus-certification-pop': '-1', 'regsms': '1538977237000', 'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%22582653%22%2C%22%24device_id%22%3A%22166249e61a4c78-053fac6ad761df-346d7809-2073600-166249e61a58b7%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22582653%22%7D', 'Hm_lvt_c3f6328a1a952e922e996c667234cdae': '1538212651,1538270493,1538275688,1539134991', 'rz_token_6658': '0d6d139d1431a0b561112d80fd474d9f.1539134991', 'http_tK_cache': '2ade8e491e5b4bda3544c11555dac723c5cef008', 'cur_ck_time': '1539134993', 'ck_request_key': 'Wbku8kJhP6nCHU7E9muEKMq1XlSCeCujruUTHQ%2B0Al8%3D', 'passport': '582653%09u7053690600037%09UFAAAFNUCwRRAgsDUgZRCV0BUQEAXQRTVQcGBgwFBQc%3D80c9900986', 'rz_u_p': 'd41d8cd98f00b204e9800998ecf8427e%3Du7053690600037', 'rz_rem_u_p': 'wfBnseEHc9Bhh%2FiLr8OhpcqlSGnMhrXjWpPqR5GJ7n4%3D%24Yf8XTznM89ixhCXODURjAtBjU6gI6w2owrLbuQYZ7bI%3D', 'sensro_profile_has_set': '1', 'autologin_status': '0', 'stat_sessid': 't9mmqlqabqv02ut8bq9nj377f1', 'PHPSESSID': 'c6lmaaju12nvjf78gnfrjvl2p1', 'Hm_lpvt_c3f6328a1a952e922e996c667234cdae': '1539135056'}
COOKIE ={'smppw_tz_auth': '1', 'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%22582653%22%2C%22%24device_id%22%3A%221667549a16e319-0a31ee0230460b-346d7809-2073600-1667549a1707dd%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22582653%22%7D', 'evaluation_result': '5', 'qualified_investor': '1', 'focus-certification-pop': '-1', 'rz_u_p': 'd41d8cd98f00b204e9800998ecf8427e%3Du7053690600037', 'passport': '582653%09u7053690600037%09UFAAAFNUCwRRAgsDUgZRCV0BUQEAXQRTVQcGBgwFBQc%3D80c9900986', 'cur_ck_time': '1539566069', 'http_tK_cache': 'bc64c956b55dacdc17a81190e6661af6d08c9acb', 'PHPSESSID': 'n3mojf4kkhuag56l94dq2k2bh1', 'stat_sessid': '236lj9c1nlpfk23235oi32k5e4', 'regsms': '1539566051000', 'Hm_lpvt_c3f6328a1a952e922e996c667234cdae': '1539566052', '_9755xjdesxxd_': '32', 'certification': '1', 'Hm_lvt_c3f6328a1a952e922e996c667234cdae': '1539566052', 'rz_rem_u_p': 'wfBnseEHc9Bhh%2FiLr8OhpcqlSGnMhrXjWpPqR5GJ7n4%3D%24Yf8XTznM89ixhCXODURjAtBjU6gI6w2owrLbuQYZ7bI%3D', 'rz_token_6658': '503063e7e2bedd751f91d56dc4808d78.1539566051', 'gdxidpyhxdE': 'uzO7%5CETjX6WKQpJ%2F1%5CEJjyrzPRO3Yxn5K61Clnaq%2B512v9jdmwl3oEnTGxHI9iwEVVm%2BHhNYbMetGYk%2B7fLHO7b0aeYT9tekOTJ8deRENznYTVngU85nPu93SVRKLS341b2NhtzjgqK%2BZf%2Ft2G9fgT5ObzEBWjHeRST1y2Y7cJCKHx9G%3A1539566955357', 'sajssdk_2015_cross_new_user': '1', 'ck_request_key': 'kn87%2FCiA0m1zUQ7CtvpyAaSsvqAerHTQnwWRU278D2o%3D', 'guest_id': '1526972159'}


# LIST_COOKIES = [{'domain': '.simuwang.com', 'httpOnly': False, 'name': 'autologin_status', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.simuwang.com', 'httpOnly': False, 'name': 'Hm_lpvt_c3f6328a1a952e922e996c667234cdae', 'path': '/', 'secure': False, 'value': '1539064558'}, {'domain': 'dc.simuwang.com', 'expiry': 1539066333, 'httpOnly': False, 'name': 'fyr_ssid_n5776', 'path': '/', 'secure': False, 'value': 'fyr_n5776_jn1ba3y7'}, {'domain': '.simuwang.com', 'expiry': 1539669332, 'httpOnly': False, 'name': 'smppw_tz_auth', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.simuwang.com', 'expiry': 1539928531.998647, 'httpOnly': False, 'name': 'rz_u_p', 'path': '/', 'secure': False, 'value': 'd41d8cd98f00b204e9800998ecf8427e%3Du7053690600037'}, {'domain': '.simuwang.com', 'expiry': 7846264558, 'httpOnly': False, 'name': 'sensorsdata2015jssdkcross', 'path': '/', 'secure': False, 'value': '%7B%22distinct_id%22%3A%22582653%22%2C%22%24device_id%22%3A%221665764efde108-0c438b67462f5b-346d7809-2073600-1665764efdf8c1%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22582653%22%7D'}, {'domain': '.simuwang.com', 'expiry': 1539928531.998816, 'httpOnly': False, 'name': 'evaluation_result', 'path': '/', 'secure': False, 'value': '5'}, {'domain': '.simuwang.com', 'expiry': 1539928531.998761, 'httpOnly': False, 'name': 'qualified_investor', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.simuwang.com', 'expiry': 1539928531.998849, 'httpOnly': False, 'name': 'focus-certification-pop', 'path': '/', 'secure': False, 'value': '-1'}, {'domain': '.simuwang.com', 'httpOnly': False, 'name': 'sensro_profile_has_set', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.simuwang.com', 'expiry': 1539928525, 'httpOnly': False, 'name': 'regsms', 'path': '/', 'secure': False, 'value': '1539064525000'}, {'domain': '.simuwang.com', 'expiry': 1539928531.998627, 'httpOnly': False, 'name': 'passport', 'path': '/', 'secure': False, 'value': '582653%09u7053690600037%09UFAAAFNUCwRRAgsDUgZRCV0BUQEAXQRTVQcGBgwFBQc%3D80c9900986'}, {'domain': 'dc.simuwang.com', 'httpOnly': False, 'name': 'PHPSESSID', 'path': '/', 'secure': False, 'value': '2vgdjadfctrmf4t9mujlsbth27'}, {'domain': '.simuwang.com', 'expiry': 1539928531.998432, 'httpOnly': False, 'name': 'cur_ck_time', 'path': '/', 'secure': False, 'value': '1539064534'}, {'domain': '.simuwang.com', 'expiry': 1539065965, 'httpOnly': False, 'name': 'rz_token_6658', 'path': '/', 'secure': False, 'value': 'e61c2f089574254dc2b6d90e107cde5f.1539064525'}, {'domain': '.simuwang.com', 'expiry': 1539928531.998559, 'httpOnly': False, 'name': 'http_tK_cache', 'path': '/', 'secure': False, 'value': '0442c0ee23cf7f4e9de748f0647ad93fc8273fad'}, {'domain': 'dc.simuwang.com', 'expiry': 1696745428, 'httpOnly': False, 'name': '_9755xjdesxxd_', 'path': '/', 'secure': False, 'value': '32'}, {'domain': '.simuwang.com', 'expiry': 1539928531.998484, 'httpOnly': False, 'name': 'ck_request_key', 'path': '/', 'secure': False, 'value': 'zmKNxhPB%2BKhme%2BTXsI613QIUopZ%2B2VsRwNTIM%2F0Vx9g%3D'}, {'domain': '.simuwang.com', 'expiry': 1539100799, 'httpOnly': False, 'name': 'sajssdk_2015_cross_new_user', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.simuwang.com', 'expiry': 1539928531.998726, 'httpOnly': False, 'name': 'certification', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.simuwang.com', 'expiry': 1570600558, 'httpOnly': False, 'name': 'Hm_lvt_c3f6328a1a952e922e996c667234cdae', 'path': '/', 'secure': False, 'value': '1539064525'}, {'domain': '.simuwang.com', 'httpOnly': False, 'name': 'stat_sessid', 'path': '/', 'secure': False, 'value': '0s1c65pag19lvjqhgj19untiq6'}, {'domain': '.simuwang.com', 'expiry': 1539928531.998671, 'httpOnly': False, 'name': 'rz_rem_u_p', 'path': '/', 'secure': False, 'value': 'wfBnseEHc9Bhh%2FiLr8OhpcqlSGnMhrXjWpPqR5GJ7n4%3D%24Yf8XTznM89ixhCXODURjAtBjU6gI6w2owrLbuQYZ7bI%3D'}, {'domain': 'dc.simuwang.com', 'expiry': 1696745428, 'httpOnly': False, 'name': 'gdxidpyhxdE', 'path': '/', 'secure': False, 'value': 'UfXmPr3706QVzsV%5CzLo013%2FS%2BL%2FpV2%5CGJKSToZ3nSdmi3%2B7PjQuwIS5LJB0BKIfMZn0ej7%5Cr2vqtSqIqxRc%2B%2Btn6%2F3vA86mwEUYL9%5CT6w9bkGwCOtn8dYyqxuOvInLviYBcaU9D6Yga%2B9AkgiE8eXqADzJZ5IvRw0iqU%2BC%5CQx%5CxnZ3Kc%3A1539065428599'}, {'domain': '.simuwang.com', 'expiry': 1570600524.495628, 'httpOnly': False, 'name': 'guest_id', 'path': '/', 'secure': False, 'value': '1526711257'}]
LIST_COOKIES =  [{'domain': '.simuwang.com', 'expiry': 1540204472, 'httpOnly': False, 'name': 'smppw_tz_auth', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.simuwang.com', 'expiry': 7846799672, 'httpOnly': False, 'name': 'sensorsdata2015jssdkcross', 'path': '/', 'secure': False, 'value': '%7B%22distinct_id%22%3A%22586581%22%2C%22%24device_id%22%3A%22166774a3b0d268-03188ef996f2bd-346d7809-2073600-166774a3b0e64a%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22586581%22%7D'}, {'domain': '.simuwang.com', 'expiry': 1540463672.876262, 'httpOnly': False, 'name': 'evaluation_result', 'path': '/', 'secure': False, 'value': '3'}, {'domain': '.simuwang.com', 'expiry': 1540463672.87624, 'httpOnly': False, 'name': 'qualified_investor', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.simuwang.com', 'expiry': 1540463672.876304, 'httpOnly': False, 'name': 'focus-certification-pop', 'path': '/', 'secure': False, 'value': '-1'}, {'domain': '.simuwang.com', 'expiry': 1540463672.876159, 'httpOnly': False, 'name': 'rz_u_p', 'path': '/', 'secure': False, 'value': 'd41d8cd98f00b204e9800998ecf8427e%3Du2353803396664'}, {'domain': '.simuwang.com', 'expiry': 1540463672.876138, 'httpOnly': False, 'name': 'passport', 'path': '/', 'secure': False, 'value': '586581%09u2353803396664%09D1EGUQsBBgYOU1EFBwcAAQFSWVEHAFEEDQ8EV1NRAAc%3D68d7217aa2'}, {'domain': '.simuwang.com', 'expiry': 1540463672.876039, 'httpOnly': False, 'name': 'cur_ck_time', 'path': '/', 'secure': False, 'value': '1539599674'}, {'domain': '.simuwang.com', 'expiry': 1540463672.876083, 'httpOnly': False, 'name': 'http_tK_cache', 'path': '/', 'secure': False, 'value': '3d9590ff1c3a1e0e725eb0cc93199edd5a891002'}, {'domain': '.simuwang.com', 'httpOnly': False, 'name': 'Hm_lpvt_c3f6328a1a952e922e996c667234cdae', 'path': '/', 'secure': False, 'value': '1539599651'}, {'domain': 'dc.simuwang.com', 'expiry': 1697280561, 'httpOnly': False, 'name': '_9755xjdesxxd_', 'path': '/', 'secure': False, 'value': '32'}, {'domain': '.simuwang.com', 'expiry': 1540463672.876205, 'httpOnly': False, 'name': 'certification', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.simuwang.com', 'expiry': 1571135650, 'httpOnly': False, 'name': 'Hm_lvt_c3f6328a1a952e922e996c667234cdae', 'path': '/', 'secure': False, 'value': '1539599651'}, {'domain': '.simuwang.com', 'httpOnly': False, 'name': 'stat_sessid', 'path': '/', 'secure': False, 'value': 'h8453hg4jv3ogje6ogupiudvg0'}, {'domain': '.simuwang.com', 'expiry': 1540463649, 'httpOnly': False, 'name': 'regsms', 'path': '/', 'secure': False, 'value': '1539599649000'}, {'domain': 'dc.simuwang.com', 'httpOnly': False, 'name': 'PHPSESSID', 'path': '/', 'secure': False, 'value': 'l2a16trgoqfq8d8rsplj2bjla4'}, {'domain': '.simuwang.com', 'expiry': 1540463672.876062, 'httpOnly': False, 'name': 'ck_request_key', 'path': '/', 'secure': False, 'value': '2UzHFT6xm5v8bmCY80KWngrjzVv3slT6Nm8%2BYj4QYNI%3D'}, {'domain': '.simuwang.com', 'expiry': 1571135645.730489, 'httpOnly': False, 'name': 'guest_id', 'path': '/', 'secure': False, 'value': '1526988814'}, {'domain': '.simuwang.com', 'expiry': 1540463672.876182, 'httpOnly': False, 'name': 'rz_rem_u_p', 'path': '/', 'secure': False, 'value': 'bqpvPtrlEaxuUG906fYzDFKjdTrJLEQtL4H6wyXS%2BO8%3D%24SejZYxPR1NQ9TmDNW0bN4bnq30qP1mm7uC4HHaL9X9g%3D'}, {'domain': '.simuwang.com', 'expiry': 1539601089, 'httpOnly': False, 'name': 'rz_token_6658', 'path': '/', 'secure': False, 'value': '9bb8fbcbcaa5fac4354b73659ba67cb0.1539599649'}, {'domain': 'dc.simuwang.com', 'expiry': 1697280561, 'httpOnly': False, 'name': 'gdxidpyhxdE', 'path': '/', 'secure': False, 'value': '%2BpEVCvYcnRInAw1XZKVhACh%2BMdSogb91h3vaUkWA235yqfyGMRgD1%2B7Ac8JPNEmXAEg7ifGmIZTBS9GowQrsZ5bK%2BVhnN%2FDxvpvwaAEWBlofADMUMG%2BRqSn%2BqKP5szszRu7DcqCn7%5CUY5tmD4%2F64OsGVivo5lKigxaXX4eI6e4zEbMqP%3A1539600561034'}, {'domain': '.simuwang.com', 'expiry': 1539619199, 'httpOnly': False, 'name': 'sajssdk_2015_cross_new_user', 'path': '/', 'secure': False, 'value': '1'}]


# Disable cookies (enabled by default)
COOKIES_ENABLED = True
# COOKIES_DEBUG = True   #记录scrapy每次的cookie
# COOKIES_ENABLES = False
# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept - Language': 'zh - CN, zh;q = 0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'dc.simuwang.com',
        'Upgrade-Insecure-Requests': '1',
        # 'Referer': 'https://dc.simuwang.com',
        # 'X - Requested - With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13.',
    #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    # 'Cookie': 'guest_id=1525751430; _9755xjdesxxd_=32; gdxidpyhxdE=L65QW%2F9x%5CNMfIgwrr9%5CPCeAP6JiXys33b%2BgMIxUi6invds%2BE%2FHA44xt%2FzeUQeXGuqbbZkItEJI1Plafgkqg3K%5C0awLqcQLl830tyLr1cjnqRi29ny1QwOjLOHaNcRR9Aw3V59V2pqLscz%2FoMHvwi9Pauicme0nZPEGnb4ckWr3REiPqt%3A1538272775074; certification=1; qualified_investor=1; evaluation_result=5; focus-certification-pop=-1; PHPSESSID=u3pgn8qnl3akdhmdr1gu9da3k0; sensro_profile_has_set=1; Hm_lvt_c3f6328a1a952e922e996c667234cdae=1538212651,1538270493,1538275688; stat_sessid=jh9n5j8gha1tg12fjom5c3pmg4; regsms=1538977237000; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22582653%22%2C%22%24device_id%22%3A%22166249e61a4c78-053fac6ad761df-346d7809-2073600-166249e61a58b7%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22582653%22%7D; rz_token_6658=3b62890de15a2e170219d48b79d62345.1539050196; http_tK_cache=f2974e07c2c384b563dd1be8370c794ffce4c0e0; cur_ck_time=1539050198; ck_request_key=si9lkzlY3ti6ao9gMFvm%2B71tVf6Zuy7kfdY%2FebBmyoU%3D; passport=582653%09u7053690600037%09UFAAAFNUCwRRAgsDUgZRCV0BUQEAXQRTVQcGBgwFBQc%3D80c9900986; rz_u_p=d41d8cd98f00b204e9800998ecf8427e%3Du7053690600037; rz_rem_u_p=wfBnseEHc9Bhh%2FiLr8OhpcqlSGnMhrXjWpPqR5GJ7n4%3D%24Yf8XTznM89ixhCXODURjAtBjU6gI6w2owrLbuQYZ7bI%3D; autologin_status=0; Hm_lpvt_c3f6328a1a952e922e996c667234cdae=1539050233'

}

USER_AGENT_LIST = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
]
USER_AGENT = random.choice(USER_AGENT_LIST)
# Override the default request headers:

# RANDOM_UA_TYPE ="random"
# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
   'paipaiwang.middlewares.PaipaiwangSpiderMiddleware': 600,
}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': None,
   # 'paipaiwang.proxy_middleware.ProxyMiddleWare': 125,
   'paipaiwang.middlewares.RequestsChrometmiddware': 300,
   "scrapy.downloadermiddlewares.useragent.UserAgentMiddleware" : None,
    # 'scrapy.downloadermiddleware.httpproxy.HttpProxyMiddleware': None,
    # 'paipaiwang.middlewares.RandomProxyMiddleware': 110,
   'paipaiwang.middlewares.RandomUserAgentMiddleware': 200,
   'paipaiwang.middlewares.PaipaiwangDownloaderMiddleware': 543,
   # 'paipaiwang.middlewares.ProxyMiddleware': 400,
    
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'paipaiwang.pipelines.PaipaiwangPipeline': 700,
'scrapy_redis.pipelines.RedisPipeline': 800,

}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# REDIS_URL = "redis://127.0.0.1:6379"
REDIS_HOST = "redis://127.0.0.1"
REDIS_PORT = 6379
# 添加 Redis 缓存url链接,防止爬取丢失
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
SCHEDULER_PERSIST = True
MYSQL_HOST = "192.168.1.79"
MYSQL_DATABASE = "simu"
MYSQL_PORT = 3306
MYSQL_USER = "root"
MYSQL_PASSWORD = 'password'
MYSQL_CHARSET = 'utf8mb4'

# MYSQL_HOST = "127.0.0.1"
# MYSQL_DATABASE = "test2"
# MYSQL_PORT = 3306
# MYSQL_USER = "root"
# MYSQL_PASSWORD = ''
# MYSQL_CHARSET = 'utf8mb4'

STMP_HOST = 'smtpdm.aliyun.com'
STMP_PORT = 25
STMP_USER = 'admin@mail.mojotv.cn'
STMP_PASSWORD = 'ZHou19871214'