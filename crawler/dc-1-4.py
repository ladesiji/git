"""
    DC学院爬虫学习第四课
    课程目标：学习 xpath 来解析HTML数据
    案例：爬取豆瓣读书的《苦行记》短评
"""

import requests
from lxml import etree
import pandas

URL = 'https://book.douban.com/subject/25744258/comments/'

def getHTML(url):
    """
        爬取url上的HTML文件
    """
    r = requests.get(url,timeout = 6)
    # r.encoding = 'utf-8'
    return r.text


def getxpath(html):
    """
        使用xpath来解析HTML文件
    """
    return etree.HTML(html)

def to_csv(data_dict, filename):
    """
        使用pandas 将数据保存到CSV
    """
    df = pandas.DataFrame(data_dict)
    df.to_csv(f'{filename}.csv')

def main():
    """
        主函数
    """
    # 爬取URL地址
    r = getHTML(URL)
    # 使用xpath解析数据
    s = getxpath(r)
    # 获取用户、日期、评论 三个列表
    data = {}
    data['author'] = s.xpath('//span[@class="comment-info"]/a/text()')
    data['date'] = s.xpath('//span[@class="comment-info"]/span/text()')
    data['comment'] = s.xpath('//p/span/text()')
    # 将数据保存在到CSV中
    to_csv(data,'comment')

if __name__ == main():
    main()
