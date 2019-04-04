# -*- coding: utf-8 -*-
import scrapy
from booking_hotel.items import BookingHotelItem


class TwoStarSpider(scrapy.Spider):
    name = '2star'
    allowed_domains = ['booking.com']
    start_urls = ['https://www.booking.com/searchresults.vi.html?dest_id=6228;dest_type=region;nflt=class%3D2%3B;ss=H%C3%A0%2BN%E1%BB%99i%2C%2BVi%E1%BB%87t%2BNam;tmpl=searchresults']

    def parse(self, response):
        selectors = response.css("div.sr_item.sr_item_new.sr_item_default.sr_property_block.sr_flex_layout.sr_item_no_dates")
        for selector in selectors:
            item = BookingHotelItem()
            link =  "https://www.booking.com" + selector.css("a.hotel_name_link.url::attr(href)").extract_first().encode("utf-8").replace("\n","")
            #get image_url
            image = selector.css("img.hotel_image::attr(src)").extract_first().encode("utf-8").replace("\n","")
            item['image'] = image
            yield response.follow(link, callback=self.parse_item, meta={'item' : item})

        next_pages = response.css("a.bui-pagination__link.paging-next")
        for next_page in next_pages:
            next_link = "https://www.booking.com" + next_page.css("::attr(href)").extract_first().encode("utf-8").replace("\n","")
            yield response.follow(next_link, self.parse)
            # print link
    def parse_item(self, response):
        item = response.meta['item']
        #get name
        try:
            name = response.css("h2.hp__hotel-name::text").extract()[1].encode("utf-8").replace("\n","")
            item['name'] = name
        except:
            pass
        #get rating
        item['rating'] = "2"
        #get url
        try:
            url =response.url
            item['url'] = url
        except:
            pass
        #get location
        try:
            location = response.css("span.hp_address_subtitle.js-hp_address_subtitle.jq_tooltip::text").extract_first().encode("utf-8").replace("\n","")
            item['location'] = location
        except:
            pass
        #get description
        try:
            description = ''.join(response.xpath('//div[contains(concat(" ",normalize-space(@class)," ")," hp_desc_main_content ")]//text()').extract()).strip().encode("utf-8") + \
            ''.join(response.xpath('//div[contains(concat(" ",normalize-space(@class)," ")," hp_desc_important_facilities ")][contains(concat(" ",normalize-space(@class)," ")," clearfix ")]//text()').extract()).strip().encode("utf-8") + \
            ''.join(response.xpath('//div[contains(concat(" ",normalize-space(@class)," ")," descriptionsContainer ")][contains(concat(" ",normalize-space(@class)," ")," clearfix ")][contains(concat(" ",normalize-space(@class)," ")," hp-section ")][contains(concat(" ",normalize-space(@class)," ")," hp-policies-block ")]//text()').extract()).strip().encode("utf-8")
            item['description'] = description
        except:
            pass
        yield item

