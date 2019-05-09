# -*- coding: utf-8 -*-
from geopy.geocoders import GoogleV3
geolocator = GoogleV3(api_key = "AIzaSyBz1zNoF9K68XtaJ_rhFNKLNQXKZcUc_Uo")
location1 = geolocator.geocode("Cung Xuân, 1 Võ Thị Sáu, Hanoi, Vietnam", timeout=None)
print((location1.latitude, location1.longitude))
