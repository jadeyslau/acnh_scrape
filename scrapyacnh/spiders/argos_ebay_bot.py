# -*- coding: utf-8 -*-
import scrapy
from re import sub
from decimal import Decimal

class ArgosEbayBotSpider(scrapy.Spider):
    name = 'argos_ebay_bot'
    allowed_domains = ['www.ebay.co.uk/itm/Nintendo-Switch-Console-Animal-Crossing-Edition/353014271280']
    start_urls = ['http://www.ebay.co.uk/itm/Nintendo-Switch-Console-Animal-Crossing-Edition/353014271280/']

    # setting the location of the output csv file
    custom_settings = {
        'FEED_URI' : 'tmp/'+name+'.csv'
    }

    def parse(self, response):
        in_stock = False
        link     = self.start_urls[0]
        product  = response.css("h1.it-ttl::text").get()
        status   = Decimal(sub(r'[^\d.]', '', response.css("#qtySubTxt > span::text").get())) # product quantity available

        if status > 0: #if more than 0 units available
            in_stock = True

        data = {
                'Status'  : status,
                'In Stock': in_stock,
                'Product' : product,
                'Link'    : link
               }

        yield data
