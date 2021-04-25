# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderreItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass



class PublicItem(scrapy.Item):
    data = scrapy.Field()
    part = scrapy.Field()
    url = scrapy.Field()
    group = scrapy.Field()
    error_url = scrapy.Field()
