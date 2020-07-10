import xlwt
import requests
from selenium import webdriver

def getData(lists):
    drive.get('http://quote.eastmoney.com/center/gridlist.html')
    listview=drive.find_element_by_class_name('listview full')

    print()

def data_write(lists):
    f = xlwt.Workbook()
    sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)  # 创建sheet
    path=''
    # 将数据写入第 i 行，第 j 列
    i = 0
    for data in lists:
        for j in range(len(data)):
            sheet1.write(i, j, data[j])
        i = i + 1

    f.save(path)  # 保存文件

drive=webdriver.Chrome('../depends/chromedriver.exe')
def main():

    lists=[]
    getData(lists)
    data_write(lists)
    drive.close()

