# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os
from itemadapter import ItemAdapter
from .filter import FilterClass


class SpiderrePipeline:
    def process_item(self, item, spider):
        return item



class SpiderPublicPipeline(FilterClass):
    def process_item(self, item, spider):
        name = spider.name
        language = spider.language
        try:
            datatype = spider.datatype
        except:
            spider.logger.info('[Warning: Please set datatype in your spider.py]')
            datatype = ''
        file_name = str(name) + '.' + str(language)
        part_file_name = str(file_name) + '.part'
        urls_name = str(name) + '.urls'
        error_urls_name = str(name) + '.urls.error'
        path = spider.path
        if not os.path.exists(path):
            os.mkdir(path)
        file_path = os.path.join(path, file_name)
        part_file_path = os.path.join(path, part_file_name)
        urls_path = os.path.join(path, urls_name)
        error_urls_path = os.path.join(path, error_urls_name)
        if 'data' in item.keys():
            data = item['data']
            # 判断数据过滤方式
            if datatype == 'sentence':
                filter_func, f_status = self.get_filter_func_by_language(language)
                data = filter_func(data)
            else:
                data = self.general_filter(data)
            if data:
                with open(file_path, 'a', encoding='utf-8')as fp:
                    fp.write(str(data) + '\n')
                    fp.flush()
        elif 'part' in item.keys():
            with open(part_file_path, 'a', encoding='utf-8')as fp:
                fp.write(str(item['part']) + '\n')
                fp.flush()
        elif 'url' in item.keys():
            with open(urls_path, 'a', encoding='utf-8')as fp:
                fp.write(str(item['url']) + '\n')
                fp.flush()
        elif 'error_url' in item.keys():
            with open(error_urls_path, 'a', encoding='utf-8')as fp:
                fp.write(str(item['error_url']) + '\n')
                fp.flush()
        return item
