from urllib import request, parse
from urllib import error
import re

page = 1
url = 'https://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'

req = request.Request(url)
req.add_header('User-Agent', user_agent)
response = request.urlopen(req)
# bytes变为字符串
content = response.read().decode('utf-8')
pattern = re.compile(r'<div.*?<h2>(.*?)</h2>.*?<span>(.*?)</span>.*?number">(.*?)</i>.*?' +
                         r'"number">(.*?)</i>', re.S)
result = re.findall(pattern, content)
files = open( r"D:/Python/hoilday_codes/sina/1.txt", 'w+', encoding='utf-8')
for item in result:
    author = item[0]
    contant = item[1]
    vote = '赞：' + item[2]
    commit = '评论数：' + item[3]
    infos = vote + ' ' + commit + ' ' + '\n\n'
    print(author)
    print(contant)
    print(infos)
    files.write(author)
    files.write(contant)
    files.write(infos)


"""
from urllib import request, parse
import urllib.request
from urllib import error
import re
for page in range(0,5):
    url = 'https://www.qiushibaike.com/hot/page/' + str(page)
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'

    req = request.Request(url)
    req.add_header('User-Agent', user_agent)
    response = request.urlopen(req)
    # bytes变为字符串
    content = response.read().decode('utf-8')
    pattern = re.compile(r'<div.*?<h2>(.*?)</h2>.*?<span>(.*?)</span>.*?number">(.*?)</i>.*?' +
                         r'"number">(.*?)</i>', re.S)
    result = re.findall(pattern, content)
    files = open( r"D:/Python/hoilday_codes/sina/1.txt", 'w', encoding='utf-8')
    for item in result:
        author = item[0]
        contant = item[1]
        vote = '赞：' + item[2]
        commit = '评论数：' + item[3]
        infos = vote + ' ' + commit + ' ' + '\n\n'
        print(author)
        print(contant)
        print(infos)
        urllib.request.urlretrieve(filename=files)
"""
"""
import urllib.request
import re
import urllib.error
headers=("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0")
opener=urllib.request.build_opener()
opener.addheaders=[headers]
urllib.request.install_opener(opener)
for i in range(1,36):
    url="http://www.qiushibaike.com/8hr/page/"+str(i)
    pagedata=urllib.request.urlopen(url).read().decode("utf-8","ignore")
    pat='<div class="content">.*?<span>(.*?)</span>.*?</div>'
    datalist=re.compile(pat,re.S).findall(pagedata)
    for j in range(0,len(datalist)):
        print("第"+str(i)+"页第"+str(j+1)+"个段子的内容是：")
        print(datalist[j])
"""