<!-- TOC -->

- [Scrapy](#scrapy)
    - [安装和环境](#安装和环境)
    - [开始项目](#开始项目)
        - [创建第一个spider](#创建第一个spider)
        - [响应解析](#响应解析)
        - [创建模型](#创建模型)
        - [保存](#保存)
    - [疑难杂症](#疑难杂症)
        - [Permission denied](#permission-denied)
    - [其他工具](#其他工具)
        - [在线xpath](#在线xpath)
        - [xpath和css选择器](#xpath和css选择器)

<!-- /TOC -->


<a id="markdown-scrapy" name="scrapy"></a>
# Scrapy
Scrapy是一个纯Python语言实现的爬虫框架，简单、易用、拓展性高使得其成为Python爬虫中的主流利器。

> https://www.osgeo.cn/scrapy/

<a id="markdown-安装和环境" name="安装和环境"></a>
## 安装和环境
以 `Anaconda` 环境和 `Pycharm` 为例，由于 `Scrapy` 库依赖于其他的第三方库，建议使用 `Anaconda` 进行安装

`Anaconda` 在 `Scrapy` 时会自动安装依赖的其他库。

<a id="markdown-开始项目" name="开始项目"></a>
## 开始项目

```bash
scrapy startproject 项目名称
```

<a id="markdown-创建第一个spider" name="创建第一个spider"></a>
### 创建第一个spider

在项目路径下通过命令行 `scrapy genspider 爬虫名称 需要爬取的网址`

```bash
(C:\ProgramData\Anaconda3) D:\Codes\Py\hi_scrapy\hi_scrapy>scrapy genspider aiit_spider www.aiit.edu.cn
Created spider 'aiit_spider' using template 'basic' in module:
  hi_scrapy.spiders.aiit_spider

```

在 `spiders` 目录中会生成默认的【spiders/aiit_spider.py】代码如下：

```py
# -*- coding: utf-8 -*-
import scrapy


class AiitSpiderSpider(scrapy.Spider):
    # 爬虫的名称，执行 crawl 命令时需要对应
    name = "aiit_spider"
    # 允许的域名
    allowed_domains = ["www.aiit.edu.cn"]
    # 入口url，交给调度器里
    start_urls = ['https://www.aiit.edu.cn/node/388']

    def parse(self, response):
        pass
```

* name ：标识蜘蛛。它在一个项目中必须是唯一的，也就是说，不能为不同的蜘蛛设置相同的名称。
* start_urls ：入口url列表
* parse() ：将调用的方法，用于处理为每个请求下载的响应。响应参数是的实例 TextResponse 它保存页面内容，并有进一步有用的方法来处理它。

修改 `parse` 方法，对响应 `response` 进行处理：

```py
def parse(self, response):
    print(response.text)
```

在终端中执行命名 `scrapy crawl xxxx` 运行爬虫

```bash
(C:\ProgramData\Anaconda3) D:\Codes\Py\hi_scrapy\hi_scrapy>scrapy crawl aiit_spider
2020-06-11 01:03:54 [scrapy.utils.log] INFO: Scrapy 1.3.3 started (bot: hi_scrapy)
2020-06-11 01:03:54 [scrapy.utils.log] INFO: Overridden settings: {'BOT_NAME': 'hi_scrapy', 'NEWSPIDER_MODULE': 'hi_scrapy.spiders', 'ROBOTSTXT_OBEY': True, 'SPIDE
R_MODULES': ['hi_scrapy.spiders']}
......
```

以上的每次通过命令执行方式较为麻烦，新建 【spiders/run.py】 文件

```py
from scrapy import cmdline

cmdline.execute('scrapy crawl aiit_spider'.split())
```

执行上面的脚本即可替代前面的命名行操作。

<a id="markdown-响应解析" name="响应解析"></a>
### 响应解析

前面 `crawl` 执行脚本得到的是响应全文，需要在此基础上通过 `xpath` 进行筛选内容

修改【spiders/aiit_spider.py】文件：

```py
class AiitSpiderSpider(scrapy.Spider):
    name = "aiit_spider"
    allowed_domains = ["www.aiit.edu.cn"]
    start_urls = ['https://www.aiit.edu.cn/node/388']

    def parse(self, response):
        # xpath 进行筛选学校要闻项
        news_selector = response.xpath('//div[@class="content"]/div')
        print('学校要闻统计：', len(news_selector))
        for news_item in news_selector:
            print(news_item)
```

执行前面创建的【run.py】，控制台打印如下：

```bash
学校要闻统计： 9 个
<Selector xpath='//div[@class="content"]/div' data='<div class="content-div clearfix">\n     '>
<Selector xpath='//div[@class="content"]/div' data='<div class="content-div clearfix">\n     '>
<Selector xpath='//div[@class="content"]/div' data='<div class="content-div clearfix">\n     '>
<Selector xpath='//div[@class="content"]/div' data='<div class="content-div clearfix">\n     '>
<Selector xpath='//div[@class="content"]/div' data='<div class="content-div clearfix">\n     '>
<Selector xpath='//div[@class="content"]/div' data='<div class="content-div clearfix">\n     '>
<Selector xpath='//div[@class="content"]/div' data='<div class="content-div clearfix">\n     '>
<Selector xpath='//div[@class="content"]/div' data='<div class="content-div clearfix">\n     '>
<Selector xpath='//div[@class="content"]/div' data='<div class="row pagination-container">\n '>
```

<a id="markdown-创建模型" name="创建模型"></a>
### 创建模型

在【items.py】中添加学校新闻对应的模型类：

```py
# 学校要闻类
class NewsItem(scrapy.Item):
    # 新闻标题
    title = scrapy.Field()
    # 摘要信息
    summary = scrapy.Field()
    # 发布者
    author = scrapy.Field()
    # 阅读量
    read_count = scrapy.Field()
    # 发布日期
    pub_date = scrapy.Field()
```

修改爬虫【spiders/aiit_spider.py】文件：

```py
# -*- coding: utf-8 -*-
import scrapy

from hi_scrapy.items import NewsItem


class AiitSpiderSpider(scrapy.Spider):
    name = "aiit_spider"
    allowed_domains = ["www.aiit.edu.cn"]
    start_urls = ['https://www.aiit.edu.cn/node/388']

    def parse(self, response):
        # xpath 进行筛选学校要闻项
        news_selector = response.xpath('//div[@class="content"]/div[contains(@class,"content-div")]')

        for news_item in news_selector:
            news_obj = NewsItem()
            # //div[contains(@class,"title")] 筛选样式中包含了title类的div标签
            news_obj['title'] = news_item.xpath('.//div[contains(@class,"title")]/a/text()').get()
            content_selector = news_item.xpath('./div[@class="contents"]')
            news_obj['summary'] = content_selector.xpath('./p/text()').get()
            news_obj['author'] = content_selector.xpath('./span[1]/text()').get()
            news_obj['read_count'] = content_selector.xpath('./span[2]/text()').get()
            news_obj['pub_date'] = content_selector.xpath('./span[3]/text()').get()
            yield news_obj

        # 找到下一页按钮对应的链接
        next_link = response.xpath('//ul[@id="pagination-digg"]/li/a[text()="下一页"]/@href').get()
        if next_link:
            yield scrapy.Request(next_link, callback=self.parse)

```

<a id="markdown-保存" name="保存"></a>
### 保存

`scrapy crawl 爬虫名称 -o 保存的文件名称 -s FEED_EXPORT_ENCIDING=utf-8`

`FEED_EXPORT_ENCIDING=utf-8` 设置编码，防止打开乱码

```py
(C:\ProgramData\Anaconda3) D:\Codes\Py\hi_scrapy\hi_scrapy>scrapy crawl aiit_spider -o aiit.csv -s FEED_EXPORT_ENCIDING=utf-8

```


<a id="markdown-疑难杂症" name="疑难杂症"></a>
## 疑难杂症

<a id="markdown-permission-denied" name="permission-denied"></a>
### Permission denied

Anaconda Navigator 在 Environments 中进行安装 `Scrapy` ：

```
ERROR conda.core.link:_execute(481): An error occurred while uninstalling package 'defaults::conda-4.4.10-py36_0'.

PermissionError(13, 'Permission denied')
```

安装 `Scrapy` 框架时权限问题，用管理员权限打开 `Anaconda` 进行安装即可。

<a id="markdown-其他工具" name="其他工具"></a>
## 其他工具

<a id="markdown-在线xpath" name="在线xpath"></a>
### 在线xpath

> https://www.toolnb.com/tools/xpath.html


<a id="markdown-xpath和css选择器" name="xpath和css选择器"></a>
### xpath和css选择器


> https://www.jianshu.com/p/489c5d21cdc7





