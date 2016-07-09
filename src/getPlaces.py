import sys

if len(sys.argv)>1:
  local=True
else:
  local=False

import io
from yelpapi import YelpAPI
from geopy.geocoders import Nominatim
import json
from mymodels import *
if not local:
  import MySQLdb

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

#print json.dumps(search_results, sort_keys=True, indent=4)

#connect to db
if not local:
  db = MySQLdb.connect("localhost","root","greylock","greylock" )
  cursor = db.cursor()
  cursor.execute("SELECT VERSION()")
  data = cursor.fetchone()
  print "Database version : %s " % data

for biz in search_results['businesses']:
  if biz['rating'] >= 3.5:
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
    sql = "INSERT INTO Flags (location_lat, location_log, rating, photo_url, name) VALUES ("+str(lat)+", "+str(lng)+", "+str(rating)+", \""+str(image)+"\", \""+name+"\")"
    print sql
    if not local:
      print "Executing"
      cursor.execute(sql)

if not local:
  db.commit()
