#Getting Flflask, render_template and request from flask
from flask import Flask, render_template, request

#Declaring the App
app = Flask(__name__)

#Starting the app route 
@app.route('/')
def main():
	return render_template('template/index.html')