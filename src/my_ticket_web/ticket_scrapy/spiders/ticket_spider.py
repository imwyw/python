# -*- coding: utf-8 -*-

import scrapy
from scrapy import Request
from ..cookie_helper import get_cookie_dict


class TicketSpiderSpider(scrapy.Spider):
    '''
    查询 A-B 车票信息
    '''
    name = "ticket_spider"

    def start_requests(self):
        # 查询车票实际调用的api
        url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2020-07-02&leftTicketDTO.from_station=HFH&leftTicketDTO.to_station=WHH&purpose_codes=ADULT'

        # 从配置中获取cookie字典
        cookie_dict = get_cookie_dict()

        yield Request(url, cookies=cookie_dict)

    def parse(self, response):
        # 写入到 ticket.json 文件
        with open('out/ticket.json', mode='wb') as f:
            f.write(response.body)
