from flask import Flask, request , render_template
from book_parser import getInfo

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"

@app.route("/<name>")
def printName(name):
    return "Hi, {}".format(name)

@app.route("/book")
def printBook():
    url = "https://www.google.co.uk/books/edition/Harry_Potter_and_the_Sorcerer_s_Stone/wrOQLV6xB-wC?hl=en"
    pageCount,title = getInfo(url)
    msg = title + " has " + pageCount + " pages"
    return msg

@app.route("/form")
def myForm():
    return render_template("form.html")

@app.route('/form', methods=['POST', "GET"])
def handleForm():
    url = request.form["text"]
    pages, title = getInfo(url)
    msg = title + " has " + pages + " pages"
    return msg

if __name__ == "__main__":
    app.run()