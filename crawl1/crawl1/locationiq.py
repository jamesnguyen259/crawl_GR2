# -*- coding: utf-8 -*-
import requests
import json
import sys
import codecs

url = "https://us1.locationiq.com/v1/search.php"
file =  'test.json'
fileout = 'out3.json'

# with open(file,'r') as f:
#     contents = json.load(f)
#     f.close()
# for index,content in enumerate(contents):
#     address = contents[index]['event_place']
#     # print(address)
#     data = {
#         'key': '836f98e04aadb6',
#         'q': address,
#         'format': 'json'
#     }
#     response = requests.get(url, params=data)
#     print(response.text)

data = {
    'key': '836f98e04aadb6',
    'q': 'Khu vực Vườn hoa Tượng đài Lý Thái Tổ, quận Hoàn Kiếm, Hà Nội',
    'format': 'json'
}
response = requests.get(url, params=data)
print(response.text)
#compare output
