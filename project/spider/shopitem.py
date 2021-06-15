import scrapy
from ..items import ShoppingItem

class MobileSpider(scrapy.Spider):
    name = 'mobile'
    start_urls = [
                  'http://webscraper.io/test-sites/e-commerce/allinone-popup-links/phones',]

    def parse(self, response):

        for product in response.css('div.col-sm-4 col-lg-4 col-md-4'):

            yield {
                'product_name': product.css('div.caption>a.title::text').ectract(),
                'product_price': product.css('div.caption> h4.pull-right price ::text').extract(),
                'product_description': product.css('div.caption> p.description::text').extract(),
                'product_review': product.css('div.ratings> p.pull-right::text').extract(),
                'product_imglnk': product.css('img.img-responsive::attr(src').extract()
            }





