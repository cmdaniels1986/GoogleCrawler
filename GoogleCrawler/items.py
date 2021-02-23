# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GooglecrawlerItem(scrapy.Item):

    orig_url = scrapy.Field()
    url = scrapy.Field()
    email_address = scrapy.Field()
    
