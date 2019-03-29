import urllib.request
import re

keyname = "手机"
key = urllib.request.quote(keyname)
""
headers = ("User-Agent", "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Mobile Safari/537.36")

opener = urllib.request.build_opener()
opener.addheaders=[headers]
urllib.request.install_opener(opener)

for i in range(1,10):
    url = "https://s.taobao.com/search?q="+key+"&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180717&ie=utf8&bcoffset=4&p4ppushleft=2%2C48&ntoffset=4&s="+str(i*44)
    data = urllib.request.urlopen(url).read().decode("utf-8", "ignore")
    pat='pic_url":"//(.*?)"'
    imagelist = re.compile(pat).findall(data)
    for j in range(0,len(imagelist)):
        thisimage=imagelist[j]
        thisimageurl="http://"+thisimage
        file = "D:/Python/hoilday_codes/sina/2/"+ str(i) +str(j)+".jpg"
        urllib.request.urlretrieve(thisimageurl,filename=file)