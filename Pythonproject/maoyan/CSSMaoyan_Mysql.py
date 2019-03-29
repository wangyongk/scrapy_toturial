# coding=utf-8
import time
import pymysql
import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup


def setMySql():
    db = pymysql.connect(host='localhost', user='root', password='root', port=3306)
    cursor = db.cursor()  # 设置游标
    sql = "CREATE DATABASE movies DEFAULT CHARACTER SET utf8"  # 新建一个movies数据库
    cursor.execute(sql)
    db = pymysql.connect(host='localhost', user='root', password='root', port=3306, db="movies")
    cursor = db.cursor()  # 设置游标
    sql = "CREATE TABLE IF NOT EXISTS movies(movie VARCHAR(255) NOT NULL,actor VARCHAR(255) NOT NULL,score VARCHAR(255) NOT NULL,realse VARCHAR(255) NOT NULL,PRIMARY KEY(movie))"
    cursor.execute(sql)
    db.close()


def getHtml(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0'}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def getdata():
    lmovie = []
    lactor = []
    ltime = []
    lscore = []
    index = 0
    for page in range(0, 100, 10):
        url = 'http://maoyan.com/board/4?offset={}'.format(page)
        Html = getHtml(url)
        if Html is None:
            contine
        Soup = BeautifulSoup(Html, 'lxml')
        names = Soup.select('div.movie-item-info > p:nth-of-type(1)')
        for name in names:
            lmovie.append(name.text)
        actors = Soup.select('div.movie-item-info > p:nth-of-type(2)')
        for actor in actors:
            actor = actor.text
            actor = actor.split('：')[-1]
            lactor.append(actor.strip())
        releasetimes = Soup.select('div.movie-item-info > p:nth-of-type(3)')
        for retime in releasetimes:
            retime = retime.text
            retime = retime.split('：')[-1]
            ltime.append(retime)
        scores = Soup.select('p.score > i:nth-of-type(1)')
        for score in scores:
            lscore.append(score.text)
        frascores = Soup.select('p.score > i:nth-of-type(2)')
        for i in range(len(frascores)):
            lscore[index] += frascores[i].text
            index += 1

        time.sleep(1)

    db = pymysql.connect(host='localhost', user='root', password='root', port=3306, db="movies")
    cursor = db.cursor()  # 设置游标
    sql = "INSERT INTO movies(movie,actor,score,realse) values(%s,%s,%s,%s)"

    for data in zip(lmovie, lactor, lscore, ltime):
        try:
            cursor.execute(sql, data)
            db.commit()
        except:
            db.rollback()
    db.close()

if __name__ == '__main__':
    setMySql()
   # 运行一次即可
    getdata()