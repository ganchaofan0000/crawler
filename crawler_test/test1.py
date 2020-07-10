from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen("http://www.pythonscraping.com/pages/page3.html")
text=BeautifulSoup(html,features="lxml")
content=text.find("table",{"id":"giftList"}).children
for a in content:
    print(a)

