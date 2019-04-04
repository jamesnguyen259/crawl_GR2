# -*- coding: utf-8 -*-
import scrapy


class AlleventSpider(scrapy.Spider):
    name = 'allevent'
    allowed_domains = ['allevents.in']
    start_urls = ['https://allevents.in/hanoi/all?page=1']

    def parse(self, response):
        selectors = response.css("div.event-body.clearfix div.left h3 a")
        for selector in selectors:
            # item = BookingHotelItem()
            link =  selector.css("::attr(href)").extract_first().encode("utf-8")
            #get image_url
            # image = selector.css("img.hotel_image::attr(src)").extract_first().encode("utf-8").replace("\n","")
            # item['image'] = image
            yield response.follow(link, callback=self.parse_item)

        next_pages = response.css("a.skyload")
        for next_page in next_pages:
            next_link = next_page.css("::attr(href)").extract_first().encode("utf-8")
            yield response.follow(next_link, self.parse)
        # pass
