# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

from ticket_scrapy.cookie_helper import get_cookie_dict


class TrainSpiderSpider(scrapy.Spider):
    '''
    对全国所有车次信息的爬取，文件较大，不要经常跑
    '''
    name = "train_spider"

    def start_requests(self):
        # 全国所有所有车次信息，即排班表
        url = 'https://kyfw.12306.cn/otn/resources/js/query/train_list.js'

        cookie_dict = get_cookie_dict()

        yield Request(url, cookies=cookie_dict)

    def parse(self, response):
        # 写入到 train_list.js 文件进行测试观察
        with open('out/train_list.js', mode='wb') as f:
            f.write(response.body)

        # todo 可以进行持久化保存，结合价格等等因素分析......

