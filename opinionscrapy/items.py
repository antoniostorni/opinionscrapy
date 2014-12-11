# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class OpinionItem(scrapy.Item):
    title = scrapy.Field()
    opinion_number = scrapy.Field()
    date = scrapy.Field()
    # define the fields for your item here like:
    # name = scrapy.Field()
