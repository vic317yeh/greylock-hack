#!/usr/bin/python
import peewee
from peewee import *
from flask import *
import MySQLdb
app = Flask(__name__)

#may fuck shit up
import sys
sys.path.insert(0, '/home/ubuntu/greylock-hack/src')
from mymodels import *
from geopy.distance import vincenty

#login
@app.route('/login', methods=['POST'])
def login():
  data=request.json
  email=data['email']
  name=data['name']
  database.connect()
  result = {"loggin": False}
  not_exists = Users.select().where(Users.email == email)
  print not_exists
  if not_exists == 0:
    newUser = Users(name=name, email=email)
    newUser.save()
    result['loggin'] = True
  return str(result)

#get flags near a user
@app.route('/getFlags', methods=['POST'])
def getFlags():
  data=request.json
  email=data['email']
  lat=data['lat']
  lng=data['long']
  curr_pos=(lat,lng)
  database.connect()
  results = Flags.select().where(Flags.fid>=0)
  ret={"res": []}
  for res in results:
    res_pos=(res.location_lat, res.location_long)
    if vincenty(curr_pos, res_pos).miles < 5:
      entry = {"name": res.name, "url": res.photo_url, "snippet": res.snippet, "rating": res.rating, "lat": res.location_lat, "long": res.location_long}
      ret["res"].append(entry)
  return str(ret)

#create user timelie
@app.route('/timeline', methods=['POST'])
def timeline():
  data=request.json
  email=data['email']
  lat=data['lat']
  lng=data['long']
  currpos=(lat,lng)
  database.connect()
  results = Userflags.select().where(Userflags.fid>=0)
  ret={"res": []}
  for res in results:
    flag = Flags.select().where(Flags.fid==res.fid)
    flag_lat = flag.location_lat
    flag_long = flag.location_log
    flag_pos = (flag_lat, flag_long)
    if vincenty(curr_pos, flag_pos).miles < 5:
      entry = {"name": res.name, "path": res.photo_path, "snippet": res.review, "rating": res.rating, "lat": flag_lat, "long": flag_long}
      ret["res"].append(entry)
  return str(ret)


@app.route('/verify', methods=['POST'])
def verify():


@app.route('/')
def hello():
  return 'hello world'

@app.route('/test_get')
def test_get():
	result = {'name': request.args['name']}
	return str(result)

@app.route('/test_post', methods=['POST'])
def test_post():
	data = json.dumps(request.json)
	result = {'login': True}
	return str(result)

#get friends emails only (will add all data later)
@app.route('/get_friends', methods=['POST'])
def getFriends():
  email=request.form['email']
  return str(User.select().where(Friends.email == email))

#route to get photos ONLY
@app.route('/get_user_photos', methods=['POST'])
def getPhotos():
  email=request.form['email']
  return str(UserFlags.select(Userflags.photo_path).where(Userflags.email == email))

if __name__ == "__main__":
    app.run()
