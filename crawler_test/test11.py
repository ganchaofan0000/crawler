from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random
from crawler_test import MySqlConnection as mysql

random.seed(datetime.datetime.now())

def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org" + articleUrl)
    bsObj = BeautifulSoup(html,features='lxml')
    title = bsObj.find("h1").get_text()
    content = bsObj.find("div", {"id": "mw-content-text"}).find("p").get_text()
    mysql.store(title, content)
    return bsObj.find("div", {"id": "bodyContent"}).findAll("a",
                                                        href=re.compile("^(/wiki/)((?!:).)*$"))


links = getLinks("/wiki/Kevin_Bacon")

try:
    while len(links) > 0:
        newArticle = links[random.randint(0, len(links) - 1)].attrs["href"]
        print(newArticle)
        links = getLinks(newArticle)
finally:
    mysql.cur.close()
    mysql.conn.close()
