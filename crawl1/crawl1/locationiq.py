# -*- coding: utf-8 -*-
import requests
import json
import sys
import codecs

url = "https://us1.locationiq.com/v1/search.php"
file =  'test.json'
fileout = 'out3.json'

try:
    with open(file,'r') as f:
        contents = json.load(f)
        f.close()
    for index,content in enumerate(contents):
        address = contents[index]['event_place']
        data = {
            'key': '836f98e04aadb6',
            'q': address,
            'format': 'json'
        }
        response = requests.get(url, params=data)
        result = response.json()
        if result and len(result):
            sys.stderr.write("Found: %s\n" % address)
            contents[index]["lat"] = result[0]['lat']
            contents[index]["lng"] = result[0]['lon']
        else:
            sys.stderr.write("Not found: %s\n" % address)
    with codecs.open(fileout,'w',encoding='utf8') as out:
        json.dump(contents,out,ensure_ascii=False)
        out.close()
except IOError:
    print('Error: File %s does not appear to exist.' % file)
