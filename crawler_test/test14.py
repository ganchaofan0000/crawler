
import re
from crawler_test.taobao_login import UsernameLogin
from crawler_test.taobaoformations import *
headers = {
    'Accept': 'application/javascript, */*;q=0.8',
    'Accept-Language':'zh-CN',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Accept-Encoding': 'gzip, deflate',
        }
# 获取网页信息
def getHTMLText(url,session):
    try:
        # 获取网页信息
        r = session.get(url, timeout=30,headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

# 得到商品信息
def parsePage(ilt, html):
    try:
        # 获取价格
        plt = re.findall(r'\"price\"\:\"[\d\.]*\"', html)
        # 获取商品title
        tlt = re.findall(r'\"title\"\:\".*?\"', html)
        # 获取商品月销量
        mslt = re.findall(r'\"month_sales\"\:\"[\d\.]*\"', html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            monthsales = eval(mslt[i].split(':')[1])
            ilt.append([price, title, monthsales])
    except:
        print("")

# 打印商品信息
def printGoodsList(ilt):
    # 格式化打印
    tplt = "{:4}\t{:8}\t{:16}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称", "月销量"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1], g[2]))

# 主函数
def main():
    # 登录淘宝
    ul = UsernameLogin(loginId, umidToken, ua, password2)
    ul.login()
    session = ul.session
    # 商品名
    goods = '书包'
    depth = 3
    start_url = 'https://s.taobao.com/search?q=' + goods
    # 存放商品信息的列表
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(48 * i)
            html = getHTMLText(url,session)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)

# 测试
main()
