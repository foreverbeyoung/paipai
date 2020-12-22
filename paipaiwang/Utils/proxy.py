#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import time
import json

import requests
from redis import StrictRedis
# from paipaiwang.settings import REDIS_HOST, REDIS_PORT


# db3 = StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=3, decode_responses=True)  # ip池


#调用的代理
url_api = 'http://api.ip.data5u.com/dynamic/get.html?order=465b3681d3b443be48528d24a62c2565&random=true&sep=3'

#
# def get_proxy():
#     proxy_list = []
#     r = requests.get(url=url_api, timeout=15)
#     result = r.text.r


    # return proxy_list


def get_proxy():
    try:
        r = requests.get(url=url_api, timeout=15)
        result = r.text.replace('b', '').replace('\n', '')
        proxy = "http://{}".format(result)
    except:
        pass
    else:
        if proxy:
            proxy_list = []

            proxy_list.append(proxy)

            print(proxy_list)
            return proxy_list


if __name__ == '__main__':
    while True:
        get_proxy()
        time.sleep(10)






