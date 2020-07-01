# -*- coding: utf-8 -*-
import scrapy
from ..items import AiitNewsItem
from selenium import webdriver


class AiitSpiderSpider(scrapy.Spider):
    # spider 名称，执行命令时需要使用 scrapy crawl aiit_spider
    name = "aiit_spider"
    # 开始爬取的地址
    start_urls = ['https://www.aiit.edu.cn/node/388']

    # 创建爬虫时，实例化浏览器对象，在下载器中间件内进行调用
    browser = webdriver.Chrome()

    def parse(self, response):
        # 遍历每一条新闻
        for item_selector in response.xpath('//div[@class="content-div clearfix"]'):
            try:
                content_item = item_selector.xpath('.//div[@class="contents"]')
                newsItem = AiitNewsItem()
                newsItem['title'] = content_item.xpath('.//div[contains(@class,"title")]/a/text()').get()
                newsItem['summary'] = content_item.xpath('./p/text()').get()
                newsItem['author'] = content_item.xpath('./span/text()').get()

                # 由于在js中异步加载具体数量，怎么拿到真实请求的 count？
                newsItem['read_count'] = content_item.xpath('./span[2]/text()').get()
                newsItem['pub_date'] = content_item.xpath('./span[3]/text()').get()

                # 找到新闻对应的图片 img src 属性值，进行拼接得到完整的 url 路径，通过 pipeline 进行下载保存
                newsItem['img_src'] = 'https://www.aiit.edu.cn' + item_selector.xpath(
                    './/div[@class="pic"]/img/@src').get()
                # 返回给管道处理
                yield newsItem
            except Exception as ex:  # 如果发生异常，不影响后面数据的爬取
                print(ex)

        # 获取到下一页链接的 href 值
        next_link = response.xpath('//ul[@id="pagination-digg"]/li/a[text()="下一页"]/@href').get()
        # print(next_link)
        if next_link:
            # 再次调度请求
            yield scrapy.Request(next_link, callback=self.parse)

    # 爬虫停止关闭时，也同步释放浏览器对象
    def close(self, spider, reason):
        self.browser.close()
