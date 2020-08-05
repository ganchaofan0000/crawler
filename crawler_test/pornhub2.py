import requests
import execjs
from lxml import etree
import re
header = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
        }
# 获得网页内容
def gethtml(url):
    html=requests.get(url,headers=header)
    html_text=html.text
    return html_text

# 爬取视频列表
def parsejs(htmlContent):
    # 先爬核心段内容，以便获取videoId
    all = etree.HTML(htmlContent).xpath('//*[@id="player"]')[0]
    all_text=etree.tostring(all).decode('utf-8')
    # 爬取videoId
    videoId = re.findall('data-video-id="(.+?)"',all_text)[-1]
    # 再爬js内容
    js = etree.HTML(htmlContent).xpath('//*[@id="player"]/script[1]/text()')[0]
    # 执行js
    # 需要补充完整
    str1="var loadScriptVar=[];var loadScriptUniqueId=[];var playerObjList = {};" + js
    jscontext = execjs.compile(str1)
    # 获取flashvars_变量
    res = jscontext.eval('flashvars_'+videoId)
    # 得到1080p、720p等视频信息列表
    # print(res['mediaDefinitions'])
    return res['mediaDefinitions']

# 下载视频
def downloadvideo(url_list):
    # 获得最高清晰度的MP4格式的视频
    url=url_list[0].get('videoUrl')
    base_path='C:\\Users\\Administrator\\Downloads\\Video\\'
    # 下载视频
    print('开始下载')
    video=requests.get(url,headers=header)
    name=url.split('?')[0].split('/')[-1]
    vedio_path=base_path+name
    with open(vedio_path,'wb') as f:
        f.write(video.content)
    print('下载完成')

# 主函数
def main():
    # p站视频链接
    url='https://cn.pornhub.com/view_video.php?viewkey=ph58838af822d2b'
    html_text=gethtml(url)
    url_list=parsejs(html_text)
    downloadvideo(url_list)

main()