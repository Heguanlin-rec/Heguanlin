# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ThaiPipeline:

    def process_item(self, item, spider):
        res = dict(item)
        en_text = res['en_text']
        thai_text = res['thai_text']
        with open('save.txt', 'a', encoding='utf-8') as fw:
            fw.write(en_text + '\t' + thai_text + '\n')
        return item
