import urllib.request
import re
import urllib.error
headers=("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0")
opener=urllib.request.build_opener()
opener.addheaders=[headers]
urllib.request.install_opener(opener)
comid="6165793094371986503"
url="http://video.coral.qq.com/filmreviewr/c/upcomment/0dfpyvfa7tp0ewe?commentid="+comid+"&reqnum=3&callback=jQuery1120026430801920245595_1478436999932&_=1478436999935"
for i in range(0,100):
    data=urllib.request.urlopen(url).read().decode()
    patnext='"last":"(.*?)"'
    nextid=re.compile(patnext).findall(data)[0]
    patcom='"content":"(.*?)",'
    comdata=re.compile(patcom).findall(data)
    for j in range(0,len(comdata)):
        print("------第"+str(i)+str(j)+"条评论内容是:")
        print(eval('u"'+comdata[j]+'"'))
        with open('腾讯视频.txt','a',encoding='utf-8') as f:
            f.write(eval('u"'+comdata[j]+'"'))
    url="http://video.coral.qq.com/filmreviewr/c/upcomment/0dfpyvfa7tp0ewe?commentid="+nextid+"&reqnum=3&callback=jQuery1120026430801920245595_1478436999932&_=1478436999935"