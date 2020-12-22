# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class PaipaiwangItem(scrapy.Item):
    company_id = scrapy.Field()

    fund_id = scrapy.Field()
    company_gsjc = scrapy.Field()
class FundItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    fund_id = scrapy.Field()
    company_id = scrapy.Field()
    fund_name = scrapy.Field()
    rzpj = scrapy.Field()
    jjjl = scrapy.Field()
    manager_id = scrapy.Field()
    paiming = scrapy.Field()
    company_name = scrapy.Field()
    cpmc = scrapy.Field()  
    tzgw = scrapy.Field()
    jjglr = scrapy.Field()
    jjtgr = scrapy.Field()
    wbjgf = scrapy.Field()
    zqjjs = scrapy.Field()
    qhjjs = scrapy.Field()
    birthday = scrapy.Field()
    yxzt = scrapy.Field()
    cplx = scrapy.Field()
    csgm = scrapy.Field()
    tzcl = scrapy.Field()
    sffj = scrapy.Field()
    sfsx = scrapy.Field()
    rgqd = scrapy.Field()
    zjqd = scrapy.Field()
    fbq = scrapy.Field()
    kfr = scrapy.Field()
    rgfl = scrapy.Field()
    shfl = scrapy.Field()
    shflsm = scrapy.Field()
    glfl = scrapy.Field()
    yjx = scrapy.Field()
    zsx = scrapy.Field()
    yjbc = scrapy.Field()
    cxqx = scrapy.Field()
    babh = scrapy.Field()
    plbs = scrapy.Field()
    
    
class CompanyItem(scrapy.Item):
    company_id = scrapy.Field()
    company_name = scrapy.Field()
    company_ljsy = scrapy.Field()
    company_dbcp = scrapy.Field()
    company_birthday = scrapy.Field()
    company_szdq = scrapy.Field()
    company_jnsy = scrapy.Field()
    company_qxjj = scrapy.Field()
    company_babh = scrapy.Field()
    company_hxrw = scrapy.Field()
    company_gsjs = scrapy.Field()
    company_tzln = scrapy.Field()
    company_employ = scrapy.Field()
    company_gsjc =scrapy.Field()
    employ_id = scrapy.Field()
class EmployItem(scrapy.Item):
    company_id = scrapy.Field()
    employ_id =scrapy.Field()
    employ_name = scrapy.Field()
    rwjs = scrapy.Field()
    gszw = scrapy.Field()
    cynx = scrapy.Field()
    qxjj = scrapy.Field()
    zybj = scrapy.Field()
    dbcp = scrapy.Field()
    dbcp_url = scrapy.Field()

class Fund_worthItem(scrapy.Item):
    fund_id = scrapy.Field() 
    date = scrapy.Field()
    unit = scrapy.Field()
    ljjz = scrapy.Field()
    ljjz1 = scrapy.Field()
    jzbd = scrapy.Field()
    
    
    
    
    
    # advisor_name = scrapy.Field()
    # advisor_id = scrapy.Field()
    # 基金经理
    # fund_managers = scrapy.Field()
    # fund_manager_intro = scrapy.Field()
    # fund_managers_id = scrapy.Field()
    # company_url = scrapy.Field()
    # company_name = scrapy.Field()
    # company_id = scrapy.Field()
    # company_desc = scrapy.Field()
    # company_founding_time = scrapy.Field()
    # # 公司备案号
    # company_records_num = scrapy.Field()
    # company_city = scrapy.Field()
    # # 基金名字
    # fund_name_text = scrapy.Field()
    # fund_name = scrapy.Field()
    # fund_id = scrapy.Field()
    # # 今年收益
    # year_earnings_text = scrapy.Field()
    # year_earnings = scrapy.Field()
    # # 累计收益
    # accumulated_income_text = scrapy.Field()
    # accumulated_income = scrapy.Field()
    # # 最新净值
    # latest_worth_text = scrapy.Field()
    # latest_worth = scrapy.Field()
    # # 累计净值
    # accumulated_worth_text = scrapy.Field()
    # accumulated_worth = scrapy.Field()
    #
    # # 投资顾问
    # fund_invest_adviser_text = scrapy.Field()
    # fund_invest_adviser = scrapy.Field()
    # # 基金管理人
    # fund_admin_text = scrapy.Field()
    # fund_admin = scrapy.Field()
    # # 托管商
    # fund_trusteeship_text = scrapy.Field()
    # fund_trusteeship = scrapy.Field()
    # # 期货经纪商
    # futures_brokerage_text = scrapy.Field()
    # futures_brokerage = scrapy.Field()
    #
    # # 基金成立时间
    # fund_time_text = scrapy.Field()
    # fund_time = scrapy.Field()
    # # 是否分级
    # is_structured_funds_text = scrapy.Field()
    # is_structured_funds = scrapy.Field()
    # # 基金类型
    # fund_type_text = scrapy.Field()
    # fund_type = scrapy.Field()
    # # 基金主策略
    # fund_strategy_text = scrapy.Field()
    # fund_strategy = scrapy.Field()
    # # 基金子策略
    # fund_substrategy_text = scrapy.Field()
    # fund_substrategy = scrapy.Field()
    # fund_start = scrapy.Field()





