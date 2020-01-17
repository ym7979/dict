"""
dict 服务端

功能：请求逻辑处理
并发模型：tcp多进程
"""
from socket import *
from multiprocessing import  Process
import sys
import signal

def handle(connfd):
    while True:
        request=connfd.recv(1024).decode()
        print(request)

# 全局变量
HOST="0.0.0.0"
PORT=7979
ADDR=(HOST,PORT)

def main():
    # 创建监听套接字
    s=socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(3)

    signal.signal(signal.SIGCHLD,signal.SIG_IGN)
    # 循环等待客户端连接
    print("Listen the port 7979")
    while True:
        try:
            c,addr=s.accept()
            print("Connect from",addr)
        except KeyboardInterrupt:
            s.close()
            sys.exit("退出服务端")
        except Exception as e:
            print(e)
            continue


            # 为客户端创建新进程
        p=Process(target=handle,args=(c,))
        p.start()

if __name__ == '__main__':
    main()

