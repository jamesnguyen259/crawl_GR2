# -*- coding: utf-8 -*-
import scrapy
from geopy.geocoders import ArcGIS
from amthuc365.items import Amthuc365Item

class Amthuc365parseSpider(scrapy.Spider):
    name = 'amthuc365parse'
    allowed_domains = ['amthuc365.vn']
    start_urls = ['http://www.amthuc365.vn/ha-noi/trang-1/']

    def parse(self, response):
        # print(response.url)
        a_selectors = response.css("div.it-rest_thumb > a:nth-child(1)")
        for selector in a_selectors:
            link = "http://www.amthuc365.vn" + selector.css("::attr(href)").extract_first()
            request = response.follow(link, callback=self.parse_item)
            yield request
        # for href in "http://www.amthuc365.vn" + response.css("div.it-rest_thumb > a:nth-child(1)::attr(href)"):
        #     yield response.follow(href, self.parse_item)
        for href in response.css("a.next::attr(href)"):
            yield response.follow(href, self.parse)

    def parse_item(self, response):
        item = Amthuc365Item()
        geolocator = ArcGIS()
        #get name
        try:
            item['name'] = response.css("div.h-info h1::text").extract_first().encode("utf-8")
        except:
            pass
        #get location
        try:
            location = ''.join(response.xpath('//div[contains(concat(" ",normalize-space(@class)," ")," h-info ")]/p[contains(concat(" ",normalize-space(@class)," ")," address ")]//text()').extract()).strip().encode("utf-8")
            item['location'] = location
            address = geolocator.geocode(location)
            item['lat'] = address.latitude
            item['lng'] = address.longitude
        except:
            pass
        #get url
        try:
            source_url = response.css("p.rest-web a::attr(href)").extract_first().encode("utf-8")
            if source_url.count("/") == 1:
                source_url = "http://www.amthuc365.vn" +  source_url
            item['source_url'] = source_url
        except:
            pass
        #get time
        try:
            time = response.css("#container > div.page-container > div.page-content > div > div.box-info__rest.clearfix > div.rest-info > div:nth-child(3) > p.mb0.closeTime::text").extract_first()
            item['time'] = time.encode("utf-8").replace(" Giờ đóng cửa:","")
        except:
            pass
        #get price
        try:
            price = response.css("#container > div.page-container > div.page-content > div > div.box-info__rest.clearfix > div.rest-info > div.row-span.mt10.timeRest.no-border > p.mb0.closeTime::text").extract_first()
            item['price'] = price.encode("utf-8").replace("Từ ", "").replace("Dưới ", "")
        except:
            pass
        #get phone number
        try:
            item['phone'] = response.css("p.rest-phone.mb5 a::attr(title)").extract_first().encode("utf-8")
        except:
            pass
        #get image:
        try:
            item['image_url'] = response.css("div.img-info img::attr(src)").extract_first().encode("utf-8")
        except:
            pass
        #get description
        try:
            item['description'] = ''.join(response.xpath('//div[contains(concat(" ",normalize-space(@class)," ")," tinimce__content ")]//text()').extract()).strip().encode("utf-8")
        except:
            pass
        yield item
