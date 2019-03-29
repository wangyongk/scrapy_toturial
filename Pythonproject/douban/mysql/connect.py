import pymysql
# 校验 用户输入的用户名和密码是否正确
# 去数据库里取数据做判断
# 1.连上数据库,获得的conn是连接
conn = pymysql.connect(host="localhost",database="movies",user="root",password="root",charset="utf8")
# 只有连接还不行,还需要获取光标,让我能够输入sql语句并执行
cursor=conn.cursor()    #cursor是光标
# 2.执行sql语句
sql="select * from movies;"    #要执行的sql语句写出来
ret = cursor.execute(sql)   #execute是执行的意思,执行sql语句
# 3.关闭光标和连接
cursor.close()
conn.close()

print("%s row in set (0.00 sec)" % ret)

'''
在这个例题中,mysql相当于是serversocket端,pycharm是客户端
客户端需要先于服务端建立连接,也就是本例题中的第1步
建立好连接后需要建立通信,也就是第2步,把我要执行的sql给执行了,并把
执行结果返回给变量ret,并保存在变量中
通信结束后需要断开连接,但在本例题中也获得了光标,需要把光标也关闭
'''
