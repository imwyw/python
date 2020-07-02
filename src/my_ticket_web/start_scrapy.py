from scrapy import cmdline

# A-B地车票信息
# cmdline.execute('scrapy crawl ticket_spider'.split())
# 带有参数的执行 query_conditions=中的query_conditions要与__init__中的参数名一样，-a 表示参数
cmdline.execute('scrapy crawl ticket_spider -a query_conditions=train_date=2020-07-30,from_station=SZH,to_station=SHH,purpose_codes=ADULT'.split())

# 全国车站信息编码
cmdline.execute('scrapy crawl station_spider'.split())

