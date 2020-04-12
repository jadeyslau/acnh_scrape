# -*- coding: utf-8 -*-
import scrapy

class JohnlewisBotTestSpider(scrapy.Spider):
    name = 'johnlewis_bot_test'
    allowed_domains = ['www.johnlewis.com/nintendo-switch-1-1-32gb-console-with-joy-con/neon/p4751133']
    start_urls = ['http://www.johnlewis.com/nintendo-switch-1-1-32gb-console-with-joy-con/neon/p4751133/']

    custom_settings = {
        'FEED_URI' : 'tmp/'+name+'.csv'
    }

    def parse(self, response):
        in_stock      = False
        link         = self.start_urls[0]
        oos_str      = "Currently unavailable"
        product      = response.css("h1.product-header__title::text").get()
        status       = response.xpath("normalize-space(//form[@class='add-to-basket-form']//div//div//button)").get()
        in_stock_tag = "Add to your basket"

        if (in_stock_tag != 'None') and (oos_str not in status):
            in_stock = True

        data = {
                'Status'  : status,
                'In Stock': in_stock,
                'Product' : product,
                'Link'    : link
               }

        yield data
