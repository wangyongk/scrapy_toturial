import pymysql
import numpy as np
import pandas as pda
import matplotlib.pylab as plt
# 导入数据
coon=pymysql.connect(host="127.0.0.1",user="root",passwd="123456",db="myhexun")
sql="select * from myhexun"
data=pda.read_sql(sql,coon)
ch=data[u"comment"]/data["hits"]
data[u"点评比"]=ch
file="./5.csv"
data.to_csv(file,index=False,encoding="utf_8_sig") #不使用encoding会出现乱码
#print(data.describe())
