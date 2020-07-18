import requests
import os
import time
import m3u8

headers = {
            'Connection': 'Keep-Alive',
            'Accept': 'text/html, application/xhtml+xml, */*',
            'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
            'User-Agent':'Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-m2 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/6.5.506 UWS/2.10.1.22 Mobile Safari/537.36'
        }
# 获取ts文件地址列表
def get_uri_from_m3u8(url):
        print("正在解析真实下载地址...")
        with open('../Data/temp.m3u8', 'wb') as file:
            file.write(requests.get(url,headers=headers).content)
        m3u8Obj = m3u8.load('../Data/temp.m3u8')
        print("解析完成.")
        return m3u8Obj.segments

# 下载ts视频，并且合成为一个整套的ts文件
def run(url,header_url):
        print("Start!")
        down_path='..\\Data\\ts\\'# ts文件流下载路径根据
        final_path='..\\Data\\'# 合成文件的存储路径
        start_time=time.time()
        uriList = get_uri_from_m3u8(url)# 获取ts文件流的路径列表
        i = 1   # count
        for key in uriList:
            if i%50==0:
                print("休眠5s")
                time.sleep(5)
            try:
                true_url=header_url+key.uri# 获得ts文件流的完整路径
                resp = requests.get(true_url, headers = headers)
            except Exception as e:
                print(e)
                return
            # 命名各个ts流文件
            if i < 10:
                name = ('p00%d.ts' % i)
            elif 10 <= i < 100:
                name = ('p0%d.ts' % i)
            else:
                name = ('p%d.ts' % i)
            # 下载ts流文件
            with open(down_path+name,'wb') as f:
                f.write(resp.content)
                print('正在下载p%d.ts' % i)
            i = i+1
        print("下载完成！总共耗时 %d s" % (time.time()-start_time))
        # 合成ts流文件，使用copy/b的方法
        print("接下来进行合并……")
        exec_str = r'copy/b ' + down_path + r'*.ts ' + final_path + 'hah.ts'
        os.system(exec_str)
        print("合并完成，请您欣赏！")
        # 删除ts流文件
        files = os.listdir(down_path)
        for filena in files:
            del_file = down_path + filena
            os.remove(del_file)
        print("碎片文件已经删除完成")

if __name__=='__main__':
    #m3u8文件地址
    m3u8_url='https://dv-h.phncdn.com/hls/videos/201902/03/205451381/,1080P_4000K,720P_4000K,480P_2000K,240P_400K,_205451381.mp4.urlset/index-f2-v1-a1.m3u8?ttl=1594793230&l=0&hash=4685871e3db15c0227aae929963d3d40'
    # ts文件地址头
    head_url='https://dv-h.phncdn.com/hls/videos/201902/03/205451381/,1080P_4000K,720P_4000K,480P_2000K,240P_400K,_205451381.mp4.urlset/'
    run(m3u8_url,head_url)