# -*- coding: utf-8 -*-
import scrapy

class DulichTodaySpider(scrapy.Spider):
    name = "dulichtoday"
    start_urls = [
            'https://dulichtoday.vn/kham-pha-ha-noi/su-kien-ha-noi',
        ]

    def parse(self, response):
        # follow links to event pages
        for href in response.css('li.post-item.post.type-post.status-publish.format-standard.has-post-thumbnail.category-su-kien-ha-noi div h2 a::attr(href) '):
            yield response.follow(href, self.parse_link)
        # follow pagination links
        for href in response.css('li.the-next-page a::attr(href)'):
            yield response.follow(href, self.parse)

    def parse_link(self, response):
        def extract_with_css(querry):
            return response.css(querry).extract_first().encode('utf-8').strip()

        def extract_with_xpath(querry):
            return response.xpath(querry).extract_first().encode('utf-8').strip()

        if 'Chủ đề' in extract_with_css('div.entry-content.entry.clearfix p span strong::text'):
          yield{
            'event_name': extract_with_css('div.entry-content.entry.clearfix h2::text'),
            'event_time': response.css('div.entry-content.entry.clearfix p span::text').extract()[1].encode('utf-8').strip(),
            'event_place': response.css('div.entry-content.entry.clearfix p span::text').extract()[2].encode('utf-8').strip()
          }
        else:
          yield {
            'event_name': extract_with_css('div.entry-content.entry.clearfix h2::text'),
            'event_time': extract_with_css('div.entry-content.entry.clearfix p span::text'),
            'event_place': response.css('div.entry-content.entry.clearfix p span::text').extract()[1].encode('utf-8').strip()
          }
