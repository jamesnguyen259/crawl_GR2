# -*- coding: utf-8 -*-
import scrapy
from urlparse import urljoin
class AllEventSpider(scrapy.Spider):
    name = "allevent"
    start_urls = [
            'https://allevents.in/hanoi/all',
        ]

    def parse(self, response):
        # follow links to event pages
        for href in response.css("div.event-body.clearfix div.left h3 a::attr('href')"):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback = self.parse_link)

    def parse_link(self, response):
        def extract_with_css(querry):
            return response.css(querry).extract_first().encode('utf-8').strip()

        def extract_with_xpath(querry):
            return response.xpath(querry).extract_first().encode('utf-8').strip()
        yield{
            'event_name' : extract_with_css('h1.overlay-h1::text')
        }

