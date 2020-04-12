# -*- coding: utf-8 -*-
import scrapy

class CurrysBotSpider(scrapy.Spider):
    name = 'currys_bot'
    allowed_domains = ['www.currys.co.uk/gbuk/s_action/compare/10206234-10206236-10206237-10206235.html']
    start_urls = ['https://www.currys.co.uk/gbuk/s_action/compare/10206234-10206236-10206237-10206235.html/']

    custom_settings = {
        'FEED_URI' : 'tmp/'+name+'.csv'
    }

    def parse(self, response):
        in_stock = False
        link     = self.start_urls[0]
        oos_str  = "Out of Stock"
        # products = response.xpath("//tr[@class=disablePrint]//td//strong")
        products = response.css("div#content").get()
        # status   = response.xpath("normalize-space(//div[@class='athenaProductPage_productAddToBasket']//span//span//button/text())").get()
        # in_stock_tag = "Add to Basket"
        print(response.body, products, 'THIS IS PRODUCTS')
        # for product in products:
        #     print(product, 'HEEEEEELLO')
            # yield {
            #     'author': quote.xpath('span/small/text()').get(),
            #     'text': quote.css('span.text::text').get(),
            # }

        # if oos_str not in status:
        #     in_stock = True
        #data = {
               #  'Status'  : status,
               #  'In Stock': in_stock,
               #  'Product' : product,
               #  'Link'    : link
               # }
        #
        # yield data
