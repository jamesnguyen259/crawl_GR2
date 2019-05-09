# -*- coding: utf-8 -*-
import scrapy
from urbanisthanoi.items import UrbanisthanoiItem
from geopy.geocoders import ArcGIS
from dateutil import parser
import datetime

class UrbanisthanoiParseSpider(scrapy.Spider):
    name = 'urbanisthanoi_parse'
    allowed_domains = ['urbanisthanoi.com']
    start_urls = ['https://urbanisthanoi.com/hanoi-events']
    start_urls.append('https://urbanisthanoi.com/hanoi-events?start=11')

    def parse(self, response):
        selectors = response.css("div.contentpaneopen")
        for selector in selectors:
            item = UrbanisthanoiItem()
            link = "https://urbanisthanoi.com" + selector.css("h2 a::attr(href)").extract_first().encode('utf-8')
            #get_image_url
            image_url = selector.css("p:nth-child(3) a img::attr(src)").extract_first().encode("utf-8")
            item['image_url'] = "https:" + image_url
            yield response.follow(link, callback=self.parse_item, meta={'item' : item})

    def parse_item(self, response):
        item = response.meta['item']
        geolocator = ArcGIS()
        #get_name:
        try:
            name = response.css("div.item-page > h1.contentheading a::text").extract_first().encode("utf-8").replace("\n\n\t\t","")
            item['name'] = name
        except:
            pass
        #get_location:
        try:
            location = response.css('div.event-detail > p:nth-child(3)::text').extract_first().encode('utf-8')
            item['location'] = location
            address = geolocator.geocode(location, timeout=None)
            lat = address.latitude
            item['lat'] = lat
            lng = address.longitude
            item['lng'] = lng
        except:
            pass
        #get_start_and_end_time:
        try:
            day = response.css('div.event-detail > p:nth-child(1)::text').extract_first().encode('utf-8')
            time = response.css('div.event-detail > p:nth-child(2)::text').extract_first().encode('utf-8')
            #may be has both start and end_time
            if " - " in time:
                start_time_str = day + " " + time.split(" - ")[0]
                start_time = parser.parse(start_time_str)
                item['start_time'] = start_time.strftime('%Y-%m-%d %H:%M:%S')

                end_str =  time.split(" - ",1)[1]
                #sometime end_str == late
                if end_str != "late":
                    temp = day + " " + end_str
                    #tommorow
                    if parser.parse(temp) < start_time:
                        end_day = parser.parse(day) + datetime.timedelta(days=1)
                        end_day_str = end_day.strftime('%A, %d %b')  + " " + end_str
                    else:
                        end_day_str = day + " " + end_str
                    item['end_time'] = parser.parse(end_day_str).strftime('%Y-%m-%d %H:%M:%S')
                else:
                    item['end_time'] = None
            #Just start_time:
            else:
                start_time_str = day + " " + time
                start_time = parser.parse(start_time_str)
                item['start_time'] = start_time.strftime('%Y-%m-%d %H:%M:%S')
                item['end_time'] = None
        except:
            pass
        #get_source_url:
        try:
            source_url = response.url
            item['source_url'] = source_url
        except:
            pass
        #get_description:
        try:
            description = ''.join(response.xpath('//*[@id="ja-content-main"]/div[2]/p[2]//text()').extract()).encode("utf-8").strip() \
                + ''.join(response.xpath('//*[@id="ja-content-main"]/div[2]/p[3]//text()').extract()).encode("utf-8").strip()
            item['description'] = description
        except:
            pass
        #get_organizer_name
        item['organizer_name'] = None
        return item



