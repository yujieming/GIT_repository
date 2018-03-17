import requests
from lxml import etree
import json
from multiprocessing import Pool

def html(url):
    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
        }
    html = requests.get(url,headers = headers).text
    parse(html)

def parse(html):
    file = etree.HTML(html)
    datas = file.xpath('//div[contains(@class,"article block")]')

    for data in datas:
        print("================================================")
        if len(data.xpath('./div/a[2]/h2/text()')):
            uid = data.xpath('./div/a[2]/h2/text()')[0]
        else:
            uid = '匿名用户'
        print(uid)
        content = data.xpath('./a[1]/div/span/text()')[0]
        print(content)
        zan = data.xpath('.//i/text()')[0]
        print(zan)
        if len(data.xpath('.//div[contains(@class,"main-text")]')):
            hot_comment = data.xpath('.//div[contains(@class,"main-text")]/text()')[0]
        else:
            hot_comment = ""
        print(hot_comment)
        items = {
                "uid":uid,
                "content":content,
                "zan":zan,
                "hot_comment":hot_comment
            }

        with open("qiushi.json","a") as f:
            try:
                f.write(json.dumps(items,ensure_ascii = False)+"\n")
            except:
                pass

if __name__ == '__main__':
    # for i in range(1,11):
    #     url = 'https://www.qiushibaike.com/8hr/page/' + str(i) +'/'
    #     html(url)
    url_list = ['https://www.qiushibaike.com/8hr/page/' + str(i) +'/'for i in range(1,11)]
    with Pool(4) as p:
        p.map(html,url_list)
    #html(url)