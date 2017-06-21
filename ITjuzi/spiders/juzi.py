# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ITjuzi.items import ItjuziItem,juziItem
import re

class JuziSpider(CrawlSpider):
    name = 'juzi'
    allowed_domains = ['itjuzi.com']
    start_urls = [
        # 'http://www.itjuzi.com/company',
        'https://www.itjuzi.com/investevents'
    ]

    rules = (
        # Rule(LinkExtractor(allow=r'/company\?page=\d+')),
        # Rule(LinkExtractor(allow=r'http://www.itjuzi.com/company/\d+'), callback="parse_item", follow=False),

        Rule(LinkExtractor(allow=r'/investevents\?page=\d+')),
        Rule(LinkExtractor(allow=r'https://www.itjuzi.com/investevents/\d+'),callback="parse_detail",follow=False),
    )
    # def parse_investevents(self,response):
    #     item=juziItem()
    #
    #     item["date"]=response.xpath('//ul[@class="list-main-eventset"]//li/i[1]/span/text()').extract()[0]
    #     item["maincell"]=response.xpath('//ul[@class="list-main-eventset"]//li/i[3]/p/a/span/text()').extract()[0]
    #     item["round"]=response.xpath('//ul[@class="list-main-eventset"]//li/i[4]/a/span/text()').extract()[0]
    #     item["money"]=response.xpath('//ul[@class="list-main-eventset"]//li/i[5]/text()').extract()[0]
    #     item["name"]=response.xpath('//ul[@class="list-main-eventset"]//li/i[6]/div/a/text()').extract()[0]
    #     yield item


    def parse_detail(self,response):
        item = juziItem()
        # 标题
        item["title"] = response.xpath('//div[@class="title"]/h1/text()').extract()[0]
        # 时间
        item["date"] = response.xpath('//div[@class="title"]/h1/span/text()').extract()[0]
        # 公司
        item["company_name"] = response.xpath('//div[@class="right-con"]/p/a/b/text()').extract()[0]
        # 轮次


        item["round"] = response.xpath('//tr/td[3]//span[2]/text()').extract()[0]
        # 融资额
        item["money"] = response.xpath('//tr/td[4]//span[2]/text()').extract()[0]
        # 股份
        item["shares"] = response.xpath('//tr/td[5]//span[2]/text()').extract()[0]
        # 公司简介
        item["company_intro"] = response.xpath('//div[@class="mart10"]/text()').extract()[0]
        # 投资方
        investors_name = response.xpath('//div[@class="right"]/h4/a/b/text()').extract()[0]
        if investors_name:
            item["investors_name"]=investors_name
        else:
            item["investors_name"]=""


        # tags
        tag= response.xpath('//div[@class="right"]/h4/span/text()').extract()
        item["tag"]=" ".join(tag)
        # 投资方简介
        # investors_name_ito= response.xpath('//div[@class="right"]/p/text()').extract()
        # item["investors_name_ito"]=investors_name_ito.replace("\n","").replace("\t","").strip()
        # 全部融资
        full_history= response.xpath('//div[@class="sec"]//div[@class="pad finan-history"]//tr/td//span/text()|a/text()').extract()
        item["full_history"]="".join(full_history)
        yield item



    # def parse_item(self, response):
    #
    #     item=ItjuziItem()
    #     # 公司名称
    #     company_name=response.xpath('//div[@class="line-title"]/span/h1/text()').extract()[0]
    #     # 投资情况
    #     tz_info=response.xpath('//div[@class="line-title"]/span/h1/span/text()').extract()[0]
    #     item["tz_info"]="".join(tz_info).replace("\n","").replace("\t","")
    #     item["company_name"]=company_name.replace("\t","").replace("\n","")
    #     # 公司口号
    #     item["slogan"]=response.xpath('//div[@class="info-line"]//h2[@class="seo-slogan"]/text()').extract()[0]
    #     # 分类
    #     item["scope"]=response.xpath('//div[@class="info-line"]//span[@class="scope c-gray-aset"]/a[1]/text()').extract()[0]
    #     # 子分类
    #     item["sub_scope"]=response.xpath('//div[@class="info-line"]//span[@class="scope c-gray-aset"]/a[2]/text()').extract()[0]
    #     # 所在城市
    #     item["city"]=response.xpath('//div[@class="info-line"]/span[2]/a[1]/text()').extract()[0]
    #     # 所在区域
    #     item["area"]=response.xpath('//div[@class="info-line"]/span[2]/a[2]/text()').extract()[0]
    #     # 公司主页
    #     home_page=response.xpath('//div[@class="link-line"]/a[3]/@href').extract()
    #     item["home_page"]=''.join(home_page)
    #     # 公司标签
    #     tags=response.xpath('//span[@class="tag"]/text()').extract()[0]
    #     item["tags"]="".join(tags)
    #     # 公司简介
    #     company_intro=response.xpath('//div[@class="des"]/text()').extract()
    #     item["company_intro"]="".join(company_intro).strip()
    #     # 公司全称
    #     company_full_name=response.xpath('//div[@class="des-more"]/div[1]/h2/text()').extract()[0]
    #     item["company_full_name"]=company_full_name.replace("公司全称：","").strip()
    #     # 成立时间：
    #     found_time=response.xpath('//div[@class="des-more"]/div[2]/h2[1]/text()').extract()[0]
    #     item["found_time"]=found_time.replace("成立时间：","").strip()
    #     # 公司规模：
    #     company_size=response.xpath('//div[@class="des-more"]/div[2]/h2[2]/text()').extract()[0]
    #     item["company_size"]=company_size.strip()
    #     # 运营状态
    #     item["company_status"]=response.xpath('//div[@class="des-more"]/div[3]/span[1]/text()').extract()[0]
    #     yield item
