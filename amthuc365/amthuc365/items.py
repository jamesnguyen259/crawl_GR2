# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Amthuc365Item(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    location = scrapy.Field()
    lat = scrapy.Field()
    lng = scrapy.Field()
    source_url = scrapy.Field()
    time = scrapy.Field()
    price = scrapy.Field()
    phone = scrapy.Field()
    image_url = scrapy.Field()
    description = scrapy.Field()
    # pass
