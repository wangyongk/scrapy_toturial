import urllib.request
import re
# 正则表达式
# aaaaa  aa aab aba aabb
#a(.*?)b
data = urllib.request.urlopen("http://news.sina.com.cn/").read()
data2 = data.decode("utf-8", "ignore")
pat = 'href="(http://news.sina.com.cn/.*?)"'
allurl=re.compile(pat).findall(data2)

for i in range(0,len(allurl)):
    try:
        print("第"+str(i)+"爬取")
        thisurl=allurl[i]
        file= r"D:/Python/hoilday_codes/sina/"+str(i)+".html"
        urllib.request.urlretrieve(thisurl,file)
        print("成功")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)




"""


python中文件路径的问题
慎用中文路径！慎重中文路径！！慎用中文路径！！！

使用斜杠“/”: "c:/test.txt"… 不用反斜杠就没法产生歧义了 
将反斜杠符号转义: "c:\\test.txt"… 因为反斜杠是转义符，
所以两个"\\"就表示一个反斜杠符号 
使用Python的raw string: r"c:\test.txt" … 
python下在字符串前面加上字母r，
表示后面是一个原始字符串raw string，
不过raw string主要是为正则表达式而不是windows路径设计的
，所以这种做法尽量少用，可能会出问题。
"""