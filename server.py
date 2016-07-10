#!/usr/bin/python
import peewee
from peewee import *
from flask import *
app = Flask(__name__)



# db = MySQLDatabase("greylock",  
#                      user="root",        
#                      passwd="greylock")

@app.route('/login', methods=['POST'])
def login():
	email=request.form['email']
	name=request.form['name']
	
	if not_exits:
		newUser = User(name=name,
					   email=email
			)
	else: 
		return

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

if __name__ == "__main__":
    app.run()
