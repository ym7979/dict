"""
dict 服务端

功能: 请求逻辑处理
并发模型 : tcp 多进程并发
"""
from socket import *
from multiprocessing import Process
import sys
import signal
from dict_db import Database


# 全局变量
HOST = '0.0.0.0'
PORT = 8000
ADDR = (HOST,PORT)

# 创建数据库连接
db = Database()

# 处理注册
def do_register(connfd,name,passwd):
    if db.register(name,passwd):
        connfd.send(b'OK')
    else:
        connfd.send(b'FAIL')

# 处理登录
def do_login(connfd,name,passwd):
    if db.login(name,passwd):
        connfd.send(b'OK')
    else:
        connfd.send(b'FAIL')

# 查询单词
def do_query(confd,name,word):
    pass

def handle(connfd):
    while True:
        request = connfd.recv(1024).decode()
        tmp = request.split(' ')
        if not request or tmp[0] == 'E':
            return
        elif tmp[0] == 'R':
            # R name passwd
            do_register(connfd,tmp[1],tmp[2])
        elif tmp[0] == 'L':
            # L name passwd
            do_login(connfd, tmp[1], tmp[2])


def main():
    # 创建监听套接字
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(3)

    # 处理僵尸进程
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)

    # 循环等待处理客户端连接
    print("Listen the port 8000")
    while True:
        try:
            c,addr = s.accept()
            print("Connect from",addr)
        except KeyboardInterrupt:
            s.close()
            db.close()
            sys.exit("退出服务端")
        except Exception as e:
            print(e)
            continue

        # 为客户端创建进程
        p = Process(target=handle,args=(c,))
        p.start()

if __name__ == '__main__':
    main()

