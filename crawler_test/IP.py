import requests
import re
from bs4 import  BeautifulSoup
import bs4
import csv
header={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}

def getIp(list):
    for n in range(1,2):
        url='http://www.89ip.cn/index_{0}.html'.format(n)
        try:
            html=requests.get(url,headers=header)
            html.raise_for_status()
            html.encoding=html.apparent_encoding
        except:
            print('ip获取出错')
        content=html.text
        soup=BeautifulSoup(content,'lxml')
        for tr in soup.find('tbody').children:
            if isinstance(tr, bs4.element.Tag):
                tds = tr.find_all('td')
                list.append([tds[0].string.replace('\n', '').replace('\t', ''),
                             tds[1].string.replace('\n', '').replace('\t', '')])

def checkIp(list):
    goodlist=[]
    url='http://ip.tool.chinaz.com/'#站长查ip
    for a in list:
        try:
            proxies = {'https':'https://' + str(a[0]) + ':' + str(a[1])}
            response = requests.get('http://httpbin.org/get', proxies=proxies,timeout=3)
            if(response.status_code==200):
                goodlist.append([a[0],a[1]])
                print(a[0]+'ip有效')
            else:
                print(a[0]+"ip失效")
        except:
            continue
    return goodlist

def main():
    list=[]
    getIp(list)
    goodlist=checkIp(list)
    #将IP写入csv文件
    with open("ip.csv", "w",encoding='utf-8',newline='') as csvfile:
        writer = csv.writer(csvfile)
        # 先写入columns_name
        writer.writerow(["ip", "端口"])
        writer.writerows(goodlist)

main()