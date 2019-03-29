import urllib.request
urllib.request.urlretrieve("https://blog.csdn.net/",
filename=r"D:\Python\hoilday_codes\1.html")


"""
关于ModuleNotFoundError: No module named 'urllib.request'; 
'urllib' is not a package的问题

.重名导致urllib包的无效化
    （1）你正在import urllib的文件命名就是urllib.py
    （2）你正在使用的文件的文件夹目录下有一个叫urllib.py的文件，
    导致你import urllib实际上导入的是当前目录下的urllib.py文件
    ，而不是库里的urllib。
"""
