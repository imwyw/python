from scrapy import cmdline

# A-B地车票信息
# cmdline.execute('scrapy crawl ticket_spider'.split())
# 带有参数的执行 query_conditions=中的query_conditions要与__init__中的参数名一样，-a 表示参数
# cmdline.execute(
#     'scrapy crawl ticket_spider -a query_conditions=train_date=2020-07-10,from_station=HFH,to_station=WHH,purpose_codes=ADULT'.split())

# 全国车站信息编码
# cmdline.execute('scrapy crawl station_spider'.split())

# 全国所有车次信息，即排班表
cmdline.execute('scrapy crawl train_spider'.split())
