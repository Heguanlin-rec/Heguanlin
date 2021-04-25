import datetime
import random
import re
import urllib.parse
import time
import scrapy
from lxml import etree

from ..items import PublicItem

class SitemapbaseSpider(scrapy.Spider):
    # 自定义此部分<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # 爬虫名字
    name = 'cbsnews'
    # 数据语种
    language = 'en'
    # 数据类型(句子或词组或...)
    datatype = 'sentence'
    # 数据存储路径
    # path = '/data/'  # 本地路径
    path = '/home/hegl/scrapyProject/spiderRE(1)/spiderRE/data'    # 服务器路径
    # 用于Bing搜索的域名
    host = 'cbsnews.com'
    # 正则匹配详情页url的规则
    pattern = "^https://www\.cbsnews\.com/[a-z]+/[a-z0-9-]+/?$"
    # 正则匹配列表页url的规则(可以为空，不匹配列表页)
    patternList = "^https://www\.cbsnews\.com/[a-z]+/?$"
    # 用于补全列表页中的url (例如: 列表页的url='/ms/sport/sdsa-sda-sdasd-sdggw.html', 需要 'https://www.theguardian.com' + url)
    target_host = ''
    custom_settings = {
        # 线程数(一般为个位数即可,第一次使用不要设置过大 可能导致目标服务器崩溃, max=32)
        "CONCURRENT_REQUESTS": 2,
        # 延迟时间
        "DOWNLOAD_DELAY": random.choice([0, 0, 0.1, 0.1, 0.6, 0.2]),
        # "DOWNLOAD_DELAY": 0,
    }
    # css选择器匹配数据所在标签的规则（在下列list中，如果匹配不到第一个元素的标签，会继续匹配第二个元素，直到匹配到相应的标签停止）
    # 是否合并标单个标签下的所有文字为一句话，t列表中是合并，f列表中是不合并
    querySelectorList_t = ['section.content__body p', 'div.content__body p']
    querySelectorList_f = []
    # 需要以 <br> 分割的文本标签
    querySelectorList_br = []
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # allowed_domains = ['www.baidu.com']
    # start_urls = ['http://www.baidu.com/']
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
    }


    def start_requests(self):
        """进入robots页面"""
        url_a = 'https://' + self.host + '/robots.txt'
        yield scrapy.Request(url=url_a, headers=self.headers, callback=self.get_sitemap_list)


    def get_sitemap_list(self, response):
        """正则匹配出 所有sitemap网址"""
        pattern = 'Sitemap: (http.*)'
        sitemap_list = re.findall(pattern, response.text)
        print(sitemap_list)
        print(type(sitemap_list))
        for g_url in sitemap_list:
            print(g_url)
            print('g_url的类型是', type(g_url))
            yield scrapy.Request(url=g_url, headers=self.headers, callback=self.get_url_list)


    def get_url_list(self, response):
        """循环获取详情页或列表页url"""
        html = scrapy.Selector(text=response.text)
        sitemap_list = html.css('sitemapindex > sitemap')
        urltag_list = html.css('urlset  > url')
        if len(sitemap_list) > 0:
            for sitemap in sitemap_list:
                loc = sitemap.css('loc::text').extract()[0]
                if '/video/' in loc:
                    continue
                yield scrapy.Request(url=loc, headers=self.headers, callback=self.get_url_list)
        elif len(urltag_list) > 0:
            for urltag in urltag_list:
                loc = urltag.css('loc::text').extract()[0]
                if ('.mp4' in loc) or ('.jpg' in loc):
                    continue
                isUsefulUrl = re.findall(self.pattern, loc)
                if self.patternList:
                    isUsefulListUrl = re.findall(self.patternList, loc)
                else:
                    isUsefulListUrl = []
                if len(isUsefulUrl) > 0:
                    yield scrapy.Request(url=loc, headers=self.headers, callback=self.parse_detail)
                elif len(isUsefulListUrl) > 0:
                    yield scrapy.Request(url=loc, headers=self.headers, meta={'target_host': loc}, callback=self.get_url_list_target)
                else:
                    self.logger.info('invalid urltag-loc=' + loc)
        else:
            self.logger.info('get_l_url error, response=' + response.url)


    def get_url_list_target(self, response):
        """解析 目标网站的非详情页， 匹配出符合规则的详情页"""
        if self.target_host:
            target_host = self.target_host
        else:
            target_host = response.meta['target_host']
        href_list = re.findall("href=\"(.*?)\"", response.text)
        for href in href_list:
            href = (target_host.strip('/') + '/' + href.strip('/')) if not 'http' in href else href
            header = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
                'referer': href,
            }
            isUsefulUrl = re.findall(self.pattern, href)
            isListUrl = re.findall(self.patternList, href)
            if len(isUsefulUrl) > 0:
                yield scrapy.Request(url=href, headers=header, callback=self.parse_detail)
            elif len(isListUrl) > 0:
                yield scrapy.Request(url=href, headers=self.headers, callback=self.get_url_list_target)


    def parse_detail(self, response):
        """解析详情页，提取数据"""
        url = urllib.parse.unquote(response.url)
        is_include_tag = False
        isJoinText = True
        items = PublicItem()
        querySelectorList = self.querySelectorList_t + self.querySelectorList_f
        for querySelector in querySelectorList:
            if querySelector in self.querySelectorList_f:
                isJoinText = False
            p_list = response.css(querySelector)
            if len(p_list) == 0:
                continue
            is_include_tag = True
            data_list = []
            for p in p_list:
                text_list = p.css(' *::text').extract()
                if isJoinText:
                    text = ''.join(text_list)
                    data_list.append(text.strip())
                else:
                    for text in text_list:
                        if text.strip():
                            data_list.append(text.strip())
            for data in data_list:
                data_l = data.split('\n')
                for data in data_l:
                    if data.strip():
                        items['data'] = data.strip()
                        # print(data)
                        yield items

        if self.querySelectorList_br:
            data_list = self.parse_by_br(response)
            if len(data_list) > 0:
                is_include_tag = True
            for data in data_list:
                data_l = data.split('\n')
                for data in data_l:
                    if data.strip():
                        items['data'] = data.strip()
                        # print(data)
                        yield items

        if is_include_tag:
            item = PublicItem()
            item['url'] = url
            yield item
        else:
            self.logger.info('p_list error, url=' + response.url)


    def parse_by_br(self, response):
        html = etree.HTML(text=response.text)
        text_l_new = []
        for querySelector in self.querySelectorList_br:
            text_list = html.xpath(querySelector)
            # print(len(text_list))
            temp_text = etree.tounicode(text_list[0]) if len(text_list) > 0 else ''
            # print(temp_text)
            if '<br>' in temp_text:
                text_l = temp_text.split('<br>')
            elif '<br/>' in temp_text:
                text_l = temp_text.split('<br/>')
            else:
                print('text_l.split by br error, maybe not found br')
                text_l = []
            for text in text_l:
                text = text.strip().replace('\n', '').replace('\r', '')
                text = re.sub('<.*?>', '', text)
                text_l_new.append(text)
        return text_l_new



    #
    def formatFOXTime(self, utc_time):
        utc_time = re.findall('(\d+-\d+-\d+T\d+:\d+:\d+)-\d+:\d+', utc_time)[0]
        UTC_FORMAT = "%Y-%m-%dT%H:%M:%S"
        localtime = datetime.datetime.strptime(utc_time, UTC_FORMAT) + datetime.timedelta(hours=8)
        return localtime
