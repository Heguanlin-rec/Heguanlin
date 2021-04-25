# -*- coding: utf-8 -*-

import os
import random
import re
import urllib.parse
import scrapy
from lxml import etree
from scrapy.http.request import Request
from ..items import PublicItem
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError, TCPTimedOutError

class RebaseSpider(scrapy.Spider):
    # 自定义此部分<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # 爬虫名字
    name = 'cbs'
    # 数据语种
    language = 'en'
    # 数据类型(句子或词组或...)
    datatype = 'sentence'
    # 数据存储路径
    # path = '/data/'  # 本地路径
    # path = '../../data'  # 服务器路径
    path = '/home/hegl/scrapyProject/spiderRE(1)/spiderRE/data'
    # 起始url
    start_urls = ['https://www.cbsnews.com/']
    # 正则匹配详情页url的规则
    # ^https://[a-z]+\.sina\.com\.cn/[a-z]+/([a-z]+/)?(?:2020|2021)-\d{2}-\d{2}/doc-\w{15}\.shtml$      新浪网
    # ^http://[a-z]+\.people\.com\.cn/(?:n1|n2)/(?:2020|2021)/\d{4}/c\d+-\d{8}\.html$          人民网
    # ^https://[a-z]+\.ifeng\.com/c/8\w{10}$                           凤凰网
    # ^https://www\.jiemian\.com/article/5[789]\d{5}\.html$                       界面新闻
    # ^https://asahichinese-j\.com/\w+(/\w+)?/1[34]\d{6}$                 朝日新闻
    # ^https://[a-z]+\.cctv\.com/(?:2020|2021)/\d{2}/\d{2}/\w{30}\.shtml\?spm=\w{6}\.\w{12}\.\w+\.\d+$         央视网
    # ^https://www\.163\.com/[a-z]+/article/\w{16}\.html$                   网易新闻
    # ^https://www\.toutiao\.com/a69\d{17}/$                                今日头条
    # ^http://www\.chinatoday\.com\.cn/zw2018/\w+/(?:2021|2020)\d{2}/t(?:2021|2020)\d{4}_\d{9}\.html$       今日中国
    # ^http://[a-z]+\.ce\.cn/[a-z]+/([a-z]+/)?([a-z]+/)?(?:2020|2021)\d{2}/\d{2}/t(?:2020|2021)\d{4}_\d{8}\.shtml$    中国经济网
    # ^https://www\.nmpa\.gov\.cn/[a-z]+/[a-z]+/([a-z]+/)?([a-z]+/)?(2020|2021)\d{13}\.html$           中文医药
    # ^http://www\.chinanews\.com/[a-z]+/(?:2020|2021)/\d{2}-\d{2}/\d{7}\.shtml$                   中新网
    # ^http://[a-z]+\.cnr\.cn/[a-z]+/([a-z]+/)?(?:2020|2021)\d{4}/t(?:2020|2021)\d{4}_\d{9}\.shtml$       央广网
    # ^http://c[a-z]+\.chinadaily\.com\.cn/a/(?:2020|2021)\d{2}/\d{2}/\w+\.html$                     中国日报网
    # ^https://www\.wsj\.com/articles/(.*?)-\d{11}$                                        The Wall Street Journal
    # ^https://www\.npr\.org/.*?(?:2020|2021)/\d{2}/\d{2}/\d{9}/.*?[a-z]$                      npr
    # ^https://www\.foxnews\.com/[a-z]+/[a-z0-9-]+$                                          fox
    pattern = "^https://www\.cbsnews\.com/[a-z]+/[a-z0-9-]+/?$"
    # 正则匹配列表页url的规则(可以为空，不匹配列表页)
    # ^http(s)?://[a-z]+\.([a-z]+\.)?sina\.com\.cn/([a-z]+/)?([a-z]+/)?$      新浪网
    # ^http://[a-z]+\.people\.com\.cn/(GB/)?(\d+/)?(\d+/)?(index\.html)?$           人民网
    # ^https://[a-z]+\.ifeng\.com$                             凤凰网
    # ^https://www\.jiemian\.com/(lists|city)/([a-z]+/)?\d+\.html$             界面新闻
    # ^https://asahichinese-j\.com/\w+(/\w+)?/$                                朝日新闻
    # ^https://[a-z]+\.cctv\.com/([a-z]+/)?(index.shtml)?\?spm=\w{6}\.\w{12}(\.\w{12})?\.\d+(\.\d+)?$          央视网
    # ^https://[a-z]+\.163\.com/([a-z]/)?$                                     网易新闻
    # ^https://www\.toutiao\.com/ch/news_[a-z]+/$                               今日头条
    # ^http://www\.chinatoday\.com\.cn/zw2018/\w+/(\w+/)?(index_\d\.html)?$       今日中国
    # ^http://[a-z]+\.ce\.cn/([a-z]+/)?([a-z]+/)?(index\.shtml)?$                  中国经济网
    # ^https://www\.nmpa\.gov\.cn/[a-z]+/[a-z]+/index(_\d{1,2})?\.html$             中文医药
    # ^http://www\.chinanews\.com/[a-z]+$                                        中新网
    # ^http://[a-z]+\.cnr\.cn/([a-z]+)?$                                          央广网
    # ^http://[a-z]+\.chinadaily\.com\.cn/(\w+/)?(\w+/)?(\w+/)?(page_\d{1,2}\.html)?$    中国日报网
    # ^https://www\.wsj\.com/[a-z]+/(.*?)(\?page=\d{1,3})?$                         The Wall Street Journal
    # ^https://www\.npr\.org/[a-z]+/.*?[a-z]$                                      npr
    # ^https://www\.foxnews\.com/[a-z]+.*?[a-z]$                                    fox
    patternList = "^https://www\.cbsnews\.com/[a-z]+/?$"
    # 用于补全列表页中的url (例如: 列表页的url='/ms/sport/sdsa-sda-sdasd-sdggw.html', 需要 'https://www.theguardian.com' + url)
    target_host = ''
    custom_settings = {
        # 线程数(一般为个位数即可,第一次使用不要设置过大 可能导致目标服务器崩溃, max=32)
        "CONCURRENT_REQUESTS": 3,
        # 延迟时间
        "DOWNLOAD_DELAY": random.choice([0, 0, 0.1, 0.1, 0, 0.2]),
        # "DOWNLOAD_DELAY": 0,
        # ip代理 默认不开启
        # "DOWNLOADER_MIDDLEWARES": {
           # 'spiderRE.middlewares.ProxyMiddleware': 543,
        # }
    }
    # css选择器匹配数据所在标签的规则（在下列list中，如果匹配不到第一个元素的标签，会继续匹配第二个元素，直到匹配到相应的标签停止）
    # 是否合并标单个标签下的所有文字为一句话，t列表中是合并，f列表中是不合并, 此处为css语法
    # 'div[id="artibody"] > p', 'div[id="article"] > p', 'div[class="article-body main-body"] > p           新浪网
    # 'div[class="rm_txt_con cf"] > p',  'div[class="show_text"] > p', 'div[class="box_con"] > p'             人民网
    # 'div[class="text-3w2e3DBc"] > p', 'div[class="text-3zQ3cZD4"] > p'            凤凰网
    # 'div.article-content p'                                                      界面新闻
    # 'div.ArticleText p'                                                           朝日新闻
    # 'div.content_area p', 'div.ystg_ind_01 p', 'div.cnt_bd p'                                             央视网
    # 'div.post_body p'                                                         网易新闻
    # 'div.article-content p'                                                      今日头条
    # 'div.TRS_Editor p'                                                        今日中国
    # 'div.TRS_Editor p'                                                      中国经济网
    # 'div.text p'                                                             中文医药
    # 'div.left_zw p'                                                          中新网
    # 'div.TRS_Editor p', 'div.article-body p'                                 央广网
    # 'div#Content p'                                                       中国日报网
    # 'div.wsj-snippet-body p', 'div.article-content p'                        The Wall Street Journal
    # 'div#storytext p'                                                      npr
    # 'div.article-body p'                                                    fox
    querySelectorList_t = ['div.content__body p', 'section.content__body p']            
    querySelectorList_f = []
    # 需要以 <br> 分割的文本标签, 此处为xpath语法
    querySelectorList_br = []
    # 根据尾缀 过滤url
    urlFilterStr = ['.jpg', '.pdf', '.png', '.mp3', '.mp4', '.flv', '.css', 'xlsx']
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # allowed_domains = ['cn.bing.com']
    start_url = True
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0",
    }
    def errback_httpbin(self, failure):
        # log all failures
        self.logger.error(repr(failure))

        # in case you want to do something special for some errors,
        # you may need the failure's type:

        if failure.check(HttpError):
            # these exceptions come from HttpError spider middleware
            # you can get the non-200 response
            response = failure.value.response
            self.logger.error('HttpError on %s', response.url)

        elif failure.check(DNSLookupError):
            # this is the original request
            request = failure.request
            self.logger.error('DNSLookupError on %s', request.url)

        elif failure.check(TimeoutError, TCPTimedOutError):
            request = failure.request
            self.logger.error('TimeoutError on %s', request.url)

    def parse(self, response):
        # target_host = response.url.split('.cn/')[0] + '.cn/'
        target_host_spl = response.url.split('/')
        target_host_spl.pop()
        target_host = '/'.join(target_host_spl)

        href_list = response.css('*::attr(href)').extract()
        #print('len=', len(href_list))
        #print(href_list)
        for href in href_list:
            # 过滤 url
            if '.js' in href[-4:]:
                continue
            if href[-4:] in self.urlFilterStr:
                continue
            # 补全 url
            if not 'http' in href[0:6]:
                if href[:2] == '//':
                    url = response.url.split('//')[0] + href
                elif href[:2] == './':
                    url = target_host.rstrip('/') + '/' + href.lstrip('./')
                elif target_host and '../' in href[:4]:
                    point_num = len(re.findall('\.\./', href))
                    t_host_list = target_host.rstrip('/').split('/')
                    for i in range(point_num):
                        t_host_list.pop()
                    t_host = '/'.join(t_host_list)
                    url = t_host.rstrip('/') + '/' + href.lstrip('../')
                elif target_host \
                        and (target_host.strip('/').split('/')[-1] != href.strip('/').split('/')[0]) \
                        and (target_host[-1:] == '/') \
                        and (len(re.findall(r'/', target_host.strip('/'))) <= 3):
                    url = target_host.rstrip('/') + '/' + href.lstrip('/')
                else:
                    t_host = target_host.split('//')[0] + '//' + target_host.split('//')[1].split('/')[0]
                    url = t_host.rstrip('/') + '/' + href.lstrip('/')
            else:
                url = href
            isUsefulUrl = re.findall(self.pattern, url)
            if self.patternList:
                isUsefulListUrl = re.findall(self.patternList, url)
            else:
                isUsefulListUrl = []
            target_header = self.headers
            target_header['referer'] = response.url
            # 如果是详情页url 发送请求
            if (len(isUsefulUrl) > 0):
                #self.logger.info('usefulUrl='+ href)
                yield Request(url=url, headers=target_header, callback=self.parse_detail, errback=self.errback_httpbin)
            # 如果是列表页， 进入列表页 匹配有用的详情页url
            elif (len(isUsefulListUrl) > 0):
                #self.logger.info('usefulListUrl=%s, response=%s'%(href, response.url))
                yield Request(url=url, headers=target_header, meta={'target_host': url}, callback=self.parse, errback=self.errback_httpbin)

    def parse_detail(self, response):
        """解析详情页，提取数据"""
        url = urllib.parse.unquote(response.url)
        self.logger.info('detail_url=%s' % (url))
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
                items['data'] = data
                # print(data)
                yield items

        if self.querySelectorList_br:
            data_list = self.parse_by_br(response)
            if len(data_list) > 0:
                is_include_tag = True
            for data in data_list:
                items['data'] = data
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
            p_list = html.xpath(querySelector)
            # print(len(p_list))
            for p in p_list:
                temp_text = etree.tounicode(p)
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
