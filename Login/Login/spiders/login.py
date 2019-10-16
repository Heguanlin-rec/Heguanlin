# -*- coding: utf-8 -*-
import scrapy

from Login.items import LoginItem


class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['www.yaozh.com']
    start_urls = ['https://www.yaozh.com/member/']
    #
    # cookie = 'SINAGLOBAL=6607555641122.385.1551491737234; UM_distinctid=16d158a1f49368-0b3db98954b6f4-404b032d-144000-16d158a1f4a2eb; Ugrow-G0=9ec894e3c5cc0435786b4ee8ec8a55cc; login_sid_t=8e5392d2f3063737c91944aaf5038efd; cross_origin_proto=SSL; TC-V5-G0=0cd4658437f38175b9211f1336161d7d; WBStorage=384d9091c43a87a5|undefined; wb_view_log=1536*8641.25; _s_tentry=passport.weibo.com; UOR=www.njupt.edu.cn,widget.weibo.com,www.sogou.com; Apache=6092254818553.7705.1571024526956; ULV=1571024526962:13:1:1:6092254818553.7705.1571024526956:1569401501033; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWShDSfYNzBybRh9mwUQ25S5JpX5K2hUgL.Fo-0e0-71hMReh-2dJLoI0YLxK-L12qLBoqLxKMLBKML12zLxKMLB--LBK2LxKqL1hnL1K2LxK-L12qLB-zLxK-LB-zL1hzLxK-LB-zL1hzt; ALF=1602560500; SSOLoginState=1571024501; SCF=Ahlu6WE_KDA0XrfdURhGT4fXpgY_sneX6vK95Jst31qhUW47um1zCO6JJBudtcTZvXzOT49UiXam56Cz3UyCFRQ.; SUB=_2A25wp54lDeRhGeNN6FcR-CnEyzmIHXVT1IjtrDV8PUNbmtAKLRLekW9NSagt7DT8-CujjUePvjSbi-SAq1nG6otf; SUHB=0mxkIUS0KdKVTa; un=13898045173; wvr=6; wb_view_log_5335087805=1536*8641.25; TC-Page-G0=2f200ef68557e15c78db077758a88e1f|1571024511|1571024511; webim_unReadCount=%7B%22time%22%3A1571024582586%2C%22dm_pub_total%22%3A1%2C%22chat_group_client%22%3A0%2C%22allcountNum%22%3A62%2C%22msgbox%22%3A0%7D'
    cookie = 'acw_tc=707c9f9a15710260059963157e795dd975fdba9b2fb87a98e3b6ef537db3d4; PHPSESSID=l0ug1p21m28g8d2lk7lk80h9h4; _ga=GA1.2.675446346.1571026051; _gid=GA1.2.1556399626.1571026051; Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94=1571026051; yaozh_userId=825605; _gat=1; Hm_lpvt_65968db3ac154c3089d7f9a4cbb98c94=1571026124; yaozh_uidhas=1; yaozh_mylogin=1571026084; acw_tc=707c9f9a15710260059963157e795dd975fdba9b2fb87a98e3b6ef537db3d4; UtzD_f52b_saltkey=z323r2c7; UtzD_f52b_lastvisit=1571028819; _ga=GA1.1.1732899634.1571035001; _gid=GA1.1.315532701.1571035001; UtzD_f52b_ulastactivity=1571026078%7C0; UtzD_f52b_creditnotice=0D0D2D0D0D0D0D0D0D719706; UtzD_f52b_creditbase=0D0D0D0D0D0D0D0D0; UtzD_f52b_creditrule=%E6%AF%8F%E5%A4%A9%E7%99%BB%E5%BD%95; _gat=1; yaozh_logintime=1571040613; yaozh_user=825605%09heguanlin945; db_w_auth=719706%09heguanlin945; UtzD_f52b_lastact=1571040614%09uc.php%09; UtzD_f52b_auth=1584z0mYxS14HmQLr6vWxbrZAMxNMVO2jedDF2E9hQCBv10SKD8ssqleiwBoikPTJFcv3EKVxe9Vu6uOFDm3Dfljkpg'
    cookies = {i.split('=')[0]: i.split('=')[1] for i in cookie.split('; ')}

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, cookies=self.cookies, callback=self.parse)

    def parse(self, response):
        # item = LoginItem()
        #
        # item['title'] = response.xpath('//*[@id="U_warp"]/div/div[1]/div/div[2]/div[1]/div[1]/div/span[1]/em/label//text()').extract_first()
        #
        # return item

        with open('login.html' , 'wb') as f:
            f.write(response.body)