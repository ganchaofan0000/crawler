import xlwt
from selenium import webdriver
import time
def getData(lists):
    drive.get('http://quote.eastmoney.com/center/gridlist.html')
    listview=drive.find_element_by_xpath('//*[@id="table_wrapper"]/div')
    ths=listview.find_elements_by_tag_name('th')
    namelist=[]
    for i in range(len(ths)-1):
        if(i!=3):
            namelist.append(ths[i].get_attribute('textContent'))
    lists.append(namelist)
    pagecount=1
    while pagecount<=2:
        listview = drive.find_element_by_xpath('//*[@id="table_wrapper"]/div')
        trs = listview.find_element_by_tag_name('tbody').find_elements_by_tag_name('tr')
        datalist=[]
        for tr in trs:
            tds=tr.find_elements_by_tag_name('td')
            for j in range(len(tds) - 1):
                if (j != 3):
                    datalist.append(tds[j].get_attribute('textContent'))
            lists.append(datalist)
            datalist=[]
        nextpage=drive.find_element_by_xpath('//*[@id="main-table_paginate"]/a[2]')
        pagecount+=1
        nextpage.click()
        time.sleep(3)

def data_write(lists):
    f = xlwt.Workbook()
    sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)  # 创建sheet
    path='../Data/沪深A股.xls'
    # 将数据写入第 i 行，第 j 列
    i = 0
    for data in lists:
        for j in range(len(data)):
            sheet1.write(i, j, data[j])
        i = i + 1

    f.save(path)  # 保存文件


def main():
    lists=[]
    getData(lists)
    data_write(lists)
    drive.close()

drive=webdriver.Chrome()
main()