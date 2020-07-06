import pymysql
from scrapy.utils.project import get_project_settings


class TrainScrapyPipeline(object):
    '''
    车次信息管道，全国排班表
    '''
    # 待插入列表
    train_list = []

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
        value_tuple = (
            item['train_date'], item['train_type'], item['train_no'],
            item['train_code'], item['start_station'], item['end_station']
        )
        self.train_list.append(value_tuple)
        # 每多少条记录执行一次提交
        batch_count = 100
        if len(self.train_list) == batch_count:
            self.bulk_add_news(self.train_list)
            # 批量插入完成后，清空待插入列表
            del self.train_list[:]
        return item

    # 3、关闭爬虫spider，此处释放资源关闭数据库连接
    def close_spider(self, spider):
        # 防止关闭爬虫时，待插入列表中仍有记录需要插库
        if len(self.train_list) > 0:
            self.bulk_add_news(self.train_list)
        self.db_conn.close()

    # 批量插入数据
    def bulk_add_news(self, value_list):
        try:
            sql = "insert into t_train(train_date,train_type,train_no,train_code,start_station,end_station) values (%s,%s,%s,%s,%s,%s)"
            self.db_cur.executemany(sql, value_list)
            self.db_conn.commit()
        except Exception as ex:
            print(ex)
            self.db_conn.rollback()
