# -*- coding: utf-8 -*-
import scrapy
from opinionscrapy.items import OpinionItem


class OpinionsSpider(scrapy.Spider):
    name = "opinions"
    allowed_domains = ["http://www.cadc.uscourts.gov"]
    # We use this URL (with last week results filter)
    # because http://www.cadc.uscourts.gov/internet/opinions.nsf is currently empty.
    start_urls = (
        'http://www.cadc.uscourts.gov/internet/opinions.nsf/OpinionsByMonday?OpenView&StartKey=20141220141201&Count=6&scode=2/',
    )

    def parse(self, response):
        # Xpath for every opinion, each one is enclosed into a <opinion> tag
        for sel in response.xpath(".//*[@id='ViewBody']/opinion"):
            item = OpinionItem()
            item['opinion_number'] = sel.xpath('div[1]/span[1]/a/text()').extract()[0]
            item['title'] = sel.xpath('div[1]/span[2]/text()').extract()[0]
            item['date'] = sel.xpath('div[2]/span[2]/text()').extract()[0]
            # yield the result
            yield item
