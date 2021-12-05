# -*- coding: utf-8 -*-
import scrapy

class NintendoBotSpider(scrapy.Spider):
    name = 'nintendo_bot'
    # acnh
    # allowed_domains = ['store.nintendo.co.uk/nintendo-switch-console/nintendo-switch-animal-crossing-new-horizons-edition/12458084.html']
    # start_urls = ['http://store.nintendo.co.uk/nintendo-switch-console/nintendo-switch-animal-crossing-new-horizons-edition/12458084.html/']

    #neon
    allowed_domains = ['store.nintendo.co.uk/nintendo-switch-console/nintendo-switch-with-neon-blue-neon-red-joy-con-controllers/12245286.html']
    start_urls = ['http://store.nintendo.co.uk/nintendo-switch-console/nintendo-switch-with-neon-blue-neon-red-joy-con-controllers/12245286.html/']


    # TEST URLS FOR IN STOCK ITEMS
    # allowed_domains = ['store.nintendo.co.uk/nintendo-switch-lite-console/nintendo-switch-lite-yellow/12258505.html']
    # start_urls = ['https://store.nintendo.co.uk/nintendo-switch-lite-console/nintendo-switch-lite-yellow/12258505.html/']

    custom_settings = {
        'FEED_URI' : 'tmp/'+name+'.csv'
    }

    def parse(self, response):
        in_stock      = False
        link         = self.start_urls[0]
        oos_str      = "Out of Stock"
        product      = response.css("h1.productName_title::text").get()
        status       = response.xpath("normalize-space(//div[@class='athenaProductPage_productAddToBasket']//span//span//button/text())").get()
        # in_stock_tag = "Add to Basket"

        if oos_str not in status:
            in_stock = True

        data = {
                'Status'  : status,
                'In Stock': in_stock,
                'Product' : product,
                'Link'    : link
               }

        yield data
