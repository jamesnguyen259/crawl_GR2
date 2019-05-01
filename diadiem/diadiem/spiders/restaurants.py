# -*- coding: utf-8 -*-
import scrapy
from geopy.geocoders import ArcGIS
from diadiem.items import RestaurantItem

class RestaurantsSpider(scrapy.Spider):
    name = 'restaurants'
    allowed_domains = ['diadiem.co']
    start_urls = []
    max_page = 278
    for page in range(1,max_page+1):
        start_urls.append('https://diadiem.co/ha-noi/nha-hang-c292-%s.html'% str(page))

    def parse(self, response):
        selectors = response.css("div.col-md-10.col-xs-9")
        for selector in selectors:
            link = "https://diadiem.co" + selector.css("a::attr(href)").extract_first().encode("utf-8")
            yield response.follow(link, callback=self.parse_item)

    def parse_item(self, response):
        item = RestaurantItem()
        geolocator = ArcGIS()
        #get name:
        try:
            name = response.css("div.col-md-7 h1::text").extract_first().encode("utf-8").strip()
            item['name'] = name
        except:
            pass
        #get location:
        try:
            location = ''.join(response.xpath('//*[@id="content-wrapper"]/div[2]/div[1]/div[1]/div[2]/div[4]//text()').extract()).strip().encode("utf-8").replace(" Thành phố","").replace("  ","")
            item['location'] = location
            address = geolocator.geocode(location)
            item['lat'] = address.latitude
            item['lng'] = address.longitude
        except:
            pass
        #get url
        try:
            source_url = response.url
            item['source_url'] = source_url
        except:
            pass
        #get time
        try:
            time = response.css("table.table.table-bordered tr td:nth-child(2)::text").extract_first().encode("utf-8").strip()
            item['time'] = time
        except:
            item['time'] = "N/A - N/A"
        #get price:
        item['price'] = "N/A"
        #get phone:
        try:
            phone = ''.join(response.xpath('//*[@id="content-wrapper"]/div[2]/div[1]/div[1]/div[2]/div[3]//text()').extract()).strip().encode("utf-8").replace("Liên hệ : ", "").replace("Đang cập nhật", "N/A")
            item['phone'] = phone
        except:
            item['phone'] = "N/A"
        #get image:
        try:
            image_url = response.css('div.col-md-5 img::attr(src)').extract_first().encode("utf-8")
            item['image_url'] = image_url
        except:
            pass
        #get description:
        try:
            description = ''.join(response.xpath('//div[contains(concat(" ",normalize-space(@class)," ")," location-content ")]//text()').extract()).strip().encode("utf-8") + \
            "\nTiện ích: \n" + ''.join(response.xpath('//div[@class="tab-content"]//text()').extract()).strip().encode("utf-8").replace("\t", "")
            item['description'] = description
        except:
            pass
        yield item
