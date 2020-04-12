# -*- coding: utf-8 -*-
import scrapy


class AoBotTestSpider(scrapy.Spider):
    name = 'ao_bot_test'
    allowed_domains = ['ao.com/product/10002200-nintendo-console-grey-72865-291.aspx']
    start_urls = ['https://ao.com/product/10002200-nintendo-console-grey-72865-291.aspx/']

    custom_settings = {
        'FEED_URI' : 'tmp/'+name+'.csv'
    }

    def parse(self, response):
        in_stock      = False
        link         = self.start_urls[0]
        oos_str      = "Unavailable"
        product      = response.css("#pageTitle::text").get()
        status       = response.css("div.inStock > span.inStockText::text").get()
        status = "Unavailable"

        if (status != 'None') and (oos_str not in status):
            in_stock = True

        data = {
                'Status'  : status,
                'In Stock': in_stock,
                'Product' : product,
                'Link'    : link
               }

        yield data
