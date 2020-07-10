import  requests
import time
#获得随机IP及端口
header={'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'}
def getrequestsIp():
    response = requests.get('http://pubproxy.com/api/proxy?type=http',headers=header
                            ,proxies={'https':'https://113.254.178.224:8383','http':'http://113.254.178.224:8383'})
    ip=response.json().get("data")[0].get("ipPort")
    proxy={'https':'https://' +ip,'http':'http://' + ip}
    return proxy

def getChromeIp():
    response = requests.get('http://pubproxy.com/api/proxy?type=http', headers=header
                            , proxies={'https': 'https://113.254.178.224:8383', 'http': 'http://113.254.178.224:8383'})
    ip=response.json().get("data")[0].get("ipPort")
    proxy='--proxy-server=http://'+ip
    return proxy