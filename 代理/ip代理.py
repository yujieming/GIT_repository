import re
import time
import urllib
import requests
from lxml import etree


class Get_Proxy(object):
    """docstring for Get_Proxy"""
    #   https://www.kuaidaili.com/free/
    def __init__(self, url = 'http://www.xicidaili.com/'):
        super(Get_Proxy, self).__init__()
        self.url = url
        self.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
        }

    # def verif_ip(self):    # 验证ip有效性
    #     user_agent ='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0'
    #     headers = {'User-Agent':user_agent}
    #     proxy = {self.t_ype:self.ip}
    #     print(proxy)
    #
    #     proxy_handler = urllib.request.ProxyHandler(proxy)
    #     opener = urllib.request.build_opener(proxy_handler)
    #     urllib.request.install_opener(opener)
    #
    #     test_url = "http://baidu.com"
    #     req = urllib.request.Request(url=test_url,headers=headers)
    #
    #     # time.sleep(1)
    #     try:
    #         res = urllib.request.urlopen(req, timeout = 7)
    #         # req = requests.get(test_url,proxies = proxy,headers = headers).text
    #         # time.sleep(1)
    #         # content = etree.HTML(req).xpath('//span/text()')
    #         content = res.read().decode('utf-8')
    #         # print(content)
    #         if content:
    #             print('IP地址可用')
    #             with open("data2.txt", "a") as fd:       # 有效ip保存到data2文件夹
    #                 fd.write(self.ip)
    #                 fd.write("\n")
    #         else:
    #             print('不可用')
    #     except Exception as e:
    #         print(e)

    def verif_ip(self):    # 验证ip有效性
        user_agent ='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0'
        headers = {'User-Agent':user_agent}
        proxy = {self.t_ype:self.ip}
        print(proxy)

        test_url = "http://baidu.com"
        # time.sleep(1)
        try:
            content = requests.get(test_url,proxies = proxy,headers = headers,timeout = 5).content.decode('utf-8')
            # content = etree.HTML(req).xpath('//span/text()')
            # content = res.read().decode('utf-8')
            # print(content)
            if content:
                print('IP地址可用')
                with open("data2.txt", "a") as fd:       # 有效ip保存到data2文件夹
                    fd.write(self.ip)
                    fd.write("\n")
            else:
                print('不可用')
        except Exception as e:
            print(e)

    def get_ip(self):
        html = requests.get(self.url,headers = self.headers).content.decode('utf-8')
        iplist = re.findall("(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?(\d{2,6}).*?(HTTP)", html, re.S)
        for ip_s in iplist:
            # print(str.lower(ip[2]))''
            self.ip = ip_s[0] + ':' + ip_s[1]
            self.t_ype = str.lower(ip_s[2])
            self.verif_ip()

if __name__ == '__main__':

    '''
    代理ip网址
    1 ：  http://www.xicidaili.com/nn/
    2 ：  https://www.kuaidaili.com/free/
    3 ：  http://www.xicidaili.com/wt/
    3 ：  http://www.xicidaili.com/nt/
    4 ：  https://www.kuaidaili.com/free/intr/
    '''

    z = Get_Proxy(url = 'http://www.xicidaili.com/nn/')
    z.get_ip()