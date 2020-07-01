# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AiitNewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 标题
    title = scrapy.Field()
    # 摘要信息
    summary = scrapy.Field()
    # 发布方
    author = scrapy.Field()
    # 阅读量
    read_count = scrapy.Field()
    # 发布日期
    pub_date = scrapy.Field()
    # 新闻图片资源连接地址 url
    img_src = scrapy.Field()
    pass
