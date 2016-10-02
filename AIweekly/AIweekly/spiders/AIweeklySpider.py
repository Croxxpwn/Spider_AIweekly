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
        "http://aiweekly.co/issues/2#start",
        "http://aiweekly.co/issues/3#start",
        "http://aiweekly.co/issues/4#start",
        "http://aiweekly.co/issues/5#start",
        "http://aiweekly.co/issues/6#start",
        "http://aiweekly.co/issues/7#start",
        "http://aiweekly.co/issues/8#start",
        "http://aiweekly.co/issues/9#start",
        "http://aiweekly.co/issues/10#start",
        "http://aiweekly.co/issues/11#start",
        "http://aiweekly.co/issues/12#start",
        "http://aiweekly.co/issues/13#start",
        "http://aiweekly.co/issues/14#start",
        "http://aiweekly.co/issues/15#start",
        "http://aiweekly.co/issues/16#start",
        "http://aiweekly.co/issues/17#start",
        "http://aiweekly.co/issues/18#start",
        "http://aiweekly.co/issues/19#start",
        "http://aiweekly.co/issues/20#start",
        "http://aiweekly.co/issues/21#start",
        "http://aiweekly.co/issues/22#start",
        "http://aiweekly.co/issues/23#start",
        "http://aiweekly.co/issues/24#start",
        "http://aiweekly.co/issues/25#start",
        "http://aiweekly.co/issues/26#start",
        "http://aiweekly.co/issues/27#start",
        "http://aiweekly.co/issues/28#start",
        "http://aiweekly.co/issues/29#start",
        "http://aiweekly.co/issues/30#start",
        "http://aiweekly.co/issues/31#start",
        "http://aiweekly.co/issues/32#start",
        "http://aiweekly.co/issues/33#start",
        "http://aiweekly.co/issues/34#start",
        "http://aiweekly.co/issues/35#start",
        "http://aiweekly.co/issues/36#start",
        "http://aiweekly.co/issues/37#start",
        "http://aiweekly.co/issues/38#start",
        "http://aiweekly.co/issues/39#start",
        "http://aiweekly.co/issues/40#start",
        "http://aiweekly.co/issues/41#start",
        "http://aiweekly.co/issues/42#start",
        "http://aiweekly.co/issues/43#start",
        "http://aiweekly.co/issues/44#start",
        "http://aiweekly.co/issues/45#start",
        "http://aiweekly.co/issues/46#start",
        "http://aiweekly.co/issues/47#start",
        "http://aiweekly.co/issues/48#start",

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


