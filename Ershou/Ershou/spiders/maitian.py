# -*- coding: utf-8 -*-
import scrapy

from Ershou.items import ErshouItem


class MaitianSpider(scrapy.Spider):
    name = 'maitian'
    allowed_domains = ['bj.maitian.cn']

    url = 'http://bj.maitian.cn/esfall/PG{}'
    page = 1
    start_urls = [url.format(page)]

    def parse(self, response):
        # 1.获取所有房子

        room_list = response.xpath('//div[@class="list_wrap"]/ul/li/div[@class="list_title"]')
        # print(len(room_list))
        # 2.解析各项信息

        item = ErshouItem()
        for room in room_list[:1]:
            item['title'] = room.xpath('./h1/a/text()').extract_first()
            item['detail'] = room.xpath('./p//text()').extract()
            detail_url = 'http://bj.maitian.cn' + room.xpath('./h1/a/@href').extract_first()
            item['price'] = room.xpath('./div/ol/strong/span/text()').extract_first()

            # yield item

            # 发送详情页的请求
            yield scrapy.Request(
                detail_url,
                callback=self.parse_detail,
                meta={'ershou': item}
            )

    def parse_detail(self, response):

        item = response.meta['ershou']
        item['shoufu'] = response.xpath('/html/body/section[2]/div[1]/table/tbody/tr[3]/td[1]//text()').extract()
        yield item

        # print(shoufu)
        # with open('ershou.html', 'wb') as f:
        #     f.write(response.body)

        # 3.循环
        # self.page += 1
        # url = self.url.format(self.page)
        #
        #
        # yield scrapy.Request(
        #     url,
        #     callback=self.parse
        #
        # )
