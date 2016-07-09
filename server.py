from flask import Flask
import sys
app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
	email=request.form['email']


if __name__ == "__main__":
    app.run()
