from scrapy import cmdline

'''
项目从此文件运行，也可以通过Terminal终端执行 scrapy crawl spider_name 进行爬取
'''
cmdline.execute('scrapy crawl aiit_spider'.split())

