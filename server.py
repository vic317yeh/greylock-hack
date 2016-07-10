#!/usr/bin/python
import peewee
from peewee import *
from flask import *
app = Flask(__name__)

#may fuck shit up
import sys
sys.path.insert(0, '/home/ubuntu/greylock-hack/src')
from mymodels import *

@app.route('/login', methods=['POST'])
def login():
	email=request.form['email']
	name=request.form['name']

  database.connect()
  result = {"loggin": False}
	if not_exits:
		newUser = User(name=name, email=email)
    newUser.save()
    result['loggin'] = True
  return str(result)

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
