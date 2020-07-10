from selenium import webdriver
from crawler_test import randomIp
chromeOptions = webdriver.ChromeOptions()

# 设置代理
#print(randomIp.getChromeIp())
#chromeOptions.add_argument(randomIp.getChromeIp())
chromeOptions.add_argument('--proxy-server=http://132.232.32.50:8888')
# 一定要注意，=两边不能有空格，不能是这样--proxy-server = http://202.20.16.82:10152
browser = webdriver.Chrome(options=chromeOptions)

# 查看本机ip，查看代理是否起作用
browser.get("http://httpbin.org/ip")
print(browser.page_source)

# 退出，清除浏览器缓存
browser.quit()