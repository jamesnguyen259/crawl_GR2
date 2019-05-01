# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HanoialleventItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    location = scrapy.Field()
    lat = scrapy.Field()
    lng = scrapy.Field()
    start_time = scrapy.Field()
    end_time = scrapy.Field()
    source_url = scrapy.Field()
    image_url = scrapy.Field()
    description = scrapy.Field()
    organizer_name = scrapy.Field()
    # pass
