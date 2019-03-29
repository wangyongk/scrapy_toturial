import re
import requests
import urllib
data=urllib.request.urlopen("https://news.sina.com.cn/").read()
data2=data.decode("utf-8","ignore")
pat='href="(https://news.sina.com.cn/.*?)"'
allurl=re.compile(pat).findall(data2)
for i in range(0,len(allurl)):
    try:
        print("第"+str(i)+"次爬取")
        thisurl=allurl[i]
        file="D:/Python/hoilday_codes/sina/"+str(i)+".html"
        urllib.request.urlretrieve(thisurl,file)
        print("成功")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)


