# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymongo
# class ItjuziPipeline(object):
#     def process_item(self, item, spider):
#         conn_mongo = pymongo.MongoClient(host="127.0.0.1", port=27017)
#         mongo_db = conn_mongo["juzi"]
#         mongo_name = mongo_db["itjuzi"]
#         data = dict(item)
#         mongo_name.insert(data)
#         return item

class juziPipeline(object):
    def process_item(self, item, spider):
        conn_mongo = pymongo.MongoClient(host="127.0.0.1", port=27017)
        mongo_db = conn_mongo["itjuzi"]
        mongo_name = mongo_db["juzi"]
        data = dict(item)
        mongo_name.insert(data)
        return item