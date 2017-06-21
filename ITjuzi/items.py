# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class juziItem(scrapy.Item):
    #标题
    title=scrapy.Field()
    # 时间
    date = scrapy.Field()
    # 公司
    company_name = scrapy.Field()
    # 轮次
    round = scrapy.Field()
    # 融资额
    money = scrapy.Field()
    # 股份
    shares=scrapy.Field()
    # 公司简介
    company_intro = scrapy.Field()
    # 投资方
    investors_name = scrapy.Field()
    #tags
    tag=scrapy.Field()
    # # 投资方简介
    # investors_name_ito=scrapy.Field()
    #全部融资
    full_history=scrapy.Field()



class ItjuziItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 公司名称
    company_name = scrapy.Field()
    # 投资情况列表：包含获投时间、融资阶段、融资金额、投资公司
    tz_info = scrapy.Field()
    # 公司口号
    slogan = scrapy.Field()
    # 分类
    scope = scrapy.Field()
    # 子分类
    sub_scope = scrapy.Field()
    # 所在城市
    city = scrapy.Field()
    # 所在区域
    area = scrapy.Field()
    # 公司主页
    home_page = scrapy.Field()
    # 公司标签
    tags = scrapy.Field()
    # 公司简介
    company_intro = scrapy.Field()
    # 公司全称：
    company_full_name = scrapy.Field()
    # 成立时间：
    found_time = scrapy.Field()
    # 公司规模：
    company_size = scrapy.Field()
    # 运营状态
    company_status = scrapy.Field()

    # # 团队信息列表：包含成员姓名、成员职称、成员介绍
    # tm_info = scrapy.Field()
    # # 产品信息列表：包含产品名称、产品类型、产品介绍
    # pdt_info = scrapy.Field()


