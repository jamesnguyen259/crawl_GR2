# -*- coding: utf-8 -*-
import googlemaps

gmaps = googlemaps.Client(key='AIzaSyCRMnAVHulNvTFJfk88m9wnotSUTxQCixY')

# Geocoding an address
geocode_result = gmaps.geocode('Khu vực Vườn hoa Tượng đài Lý Thái Tổ, quận Hoàn Kiếm, Hà Nội')
print(geocode_result)
