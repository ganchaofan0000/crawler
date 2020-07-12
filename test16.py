from selenium import webdriver
import requests



ip='118.24.155.27:8118'
#requests测试IP
proxy1={"http":"http://"+ip,"https":"https://"+ip}
try:
    html=requests.get('http://wenshu.court.gov.cn/', proxies=proxy1)
except:
    print('requests代理IP失效')
else:
    print('requests代理IP有效')

#chrome测试IP
chromeOptions = webdriver.ChromeOptions()
proxy2='--proxy-server=http://'+ip
chromeOptions.add_argument(proxy2)
# 一定要注意，=两边不能有空格，不能是这样--proxy-server = http://202.20.16.82:10152
try:
    browser = webdriver.Chrome(options=chromeOptions)
# 查看本机ip，查看代理是否起作用

    browser.get("http://wenshu.court.gov.cn/")
except:
    print('chrome代理IP失效')
else:
    print('chrome代理IP有效')
    print(browser.page_source)

browser.quit()