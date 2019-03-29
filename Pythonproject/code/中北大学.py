from bs4 import BeautifulSoup
from datetime import datetime
import requests
url="http://www.nuc.edu.cn/"
res=requests.get(url)
res.encoding="utf-8"

soup=BeautifulSoup(res.text,"html.parser")
for news in soup.select("div"):
    if len(news.select(".time")) > 0:
        print(news.select(".time"))