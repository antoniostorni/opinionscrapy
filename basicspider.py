# -*- coding: utf-8 -*-
import scrapy

class OpinionItem(scrapy.Item):
    title = scrapy.Field()
    opinion_number = scrapy.Field()
    date = scrapy.Field()
    # define the fields for your item here like:
    # name = scrapy.Field()


class OpinionsSpider(scrapy.Spider):
    name = "opinions"
    allowed_domains = ["http://www.cadc.uscourts.gov"]
    start_urls = (
        'http://www.cadc.uscourts.gov/internet/opinions.nsf/OpinionsByMonday?OpenView&StartKey=20141220141201&Count=6&scode=2/',
    )

    def parse(self, response):
       for sel in response.xpath(".//*[@id='ViewBody']/opinion"):
           item = OpinionItem()
           item['opinion_number'] = sel.xpath('div[1]/span[1]/a/text()').extract()[0]
           item['title'] = sel.xpath('div[1]/span[2]/text()').extract()[0]
           item['date'] = sel.xpath('div[2]/span[2]/text()').extract()[0]
           yield item

