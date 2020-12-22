# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
#
# # 格式转换工具
# from pprint import pprint
#
# # time.sleep(3)
# # # 登录成功之后，获取到selenium的cookie
# # cookie = [item["name"] + ":" + item["value"] for item in seleniumCookies]
# # cookMap = {}
# # for elem in cookie:
# #     str = elem.split(':')
# #     cookMap[str[0]] = str[1]
# # print(f"cookMap = {cookMap}")
# # # 中间件，对Request进行加工
# # # 开始用这个转换后的cookie重新构造Request，从源码中来看Request构造的原型
# # # E:\Miniconda\Lib\site-packages\scrapy\http\request\__init__.py
# # cookies = cookMap  # 让这个带有登录后cookie的Request继续爬取
# # return cookies
# def cookie_to_dict(value):
#     if isinstance(value, str):
#         value = eval(value)
#         cookie = [item["name"] + ":" + item["value"] for item in value]
#         cookies = {}
#         for elem in cookie:
#             str = elem.split(':')
#             cookies[str[0]] = str[1]
#
#         # cookies = {}
#         # for i in value.split(';'):
#         #     if i.strip():
#         #         kv = i.replace('"', '').split('=', 1)
#         #         if '|' in kv[-1]:
#         #             cookies.update({kv[0].strip(): {j.split('=', 1)[0].strip(): j.split('=', 1)[-1].strip() for j in kv[-1].split('|')}})
#         #         else:
#         #             cookies.update({kv[0].strip(): kv[-1].strip()})
#         return cookies
#     elif isinstance(value, dict):
#         return value
#     else:
#         raise ValueError('value is not str or dict')
#
#
# def header_to_dict(value):
#     if isinstance(value, str):
#         headers = {}
#         for i in value.split('\n'):
#             if i.strip():
#                 kv = i.split(':', 1)
#                 headers.update({kv[0].strip(): kv[-1].strip()})
#         return headers
#     else:
#         return value
