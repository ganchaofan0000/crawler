# 说明：loginId、umidToken、ua、password2这4个参数都是从浏览器登录页面复制过来的。
# 如何复制4个参数：
# # 1、浏览器打开：https://login.taobao.com/member/login.jhtml
# # 2、F12打开调试窗口，左边有个Preserve log，勾选上，这样页面跳转请求记录不会丢失
# # 3、输入用户名密码登录，然后找到请求：newlogin/login.do 这个是登录请求
# # 4、复制上面的4个参数到下面，基本就可以运行了
# # 5、如果运行报错可以微信私聊猪哥，没加猪哥微信的可以关注猪哥微信公众号[裸睡的猪]，回复：加群

# 淘宝用户名：手机 用户名 都可以
loginId = '13687900235'
# 改版后增加的参数，后面考虑解密这个参数
umidToken = '007c3b073388b80bcb08bd2924e24e787fee1526',
# 淘宝重要参数，从浏览器或抓包工具中复制，可重复使用
ua = '125#cd2caaHCcWBm4fucKN4hl1dSuwm73O3GWHZWpz7CH5O15Zy0sS1ACcVb' \
     'tzUNYDXk3rMl6G+1BF8jQYDCzwBvPAFZgxjuxNMDYEx/6PAyuRbwtXGTAGqXlc4Iur' \
     'jF0Bq10XAm6pDEaMHkambeqtvc4jDPV50JeyG6yxSRBNGhmH3qnPP51Dc1VKpwPDyxXb' \
     'GbWMTRx1ob6b+6vttuWW4yD+KFo/IoKk6dXF4bgUokDOz8OrtNeUvd/p/xOw1nqXiccgapEg' \
     'sSUXoSvHikGaeiiTi/t8sSGvLbGcTN3ylSiGcfG31xGVCiivEftY7fGDSbGcVJEjS4cXrs0j//pd+I' \
     'iahGA+OgIluOX1wvfFQNI00wUQNLMTx4qkcoGwJREg/FhQk2JNTDd7KvfKPUi4RCr3oMQnPdBP1EpWltjMh' \
     'SaHvbFz+gWMCfXm3E46r/U22Q54VBwmNwyW92W8DFFuThs03go1yIRVYkAoxjDbWFOwsvLXOWmaZnBm+5j7Wt' \
     'NBhu0zFhY+o6Vq6okVOjCbgCxQ6pSM/8XHWZxIrySTEiA/Y6AnutIL8Al7WKd6+Mwj60YaXW5JgdW7w8laNVxzxb' \
     'Qr/9iecc8x4f5pOz803XkBoOQrOMQqJrc/JA4w10MJS1lcbgF6t5UmZlTVlzhy5Re0RSimEDntDsMrBmHy3TvZShhBp' \
     'cj4T0mMPB5av1sR8zhWJmza6sJ6DvkTWfD+NkoEJFXjk5vgpSNpYRViITsbzO5raVS6yECO5yIqIyuPzrjCliHAvV' \
     '8L7KIqRIjMJGyV+DAiwFQNAPkBmtk68L' \
     'nw+qfGmv+cvsgJ/SF6W2YZcX894EeIz8GxDb2KlroeGXdeMzeIJQvB3pDg=='
# 加密后的密码，从浏览器或抓包工具中复制，可重复使用
password2 = 'b35db2329549711ac32405772780bd172390623948c7bca57d694ed64eed8cfca0da5e' \
            '143cbdc91938c01d2968787d1ff10022c4dd2a3c7c3396f3d775d83ae3cc16ac2f9ee401c4' \
            '3fb24e3698c393c5fd210b22bc1adb8251d48946294e281511eeebee8b285f83ffe31d82d80dd' \
            '37d2ae13ac05f65c5400c7fa9de78e7e51e'