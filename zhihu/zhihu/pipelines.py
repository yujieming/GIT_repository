# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.conf import settings
import pymongo

class ZhihuPipeline(object):
    def __init__(self):
        host = settings['MONGOOB_HOST']
        port = settings['MONGOOB_PORT']
        dbname = settings['MONGOOB_DBNAME']
        client = pymongo.MongoClient(host=host,port=port)
        tdb = client[dbname]
        self.post = tdb[settings['MONGOOB_DOCNAME']]
    def process_item(self, item, spider):
        zhihu = dict(item)
        print(zhihu)
        self.post.insert(zhihu)
        return item
