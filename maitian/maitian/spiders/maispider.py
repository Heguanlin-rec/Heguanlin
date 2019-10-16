# -*- coding: utf-8 -*-
import scrapy

from maitian.items import MaitianItem


class MaispiderSpider(scrapy.Spider):
    name = 'maispider'
    allowed_domains = ['xm.maitian.cn']
    start_urls = ['http://xm.maitian.cn/esfxq/IH10029304']
                  # 'http://xm.maitian.cn/esfxq/IH10029304',
                  # 'http://xm.maitian.cn/esfxq/IH10029304',
                  # 'http://xm.maitian.cn/esfxq/IH10029304',
                  # 'http://xm.maitian.cn/esfxq/IH10029304',
                  # 'http://xm.maitian.cn/esfxq/IH10029304',
                  # 'http://xm.maitian.cn/esfxq/IH10029304']

    def parse(self, response):
        item = MaitianItem()

        item['room_title'] = response.xpath('//*[@id="status"]/section[1]/dl/h3/span//text()').extract_first()

        yield item