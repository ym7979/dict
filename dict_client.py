"""
dict 客户端
"""
from getpass import getpass #隐藏密码
from socket import *

# 服务器地址
ADDR = ("127.0.0.1", 7979)
# 套接字作为全局变量
s = socket()
s.connect(ADDR)


# 注册功能
def do_register():
    while True:
        name = input("User:")
        passwd = getpass("Password:")
        passwd1 = getpass("Again:")
        if passwd != passwd1:
            print("两次密码不一致")
        if (" " in name) or (" " in passwd):
            print("用户名和密码不能有空格")
            continue

        msg = "R %s %s" % (name, passwd)
        s.send(msg.encode())  # 发请求
        data = s.recv(128).decode()  # 接收反馈
        if data == "OK":
            print("注册成功")
        else:
            print("注册失败")
        return



# 网路连接
def main():
    while True:
        print("""
        =====================Welcome======================
        1.注册             2.登录           3.退出 
        ==================================================      
        """)
        cmd = input("输入选项：")
        s.send(cmd.encode())
        if cmd == "1":
            do_register()  # 注册


if __name__ == '__main__':
    main()
