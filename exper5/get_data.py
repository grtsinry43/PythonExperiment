"""
@author grtsinry43
@date 2024/12/19 09:31
@description 热爱可抵岁月漫长
"""
from json import JSONDecoder

import requests
import json
import io
import re
from bs4 import BeautifulSoup


def get_data(url):
    ua = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    headers = {
        'User-Agent': ua,
        'Cookie': io.open('cookie.txt', 'r', encoding='utf-8').read()
    }
    response = requests.get(url, headers=headers)
    return response.text


def parse_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    movies = []
    for item in soup.select('ol.grid_view li div.item'):
        name = re.sub(r'\s', '', item.select_one('span.title').get_text(strip=True).split('/')[0])
        print("name:", name)
        # 取出英文名，从所有名字中找出名字均为英文或空格匹配等等，没有则为空
        en_name = ''
        all_name = item.select('span.title')
        all_name.append(item.select_one('span.other'))
        for i in all_name:
            if re.match(r'^[a-zA-Z\s]*$', i.get_text(strip=True)[3:]):
                en_name = i.get_text(strip=True)[2:]
        item_link = re.sub(r'\s', '', item.select_one('div.hd a').attrs.get("href"))
        img_src = item.select_one('div.pic img')['src']
        info = item.select_one('div.bd p').get_text(strip=True)
        comment = item.select_one('span.inq').get_text(strip=True) if item.select_one('span.inq') else ''
        # 根据其链接获取更多信息
        print("获取更多信息: ", item_link)
        html = get_data(item_link)
        soup = BeautifulSoup(html, 'html.parser')
        intro = soup.select_one('div#link-report-intra').get_text(strip=True)
        directors = [a.get_text(strip=True) for a in soup.select('div#info span:nth-child(1) span.attrs a')]
        actors = [a.get_text(strip=True) for a in soup.select('div#info span:nth-child(3) span.attrs a')]
        types = [a.get_text(strip=True) for a in soup.select('div#info span[property="v:genre"]')]
        # print(directors, actors, types)
        short_comment_link = soup.select('div.review-item h2 a')[0].attrs.get('href')
        print("影评api " + short_comment_link.replace("/review", "/j/review") + "full")
        short_comment = JSONDecoder().decode(get_data(short_comment_link.replace("/review", "/j/review") + "full"))[
            'html']
        movies.append({
            'name': name,
            'en_name': en_name,
            'imgSrc': img_src,
            'info': info,
            'intro': intro,
            'short_comment': short_comment,
            'item_link': item_link,
            'comment': comment,
            'directors': directors,
            'actors': actors,
            'types': types
        })
        print(name + "已保存")
        print("======")
        # print({
        #     'name': name,
        #     'en_name': en_name,
        #     'imgSrc': img_src,
        #     'info': info,
        #     'intro': intro,
        #     'short_comment': short_comment,
        #     'item_link': item_link,
        #     'comment': comment
        # })
    return movies


def save_data(data):
    with io.open('result.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(data, ensure_ascii=False))


def main():
    url = "https://movie.douban.com/top250?start=0"
    result = []
    for i in range(10):
        html = get_data(url)
        result += parse_data(html)
        save_data(result)
        url = f"https://movie.douban.com/top250?start={i * 25}"
        print(f"第{i + 1}页数据已保存")
    save_data(result)


if __name__ == '__main__':
    main()
