# -*- coding: utf-8 -*-
import scrapy
import re
from fangtianxia.items import NewHouseItem,ESFHouseItem
from scrapy_redis.spiders import RedisSpider

class FangSpider(RedisSpider):
    name = 'fang'
    allowed_domains = ['fang.com']

    redis_key = "fang:start_urls"
    # start_urls = ['https://www.fang.com/SoufunFamily.htm']

    def parse(self, response):
        trs = response.xpath('//div[@class="outCont"]//tr')
        province_text = None
        for tr in trs:
            tds = tr.xpath('.//td[not(@class)]')
            td_province = tds[0]
            province = td_province.xpath('.//text()').get()
            province = re.sub(r'\s', '', province)
            if province:
                province_text = province

            # 不爬取海外国家
            if province_text == '其它':
                continue
            td_city = tds[1]
            cities = td_city.xpath('.//a')
            for td in cities:
                city_name = td.xpath('.//text()').get()
                city_url = td.xpath('.//@href').get()
                # 构建新房的url链接
                url_module = city_url.split('.', 1)
                scheme = url_module[0]
                domain = url_module[1]
                newhouse_url = scheme + '.newhouse.' + domain + 'house/s'
                # print(newhouse_url)

                # 构建二手房的url链接
                esf_url = scheme + '.esf.' + domain
                # print(esf_url)

                yield scrapy.Request(url=newhouse_url, callback=self.parse_newhouse,
                                     meta={"info": (province_text, city_name)})
                yield scrapy.Request(url=esf_url, callback=self.parse_esf, meta={"info": (province_text, city_name)})

            #     break
            # break

    def parse_newhouse(self, response):
        province, city = response.meta.get('info')
        lis = response.xpath('//div[contains(@class,"nl_con")]/ul/li')
        for li in lis:
            name_li = li.xpath(".//div[@class='nlcd_name']/a/text()").get()
            # name_li = filter(lambda x:x is not None,name_li)
            if name_li is not None:
                name = name_li.strip()
            else:
                name = ""
            house_type_list = li.xpath('.//div[contains(@class,"house_type")]/a/text()').getall()
            house_type_list = list(map(lambda x:re.sub(r"\s", "" ,x),house_type_list))
            rooms = list(filter(lambda x:x.endswith("居"),house_type_list))
            area = "".join(li.xpath('.//div[contains(@class,"house_type")]/text()').getall())
            area = re.sub(r'\s|－|/',"",area)
            address = li.xpath(".//div[@class='address']/a/@title").get()
            district_text = "".join(li.xpath(".//div[@class='address']/a//text()").getall())
            a = re.search(r".*\[(.+)\].*", district_text)
            if a is not None:
                district = a.group(1)
            else:
                district = ""
            sale = li.xpath(".//div[contains(@class,'fangyuan')]/span/text()").get()
            price = "".join(li.xpath(".//div[@class='nhouse_price']//text()").getall())
            price = re.sub(r"\s|广告","",price)
            b = li.xpath(".//div[@class='nlcd_name']/a/@href").get()
            if b is not None:
                url ='https:' + li.xpath(".//div[@class='nlcd_name']/a/@href").get()
            else:
                url = ""
            item = NewHouseItem(name=name,rooms=rooms,area=area,address=address,district=district,sale=sale,price=price,url=url,province=province,city=city)
            yield item

        next_url = response.xpath("//div[@class='page']//a[@class='next']/@href").get()
        if next_url:
            yield scrapy.Request(url=response.urljoin(next_url),callback=self.parse_newhouse,meta={'info':(province,city)})
#
    def parse_esf(self, response):
        province, city = response.meta.get('info')
        dls = response.xpath("//div[contains(@class,'shop_list_4')]/dl")
        for dl in dls:
            item = ESFHouseItem(province=province,city=city)
            c = dl.xpath(".//p[@class='add_shop']/a/text()").get()
            if c is not None:
                name = c.strip()
            else:
                name = ""
            item['name'] = name
            infos = dl.xpath(".//p[@class='tel_shop']/text()").getall()
            infos = list(map(lambda x:re.sub(r"\s","",x),infos))
            for info in infos:
                if "厅" in info:
                    item['rooms'] = info
                elif '层' in info:
                    item['floor'] = info
                elif '向' in info:
                    item['toward'] = info
                elif '㎡' in info:
                    item['area'] = info
                else:
                    item['year'] = info
            item['address'] = dl.xpath(".//p[@class='add_shop']/span/text()").get()
            item['price'] = "".join(dl.xpath(".//dd[@class='price_right']/span[@class='red']//text()").getall())
            item['unit'] = dl.xpath(".//dd[@class='price_right']/span[not(@class)]/text()").get()
            d = dl.xpath(".//h4[@class='clearfix']/a/@href").get()
            url = response.urljoin(d)
            item['url'] = url
            yield item
        next_url = response.xpath("//div[@id='list_D10_15']/p/a/@href").get()
        yield scrapy.Request(url=response.urljoin(next_url),callback=self.parse_esf,meta={"info":(province,city)})