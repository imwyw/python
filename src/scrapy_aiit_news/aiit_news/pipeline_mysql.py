import pymysql
from scrapy.utils.project import get_project_settings


# 自定义 pipeline
class MysqlPipeline(object):
    # 待插入列表
    news_list = []

    # 1、启用 spider，此方法内适合写入数据库的连接
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

    # 2、处理 item 数据，适合进行数据的操作，比如插库
    def process_item(self, item, spider):
        value_tuple = (item['title'], item['summary'], item['author'], item['read_count'], item['pub_date'])
        self.news_list.append(value_tuple)
        # 每一页有 8 条记录
        page_count = 8
        if len(self.news_list) == page_count:
            self.bulk_add_news(self.news_list)
            # 批量插入完成后，清空待插入列表
            del self.news_list[:]
        return item

    # 3、关闭爬虫spider，此处释放资源关闭数据库连接
    def close_spider(self, spider):
        # 防止关闭爬虫时，待插入列表中仍有记录需要插库
        if len(self.news_list) > 0:
            self.bulk_add_news(self.news_list)
        self.db_conn.close()

    # 批量插入数据
    def bulk_add_news(self, value_list):
        try:
            sql = "insert into aiit_news(title,summary,author,read_count,pub_date) values (%s,%s,%s,%s,%s)"
            self.db_cur.executemany(sql, value_list)
            self.db_conn.commit()
        except Exception as ex:
            print(ex)
            self.db_conn.rollback()
