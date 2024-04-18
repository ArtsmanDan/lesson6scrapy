# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from pymongo import MongoClient


class UnsplashPipeline:
    def process_item(self, item, spider):
        item['url_image'] = item['url_image'].split(',')[-1].split()[0]
        return item


class ImagesUnsplahPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if item['url_image']:
            try:
                yield scrapy.Request(item['url_image'])
            except Exception as e:
                print(e)
        return item

    def item_completed(self, results, item, info):
        if results:
            item['url_image'] = [x[1] for x in results if x[0]]
        return item


class UnsplashMongodbPipeline:
    def __init__(self):
        client = MongoClient('localhost', 27018)
        self.mongo_base = client.images18042023

    def process_item(self, item, spider):
        collection = self.mongo_base[spider.name]
        collection.insert_one(item)
        return item
