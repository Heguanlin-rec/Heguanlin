# -*- coding: utf-8 -*-
import scrapy


class LoginCodeSpider(scrapy.Spider):
    name = 'login_code'
    allowed_domains = ['www.yaozh.com']

    # 1. 登录页面---> 找齐登录需要的参数
    start_urls = ['https://www.yaozh.com/login']

    def parse(self, response):
        # 2.代码登录
        login_url = 'https://www.yaozh.com/login'
        formdata = {
            'username': 'heguanlin945',
            'pwd': 'heguanlin6433',
            'formhash': response.xpath('//input[@id="formhash"]/@value').extract_first(),
            'backurl': response.xpath('//input[@id="backurl"]/@value').extract_first()

        }

        # 发送登录请求 POST
        yield scrapy.FormRequest(
            login_url,
            formdata=formdata,
            callback=self.parse_login
        )

    def parse_login(self, response):
        # scrapy携带着有效的cookie继续请求目标数据

        # 3.访问目标页面
        member_url = 'https://www.yaozh.com/member'
        yield scrapy.Request(
            member_url,
            callback=self.parse_member
        )

    def parse_member(self, response):
        with open('login_code.html', 'wb') as f:
            f.write(response.body)
