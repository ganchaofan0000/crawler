import re
import os
import json
from crawler_test.taobaoformations import *
import requests


# s = requests.Session()
# cookies序列化文件
# COOKIES_FILE_PATH = 'taobao_login_cookies.txt'


class UsernameLogin:
    # s = requests.Session()
    # # cookies序列化文件
    # COOKIES_FILE_PATH = 'taobao_login_cookies.txt'
    def __init__(self, loginId, umidToken, ua, password2):
        """
        账号登录对象
        :param loginId: 用户名
        :param umidToken: 新版登录新增参数
        :param ua: 淘宝的ua参数
        :param password2: 加密后的密码
        """
        # 检测是否需要验证码的URL
        self.user_check_url = 'https://login.taobao.com/newlogin/account/check.do?appName=taobao&fromSite=0'
        # 验证淘宝用户名密码URL
        self.verify_password_url = "https://login.taobao.com/newlogin/login.do?appName=taobao&fromSite=0"
        # 访问st码URL
        self.vst_url = 'https://login.taobao.com/member/vst.htm?st={}'
        # 淘宝个人 主页
        self.my_taobao_url = 'http://i.taobao.com/my_taobao.htm'

        # 淘宝用户名
        self.loginId = loginId
        # 淘宝用户名
        self.umidToken = umidToken
        # 淘宝关键参数，包含用户浏览器等一些信息，很多地方会使用，从浏览器或抓包工具中复制，可重复使用
        self.ua = ua
        # 加密后的密码，从浏览器或抓包工具中复制，可重复使用
        self.password2 = password2
        # 淘宝session会话
        self.session = requests.Session()
        # cookies序列化文件
        self.COOKIES_FILE_PATH = 'taobao_login_cookies.txt'
        # 请求超时时间
        self.timeout = 3

    def _user_check(self):
        """
        检测账号是否需要验证码
        :return:
        """
        data = {
            'loginId': self.loginId,
            'ua': self.ua,
        }
        try:
            response = self.session.post(self.user_check_url, data=data, timeout=self.timeout)
            response.raise_for_status()
        except Exception as e:
            print('检测是否需要验证码请求失败，原因：')
            raise e
        check_resp_data = response.json()['content']['data']
        needcode = False
        # 判断是否需要滑块验证，一般短时间密码错误多次可能出现
        if 'isCheckCodeShowed' in check_resp_data:
            needcode = True
        print('是否需要滑块验证：{}'.format(needcode))
        return needcode

    def _get_umidToken(self):
        """
        获取umidToken参数
        :return:
        """
        response = self.session.get('https://login.taobao.com/member/login.jhtml')
        st_match = re.search(r'"umidToken":"(.*?)"', response.text)
        print(st_match.group(1))
        return st_match.group(1)

    # 装饰器，作用是把类中的方法变成属性来进行调用
    @property
    def _verify_password(self):
        """
        验证用户名密码，并获取st码申请URL
        :return: 验证成功返回st码申请地址
        """
        verify_password_headers = {
            'Origin': 'https://login.taobao.com',
            'content-type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': 'https://login.taobao.com/member/login.jhtml?spm=a21bo.2017.754894437.1.5af911d9HjW9WC&f=top&redirectURL=https%3A%2F%2Fwww.taobao.com%2F',
        }
        # 验证用户名密码参数
        verify_password_data = {
            'ua': self.ua,
            'loginId': self.loginId,
            'password2': self.password2,
            'umidToken': self.umidToken,
            'appEntrance': 'taobao_pc',
            'isMobile': 'false',
            'returnUrl': 'https://www.taobao.com/',
            'navPlatform': 'MacIntel',
        }
        try:
            response = self.session.post(self.verify_password_url, headers=verify_password_headers, data=verify_password_data,
                              timeout=self.timeout)
            response.raise_for_status()
            # 从返回的页面中提取申请st码地址
        except Exception as e:
            print('验证用户名和密码请求失败，原因：')
            raise e
        # 提取申请st码url
        apply_st_url_match = response.json()['content']['data']['asyncUrls'][0]
        # 存在则返回
        if apply_st_url_match:
            print('验证用户名密码成功，st码申请地址：{}'.format(apply_st_url_match))
            return apply_st_url_match
        else:
            raise RuntimeError('用户名密码验证失败！response：{}'.format(response.text))

    def _apply_st(self):
        """
        申请st码
        :return: st码
        """
        apply_st_url = self._verify_password
        try:
            response = self.session.get(apply_st_url)
            response.raise_for_status()
        except Exception as e:
            print('申请st码请求失败，原因：')
            raise e
        st_match = re.search(r'"data":{"st":"(.*?)"}', response.text)
        if st_match:
            print('获取st码成功，st码：{}'.format(st_match.group(1)))
            return st_match.group(1)
        else:
            raise RuntimeError('获取st码失败！response：{}'.format(response.text))

    def login(self):
        """
        使用st码登录
        :return:
        """
        # 加载cookies文件
        if self._load_cookies():
            return True
        # 判断是否需要滑块验证
        self._user_check()
        st = self._apply_st()
        headers = {
            'Host': 'login.taobao.com',
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }
        try:
            response = self.session.get(self.vst_url.format(st), headers=headers)
            response.raise_for_status()
        except Exception as e:
            print('st码登录请求，原因：')
            raise e
        # 登录成功，提取跳转淘宝用户主页url
        my_taobao_match = re.search(r'top.location.href = "(.*?)"', response.text)
        if my_taobao_match:
            print('登录淘宝成功，跳转链接：{}'.format(my_taobao_match.group(1)))
            self.my_taobao_url = my_taobao_match.group(1)
            self._serialization_cookies()
            return True
        else:
            raise RuntimeError('登录失败！response：{}'.format(response.text))

    def _load_cookies(self):
        # 1、判断cookies序列化文件是否存在
        if not os.path.exists(self.COOKIES_FILE_PATH):
            return False
        # 2、加载cookies
        self.session.cookies = self._deserialization_cookies()
        # 3、判断cookies是否过期
        try:
            self.get_taobao_nick_name()
        except Exception as e:
            os.remove(self.COOKIES_FILE_PATH)
            print('cookies过期，删除cookies文件！')
            return False
        print('加载淘宝cookies登录成功!!!')
        return True

    def _serialization_cookies(self):
        """
        序列化cookies
        :return:
        """
        cookies_dict = requests.utils.dict_from_cookiejar(self.session.cookies)
        with open(self.COOKIES_FILE_PATH, 'w+', encoding='utf-8') as file:
            json.dump(cookies_dict, file)
            print('保存cookies文件成功！')

    def _deserialization_cookies(self):
        """
        反序列化cookies
        :return:
        """
        with open(self.COOKIES_FILE_PATH, 'r+', encoding='utf-8') as file:
            cookies_dict = json.load(file)
            cookies = requests.utils.cookiejar_from_dict(cookies_dict)
            return cookies

    def get_taobao_nick_name(self):
        """
        获取淘宝昵称
        :return: 淘宝昵称
        """
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }
        try:
            response = self.session.get(self.my_taobao_url, headers=headers)
            response.raise_for_status()
        except Exception as e:
            print('获取淘宝主页请求失败！原因：')
            raise e
        # 提取淘宝昵称
        nick_name_match = re.search(r'<input id="mtb-nickname" type="hidden" value="(.*?)"/>', response.text)
        if nick_name_match:
            print('登录淘宝成功，你的用户名是：{}'.format(nick_name_match.group(1)))
            return nick_name_match.group(1)
        else:
            raise RuntimeError('获取淘宝昵称失败！response：{}'.format(response.text))


if __name__ == '__main__':
    ul = UsernameLogin(loginId, umidToken, ua, password2)
    ul.login()
    ul.get_taobao_nick_name()