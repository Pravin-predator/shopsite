import scrapy


class MobileSpider(scrapy.Spider):
    name = 'mobile'
    start_urls = [
                  'https://webscraper.io/test-sites/e-commerce/allinone-popup-links/phones', ]

    def parse(self, response):

            for product in response.css("div.thumbnail"):

                yield {
                'product_name' : product.css('a.title::text').get(),
                'product_price': product.css('div.caption> h4.pull-right.price::text').get(),
                'product_description' : product.css('div.caption> p.description::text').get(),
                'product_review' : product.css('div.ratings> p.pull-right::text').get(),
                'product_imageLink' : product.css('img.img-responsive::attr(src)').get()


            }





