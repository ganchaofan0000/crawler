import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
header={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}

def getnamepage(name):
    drive.get('http://image.baidu.com/')
    search_box=drive.find_element_by_id('kw')
    search_box.send_keys(name)
    search_box.send_keys(Keys.ENTER)
    time.sleep(2)



def getimageurl(list,num):
    ele=drive.find_element_by_id('sizeFilter')
    ActionChains(drive).move_to_element(ele).perform()
    time.sleep(1)
    ele1=drive.find_element_by_xpath('//*[@id="sizeFilter"]/div/ul/li[4]')
    #ActionChains(drive).move_to_element(ele1).perform()
    ele1.click()
    time.sleep(1)
    ele2=drive.find_element_by_xpath('//*[@id="imgid"]/div/ul/li[1]/div/a/img')
    ele2.click()
    #实现跳转，由于百度图片的展示界面存在页面的自己的偷偷变化
    drive.switch_to.window(drive.window_handles[1])
    time.sleep(1)
    count=0
    while count<num:
        ele3=drive.find_element_by_xpath('//*[@id="currentImg"]')
        url=ele3.get_attribute('src')
        if url:
            count+=1
            list.append(url)
            ele2=drive.find_element_by_xpath('//*[@id="container"]/span[2]')
            ele2.click()
            time.sleep(1)
        else:
            ele2 = drive.find_element_by_xpath('//*[@id="container"]/span[2]')
            ele2.click()
            time.sleep(1)

def getimage(list):
    print(list)
    x=0
    for url in list:
        x+=1
        try:
            path='../image/%d.jpg'%x
            image=requests.get(url)
            time.sleep(0.5)
            with open(path,'wb',) as f:
                f.write(image.content)
                print(str(x)+'.jpg'+'爬取成功！')
                time.sleep(0.5)
        except:
            print(str(x)+'.jpg'+'爬取失败！')

if __name__ == '__main__':
    drive=webdriver.Chrome()
    #proxy=randomIp.getIp()
    imagename='美女'
    num=20
    pageUrlList=[]
    getnamepage(imagename)
    getimageurl(pageUrlList,num)
    getimage(pageUrlList)
    drive.close()
