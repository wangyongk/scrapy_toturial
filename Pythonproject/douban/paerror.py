import urllib.error
import urllib.request
try:
    urllib.request.urlopen("http://www.jianshu.com/") # 使用http 而不是https
except urllib.error.URLError as e:
    if hasattr(e, "code"):
        print(e.code)
    if hasattr(e, "reason"):
        print(e.reason)

#
# import urllib.request
#
# url = "https://www.jianshu.com/p/abdd3fdfbe44"
# heaers = ("User-Agent", "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Mobile Safari/537.36")
# opener = urllib.request.build_opener()
# opener.addheaders=[heaers]
# data = opener.open(url).read()
# fh = open(r"D:\Python\hoilday_codes\4.html", "wb")
# fh.write(data)
# fh.close()



