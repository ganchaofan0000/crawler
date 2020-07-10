import urllib.request
import re
from bs4 import BeautifulSoup

html = urllib.request.urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj = BeautifulSoup(html,features="lxml")
with open('../reward/wiki.txt',mode='w',encoding='utf-8') as file:
    for link in bsObj.find("div", {"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$")):
        if 'href' in link.attrs:
            file.write(link.attrs['href']+'\n')