#!/usr/bin/env python
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/8 22:00
# @Author  : 蒲天恩
# @File    : do_mysql.py
import pymysql
class DoMysql:
    def __init__(self):
        host = "192.168.126.122"
        port = 3306
        user = "root"
        password = "tiger"
        # 连接数据库
        self.mysql = pymysql.connect(host=host, user=user, password=password, port=port,
                                database="tms", charset="utf8")
        # 创建一个游标查询sql
        self.cursor = self.mysql.cursor(cursor=pymysql.cursors.DictCursor)
    def get_fetchone(self,sql):
        # 执行sql语句
        self.cursor.execute(sql)
        self.mysql.commit()
        # 查询结果
        result = self.cursor.fetchone()
        return result
    def get_fetchall(self,sql):
        # 执行sql语句
        self.cursor.execute(sql)
        self.mysql.commit()
        # 查询结果
        result = self.cursor.fetchall()
        return result
    def get_close(self):
        # 关闭游标 关闭数据库
        self.cursor.close()
        self.mysql.close()
if __name__ == '__main__':
    res = DoMysql().get_fetchall("select * from recipe_sign_info")
    print(res[0]["uniqueid"])
