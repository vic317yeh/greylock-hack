#!/usr/bin/python
# import peewee
# from peewee import *
from flask import Flask
from flask import request
import sys
app = Flask(__name__)

# db = MySQLDatabase("greylock",  
#                      user="root",        
#                      passwd="greylock")
# # DB models
# class User(Model):
# 	uid = IntegerField()
# 	email = CharField()
# 	name = TextField()
# 	location_lat = DecimalField()
# 	location_log = DecimalField()
# 	class Meta:
#         database = db

# class Friends(Model):
# 	email = CharField()
# 	friend_email = CharField()
# 	class Meta:
#         database = db

# class Flags(Model):
# 	fid = IntegerField()
# 	name = TextField()
# 	lat = DecimalField()
# 	log = DecimalField()
# 	rating = IntegerField()
# 	url = TextField()
# 	class Meta:
#         database = db

# class UserFlags(Model):
# 	email = CharField()
# 	fid = IntegerField()
# 	ts = BigIntegerField()
# 	rating = IntegerField()
# 	review = TextField()
# 	class Meta:
#         database = db



# @app.route('/login', methods=['POST'])
# def login():
# 	email=request.form['email']
# 	name=request.form['name']
	
# 	if not_exits:
# 		newUser = User(name=name,
# 					   email=email
# 			)
# 	else: 
# 		return

@app.route('/')
def hello():
	return 'hello world'

@app.route('/test_get')
def test_get():
	result = {
		"name": request.args['name']	
	}
	return str(result)


@app.route('/test_post', methods=['POST'])
def test_post():
	result = {
		"name": request.form['name']	
	}
	return str(result)



if __name__ == "__main__":
    app.run()
