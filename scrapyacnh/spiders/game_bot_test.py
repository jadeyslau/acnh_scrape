# -*- coding: utf-8 -*-
import scrapy

class GameBotTestSpider(scrapy.Spider):
    name = 'game_bot_test'
    allowed_domains = ['www.game.co.uk/en/nintendo-switch-neon-improved-battery-animal-crossing-new-horizons-2729644']
    start_urls = ['http://www.game.co.uk/en/nintendo-switch-neon-improved-battery-animal-crossing-new-horizons-2729644/']

    #setting the location of the output csv file
    custom_settings = {
        'FEED_URI' : 'tmp/'+name+'.csv'
    }

    def parse(self, response):
        in_stock      = False
        link          = self.start_urls[0]
        oos_str       = "Sorry, this product is currently out of stock"
        product       = response.css(".container > h1::text").get()
        status        = response.xpath("normalize-space(//div[@class='outOfStock']/text())").get()
        in_stock_tag  = response.xpath("//strong[@class='btnName']/text()").get()

        if (in_stock_tag != 'None') and (oos_str not in status):
            in_stock = True

        data = {
                'Status'  : status,
                'In Stock': in_stock,
                'Product' : product,
                'Link'    : link
               }

        yield data
