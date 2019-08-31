import requests
from urllib.parse import urlencode
from pyquery import PyQuery as pq
from pymongo import MongoClient

base_url = 'https://m.weibo.cn/api/container/getIndex?'
headers = {
    'referer': 'https://m.weibo.cn/u/2830678474',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}


def get_page(page):
    params = {
        'value': '2830678474',
        'containerid': '1076032830678474',
        'type': 'uid',
        'page': page
    }

    url = base_url + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print('error', e.args)


def parse_page(json):
    if json:
        items = json.get('data').get('cards')
        for item in items:
            i = item.get('mblog')
            weibo = {}
            weibo['id'] = i.get('id')
            weibo['text'] = pq(i.get('text')).text()
            weibo['attitudes'] = i.get('attitudes_count')
            weibo['comments'] = i.get('comments_count')
            weibo['reposts'] = i.get('reposts_count')
            yield weibo


def write_to_file(result):
    client = MongoClient()
    db = client.weibo
    collection = db.weibo
    if collection.insert(result):
        print('Saved to Mongo')


if __name__ == '__main__':
    for page in range(1, 11):
        json = get_page(page)
        results = parse_page(json)
        for result in results:
            print(result)
            write_to_file(result)



