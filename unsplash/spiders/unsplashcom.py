import scrapy
from scrapy.http import HtmlResponse
from unsplash.items import UnsplashItem
from scrapy.loader import ItemLoader


# //img[@itemprop="thumbnailUrl"]/@srcset
# //img[@itemprop="thumbnailUrl"]/@alt
# //h1
# //li/a

class UnsplashSpider(scrapy.Spider):
    name = "Unsplashcom"
    allowed_domains = ["unsplash.com"]
    start_urls = ["https://unsplash.com/"]

    def parse(self, response: HtmlResponse, **kwargs):
        links_categories = response.xpath('//li/a/@href').getall()
        links_categories = [x for x in links_categories if x.startswith('/t/')]
        print()
        for link in links_categories:
            yield response.follow(link, callback=self.image_parse)

    def image_parse(self, response: HtmlResponse):

        # category = response.xpath('//h1/text()').get()
        images = response.xpath('//img[@itemprop="thumbnailUrl"]')
        for image in images:
            name_image = image.xpath('@alt').get()
            url_image = image.xpath('@srcset').get()
            #     yield UnsplashItem(
            #
            #         category=category,
            #         name_image=name_image,
            #         url_image=url_image
            #     )
            loader = ItemLoader(item=UnsplashItem(), response=response)
            loader.add_value('url_category', response.url)
            loader.add_xpath('category', '//h1/text()')
            loader.add_value('name_image', name_image)
            loader.add_value('url_image', url_image)
            yield loader.load_item()
