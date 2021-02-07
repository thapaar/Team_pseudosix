from flask import Flask, render_template, request

#Declaring the App
app = Flask(__name__)

#Starting the app route 
@app.route('/')
def home():
	return render_template('index.html')

# Retrieves the login & register view
@app.route('/templates')
def register():
	return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)