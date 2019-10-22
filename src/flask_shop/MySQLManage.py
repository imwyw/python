# coding:utf-8
import MySQLdb


class MysqlManage():
    def __init__(self):
        # 连接MYsql数据库服务器
        self.db_conn = MySQLdb.connect(
            host="localhost",  # 主机
            user="root",  # 用户名
            password="123456",  # 密码
            db="shopping",  # 数据库
            charset="utf8"  # 编码格式为utf8
        )
        # 获取游标
        self.db_cursor = self.db_conn.cursor()

    # 从mysql中获取商品
    def get_goods_from_mysql(self, id=None):
        if id == None:
            # 执行select语句，获取所有表中的数据
            SQL = "select * from goods"
        else:
            SQL = "select * from goods where id=%d" % id

        self.db_cursor.execute(SQL)
        # 获取所有数据
        g = self.db_cursor.fetchall()  # 得到所有商品的元组
        all_goods = []  # 保存所有商品的列表
        for one in g:
            all_goods.append(list(one))
        return all_goods

    def insert_to_db(self, login_info):  # login_info字典
        SQL = "select * from login where user='%s'" % login_info["user"]
        result = self.db_cursor.execute(SQL)  # 获取到数据
        if result:  # 用户已经存在
            return -1

        SQL = "insert into login values('%s','%s','%s','%s','%s')" % (login_info["user"],
                                                                      login_info["psd"],
                                                                      login_info["country"],
                                                                      login_info["sex"],
                                                                      login_info["like"])
        result = self.db_cursor.execute(SQL)
        if result == 1:
            self.db_conn.commit()
        else:
            self.db_conn.rollback()  # 回滚

        return result

    def login(self, user, psd):
        SQL = "select * from login where user='%s' and psd='%s'" % (user, psd)
        result = self.db_cursor.execute(SQL)  # 获取到数据
        return result


if __name__ == "__main__":
    pass
