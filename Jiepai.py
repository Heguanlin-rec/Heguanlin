import requests
from urllib.parse import urlencode
import os
from hashlib import md5
from multiprocessing.pool import Pool

def get_one_page(offset):
    base_url = 'https://www.toutiao.com/api/search/content/?'
    params = {
        'aid' : '24',
        'app_name' : 'web_search',
        'offset' : offset,
        'format' : 'json',
        'keyword' : '%E8%A1%97%E6%8B%8D',
        'autoload' : 'true',
        'count' : '20',
        'en_qc' : '1',
        'cur_tab' : '1',
        'from':'search_tab',
        'pd' : 'synthesis'
    }
    headers = {
        'cookie': 'tt_webid = 6719017586078615043;WEATHER_CITY = % E5 % 8C % 97 % E4 % BA % AC;tt_webid = 6719017586078615043;csrftoken = f7a7b081d518ebb2f03a8a3f484fe7b7;UM_distinctid = 16c3d19a69d35e - 0af4a62be81f07 - 40b032d - 144000 - 16c3d19a69e357;CNZZDATA1259612802 = 1899833717 - 1564390857 - https % 253A % 252F % 252Fwww.toutiao.com % 252F % 7C1564452301;__tasessionId = fmz46v0lq1567130924930;s_v_web_id = 0acaee5c822950f92b6012d61a8d4e6c',
        'referer': 'https: // www.toutiao.com / search /?keyword = % E8 % A1 % 97 % E6 % 8B % 8D',
        'user-agent':'Mozilla / 5.0(Windows NT 6.1;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 75.0.3770.100Safari / 537.36',
        'x-requested -with': 'XMLHttpRequest'
    }

    url = base_url + urlencode(params)
    response = requests.get(url, headers=headers)
    try:
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None


def parse_one_page(json):
    if json.get('data'):
        for item in json.get('data'):
            title = item.get('title')
            images = item.get('image_list')
            if images != None:
                for image in images:
                    if image == None:
                        continue
                    else:
                        yield{
                            'image':image.get('url'),
                            'title':title
                        }

def write_to_file(content):
    if not os.path.exists(content.get('title')):
        os.mkdir(content.get('title'))
    try:
        response = requests.get(content.get('image'))
        if response.status_code == 200:
            file_path = '{0}/{1}.{2}'.format(content.get('title'), md5(response.content).hexdigest(), 'jpg')
            if not os.path.exists(file_path):
                with open(file_path,'wb') as f:
                    f.write(response.content)
                print('Download image path is %s' % file_path)
            else:
                print('Already Downloaded', file_path)
    except requests.ConnectionError:
        print('Failed to Save Image')

def main(offset):
    json = get_one_page(offset)
    for item in parse_one_page(json):
        print(item)
        write_to_file(item)

GROUP_START = 1
GROUP_END = 20

if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    pool.map(main, groups)
    pool.close()
    pool.join()












