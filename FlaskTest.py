from flask import Flask, request , render_template
from book_parser import getInfo
import time

app = Flask(__name__)

@app.route("/")
@app.route("/index.html")
def index():
    # return "Hello World"
    return render_template("index.html")

@app.route("/<name>")
def printName(name):
    return "Hi, {}".format(name)

@app.route("/book")
def printBook():
    url = "https://www.google.co.uk/books/edition/Harry_Potter_and_the_Sorcerer_s_Stone/wrOQLV6xB-wC?hl=en"
    pageCount,title = getInfo(url)
    f = open("booklist.txt","a")
    f.write(title +"," + pageCount)
    f.close()
    msg = title + " has " + pageCount + " pages"
    return msg

@app.route("/form")
def myForm():
    return render_template("form.html")

@app.route('/form', methods=['POST'])
def handleForm():
    url = request.form["text"]
    pages, title = getInfo(url)
    msg = title + " has " + pages + " pages"
    return render_template("form.html" , message = msg)

@app.route("/easy_test")
def viewEasyTest():
        return render_template("Easysample.html")

@app.route("/easy_test", methods=["POST","GET"] )
def handleButtons():
    # setting dummy values first
    start = 0.0
    end = 3.0
    msg = "green"
    # word count correct for wizard of oz
    wordCount = 513

    if request.method == "GET":
        if request.form["btn"] == "start":
            start = time.time() # seconds since 1 jan 1970
        elif request.form["btn"] == "stop":
            end= time.time() # seconds now 
            lapsed = end - start
            lapsed = lapsed / 60 # div by 60 to get minutes
            round(lapsed)
            minPerPage= lapsed / wordCount
            f = open("booklist.txt","r")
            details = f.readline()
            f.close()
            title, pc = details.split(",")
            totalTime = pc * lapsed

            msg = "This page of " + wordCount + " words, took you " + lapsed + " Minutes to read ,therefore " + title + "will take you" + totalTime + "Minutes" 
        return render_template("Easysample.html" , message = msg)

@app.route("/easy")
def easy1():
    return 


if __name__ == "__main__":
    app.run()