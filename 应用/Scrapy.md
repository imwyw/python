<!-- TOC -->

- [Scrapy](#scrapy)
    - [安装和环境](#安装和环境)
    - [开始项目](#开始项目)
        - [创建第一个spider](#创建第一个spider)
        - [响应解析](#响应解析)
        - [创建模型](#创建模型)
        - [保存](#保存)
    - [Pipeline-管道处理](#pipeline-管道处理)
        - [自定义Pipeline](#自定义pipeline)
            - [process_item(item, spider)](#process_itemitem-spider)
            - [open_spider(self, spider)](#open_spiderself-spider)
            - [close_spider(spider)](#close_spiderspider)
            - [from_crawler(cls, crawler)（了解）](#from_crawlercls-crawler了解)
            - [创建Pipeline](#创建pipeline)
        - [Mysql持久化](#mysql持久化)
            - [处理插入数据](#处理插入数据)
            - [批量插入数据](#批量插入数据)
    - [资源下载](#资源下载)
        - [图片保存](#图片保存)
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
> https://wiki.jikexueyuan.com/project/scrapy/start-scrapy.html

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

<a id="markdown-pipeline-管道处理" name="pipeline-管道处理"></a>
## Pipeline-管道处理
`Item Pipeline` 的主要功能有如下4点：
* 清理HTML数据。
* 验证爬取数据，检查爬取字段。
* 查重并丢弃重复内容。
* 将爬取结果保存到数据库。

<a id="markdown-自定义pipeline" name="自定义pipeline"></a>
### 自定义Pipeline

我们可以自定义Item Pipeline，只需要实现指定的方法，其中必须要实现的一个方法是： `process_item(item, spider)`

另外还有如下几个比较实用的方法：

* `open_spider(spider)`
* `close_spider(spider)`
* `from_crawler(cls, crawler)`


<a id="markdown-process_itemitem-spider" name="process_itemitem-spider"></a>
#### process_item(item, spider)

`process_item()` 是必须要实现的方法，被定义的 `Item Pipeline` 会默认调用这个方法对Item进行处理。

比如，我们可以进行数据处理或者将数据写入到数据库等操作。

它必须返回Item类型的值或者抛出一个DropItem异常。

process_item()方法的参数有如下两个：
* item，是Item对象，即被处理的Item；
* spider，是Spider对象，即生成该Item的Spider。

process_item()方法的返回类型归纳如下：
* 如果它返回的是Item对象，那么此Item会被低优先级的Item Pipeline的process_item()方法处理，直到所有的方法被调用完毕；
* 如果它抛出的是DropItem异常，那么此Item会被丢弃，不再进行处理。

<a id="markdown-open_spiderself-spider" name="open_spiderself-spider"></a>
#### open_spider(self, spider)
open_spider()方法是在Spider开启的时候被自动调用的。

在这里我们可以做一些初始化操作，如开启数据库连接等。

其中，参数spider就是被开启的Spider对象。

<a id="markdown-close_spiderspider" name="close_spiderspider"></a>
#### close_spider(spider)
close_spider()方法是在Spider关闭的时候自动调用的。

在这里我们可以做一些收尾工作，如关闭数据库连接等。

其中，参数spider就是被关闭的Spider对象。

<a id="markdown-from_crawlercls-crawler了解" name="from_crawlercls-crawler了解"></a>
#### from_crawler(cls, crawler)（了解）
from_crawler()方法是一个类方法，用@classmethod标识，是一种依赖注入的方式。

它的参数是crawler，通过crawler对象，我们可以拿到Scrapy的所有核心组件，

如全局配置的每个信息，然后创建一个Pipeline实例。参数cls就是Class，最后返回一个Class实例。

<a id="markdown-创建pipeline" name="创建pipeline"></a>
#### 创建Pipeline
可以在默认的【pipelines.py】文件中添加 `Pipeline` 类，也可以选择新建文件编写 `Pipeline` 类。

多个 `Pipeline` 的执行有先后顺序，取决于 【settings.py】中的设置：

```py
# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'hi_scrapy.pipelines.HiScrapyPipeline': 300,
    'hi_scrapy.pipelines.RedisPipeline': 301
}
```

其中数字越小优先级越高。

<a id="markdown-mysql持久化" name="mysql持久化"></a>
### Mysql持久化

<a id="markdown-处理插入数据" name="处理插入数据"></a>
#### 处理插入数据

在 `mysql` 中创建数据库 `aiit_db`，执行脚本创建表：

```sql
DROP TABLE IF EXISTS `aiit_news`;
CREATE TABLE `aiit_news` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) DEFAULT NULL,
  `summary` varchar(1000) DEFAULT NULL,
  `author` varchar(50) DEFAULT NULL,
  `read_count` int(11) DEFAULT NULL,
  `pub_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

取消【setting.py】中关于 `pipeline` 的配置：

```py
# 取消该部分注释，否则无法处理数据
# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'hi_scrapy.pipelines.HiScrapyPipeline': 300,
}

# 增加部分 数据库连接配置
MYSQL_HOST = 'localhost'
MYSQL_DBNAME = 'aiit_db'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWD = '123456'
```

修改【pipelines.py】文件：

```py
from scrapy.utils.project import get_project_settings
import pymysql


class HiScrapyPipeline(object):
    def __init__(self):
        pass

    # 打开数据库
    def open_spider(self, spider):
        settings = get_project_settings()
        self.db_conn = pymysql.connect(
            host=settings['MYSQL_HOST'],
            port=settings['MYSQL_PORT'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8'
        )
        self.db_cur = self.db_conn.cursor()

    # 爬取结束，提交sql，关闭连接
    def close_spider(self, spider):
        self.db_conn.commit()
        self.db_conn.close()

    # 对数据进行处理
    def process_item(self, item, spider):
        self.add_news(item)
        return item

    # 新增新闻业务
    def add_news(self, item):
        values = (item['title'], item['summary'], item['author'], item['read_count'], item['pub_date'])
        sql = "insert into aiit_news(title,summary,author,read_count,pub_date) values (%s,%s,%s,%s,%s)"

        # 每插入一条就提交
        self.db_cur.execute(sql, values)
        self.db_conn.commit()


```

<a id="markdown-批量插入数据" name="批量插入数据"></a>
#### 批量插入数据
当数据量较大时，每条记录进行一次插库操作比较影响性能，效率较低，我们采用 `executemany` 进行批量插入提高效率：

新增待插入列表，当达到一定数量时，进行批量插入，并提交，代码如下：

```py
from scrapy.utils.project import get_project_settings
import pymysql


class HiScrapyPipeline(object):
    # 用于批量插入时，保存批量插入的列表
    news_list = []

    def __init__(self):
        pass

    # 打开数据库
    def open_spider(self, spider):
        settings = get_project_settings()
        self.db_conn = pymysql.connect(
            host=settings['MYSQL_HOST'],
            port=settings['MYSQL_PORT'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8'
        )
        self.db_cur = self.db_conn.cursor()

    # 爬取结束，提交sql，关闭连接
    def close_spider(self, spider):
        self.db_conn.commit()
        self.db_conn.close()

    # 对数据进行处理
    def process_item(self, item, spider):
        self.news_list.append(
            (item['title'], item['summary'], item['author'], item['read_count'], item['pub_date'])
        )

        # 每页8条记录
        page_count = 8
        if len(self.news_list) == page_count:
            self.bulk_add_news(self.news_list)
            # 清空待插入列表
            del self.news_list[:]

        return item

    # 批量插入操作
    def bulk_add_news(self, value_list):
        try:
            sql = "insert into aiit_news(title,summary,author,read_count,pub_date) values (%s,%s,%s,%s,%s)"
            self.db_cur.executemany(sql, value_list)
            self.db_conn.commit()
        except:
            self.db_conn.rollback()
        pass

```

<a id="markdown-资源下载" name="资源下载"></a>
## 资源下载

<a id="markdown-图片保存" name="图片保存"></a>
### 图片保存



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


---

参考引用：

[Scrapy框架的使用之Item Pipeline的用法](https://juejin.im/post/5af95280f265da0ba17ca1ba)


