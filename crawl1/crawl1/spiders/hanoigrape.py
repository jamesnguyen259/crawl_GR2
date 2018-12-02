# -*- coding: utf-8 -*-
import scrapy


class HanoigrapeSpider(scrapy.Spider):
    name = 'hanoigrape'
    allowed_domains = ['https://hanoigrapevine.com/vi/tag/whats-on-hanoi/']
    start_urls = ['https://hanoigrapevine.com/vi/tag/whats-on-hanoi/']

    def parse(self, response):
        for event in response.css('div.td_mod_wrap.td_mod8 div.item-details'):
            yield {
                'name' : event.css('h3 a::attr(title)').extract_first().encode('utf-8')
            }


