from scrapy import cmdline

# A-B地车票信息
cmdline.execute('scrapy crawl ticket_spider'.split())

# 全国车站信息编码
# cmdline.execute('scrapy crawl station_spider'.split())
