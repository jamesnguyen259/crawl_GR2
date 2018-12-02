# -*- coding: utf-8 -*-
import scrapy


class HanoialleventSpider(scrapy.Spider):
    name = 'hanoiallevent'
    start_urls = [
                'https://allevents.in/hanoi/all',
            ]

    def parse(self, response):
        for event in response.css('.event-item.bound .event-body.clearfix'):
            yield {
                'name': event.css('.left h3 a)').extract_first(),
                'place' : event.css('.left p.location span::text').extract_first(),
                'time': event.css('.right span::text').extract_first(),
            }
