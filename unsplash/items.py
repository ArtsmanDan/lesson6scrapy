# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, MapCompose, Compose

class UnsplashItem(scrapy.Item):
    # define the fields for your item here like:
    _id = scrapy.Field()
    url_category = scrapy.Field(output_processor=TakeFirst())
    category = scrapy.Field(output_processor=TakeFirst())
    name_image = scrapy.Field(output_processor=TakeFirst())
    url_image = scrapy.Field(output_processor=TakeFirst())
