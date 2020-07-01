from time import sleep
from scrapy.http import HtmlResponse

'''
自定义下载器中间件
需要在 settings 中配置开启 DOWNLOADER_MIDDLEWARES 中间件

当每个request通过下载中间件时，该方法被调用。
必须返回其中之一: 返回 None 、返回一个 Response 对象、返回一个 Request 对象或raise IgnoreRequest 
返回 None ，Scrapy将继续处理该request，执行其他的中间件的相应方法
返回 Response 对象，Scrapy将不会调用 任何 其他的 process_request() 或 process_exception() 方法
返回 Request 对象，Scrapy将停止调用 process_request方法并重新调度可以返回新的request。
'''


class SeleniumDownloaderMiddleware(object):
    # 当每个request通过下载中间件时，该方法被调用。
    def process_request(self, request, spider):
        # 如果包含'node'段，即是新闻类别
        if str.find(request.url, 'node') > -1:
            # 获取spider爬虫内实例化的浏览器对象 browser
            browser = spider.browser
            # 操作浏览器对象打开 请求 request url
            browser.get(request.url)
            # 等待 1 秒，确保页面js动态渲染完成
            # sleep(1)
            # 获取渲染后的页面源代码 html
            html = browser.page_source
            # 构造一个新的response，交给 spider parse 进行处理
            return HtmlResponse(url=browser.current_url, request=request, body=html.encode(), encoding='utf-8')
        else:
            # 不需要经过 selenium 处理的请求
            return None
