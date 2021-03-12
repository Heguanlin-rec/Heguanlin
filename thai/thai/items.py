# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ThaiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    en_text = scrapy.Field()
    thai_text = scrapy.Field()
