import hashlib  # 加密

import pymysql


def change_passwd(passwd):
    hash = hashlib.md5()  # 使用md5对象加密
    hash.update(passwd.encode())#加密（只可用字节串）
    return hash.hexdigest()


class Database:
    def __init__(self):
        # 连接数据库
        self.db = pymysql.connect(host='localhost',
                                  port=3306,
                                  user='root',
                                  password='123456',
                                  database='dict',
                                  charset='utf8')

        # 生成游标对象 (操作数据库,执行sql语句,获取结果)
        self.cur = self.db.cursor()

    def close(self):
        # 关闭游标和数据库连接
        self.cur.close()
        self.db.close()

    def register(self, name, passwd):  # 注册
        sql = "select name from user where name = '%s';" % name
        self.cur.execute(sql)
        # 如查到内容，返回FALSE
        if self.cur.fetchone():
            return False
        # 插入数据库
        sql = "insert into user (name,password) values(%s,%s);"
        passwd=change_passwd(passwd)#在数据库中密码加密
        try:
            self.cur.execute(sql, [name, passwd])
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False

    def login(self, name, passwd):  # 登录
        sql = "select name from user " \
              "where name=%s and password=%s;"
        passwd = change_passwd(passwd)
        self.cur.execute(sql,[name,passwd])
        if self.cur.fetchone():
            return True
        else:
            return  False


if __name__ == '__main__':
    db = Database()
    db.register('Tom', '123')
    db.login('Tom', '123')
    db.close()
