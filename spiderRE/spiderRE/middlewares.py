# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import json
import time

import requests
from scrapy import signals
from scrapy.http import HtmlResponse as Response

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class SpiderreSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class SpiderreDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)



import logging




class ProxyMiddleware(object):

    def __init__(self):
        self.proxies = {}
        self.time_num = 0
        self.RetryCode = [408, 429, 404, 443, 403, 401]
        self.retry_num = 0

    def get_one_proxies(self):
        api_url = "http://ip.ipjldl.com/index.php/api/entry?method=proxyServer.generate_api_url&packid=0&fa=0&fetch_key=&groupid=0&qty=1&time=1&pro=&city=&port=1&format=json&ss=5&css=&ipport=1&dt=1&specialTxt=3&specialJson=&usertype=2"
        proxies = {"https": ""}
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36',
            'x-client-data': 'CIy2yQEIpLbJAQjBtskBCPqcygEIqZ3KAQ=='}
        try:
            response = requests.get(url=api_url, headers=headers, timeout=5)
            ip = json.loads(str(response.content.decode('utf-8')))
            proxies["https"] = "https://" + ip["data"][0]["IP"]
            # proxies["http"] = "http://" + ip["data"][0]["IP"]
        except Exception as e:
            print("get_one_proxies:", e)
            time.sleep(1)
            self.get_one_proxies()
        logging.info("获取一次代理为：" + str(proxies))
        return proxies

    def process_request(self, request, spider):
        pass

    def process_response(self, request, response, spider):
        if (response.status in self.RetryCode) and (self.retry_num < 3):
            if 'You have been locked out.' in response.text:
                spider.logger.info('error: You have been locked out.')
            self.retry_num += 1
            if not self.proxies:
                self.proxies = self.get_one_proxies()
                self.time_num = int(time.time())
            time_num = int(time.time())
            if time_num > (self.time_num + 50):
                self.proxies = self.get_one_proxies()
                self.time_num = int(time.time())
            request._set_url(request.url)
            request.meta['proxy'] = self.proxies['https']
            return request
        else:
            self.retry_num = 0
            return response


class RequestsMiddleware:
    name_list = ['Akha_jw']

    def process_request(self, request, spider):
        # pass

    # def process_response(self, request, response, spider):
    #     spider.logger.info('name=%s'%spider.name)
        if spider.name in self.name_list:
            # window_ck = "DUP=Q=JJJJXryd5-L3QuK4aqLt4w2&T=399963991&A=2&IG=D81DA1207A0E457DB8787259E0BBC73A; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=D7F2FA032A1A4744A66235DE51854B61&dmnchg=1; _EDGE_V=1; MUID=30AB513421EC63D834DC5E3920C262B7; MUIDB=30AB513421EC63D834DC5E3920C262B7; _FP=hta=on; ABDEF=V=0&ABDV=10&MRNB=1597197127944&MRB=0; NAP=V=1.9&E=1823&C=eBSVUIIJl2l-LuZJ3Z-528TDWaaSTAFczziRKnqbmNZ99pQJO4S00A&W=1; SerpPWA=reg=1; _SS=SID=02D5367371E067442F3B397D70CE66A0&bIm=643873&h5comp=2; ENSEARCH=BENVER=1; ipv6=hit=1599110758356&t=4; SRCHUSR=DOB=20200720&T=1599109585000&POEX=W; WLS=C=&N=; SNRHOP=I=&TS=; ULC=P=160D0|9:4&H=160D0|9:4&T=160D0|9:4; SRCHHPGUSR=DM=0&CW=1920&CH=969&DPR=1&UTC=480&HV=1599109903&WTS=63734706697; _EDGE_S=mkt=zh-cn&SID=24E7E7376907665A2F38E80D682967E6"
            # request.headers.setdefault('cookie', window_ck)
            headers = {
                # "cookie": request.headers['cookie'].decode(),
                # "referer": request.headers['referer'].decode(),
                "user-agent": request.headers['user-agent'].decode(),
            }
            url = request.url
            r = requests.get(url=url, headers=headers)
            r.encoding = 'utf-8'
            response = Response(url=r.url, status=r.status_code, body=r.text,
                                encoding=request.encoding, request=request)

            return response