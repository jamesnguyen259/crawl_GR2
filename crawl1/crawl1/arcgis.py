# -*- coding: utf-8 -*-
from geopy.geocoders import ArcGIS
geolocator = ArcGIS()
location1 = geolocator.geocode("Số 1 Đường Thanh Niên - Quận Tây Hồ - Hà Nội", timeout=None)

print((location1.latitude, location1.longitude))
# from dateutil import parser
# import datetime

# end = parser.parse("Saturday, 4 May 11:59pm").strftime('%Y-%m-%d %H:%M:%S')
# print end


# link: "https://urbanisthanoi.com" + div.contentpaneopen h2 a::attr(href)
# next: li.pagination-next a::attr(href)    get first 2 => top2 = next[:2]
#image_url: div.contentpaneopen p:nth-child(3) a img::attr(src) replace("//","")

#location: response.css('div.event-detail > p:nth-child(3)::text').extract_first().encode('utf-8')
#lat, lng

#day: response.css('div.event-detail > p:nth-child(1)::text').extract_first().encode('utf-8')
#time: response.css('div.event-detail > p:nth-child(2)::text').extract_first().encode('utf-8')
# day = "Friday, 3 May"
# time = "11:00pm - 5:00am"
# start_time_str = day + " " + time.split(" - ")[0]
# start_time = parser.parse(start_time_str)
# event_start_time = start_time.strftime('%Y-%m-%d %H:%M:%S')

# end_str =  time.split(" - ",1)[1]
# if end_str != "late":
#     temp = day + " " + end_str
#     if parser.parse(temp) < start_time:
#         end_day = parser.parse(day) + datetime.timedelta(days=1)
#         end_day_str = end_day.strftime('%A, %d %b')  + " " + end_str
#     else:
#         end_day_str = day + " " + end_str
#     event_end_time = parser.parse(end_day_str).strftime('%Y-%m-%d %H:%M:%S')
# else:
#     event_end_time = None

# print event_start_time
# print event_end_time

#source_url
#description: div.item-page > p:nth-child(7)::text + div.item-page > p:nth-child(8)::text
#organizer_name : "N/A"
# time = "12:00pm - 13:00pm"
# day = "Sunday, 12 May"

# if " - " in time:
#     start_time_str = day + " " + time.split(" - ")[0]
#     start_time = parser.parse(start_time_str)
#     start = start_time.strftime('%Y-%m-%d %H:%M:%S')

#     end_str =  time.split(" - ",1)[1]
#     #sometime end_str == late
#     if end_str != "late":
#         temp = day + " " + end_str
#         #tommorow
#         if parser.parse(temp) < start_time:
#             end_day = parser.parse(day) + datetime.timedelta(days=1)
#             end_day_str = end_day.strftime('%A, %d %b')  + " " + end_str
#         else:
#             end_day_str = day + " " + end_str
#         end = parser.parse(end_day_str).strftime('%Y-%m-%d %H:%M:%S')
#     else:
#         end = None
# #Just start_time:
# else:
#     start_time_str = day + " " + time
#     start_time = parser.parse(start_time_str)
#     start = start_time.strftime('%Y-%m-%d %H:%M:%S')
#     end = None
# print start
# print end
