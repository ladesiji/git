"""
   豆瓣读书（苦行记）短评爬取
"""

import requests

r = requests.get("https://www.douban.com/book/subject/25744258/comments").text

from bs4 import BeautifulSoup

soup = BeautifulSoup(r,'lxml')
pattern = soup.find_all('span','short')
for item in pattern:
    print(item.string)

import pandas

comments = []
for item in pattern:
    comments.append(item.string)
df = pandas.DataFrame(comments)
df.to_csv('comments.csv')
