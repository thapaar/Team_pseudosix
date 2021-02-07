from flask import Flask
from book_parser import newStyle

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
    pageCount,title = newStyle(url)
    msg = title + " has " + pageCount + " pages"
    return msg

if __name__ == "__main__":
    app.run()