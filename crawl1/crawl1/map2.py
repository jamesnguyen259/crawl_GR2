import sys
import codecs
from opencage.geocoder import OpenCageGeocode
from pprint import pprint
import json

key = 'b7085ed06f1e472591b5f9f6c02f089f'
geocoder = OpenCageGeocode(key)
file = 'test.json'
fileout = 'out2.json'

try:
  with open(file,'r') as f:
    contents = json.load(f)
    f.close()
  for index, content in enumerate(contents):
    address = contents[index]['event_place']
    # print(address)
    result = geocoder.geocode(address)
    if result and len(result):
      contents[index]["lat"] = result[0]['geometry']['lat']
      contents[index]["lng"] = result[0]['geometry']['lng']
      print(contents[index])
    else:
      sys.stderr.write("Not found: %s\n" % address)
  # out = open(fileout,"w+")
  # json.dump(contents,out)
  with codecs.open(fileout,'w',encoding='utf8') as out:
    json.dump(contents,out,ensure_ascii=False)
  out.close()
except IOError:
  print('Error: File %s does not appear to exist.' % file)
# except RateLimitExceededError as ex:
#   print(ex)

# pprint(str(results[0]['components']['city']))
# pprint(json.dumps(results))
