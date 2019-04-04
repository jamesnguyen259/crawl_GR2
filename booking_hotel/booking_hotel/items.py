# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BookingHotelItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    location = scrapy.Field()
    url = scrapy.Field()
    image = scrapy.Field()
    description = scrapy.Field()
    rating = scrapy.Field()
    # pass
