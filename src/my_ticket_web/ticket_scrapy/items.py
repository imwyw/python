# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TicketScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class StationScrapyItem(scrapy.Item):
    '''
    车站相关信息
    '''
    # 车站缩写 bjb
    short_name = scrapy.Field()
    # 车站名称 北京北
    full_name = scrapy.Field()
    # 车站电码编号 VAP
    station_code = scrapy.Field()
    # 车站全拼 beijingbei
    station_pin = scrapy.Field()
    # 车站缩写2 bjb
    short_name2 = scrapy.Field()
    # 车站数字编码 0
    num_code = scrapy.Field()

    pass
