# -*- coding: utf-8 -*-
import scrapy

class VeryBotSpider(scrapy.Spider):
    name = 'very_bot'
    allowed_domains = ['www.very.co.uk/nintendo-switch-nintendo-switch-animal-crossing-new-horizons-edition-console/1600456594.prd']
    start_urls = ['http://www.very.co.uk/nintendo-switch-nintendo-switch-animal-crossing-new-horizons-edition-console/1600456594.prd/']

    # Google cached version...
    # allowed_domains = ['webcache.googleusercontent.com/search?q=cache:m7UzQGUY-doJ:https://www.very.co.uk/nintendo-switch-nintendo-switch-animal-crossing-new-horizons-edition-console/1600456594.prd+']
    # start_urls = ['https://webcache.googleusercontent.com/search?q=cache:m7UzQGUY-doJ:https://www.very.co.uk/nintendo-switch-nintendo-switch-animal-crossing-new-horizons-edition-console/1600456594.prd+/']

    #setting the location of the output csv file
    # custom_settings = {
    #     'FEED_URI' : 'tmp/'+name+'.csv'
    # }

    def parse(self, response):
        in_stock      = False
        link          = self.start_urls[0]
        oos_str       = "Out of stock"
        product       = response.css("h1.productHeading > span::text").get()
        status        = response.xpath("normalize-space(//div[@class='stockMessaging']//span[@class='indicator']/text())").get()
        in_stock_tag  = 'Available'

        if oos_str not in status:
            in_stock = True

        data = {
                'Status'  : status,
                'In Stock': in_stock,
                'Product' : product,
                'Link'    : link
               }
        print(data)
        # yield data
