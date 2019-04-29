"""
    DC学院第一章第6节
    课程目标：学习构造request hearder, 应对简单的反爬措施 
    实例：爬取知乎vczh 轮子哥的关注者
    
"""

import requests
import pandas as pd
import time

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    # 'x-zse-84': 'mTFqkerqe02pSLYqmTH0g4U0gwSfkRtyfRYBUJXBSR2YH9tysXtqc7U067txk7ty'
}
user_data = []
def user_data_page(page):
    for i in range(page):
        url = f'https://www.zhihu.com/api/v4/members/excited-vczh/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset={i*20}&limit=20'
        user_data.extend(requests.get(url,headers = headers).json()['data'])
        print("正在爬取第{}页".format(i+1))
        time.sleep(1)
user_data_page(10)
import pandas as pd
df = pd.DataFrame(user_data)
df.to_csv('fllowees.csv')
