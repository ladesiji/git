"""
    实现自动抓取AQI  （http://pm25.in/）
    日期：2019/2/19

"""

import requests, csv
from bs4 import BeautifulSoup


def get_city_aqi(city_pinyin):
    """
        抓取网页内容
    """
    url = 'http://pm25.in/' + city_pinyin
    r = requests.get(url, timeout=60)
    soup = BeautifulSoup(r.text, 'lxml')
    div_list = soup.find_all('div',{'class': 'span1'})

    city_aqi = []
    for i in range(8):
        div_content = div_list[i]
        # caption = div_content.find('div', {'class': 'caption'}).text.strip()
        value = div_content.find('div', {'class': 'value'}).text.strip()
        city_aqi.append(value)
    return city_aqi


def get_city_list():
    """
        获取城市列表
    """
    url = 'http://pm25.in/'
    r = requests.get('http://pm25.in/', timeout=60)
    soup = BeautifulSoup(r.text, 'lxml')
    city_div = soup.find_all('div', {'class':'bottom'})[1]
    city_link_list = city_div.find_all('a')
    city_list = []
    for city_link in city_link_list:
        city_name = city_link.text
        city_pinyin = city_link['href'][1:]
        city_list.append((city_name,city_pinyin))
    return city_list


def main():
    """
        主函数
    """
    city_list = get_city_list()
    header = ['City', 'AQI', 'PM2.5/1h', 'PM10/1h',
              'CO/1h', 'NO2/1h', 'O3/1h', 'O3/8h', 'SO2/1h']
    with open('china_city_cqi.csv', 'w', encoding='gbk',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)

        for i,city in enumerate(city_list):
            if i % 10 == 0:
                print("当前进度{}%，已处理{}条记录，请耐心等待".format(round(i/len(city_list)*100),i))
            city_name = city[0]
            city_pinyin = city[1]
            city_aqi = get_city_aqi(city_pinyin)
            row = [city_name] + city_aqi
            writer.writerow(row)
    print('任务完成，文件已保存')


if __name__ == main():
    main()

