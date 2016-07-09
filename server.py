#!/usr/bin/python
import MySQLdb
from flask import Flask
app = Flask(__name__)

db = MySQLdb.connect(host="localhost",   
                     user="root",        
                     passwd="greylock",  
                     db="greylock")   
# create a cursor object for queries
ur = db.cursor()

@app.route('/login', methods=['POST'])
def login():
	email=request.form['email']
	name=request.form['name']
	query_cmd = ''
	cur.execute(query_cmd)



if __name__ == "__main__":
    app.run()
