from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
content=BeautifulSoup(html,features="lxml")

list=content.findAll("span",{"class":"green"})
allText = content.findAll(id="text")
print(allText[0].get_text())
print(len(allText))
#for name in list:
#    print(name)