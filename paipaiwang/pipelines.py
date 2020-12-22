# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
# import json
# import codecs
#
import pymysql
from paipaiwang.settings import MYSQL_HOST,MYSQL_PASSWORD,MYSQL_USER,MYSQL_PORT,MYSQL_DATABASE
from paipaiwang.items import FundItem,Fund_worthItem,CompanyItem,EmployItem

class PaipaiwangPipeline(object):


    def __init__(self):
        self.cur =pymysql.connect(host=MYSQL_HOST,port=MYSQL_PORT,user=MYSQL_USER,password=MYSQL_PASSWORD,database=MYSQL_DATABASE)
        self.conn = self.cur.cursor()
    def process_item(self, item, spider):
        # print(item)
        if isinstance(item,FundItem):
            # print( "insert into fund (manager_id,company_id,name,rzpj,jjjl,paiming,cpmc,tzgw,jjglr,jjtgr,wbjgf,zqjjs,qhjjs,birthday,yxzt,cplx,csgm,tzcl,sffj,sfsx,rgqd,zjqd,fbq,kfr,rgfl,shfl,shflsm,glfl,yjx,zsx,yjbc,cxqx,babh,plbs,fund_id) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)",
            #     (item['manager_id'], item['company_id'], item["fund_name"], item['rzpj'], item['jjjl'],
            #      item['paiming'],item['cpmc'],item['tzgw'],item['jjglr'],item['jjtgr'],item['wbjgf'],item['zqjjs'],item['qhjjs'],item['birthday'],item['yxzt'], item['cplx'], item['csgm'], item['tzcl'], item['sffj'], item['sfsx'], item['rgqd'], item['zjqd'], item['fbq'], item['kfr'], item['rgfl'], item['shfl'], item['shflsm'], item['glfl'], item['yjx'], item['zsx'], item['yjbc'], item['cxqx'], item['babh'], item['plbs'],item['fund_id']))

            self.conn.execute(
                "insert into fund (manager_id,company_id,name,rzpj,jjjl,paiming,cpmc,tzgw,jjglr,jjtgr,wbjgf,zqjjs,qhjjs,birthday,yxzt,cplx,csgm,tzcl,sffj,sfsx,rgqd,zjqd,fbq,kfr,rgfl,shfl,shflsm,glfl,yjx,zsx,yjbc,cxqx,babh,plbs,fund_id) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (item['manager_id'], item['company_id'], item["fund_name"], item['rzpj'], item['jjjl'],
                 item['paiming'],item['cpmc'],item['tzgw'],item['jjglr'],item['jjtgr'],item['wbjgf'],item['zqjjs'],item['qhjjs'],item['birthday'],item['yxzt'], item['cplx'], item['csgm'], item['tzcl'], item['sffj'], item['sfsx'], item['rgqd'], item['zjqd'], item['fbq'], item['kfr'], item['rgfl'], item['shfl'], item['shflsm'], item['glfl'], item['yjx'], item['zsx'], item['yjbc'], item['cxqx'], item['babh'], item['plbs'], item['fund_id']))

            self.cur.commit()
        elif isinstance(item,Fund_worthItem):

            self.conn.execute(
                "insert into fund_worth (fund_id,date,unit,ljjz,ljjz1,jzbd) values(%s, %s, %s, %s, %s, %s)",
                (item['fund_id'], item['date'], item['unit'], item['ljjz'], item['ljjz1'], item['jzbd']  ))

            self.cur.commit()
        elif isinstance(item,CompanyItem):
            # print("insert into company (name,ljsy,dbcp,birthday,szdq,jnsy,gsjc,qxjj,babh,hxrw,gsjs,tzln,company_id)values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s ,%s ,%s)",
            #     (item['company_name'], item['company_ljsy'], item["company_dbcp"], item['company_birthday'], item['company_szdq'],item['company_jnsy'],item['company_gsjc'],item['company_qxjj'], item['company_babh'], item['company_hxrw'], item['company_gsjs'], item['company_tzln'], item['company_id'] ))


            self.conn.execute(
                "insert into company (name,ljsy,dbcp,birthday,szdq,jnsy,gsjc,qxjj,babh,hxrw,gsjs,tzln,company_id)values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s ,%s ,%s)",
                (item['company_name'], item['company_ljsy'], item["company_dbcp"], item['company_birthday'], item['company_szdq'],item['company_jnsy'],item['company_gsjc'],item['company_qxjj'], item['company_babh'], item['company_hxrw'], item['company_gsjs'], item['company_tzln'] ,item['company_id']))

            self.cur.commit()
        elif isinstance(item,EmployItem):
            # print("insert into employ (name,rwjs,company_id,gszw,cynx,qxjj,zybj,dbcp,employ_id) values(%s, %s, %s, %s, %s, %s, %s, %s,%s)",
            #     (item['employ_name'], item['rwjs'], item['gszw'], item['cynx'], item['qxjj'], item['zybj'], item['dbcp'], item['employ_id']))

            self.conn.execute(
                "insert into employ (name,rwjs,company_id,gszw,cynx,qxjj,zybj,dbcp,employ_id) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (item['employ_name'], item['rwjs'], item["company_id"],item['gszw'], item['cynx'], item['qxjj'], item['zybj'], item['dbcp'], item['employ_id']))

            self.cur.commit()
    def spider_closed(self, spider):
        self.conn.close()
        self.cur.close()

