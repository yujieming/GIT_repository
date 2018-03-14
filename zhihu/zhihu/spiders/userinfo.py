# -*- coding: utf-8 -*-
import scrapy
import re
import json
from zhihu.items import ZhihuItem

class UserinfoSpider(scrapy.Spider):
    name = 'userinfo'
    allowed_domains = ['zhihu.com']
    start_urls = ['https://www.zhihu.com/api/v4/members/cmf2015/followers?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=0&limit=20']

    def parse(self, response):
        data = json.loads(response.body.decode('unicode_escape'))['data']
        num = len(data)
        if num < 20:
            pass
        else:
            page_offset = re.findall("&offset=(.*?)&",response.url)[0]
            new_page_offset = page_offset+str(20)
            next_page_url = response.url.replace("&offset="+str(page_offset)+"&","&offset="+new_page_offset+"&")
            yield  scrapy.Request(url = next_page_url,callback=self.parse)

        for eve_user in data:
            item = ZhihuItem()
            item['name'] = eve_user['name']
            item['user_type'] = eve_user['user_type']
            item['follower_count'] = eve_user['follower_count']
            item['headline'] = eve_user['headline']
            item['url_token'] = eve_user['url_token']
            item['answer_count'] = eve_user['answer_count']
            item['gender'] = eve_user['gender']
            yield item

            new_url = 'https://www.zhihu.com/api/v4/members/'+eve_user['url_token']+'/followers?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=0&limit=20'
            yield scrapy.Request(url=new_url,callback=self.parse)