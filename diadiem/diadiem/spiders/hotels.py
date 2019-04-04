# -*- coding: utf-8 -*-
import scrapy
from diadiem.items import HotelItem

class HotelsSpider(scrapy.Spider):
    name = 'hotels'
    allowed_domains = ['diadiem.co']
    start_urls = []
    max_page = 2
    for page in range(1,max_page+1):
        start_urls.append('https://diadiem.co/ha-noi/khach-san-c46-%s.html'% str(page))

    def parse(self, response):
        selectors = response.css("div.col-md-10.col-xs-9")
        for selector in selectors:
            link = "https://diadiem.co" + selector.css("a::attr(href)").extract_first().encode("utf-8")
            yield response.follow(link, callback=self.parse_item)

    def parse_item(self, response):
        item = HotelItem()
        #get name:
        try:
            name = response.css("div.col-md-7 h1::text").extract_first().encode("utf-8")
            item['name'] = name
        except:
            pass
        #get location:
        try:
            location = ''.join(response.xpath('//*[@id="content-wrapper"]/div[2]/div[1]/div[1]/div[2]/div[4]//text()').extract()).strip().encode("utf-8")
            item['location'] = location
        except:
            pass
        #get url
        try:
            source_url = response.url
            item['source_url'] = source_url
        except:
            pass
        #get image:
        try:
            image_url = "https://diadiem.co" + response.css('div.col-md-5 img::attr(src)').extract_first().encode("utf-8")
            item['image_url'] = image_url
        except:
            pass
        #rating:
        item['rating'] = "Not rated"
        #get description:
        try:
            description = ''.join(response.xpath('//div[contains(concat(" ",normalize-space(@class)," ")," location-content ")]//text()').extract()).strip().encode("utf-8") + \
            "\nTiện ích: \n" + ''.join(response.xpath('//div[@class="tab-content"]//text()').extract()).strip().encode("utf-8").replace("\t", "")
            item['description'] = description
        except:
            pass

        yield item
