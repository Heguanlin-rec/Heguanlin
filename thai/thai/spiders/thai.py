import scrapy
from ..items import ThaiItem

class QuoteSpider(scrapy.Spider):
    name = 'thai'
    start_urls = []

    # 获取全部翻页链接
    # for i in range(1, 23):
    #     url = 'https://engoo.co.th/app/words/list/en/e?page=' + str(i)
    #     start_urls.append(url)


    def start_requests(self):
        # 获取全部翻页链接
        for i in range(1, 17):
            url = 'https://engoo.co.th/app/words/list/en/a?page=' + str(i)
            yield scrapy.Request(url=url)
            #break


    # 获取每页的url
    def parse(self, response):
        urls = response.xpath("//div[@class='css-rv942s']/span/a/@href").extract()
        for url in urls:
            url_new = "https://engoo.co.th" + url
            yield scrapy.Request(url_new, callback=self.parse_item)
            #break


    """解析页面：错误"""

    # def parse(self, response):
    #     divs = response.xpath("//div[@class='css-rv942s']")
    #     for div in divs:
    #         item = ThaiItem()
    #         item['en'] = div.xpath("./span[@class='css-1sylyko']/a/text()").extract_first()
    #         item['thai'] = div.xpath("./span[@class='css-epvm6']/span/div[@class='css-jiq801']/text()").extract_first()
    #         yield item
    #
    #     next = response.xpath("//div[@class='css-x9n345']/div/a[last()]/@href").extract_first()
    #     new_url = 'https://engoo.co.th' + next
    #
    #     yield scrapy.Request(url=new_url, callback=self.parse)   # 这个请求完成后，响应会重新经过parse方法处理，得到第二页的解析结果，一直循环到最后一页

    # 抓取详细页的内容
    def parse_item(self, response):

        divs_top = response.xpath("//div[@class='css-1p8520y']")
        item = ThaiItem()
        for div in divs_top:
            en_text_l = div.xpath(".//div/span[@class='css-79elbk']/span//text()").extract()
            en_text = ''.join(en_text_l)
            item['en_text'] = en_text
            item['thai_text'] = div.xpath(".//div[@class='css-79elbk']/span[@lang='th']/span/text()").extract_first()
            # print(item)
            yield item

        divs_bot = response.xpath("//div[@class='css-kp3nri']")
        for div in divs_bot:
            item['en_text'] = div.xpath("./div[@class='css-nipsa6']/span[@class='css-35ezg3']/text()").extract_first()
            item['thai_text'] = div.xpath("./div[@class='css-nipsa6']/span[@class='css-l3ddl3']/text()").extract_first()
            # print(item)
            yield item

