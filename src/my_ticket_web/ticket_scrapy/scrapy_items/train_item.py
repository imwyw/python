import scrapy


class TrainScrapyItem(scrapy.Item):
    '''
    车次相关信息
    '''
    # 猜测是发车时间
    train_date = scrapy.Field()
    # 列车类型 D,T,G,C,O,K,Z
    train_type = scrapy.Field()
    # 车次编号
    train_no = scrapy.Field()
    # 车次
    train_code = scrapy.Field()
    # 起始站
    start_station = scrapy.Field()
    # 终点站
    end_station = scrapy.Field()

    pass