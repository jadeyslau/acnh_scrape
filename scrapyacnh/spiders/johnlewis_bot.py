# -*- coding: utf-8 -*-
import scrapy

class JohnlewisBotSpider(scrapy.Spider):
    name = 'johnlewis_bot'
    allowed_domains = ['www.johnlewis.com/nintendo-switch-1-1-console-with-animal-crossing-new-horizons-game-bundle/p4918594']
    start_urls = ['http://www.johnlewis.com/nintendo-switch-1-1-console-with-animal-crossing-new-horizons-game-bundle/p4918594/']

    # TEST URLS FOR IN STOCK ITEMS
    # allowed_domains = ['www.johnlewis.com/nintendo-poke-ball-plus-switch-controller-and-pokemon-container/p3850568']
    # start_urls = ['http://www.johnlewis.com/nintendo-poke-ball-plus-switch-controller-and-pokemon-container/p3850568/']

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
