import pymysql
import requests
from bs4 import BeautifulSoup
import bs4
import re
def getuniveserty(list,url):
    #获取html
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
    except:
        print("html获取失败")

    soup=BeautifulSoup(r.text,"lxml")
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds=tr.find_all('td')
            list.append([tds[0].string,tds[1].string,tds[4].string])

def inmysql(lists):
    conn = pymysql.connect(host='localhost', user='root', passwd='11142000lg', database='school', charset='utf8')
    cur = conn.cursor()
    for list in lists[:100]:
        cur.execute("INSERT INTO univeserty (u_rank, name,score) VALUES ("+list[0]+",\""+list[1]+"\","+list[2]+")")
        cur.connection.commit()

    conn.close()
    cur.close()
    print('数据爬取成功')

url='http://www.zuihaodaxue.com/zuihaodaxuepaiming2020.html'
lists=[]
getuniveserty(lists,url)
inmysql(lists)
#print(lists[:10])






