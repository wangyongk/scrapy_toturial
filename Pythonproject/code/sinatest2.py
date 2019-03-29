import requests
res=requests.get("https://news.sina.com.cn/")
res.encoding='utf-8'
print(res.text)