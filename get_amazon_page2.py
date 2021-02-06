# Add links to urllist for more pages. 
# Code can be expanded to scrape more.

import requests
# from bs4 import BeautifulSoup
def main():
    url = 'https://www.amazon.com/Flash-Boys-Wall-Street-Revolt/dp/0393244660'
    # get amazon's response in bytes
    r = requests.get(url)
    # focus on content part and convert to regular text
    c = r.content.decode("utf-8")
    # split into lines
    lines = c.split("\n")
    # find the one that contains "print length" phrase
    desiredLine= ""
    for l in lines:
       print(l)
        # if "Print length" in l:
        #     desiredLine = l

    print(desiredLine)

if __name__ == "__main__":
    main()