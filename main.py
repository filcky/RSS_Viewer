""" 
    先从一个URL爬取一个专题的新闻然后以输出

 """
from choice import make_a_choice as mc
import codecs

import requests

import feedparser

class RssViewer:

    def __init__(self,url):
        self.url = url

    def input_get(self):
        # 添加浏览器信息
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36'}
        # get方法获取
        page = requests.get(self.url, headers=headers)
        # 编码设置为“UTF-8”
        page.encoding = 'utf-8'
        page_content = page.text
        # 下面采用feedparse解析rss的xml文件
        rss=feedparser.parse(page_content)
        # 获取title
        title = rss.feed.title
        print(type(title))
        print(title+'.txt')
        # 输出单独频道xml文件的txt文本
        with open(title+'.txt','w',encoding='utf-8') as f:
            f.write(page_content)
    # 解析txt文本的具体新闻的链接
    def parse_each_news(self):
        rss =feedparser.parse('news.txt')
        print(rss.feed.title)

# 设置按需选择订阅源


if __name__ == '__main__':
    url = 'http://news.qq.com/newsgj/rss_newswj.xml'
    one_viewer = RssViewer(url)
    one_viewer.input_get()
    one_viewer.parse_each_news()

