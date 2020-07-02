# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import datetime

import scrapy


class TicketScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 记录爬取时间，即当前时间
    query_time = scrapy.Field()

    # 0 看着像什么校验码，不确定，内容很长
    valid_code = scrapy.Field()
    # 1 预订 固定值

    # 2 列车号
    train_no = scrapy.Field()
    # 3 车次
    train_code = scrapy.Field()

    # 4 始发站代码
    start_station_code = scrapy.Field()
    # 5 终点站代码
    end_station_code = scrapy.Field()

    # 6 出发站代码
    from_station_code = scrapy.Field()
    # 7 目的地代码
    dest_station_code = scrapy.Field()
    # 出发站名称
    from_station_name = scrapy.Field()
    # 目的地名称
    dest_station_name = scrapy.Field()

    # 8 出发时刻
    start_time = scrapy.Field()
    # 9 到达时刻
    arrive_time = scrapy.Field()
    # 10 历时
    run_time = scrapy.Field()

    # 11 能否购买？ Y：可以，N：不可以，IS_TIME_NOT_BUY：暂停发售/列车停运
    can_buy = scrapy.Field()

    # 12 未知校验码。。。
    valid_code2 = scrapy.Field()

    # 13 起始站发车日期
    start_station_date = scrapy.Field()

    # 21 高级软卧
    gr_num = scrapy.Field()
    # 22 其他
    qt_num = scrapy.Field()
    # 23 软卧，一等卧
    rw_num = scrapy.Field()
    # 24 软座
    rz_num = scrapy.Field()
    # 25 特等？未知。。。
    tz_num = scrapy.Field()
    # 26 无座
    wz_num = scrapy.Field()
    # 27 未知
    unknow1_num = scrapy.Field()
    # 28 硬卧，二等卧
    yw_num = scrapy.Field()
    # 29 硬座
    yz_num = scrapy.Field()
    # 30 二等座
    edz_num = scrapy.Field()
    # 31 一等座
    ydz_num = scrapy.Field()
    # 32 商务座
    swz_num = scrapy.Field()
    # 33 动卧
    dw_num = scrapy.Field()

    remark = scrapy.Field()

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
