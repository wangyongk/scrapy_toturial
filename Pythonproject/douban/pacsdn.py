import urllib.request
import re

url = "http://blog.csdn.net/"

headers = ("User-Agent",
           "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Mobile Safari/537.36")
opener = urllib.request.build_opener()

opener.addheaders = [headers]

urllib.request.install_opener(opener)
data = urllib.request.urlopen(url).read().decode("utf-8", "ignore")

pat = '<h2><a href="(.*?)"'

result = re.compile(pat).findall(data)
for i in range(0, len(result)):
    print("第" + str(i) + "爬取")
    thisurl = result[i]
    file = r"D:/Python/hoilday_codes/sina/" + str(i) + ".html"
    urllib.request.urlretrieve(thisurl, file)
    print("成功")