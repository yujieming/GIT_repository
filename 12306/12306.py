import requests
import json

# import http.cookiejar as HC

dict_imgae = {
    1: '36,45',
    2: '120,45',
    3: '180,45',
    4: '260,45',
    5: '36,120',
    6: '120,120',
    7: '180,120',
    8: '260,120',
}


# 订票接口https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=2018-03-06&leftTicketDTO.from_station=HZH&leftTicketDTO.to_station=SHH&purpose_codes=ADULT
session = requests.session()
login = {
    'username': '18355093255',
    'password': 'cock159357',
    'appid': 'otn'
}

headers = {
    'Referer': 'https://kyfw.12306.cn/otn/login/init',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
# session.cookies = HC.LWPCookieJar(filename='cookies')
# #  如果存在cookies文件，则加载，如果不存在则提示
# try:
#   session.cookies.load(ignore_discard=True)
# except:
#   print('未找到cookies文件')


url_captcha = "https://kyfw.12306.cn/passport/captcha/captcha-check"
url_get_captch = "https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&0.7102500961258784"
url_login = 'https://kyfw.12306.cn/passport/web/login'
url_my12306 = 'https://kyfw.12306.cn/otn/index/initMy12306'
r = session.get(url_get_captch)
coding = r.content

with open('image.png', "wb") as f:
    f.write(coding)

data_input = input("输入坐标：1 2 3 4 \n\t\t  5 6 7 8")
list_i = data_input.split(' ')
in_put = ''
for i in list_i:
    i = int(i)
    in_put = in_put + dict_imgae[i] + ','

print(in_put)
data = {
    'answer': in_put,
    'login_site': 'E',
    'rand': 'sjrand'
}
req = session.post(url_captcha, data=data, headers=headers)
flag = json.loads(req.text)
print(flag)
if flag['result_code'] == '4':
    html = session.post(url_login, data=login, headers=headers)
    req = session.get(url_my12306)
    print(html.text)
    # print(req.url)
    # with open("my12306.html","w") as f:
    #     f.write(req.text.encode("gb2312"))
    flag = json.loads(html.text)
    if flag['result_code'] == 0:
        data = {
            "uamtk": flag["uamtk"]
        }
        data_2 = {
            '_json_att': ''
        }
        html = session.post('https://kyfw.12306.cn//otn/login/userLogin', data=data_2, headers=headers)
        headers = {
            'Referer': 'https://kyfw.12306.cn/otn/passport?redirect=/otn/login/userLogin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        }
        data_3 = {
            'appid': 'otn'
        }
        tk = session.post("https://kyfw.12306.cn/passport/web/auth/uamtk", data=data_3, headers=headers)
        flag = json.loads(tk.text)
        if flag['result_code'] == 0:
            tk = flag['newapptk']
            data_4 = {
                "tk": tk
            }
            last_url = "https://kyfw.12306.cn/otn/uamauthclient"
            html = session.post(last_url, data=data_4, headers=headers)
            print(html.text)
            html_12306 = session.get("https://kyfw.12306.cn/otn/login/userLogin")
            print(html_12306.text)
