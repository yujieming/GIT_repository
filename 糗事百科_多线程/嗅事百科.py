import threading
import queue
# import urllib.request
from lxml import etree
import requests
import codecs


class ThreadCrawl(threading.Thread):
    """docstring for ThreadCrawl"""
    def __init__(self, threadName,pageQueue,dataQueue):
        super(ThreadCrawl, self).__init__()
        self.threadName = threadName
        self.dataQueue = dataQueue
        self.pageQueue = pageQueue
        self.headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
        }

    def run(self):
        print("启动：",self.threadName)
        while not CRAWL_EXIT:
            try:
            #取出一个数字，先进先出
            #可选参数 为 block 默认值为 True
            #1 如果队列为空 ，BLOCK 为true的话 不会结束，会进入阻塞状态
            #2 如果列表为空   BLOCK 为Flase的话 会弹出一个Queue.empty（）的异常
                page = self.pageQueue.get(False)
                url = 'https://www.qiushibaike.com/8hr/page/' + str(page) + '/'
                html = requests.get( url,headers = self.headers).text
                global dataQueue
                dataQueue.put(html)
                # print(dataQueue.qsize())
            except:
                pass
        print("结束：",self.threadName)

class ThreadParse(threading.Thread):
    """docstring for ThreadParse"""
    def __init__(self,threadName,dataQueue):
        super(ThreadParse, self).__init__()
        self.threadName = threadName
        self.dataQueue = dataQueue
        self.lock = lock
        self.f = f

    def run(self):
        while not PARSE_EXIT:
            try:
                html = self.dataQueue.get(False)
                # print("===========================================",html)
                self.parse(html)
            except:
                pass

    def parse(self,html):

        # print(html)
        html = etree.HTML(html)
        datas = html.xpath('//div[contains(@class,"article block")]')
        # print(datas)
        items = {}

        for data in datas:

            uid = data.xpath('./div/a[2]/h2/text()')[0]
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
            with self.lock:
                self.f.write(json.dumps(items,ensure_ascii=False))
            

def main():
    
    #创建列队
    #创建10个页面的列队
    global pageQueue
    for i in range(1,11):
        pageQueue.put(i)

    #创建HTML源码列队
    #dataQueue = queue.Queue()


    #创建三个采集线程的名字
    crawlList = ["一号","二号","三号"]


    threadcrawl = []
    for threadName in crawlList:
        thread = ThreadCrawl(threadName, pageQueue, dataQueue)
        thread.start()
        threadcrawl.append(thread)
    
    print("-------",dataQueue.qsize())
    
    parseList = ["解析一号","解析二号","解析三号"]
    threadparse = []
    for threadName in parseList:
        thread = ThreadParse(threadName,dataQueue)
        thread.start()
        threadparse.append(thread)

    while not pageQueue.empty():
        pass

    global CRAWL_EXIT
    CRAWL_EXIT = True
    print("========",dataQueue.qsize())

    while not dataQueue.empty():
        pass
    global PARSE_EXIT
    PARSE_EXIT = True


    print("pageQueue为空")
    for thread in threadcrawl:
        thread.join()
        print("1")

    print("dataQueue为空")
    for thread in threadparse:
        thread.join()
        print("2")
    with lock:
        f.close()



if __name__ == '__main__':
    CRAWL_EXIT = False
    PARSE_EXIT = False
    pageQueue = queue.Queue(10)
    dataQueue = queue.Queue()
    lock = threading.Lock()
    f = codecs.open('out.txt','a','utf-8')
    main()