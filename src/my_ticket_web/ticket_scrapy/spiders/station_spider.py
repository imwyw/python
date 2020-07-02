# -*- coding: utf-8 -*-

import scrapy
from scrapy import Request
from ..cookie_helper import get_cookie_dict
import re
from ..items import StationScrapyItem


class StationSpiderSpider(scrapy.Spider):
    '''
    查询所有车站信息和编码等
    '''
    name = 'station_spider'
    # 覆盖默认的settings配置，针对不同的spider应用不同的管道
    custom_settings = {
        'ITEM_PIPELINES': {
            'ticket_scrapy.pipelines.StationScrapyPipeline': 300,
        }
    }

    def start_requests(self):
        # 全国所有车站的电码信息编号
        url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js'

        cookie_dict = get_cookie_dict()

        yield Request(url, cookies=cookie_dict)

    def parse(self, response):
        # 写入到 station.js 文件进行测试观察
        with open('out/station.js', mode='wb') as f:
            f.write(response.body)

        # 返回解析一段 js 脚本
        js_str = response.body.decode('utf-8')
        # 正则匹配 获取单引号中内容
        all_station = re.findall("'.*'", js_str)[0]
        # 按照 @ 符号进行分隔，获取到每个车站信息
        station_list = str(all_station).split('@')

        '''
        每段结构：bjb|北京北|VAP|beijingbei|bjb|0
        车站缩写|车站名称|车站电码编号|车站全拼|车站缩写2|车站数字编码
        再次进行拆分并对应到 item 类，管道处理进行插库
        '''
        for st_str in station_list:
            try:
                # 坑大了，去掉所有的单双引号，防止sql出错
                info_list = st_str.replace("'", "").replace('"', '').split('|')

                # 如果拆分得到的数据不对则跳过
                if len(info_list) < 5:
                    continue
                station_item = StationScrapyItem()
                station_item['short_name'] = info_list[0]
                station_item['full_name'] = info_list[1]
                station_item['station_code'] = info_list[2]
                station_item['station_pin'] = info_list[3]
                station_item['short_name2'] = info_list[4]
                station_item['num_code'] = info_list[5]
                yield station_item
            except Exception as ex:
                print(ex)
