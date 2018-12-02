import scrapy


class DulichTodaySpider(scrapy.Spider):
    name = "dulichtoday"
    start_urls = [
            'https://dulichtoday.vn/kham-pha-ha-noi/su-kien-ha-noi',
        ]

    def parse(self, response):
        # follow links to event pages
        for href in response.css('div.latestPost-layout a::attr(href) '):
            yield response.follow(href, self.parse_link)
        # follow pagination links
        for href in response.css('div.nav-links a::attr(href)'):
            yield response.follow(href, self.parse)

    def parse_link(self, response):
        def extract_with_css(querry):
            return response.css(querry).extract_first().encode('utf-8').strip()

        def extract_with_xpath(querry):
            return response.xpath(querry).extract_first().encode('utf-8').strip()

        yield {
                'event_name': extract_with_css('div.junkie-alert.yellow h2::text'),
                'event_time': extract_with_css('div.junkie-alert.yellow p::text')
            }
