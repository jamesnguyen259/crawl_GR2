# -*- coding: utf-8 -*-
import scrapy

class DulichTodaySpider(scrapy.Spider):
    name = "dulichtoday"
    start_urls = [
            'https://dulichtoday.vn/kham-pha-ha-noi/su-kien-ha-noi',
        ]

    def parse(self, response):
        for url in response.css('div.latestPost-layout'):
            yield{
                    'event_url': url.css('a::attr(href)').extract_first(),
            }

        next_page = response.css('div.nav-links a.next.page-numbers::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
