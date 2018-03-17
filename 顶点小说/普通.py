import requests
from lxml import etree
import re


def get_url_list(url):
    
    html = requests.get(url,headers = headers)
    html.encoding = "GB2312"
    html = html.text
    data_list = re.findall(r'<td class="L"><a href="(.*?)">(.*?)</a></td>',html)
    
    return data_list
    # for data in data_list:
        
    #     print('https://www.x23us.com/html/64/64405/'+data[0],data[1]+'\n')
    

    # items = {}
    # for data in data_list:
    #     items['link'] = 'https://www.x23us.com/html/64/64405/'+str(data[0])
    #     items['name'] = data[1]
    # print(items)
    # return items


def downlode(url,name):
    html = requests.get(url,headers = headers)
    html.encoding = "gb2312"
    html = etree.HTML(html.text)
    data = html.xpath('//dl/dd[3]/text()')
    data = "\n".join(data)
    print(name)
    with open(name+'.txt','w',encoding='utf-8') as f:
        f.write(data)


def main():
      
    url = 'https://www.x23us.com/html/64/64405/'
    for data in get_url_list(url):
        url = 'https://www.x23us.com/html/64/64405/'+data[0]
        name = data[1]
        downlode(url ,name)



if __name__ == '__main__':
    headers = {
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
            }

    main()
