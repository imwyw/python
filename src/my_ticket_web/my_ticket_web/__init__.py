import pymysql

'''
Django 3.0 和 pymysql 报以下错误，
mysqlclient 1.3.13 or newer is required; you have 0.7.9.None.
简单粗暴的解决方案，直接修改版本信息
'''
pymysql.version_info = (1, 3, 13, 'final', 0)

pymysql.install_as_MySQLdb()

from django.db.backends.mysql.base import DatabaseWrapper

# 因为Django2.2+ 和 MySQL5.5 的日期时间字段映射有问题，需要调整
DatabaseWrapper.data_types['DateTimeField'] = 'datetime'