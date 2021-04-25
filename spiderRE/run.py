# coding: utf-8
from scrapy import cmdline
# from setting import spider_name
spider_name = 'people'
cmdline.execute(("scrapy crawl %s"%spider_name).split())