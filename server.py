#!/usr/bin/python
import peewee
from peewee import *
from flask import *
import os
import time

from werkzeug.utils import secure_filename
import urllib, cStringIO

UPLOAD_FOLDER = os.path.dirname(os.path.realpath(__file__)) + '/static/img/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

import MySQLdb
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from PIL import Image
import imagehash

DIFFERENCE_BAR = 10

def match(userImgSrc, targetImgSrc):
    userImgSrc =cStringIO.StringIO(urllib.urlopen(userImgSrc).read())
    targetImgSrc = cStringIO.StringIO(urllib.urlopen(targetImgSrc).read())
    user_img = Image.open(userImgSrc)
    target_img = Image.open(targetImgSrc)
    user_hash = imagehash.average_hash(user_img)
    target_hash = imagehash.average_hash(target_img)
    result = True if user_hash-target_hash <= DIFFERENCE_BAR else False
    return result


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
    res_pos=(res.location_lat, res.location_log)
    if vincenty(curr_pos, res_pos).miles < 20:
      entry = {"name": res.name, "url": res.photo_url, "snippet": res.snippet, "rating": res.rating, "lat": str(res.location_lat), "long": str(res.location_log)}
      ret["res"].append(entry)
  return str(ret)

#create user timelie
@app.route('/timeline', methods=['POST'])
def timeline():
  data=request.json
  email=data['email']
  lat=data['lat']
  lng=data['long']
  curr_pos=(lat,lng)
  database.connect()
  results = Userflags.select().where(Userflags.fid>=0)
  ret={"res": []}
  for res in results:
    flag = Flags.get(Flags.fid == res.fid)
    flag_lat = flag.location_lat
    flag_long = flag.location_log
    flag_pos = (flag_lat, flag_long)
    if vincenty(curr_pos, flag_pos).miles < 20:
      entry = {"email": res.email, "path": res.photo_path, "snippet": res.review, "rating": res.rating, "lat": str(flag_lat), "long": str(flag_long)}
      ret["res"].append(entry)
  return str(ret)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

import base64

@app.route('/verify', methods=['POST'])
def verify():
  email = request.json['email']
  lat = request.json['lat']
  lng = request.json['long']
  f = request.json['image']
  targetUrl = request.json['targetUrl']
  filename = str(hash(f))+'.jpg'
  name = UPLOAD_FOLDER + filename
  print name
  g = open(name, 'w')
  g.write(base64.decodestring(f))
  g.close()
  result = match(UPLOAD_FOLDER + filename, targetUrl)
  if result:
    newUserFlag = Usersflags(email=email, timestamp=int(time.time()), photo_path="https://52.40.56.30/"+name)
    newUserFlag.save()

  return str({'result':result})

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
