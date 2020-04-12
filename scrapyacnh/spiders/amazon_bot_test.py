# -*- coding: utf-8 -*-
import scrapy
from re import sub
from decimal import Decimal

class AmazonBotTestSpider(scrapy.Spider):
    name = 'amazon_bot_test'
    allowed_domains = ['www.amazon.co.uk/gp/offer-listing/B081W4XHMZ/ref=olp_twister_child?ie=UTF8&mv_edition=all&mv_platform_for_display=1']
    start_urls = ['https://www.amazon.co.uk/gp/offer-listing/B081W4XHMZ/ref=olp_twister_child?ie=UTF8&mv_edition=all&mv_platform_for_display=1']

    # setting the location of the output csv file
    custom_settings = {
        'FEED_URI' : 'tmp/'+name+'.csv'
    }

    def parse(self, response):
        in_stock = False
        link     = self.start_urls[0]
        product  = response.css("#variationsTwister > div > span::text").getall()[1]
        status   = Decimal(sub(r'[^\d.]', '', response.css("span.olpOfferPrice::text").get()))


        if status < 300: #if lower than £400
            in_stock = True

        data = {
                'Status'  : status,
                'In Stock': in_stock,
                'Product' : product,
                'Link'    : link
               }

        yield data
