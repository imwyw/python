# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request


class TicketSpiderSpider(scrapy.Spider):
    name = "ticket_spider"

    def start_requests(self):
        url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2020-07-02&leftTicketDTO.from_station=HFH&leftTicketDTO.to_station=WHH&purpose_codes=ADULT'

        cookie_string = 'JSESSIONID=C6C16A65A7D70E9A1449DCD8D77D8C22; BIGipServerotn=1123025418.24610.0000; RAIL_EXPIRATION=1593909829657; RAIL_DEVICEID=GV6oOya49MBk7vleDYUHXiM4u1Bv_7GeuT25MpZ0FG-dML-zAlTrdshFpDaPxsVblIvkgALUV-YmyFuKvmwPO5e1gTlb_hSjXbnQ_o39XqptPUOy6VOyYMgqWc3G3DFgBunCUlmwygy-GuciT1kEFqvhSonGqH9p; BIGipServerpool_passport=384631306.50215.0000; route=6f50b51faa11b987e576cdb301e545c4; _jc_save_fromStation=%u5408%u80A5%2CHFH; _jc_save_toStation=%u829C%u6E56%2CWHH; _jc_save_toDate=2020-07-02; _jc_save_wfdc_flag=dc; _jc_save_fromDate=2020-07-02'
        # 定义 cookie 字典
        cookie_dict = {}
        # cookie 字符串中每对 key-value 以分号分隔
        cookie_array = cookie_string.split(';')
        for cookie_item in cookie_array:
            # 以等号拆分，取出 key 和 value 对应的值
            item_key = cookie_item.split('=')[0].replace(' ', '')
            item_value = cookie_item.split('=')[1]
            cookie_dict[item_key] = item_value

        yield Request(url, cookies=cookie_dict)

    def parse(self, response):
        # 写入到 ticket.json 文件
        with open('ticket.json', mode='wb') as f:
            f.write(response.body)
