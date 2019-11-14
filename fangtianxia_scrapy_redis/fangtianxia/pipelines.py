# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import JsonLinesItemExporter
from fangtianxia.items import ESFHouseItem,NewHouseItem

class NewhousePipeline():
    def __init__(self):
        self.newhouse_fp = open('newhouse.json', 'wb')
        self.newhouse_exporter = JsonLinesItemExporter(self.newhouse_fp, ensure_ascii=False)

    def process_item(self, item, spider):
        if isinstance(item,NewHouseItem):
            self.newhouse_exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.newhouse_fp.close()

class ESFhousePipeline():
    def __init__(self):
        self.esfhouse_fp = open('esfhouse.json', 'wb')
        self.esfhouse_exporter = JsonLinesItemExporter(self.esfhouse_fp, ensure_ascii=False)

    def process_item(self, item, spider):
        if isinstance(item,ESFHouseItem):
            self.esfhouse_exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.esfhouse_fp.close()
