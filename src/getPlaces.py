import sys
import peewee

if len(sys.argv)>1:
    local=True
else:
    local=False

import io
from yelpapi import YelpAPI
from geopy.geocoders import Nominatim
import json
from mymodels import *

yelp_api = YelpAPI('rRkbtARpvQcSL3l-ZRIN0w',
        'G3KrPharmO7HX1FiZ0ApyrZll2Q',
        '2NNgzN1Z7k3_Ssq8BJnDM0n05Rs0IxV_',
        'd5ddPgXCn21G9Z3VIYkiQ51Wzvc')

geolocator = Nominatim()

#logic to convert lat-long to yelpable address
#currently not needed, maybe add later
'''
loc = geolocator.reverse("37.777111, -122.415153")
addr = loc.raw['address']

if 'city' in addr:
    city=addr['city']
else:
    city=addr['town']

address = addr['house_number'] + " " +addr['road'] + ", " + city +", " + addr['state']
print address'''

address="san jose"

search_results = yelp_api.search_query(term="tourist attractions",
    location=address, sort=2, radius_filter=32000)

#print json.dumps(search_results, sort_keys=True, indent=4)

#connect to db
if not local:
    database.connect()

for biz in search_results['businesses']:
    if biz['rating'] >= 3:
        name = biz['name']
        image =  biz['image_url']
        rating = biz['rating']
        lat = biz['location']['coordinate']['latitude']
        lng = biz['location']['coordinate']['longitude']
        print name
        print image
        print rating
        print lat
        print lng
        do = raw_input("ADD: ")
        if do=="y":
            currFlag = Flags(name=name, photo_url = image, rating = rating,
                location_lat = lat, location_log = lng)
            currFlag.save()
