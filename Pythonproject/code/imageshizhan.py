url="https://s.taobao.com/search?q="+key+"&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s="+str(i*44)
import urllib.request
import re
keyname="连衣裙"
key=urllib.request.quote(keyname)
headers=("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0")
opener=urllib.request.build_opener()
opener.addheaders=[headers]
urllib.request.install_opener(opener)
for i in range(1,3):
    url = "https://s.taobao.com/search?q="+key+ "&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s="+str(i*44)
    data=urllib.request.urlopen(url).read().decode("utf-8","ignore")
    pat='pic_url":"//(.*?)"'
    imagelist=re.compile(pat).findall(data)
    for j in range(0,len(imagelist)):
        thisimg=imagelist[j]
        thisimgurl="http://"+thisimg
        file="img/"+str(i)+str(j)+".jpg"
        urllib.request.urlretrieve(thisimgurl,filename=file)