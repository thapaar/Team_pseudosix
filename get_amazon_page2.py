# Add links to urllist for more pages. 
# Code can be expanded to scrape more.

import requests

def newStyle(url):

        # pretend scraper is firefox 
    headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0"}
    # ensure page is new style google books
    r = requests.get(url, headers=headers)
    # focus on content part and convert to regular text
    c = r.content.decode("utf-8")
    # chopping out small portion of entire page 
    # find position of start of phrase "page Count"
    start = c.find("Page count:")
    # include 60 chars on from that
    end = start + 60
    # isolate that section
    desiredSection = c[start:end]
    # page number is in between the last > and last < find these from Right to Left
    start = desiredSection.rfind(">") +1
    end = desiredSection.rfind("<") 
    pageCount = desiredSection[start:end]
    titleStart = c.find('role="heading"') 
    titleEnd =  titleStart +70
    titleSection = c[titleStart:titleEnd]
    firstClose = titleSection.find(">") +1
    firstOpen = titleSection.find("<")
    title = titleSection[firstClose:firstOpen]
    print(pageCount , title)

def oldStyle(url):
    # pretend scraper is firefox 
    headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0"}
    r = requests.get(url, headers=headers)
    # focus on content part and convert to regular text
    c = r.content.decode("utf-8")
    # chopping out small portion of entire page 
    # find position of start of phrase "page Count"
    start = c.find("Length</")
    # include 60 chars on from that
    end = start + 70
    # isolate that section
    desiredSection = c[start:end]
    # print(desiredSection)
    start = desiredSection.rfind(">") + 1
    end = desiredSection.rfind(" ")
    pageCount = desiredSection[start:end]

    titleStart = c.find('<title>')
    titleEnd =  c.find("</title>")
    titleSection = c[titleStart:titleEnd]
    titleSection = titleSection.strip("<title>")
    titleEnd = titleSection.find("- Go")
    title = titleSection[0:titleEnd]
    print(pageCount, title)

def main():
    url = "https://books.google.co.uk/books/about/War_and_Peace.html?id=s-OQ2yHDIMQC&redir_esc=y"
    # url = "https://www.google.co.uk/books/edition/A_Tale_of_Two_Cities/5EIPAAAAQAAJ?hl=en&gbpv=0&bsq=tale%20of%20two%20cities"
    #url = "https://www.google.co.uk/books/edition/Harry_Potter_and_the_Sorcerer_s_Stone/wrOQLV6xB-wC?hl=en"
    if "books.google" in url:
        oldStyle(url)
    else:
        newStyle(url)

if __name__ == "__main__":
    main()