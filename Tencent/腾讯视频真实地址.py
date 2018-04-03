# -*- coding: utf-8 -*-
# @Time    : 2018/3/8 13:06
# @Author  : TCJ
# @File    : find_link.py
# @Software: PyCharm
"""
=====只有五分钟
"""

import re
import requests
import  json


from bs4 import BeautifulSoup




if __name__ == '__main__':
    headers = {
        'Referer': 'https://m.v.qq.com/play.html?cid=2iqrhqekbtgwp1s&vid=r0135cxr0ql&ptag=v.qq.com%23v.play.adaptor%232&mreferrer=http%3A%2F%2Fv.qq.com%2Fdetail%2F2%2F2iqrhqekbtgwp1s.html',
        'coockie':'pgv_pvi=9013775360; ptui_loginuin=780450345; pt2gguin=o0780450345; RK=XNCdZvwFeH; ptcz=190c3378479545cb51048cfb8ead58dbcab69ea5cb98f42fe39e29c8171d1254; pgv_pvid=2973107078; tvfe_boss_uuid=686c29fe5ef4c023; o_cookie=780450345; luin=o0780450345; lskey=000100002c6dbcd50cbc7f1bf7c89c9b041628da0c31344b0871f8320a70b3fb92c9db8d0a76708e6fb8ec94; main_login=qq; vuserid=405097498; vusession=e68a5f4c181c44b2c6e9e1f15382; mobileUV=1_16203ae81fb_de5b5; pgv_info=ssid=s624345616; qv_swfrfh=; qv_swfrfc=v20; qv_swfrfu=',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Mobile Safari/537.36'
    }
    proxies = {
        "http": "http://120.92.119.20:10000",

    }
    get_start_url = input("请将视频连接填入>>>")
    get_start_url = get_start_url.split('/')[-2:]
    index = get_start_url[0]
    title = get_start_url[1][:-6]
    print(index, title)
    request_url = 'https://h5vv.video.qq.com/getinfo?guid=2a790ebc1025cf85666b47256b90f359&flowid=7486ef68404a539e4e18dfc86f2a5331_70901&platform=11001&sdtfrom=v1103&defnpayver=0&appVer=3.3.394&host=m.v.qq.com&ehost=https%3A%2F%2Fm.v.qq.com%2Fplay.html%3Fcid%3D2iqrhqekbtgwp1s%26vid%3Dc01350046ds%26ptag%3Dv_qq_com%2523v.play.adaptor%25233&sphttps=1&_rnd=1520555401&spwm=4&vid=' + title + '&defn=auto&fhdswitch=0&show1080p=0&isHLS=0&fmt=auto&defsrc=1&_qv_rmt=N4A2n2W9A12477L%2BT%3D&_qv_rmt2=SumGGXET150996cLw%3D&_1520497976978='
    req = requests.get(request_url,headers = headers,proxies = proxies)
    print(request_url)
    soup = BeautifulSoup(req.text, "html.parser")
    print(soup)
    print(soup.find_all('fn')[0].string)
    vi_title = soup.find_all('lnk')[0].string
    print(vi_title)
    print(soup.find_all('keyid'))
    url = soup.find_all('url')[-1].string
    print(url)
    key = soup.fvkey.string
    #print(tag)
    last_url = url + vi_title + '.mp4?&vkey=' + key
    print(last_url)
