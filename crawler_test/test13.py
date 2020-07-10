import re
import requests

def getHTMLtext(url):
    #headers={'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'}
    # try:
        html=requests.get(url)
        #print(html.request.headers)
        html.raise_for_status()
        html.encoding=html.apparent_encoding
        #print(html.text)
        return html.text
    # except:
    #     print("页面获取错误")
    #     return ""


def getData(list,html):
    try:
        titles=re.findall(r'\"raw_title\":\".*?\"',html)
        prices=re.findall(r'\"view_price\":\"[\d\.]*\"',html)
        #print(len(titles))
        for i in range(len(titles)):
            price=eval(prices[i].split(':')[1])
            title=eval(titles[i].split(':')[1])
            list.append([price,title])
    except:
        print("页面解析错误")


def printData(list):
    tplt='{:4}\t{:8}\t{:16}'
    print(tplt.format('序号','价格','描述'))
    count=0
    for a in list:
        count=count+1
        print(tplt.format(count,a[0],a[1]))

def main():
    Baseurl='https://s.taobao.com/search?q='
    list=[]
    name='书包'
    depth=2
    html1 = getHTMLtext('https://s.taobao.com/search?q=书包&s=0')
    print(html1)
    for i in range(depth):
        url=Baseurl+name+'&s='+str(44*i)
        #print(url)
        html=getHTMLtext(url)
        getData(list,html)
    printData(list)


main()
