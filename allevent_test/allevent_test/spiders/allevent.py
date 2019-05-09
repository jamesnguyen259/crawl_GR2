# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
from allevent_test.items import AlleventTestItem
# from geopy.geocoders import ArcGIS
import sys
from dateutil import parser
from datetime import datetime

reload(sys)
sys.setdefaultencoding('utf-8')

script = """
function main(splash)
    splash.resource_timeout = 3
    splash:init_cookies(splash.args.cookies)
    local url = splash.args.url
    assert(splash:go(url))
    assert(splash:wait(5))
    return {
        cookies = splash:get_cookies(),
        html = splash:html()
    }
end
"""

script2 = """
function main(splash)
    splash.resource_timeout = 3
    splash:init_cookies(splash.args.cookies)
    local url = splash.args.url
    assert(splash:go(url))
    assert(splash:wait(0.5))
    return {
        cookies = splash:get_cookies(),
        html = splash:html()
    }
end
"""

class AlleventSpider(scrapy.Spider):
    name = 'allevent'
    allowed_domains = ['allevents.in']
    start_urls = ['https://allevents.in/hanoi/all']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, endpoint='execute', args={'lua_source': script})

    def parse(self, response):
        url_selectors = response.css("div.event-body.clearfix div.left h3 a::attr(href)")
        for url in url_selectors.extract()[:10]:
            yield SplashRequest(url.encode('utf-8'), callback=self.parse_item, endpoint='execute', args={'lua_source': script2})

    def parse_item(self, response):
        item = AlleventTestItem()
        # geolocator = ArcGIS()
        #get_name
        try:
            name = response.css('h1.overlay-h1::text').extract_first().encode("utf-8")
            item['name'] = name
        except:
            pass

        try:
            location = response.css('span.venue-popover.ml5::attr(data-content)').extract_first().encode("utf-8")
            # address = geolocator.geocode(location)
            # item['lat'] = address.latitude
            # item['lng'] = address.longitude
            item['location'] = location
        except:
            pass

        try:
            event_time = response.css('#event-detail-fade > div.event-head.wdiv > div.pd-lr-10.span9 > ul > li:nth-child(1)::text').extract_first().encode("utf-8").replace('\n\t\t\t\t\t\t\n\t\t\t\t\t\t','').replace('\t\t\t\t\t\t\t\t\t\t\t\t','')
            # item['time'] = event_time
            if event_time.count(" at ") == 2 and event_time.count(" to ") == 1:
                temp = event_time.replace(" at "," ")
                start = temp.split(" to ")[0]
                end = temp.split(" to ",1)[1]
                event_end_time = parser.parse(end).strftime('%Y-%m-%d %H:%M:%S')
            elif " to " in event_time:
                start = event_time.split(" to ")[0].replace(" at ", " ")
                end = event_time.split(" at ")[0] + " " + event_time.split(" to ",1)[1]
                event_end_time = parser.parse(end).strftime('%Y-%m-%d %H:%M:%S')
            else:
                start = event_time.replace(" at ", " ")
                event_end_time = None
            event_start_time = parser.parse(start).strftime('%Y-%m-%d %H:%M:%S')
            item['start_time'] = event_start_time
            item['end_time'] = event_end_time

        except:
            pass

        return item
