# -*- coding: utf-8 -*-
import scrapy

class TestSpider(scrapy.Spider):
    name = "test"
    start_urls = [
        'https://dulichtoday.vn/kham-pha-ha-noi/su-kien-ha-noi/hoi-nghi-bat-dong-san-quoc-te-irec-2018.html',
        'https://dulichtoday.vn/kham-pha-ha-noi/su-kien-ha-noi/cho-phien-ha-noi-2018.html'
    ]

    def parse(self, response):
        def extract_with_css(querry):
            return response.css(querry).extract_first().encode('utf-8').strip()
        # for content in response.css('div.junkie-alert.yellow p'):
        if 'Chủ đề' in extract_with_css('div.junkie-alert.yellow p span strong::text'):
          yield{
            'time': response.css('div.junkie-alert.yellow p span::text').extract()[1].encode('utf-8').strip(),
            'place': response.css('div.junkie-alert.yellow p span::text').extract()[2].encode('utf-8').strip()
          }
        else:
          yield {
            'time': extract_with_css('div.junkie-alert.yellow p span::text'),
            'place': response.css('div.junkie-alert.yellow p span::text').extract()[1].encode('utf-8').strip()
          }
