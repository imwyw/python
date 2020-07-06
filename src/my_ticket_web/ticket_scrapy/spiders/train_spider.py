# -*- coding: utf-8 -*-
import json
import re

import scrapy
from scrapy import Request

from ticket_scrapy.cookie_helper import get_cookie_dict
from ticket_scrapy.scrapy_items.train_item import TrainScrapyItem


class TrainSpiderSpider(scrapy.Spider):
    '''
    对全国所有车次信息的爬取，文件较大，不要经常跑
    '''
    name = "train_spider"
    # 覆盖默认的settings配置，针对不同的spider应用不同的管道
    custom_settings = {
        'ITEM_PIPELINES': {
            'ticket_scrapy.pipelines.pipeline_train.TrainScrapyPipeline': 300,
        }
    }

    def start_requests(self):
        # 全国所有所有车次信息，即排班表
        url = 'https://kyfw.12306.cn/otn/resources/js/query/train_list.js'

        cookie_dict = get_cookie_dict()

        yield Request(url, cookies=cookie_dict)

    def parse(self, response):
        try:
            # 写入到 train_list.json 文件进行测试观察
            with open('out/train_list.json', mode='wb') as f:

                js_str = response.body
                # 匹配 json 段内容
                json_str = re.findall('{.*$', js_str.decode('utf-8'))[0]
                # 编码重新写入文件中，以便后续处理需求
                f.write(json_str.encode('utf-8'))

                # 解析得到json字典值，进而处理
                json_dict = json.loads(json_str)
                # 构造一个列车车次信息
                train_item = TrainScrapyItem()

                # item_date 是日期，item_type_list 是该日期的所有车次
                # todo，需要重构，三层循环有点恶心。。。
                for (item_date, item_type_list) in json_dict.items():
                    # item_type 是 列车类型，train_list 是该车次下所有的列车信息列表
                    for (item_type, train_list) in item_type_list.items():
                        # 每个车次类型下所有详情信息
                        for train_info in train_list:
                            train_item['train_date'] = item_date
                            train_item['train_type'] = item_type
                            train_item['train_no'] = train_info['train_no']
                            info_code = train_info['station_train_code'].split('(')[0]
                            station_a2b = train_info['station_train_code'].split('(')[1].replace(')', '')
                            train_item['train_code'] = info_code
                            train_item['start_station'] = station_a2b.split('-')[0]
                            train_item['end_station'] = station_a2b.split('-')[1]
                            yield train_item
                            pass
                        pass
                    pass


        except Exception as ex:
            print(ex)
