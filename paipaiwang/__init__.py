# import requests
# # headers = {
# #             'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13.',
# #             'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
# #             'Accept-Encoding': 'gzip, deflate',
# #             'Accept - Language': 'zh - CN, zh;q = 0.8',
# #             'Host': 'dc.simuwang.com',
# #             'Referer': 'http://dc.simuwang.com',
# #             'X - Requested - With': 'XMLHttpRequest',
# #         }
# page=1
# ticket='7ced4882c35682a0b570d86f5d7707fd'
# data={
#     'curpage':page,
#     'ticket':ticket,
#     'ptype':"qmp_pc",
#     'version':"1.0",
#     'unionid':"oP3fkwCIIGM082hz48KnF9RxoR-o"
# }
# headers = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#     "Accept-Encoding": "gzip, deflate",
#     "Accept-Language": "en-US,en;q=0.5",
#     "Connection": "keep-alive",
#     "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0"}
# # url = "https://dc.simuwang.com/company/CO000002AT.html"
# # response = requests.get(url=url)
# # print(response)
# html = requests.post('http://qimingpian.com/h/jigous',data=data,headers=headers).text
# print(html)


