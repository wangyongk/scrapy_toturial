import socket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("127.0.0.1",8000))
while True: #调用了while循环并且是True代表永远不会断开
    a=input() #调用了input 语句
    client.send(a.encode("utf-8")) # 客户端socket 发送数据给服务端
    data = client.recv(1024) # 接受的数据
    print(data.decode("utf8"))
