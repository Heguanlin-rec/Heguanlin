
from scrapy import cmdline
# from setting import spider_name
spider_name = 'thai'
cmdline.execute(("scrapy crawl %s" % spider_name).split())