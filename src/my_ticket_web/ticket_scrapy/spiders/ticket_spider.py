# -*- coding: utf-8 -*-
import datetime
import json

import scrapy
from scrapy import Request
from ..cookie_helper import get_cookie_dict
from ..items import TicketScrapyItem


class TicketSpiderSpider(scrapy.Spider):
    '''
    查询 A-B 车票信息
    '''
    name = "ticket_spider"

    def __init__(self, query_conditions):
        # 从命令行中获取参数
        query_list = query_conditions.split(",")
        self.train_date = query_list[0].split("=")[1]  # 日期
        self.from_station = query_list[1].split("=")[1]  # 出发地
        self.to_station = query_list[2].split("=")[1]  # 目的地
        self.purpose_codes = query_list[3].split("=")[1]  # 成人/学生

    # 覆盖默认的settings配置，针对不同的spider应用不同的管道
    custom_settings = {
        'ITEM_PIPELINES': {
            'ticket_scrapy.pipelines.TicketScrapyPipeline': 300,
        }
    }

    def start_requests(self):
        # 查询车票实际调用的api
        # url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2020-07-31&leftTicketDTO.from_station=HFH&leftTicketDTO.to_station=WHH&purpose_codes=ADULT'
        url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=%s' \
              % (self.train_date, self.from_station, self.to_station, self.purpose_codes)

        # 从配置中获取cookie字典
        cookie_dict = get_cookie_dict()

        yield Request(url, cookies=cookie_dict)

    def parse(self, response):
        # 写入到 ticket.json 文件，方便观察对比
        with open('out/ticket.json', mode='wb') as f:
            f.write(response.body)

        # 将响应的json字符串转换为字典值
        left_ticket_dict = json.loads(response.text)
        # 遍历每个车次信息
        for ticket_info in left_ticket_dict['data']['result']:
            # print(ticket_info)
            try:
                tk_item = self.get_ticket_item(ticket_info)
                if tk_item:
                    yield tk_item
            except Exception as ex:
                print(ex)

    def get_ticket_item(self, info_str):
        '''
        将json字符串转换为车票对象
        :return: 车票对象，可以被管道直接处理
        '''
        info_list = str(info_str).split('|')
        if len(info_list) < 34:
            return None

        ticket_item = TicketScrapyItem()
        # ticket_item['valid_code'] = info_list[0]

        ticket_item['train_no'] = info_list[2]
        ticket_item['train_code'] = info_list[3]

        ticket_item['start_station_code'] = info_list[4]
        ticket_item['end_station_code'] = info_list[5]

        ticket_item['from_station_code'] = info_list[6]
        ticket_item['dest_station_code'] = info_list[7]

        ticket_item['start_time'] = info_list[8]
        ticket_item['arrive_time'] = info_list[9]
        ticket_item['run_time'] = info_list[10]

        ticket_item['can_buy'] = info_list[11]

        # ticket_item['valid_code2'] = info_list[12]

        ticket_item['start_station_date'] = info_list[13]

        ticket_item['gr_num'] = info_list[21]
        ticket_item['qt_num'] = info_list[22]
        ticket_item['rw_num'] = info_list[23]
        ticket_item['rz_num'] = info_list[24]
        ticket_item['tz_num'] = info_list[25]
        ticket_item['wz_num'] = info_list[26]
        ticket_item['unknow1_num'] = info_list[27]
        ticket_item['yw_num'] = info_list[28]
        ticket_item['yz_num'] = info_list[29]
        ticket_item['edz_num'] = info_list[30]
        ticket_item['ydz_num'] = info_list[31]
        ticket_item['swz_num'] = info_list[32]
        ticket_item['dw_num'] = info_list[33]

        # 设置当前日期
        ticket_item['query_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        return ticket_item
