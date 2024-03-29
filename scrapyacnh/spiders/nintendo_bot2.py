# -*- coding: utf-8 -*-
import scrapy

class NintendoBot2Spider(scrapy.Spider):
    name = 'nintendo_bot2'
    # acnh
    # allowed_domains = ['store.nintendo.co.uk/nintendo-switch-console/nintendo-switch-animal-crossing-new-horizons-edition-pack/12458669.html']
    # start_urls = ['http://www.store.nintendo.co.uk/nintendo-switch-console/nintendo-switch-animal-crossing-new-horizons-edition-pack/12458669.html/']

    # grey
    allowed_domains = ['store.nintendo.co.uk/nintendo-switch-console/nintendo-switch-with-grey-joy-con-controllers/12245184.html']
    start_urls = ['http://store.nintendo.co.uk/nintendo-switch-console/nintendo-switch-with-grey-joy-con-controllers/12245184.html/']

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
