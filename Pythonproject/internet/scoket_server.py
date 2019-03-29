import socket
import threading
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("0.0.0.0",8000))
server.listen()
def handle_sock(sock,addr):
    while True:
        data = sock.recv(1024)
        b=data.decode("utf-8")
        print(data.decode("utf-8"))
        a = input("")
        sock.send(a.encode("utf8"))
while True:
    sock, addr = server.accept() #接受不同client 端的
    client_thread=threading.Thread(target=handle_sock,args=(sock,addr)) #把sock 加入线程内
    client_thread.start() #启动线程
