# -*- coding: utf-8 -*-
from geopy.geocoders import ArcGIS
geolocator = ArcGIS()
location1 = geolocator.geocode("Nha Khoa Quốc Tế 108, Số 8 Bala - Hà Đông, Hanoi, Vietnam, Hanoi, Vietnam")
# location2 = geolocator.geocode("46 Lương Ngọc Quyến , Phường Lý Thái Tổ, Quận Hoàn Kiếm, Hà Nội")
print((location1.latitude, location1.longitude))
# print location1.latitude
# print((location2.latitude, location2.longitude))
