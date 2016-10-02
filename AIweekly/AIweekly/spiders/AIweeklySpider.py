# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from AIweekly.items import AiweeklyItem
import re


class AIweeklySpider(CrawlSpider):
    name = "aiweekly"
    allowed_domains = ["aiweekly.co"]
    start_urls = [
        "http://aiweekly.co/issues/1#start",      
    ]
    rules = [
        Rule(LinkExtractor(
            allow=r"/issues/[0-9]+#start"),"parse_item"),
        Rule(LinkExtractor(
            allow=r"/issues/[0-9]+"),"parse_item"),
    ]

    def parse_item(self, response):
        
        item = AiweeklyItem()

        item['title'] = response.xpath(
            r"//h3[@class='item__title']/a/text()").extract()

        item['link'] = response.xpath(
            r"//h3[@class='item__title']/a/@href").extract()

        return item


