import pymysql

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

    def register(self,name,passwd):
        sql="select name from user where name='%s';"%name
        self.cur.execute(sql)
        # 如果查到内容返回False
        if self.cur.fetchone():
            return False
        # 插入数据库
        sql="insert into user (name,passwd) values (%s,%s);"
        try:
            self.cur.execute(sql,[name,passwd])
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False

    def login(self,name,passwd):
        pass

if __name__ == '__main__':
    db = Database()
    db.register('Tom','123')
    db.login('Tom','123')
    db.close()