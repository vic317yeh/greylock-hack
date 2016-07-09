import io
from yelpapi import YelpAPI
from geopy.geocoders import Nominatim
import json

yelp_api = YelpAPI('rRkbtARpvQcSL3l-ZRIN0w',
    'G3KrPharmO7HX1FiZ0ApyrZll2Q',
    '2NNgzN1Z7k3_Ssq8BJnDM0n05Rs0IxV_',
    'd5ddPgXCn21G9Z3VIYkiQ51Wzvc')

geolocator = Nominatim()
loc = geolocator.reverse("37.777111, -122.415153")
addr = loc.raw['address']

if 'city' in addr:
  city=addr['city']
else:
  city=addr['town']

address = addr['house_number'] + " " +addr['road'] + ", " + city +", " + addr['state']
print address

search_results = yelp_api.search_query(term="tourist attractions",
    location=address, limit=20, sort=2, radius_filter=8000)

print json.dumps(search_results, sort_keys=True, indent=4)

for biz in search_results['businesses']:
  print biz['name']
  print biz['image_url']
  print biz['rating']
  print biz['location']['coordinate']['latitude']
  print biz['location']['coordinate']['longitude']
