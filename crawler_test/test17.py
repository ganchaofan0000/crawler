import re

if __name__ == '__main__':

    #用于测试的字符串
    str = "<h1>liuwei</h1><a href='www.baidu.com'></a><h1>zhangbin</h1><a href='www.love.com'></a>"

    regex = re.compile("<h1>(.+?)</h1><a(.+?)></a>")      #定义了两个group,两个括号

    res = regex.search(str)                               #search用于找到第一个满足匹配的子串，并返回
    print(res)
    print("group1:%s" %res.group(1))                      #输出结果为liuwei
    print("group2:%s" %res.group(2))                      #输出结果为href='www.baidu.com'

    res1 = regex.findall(str)                             #findall输出所有满足的匹配
    print("res1:%s" %res1)

    print(res1[0])                                        #输出结果为('liuwei', 'www.baidu.com')
    print(res1[1])                                        #输出结果为('zhangbin, 'www.love.com')