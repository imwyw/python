# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class AiitNewsPipeline(object):
    def process_item(self, item, spider):
        # 将 spider yield 数据进行持久化保存到 mysql
        return item



