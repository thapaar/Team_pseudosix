import time
import requests

def getText(fileName):
    #opening filename passed into the function 
    f= open(fileName)
    
    # add entire file to a variable to be dealt with later
    content = f.read()
    # clse the file no longer needed
    f.close()
    # return contents for printing
    return content

def getWordCount(entirePassage):
    #trying to extract the words first change any line breaks into spaces
    entirePassage = entirePassage.replace("\n", " ")
    # now passage contains only words and spaces  
    
    # split passage on spaces 
    words = entirePassage.split(" ")
    #we are left with a list of words 

    # get length of list and possibly number of words
    wc = len(words)

    # go through list reemove blank words if any
    for i in range():
        if words[i] == "":
            del words[i]

    # recalculate lengtth
    wc = len(words)

    return wc


def main():
    print("Reading Test")
    print("Please choose reading sample (hit 's' when finished):")

    print("1. Sample A \n2. Sample B \n3. Sample C")

    choice = input("Please Pick a number ")

    # if users choice is not allowed keep asking
    while choice not in ["1", "2", "3"]: 
            choice = input("Please Pick a number: ")
    
    # convert string of choice into number
    choice = int(choice)
    
    # dummy value for now, update later
    fileName = ""
    # adjust filename to user's choice
    if choice == 1:
        fileName = "reading_sample.txt"
    elif choice == 2:
        fileName = "reading_sample.txt"
    elif choice == 3:
        fileName = "reading_sample.txt"

    # retrieve sample 
    print(fileName)
    # sample = getText(fileName)
    sample = getText(fileName)
    
    # get page count
    numOfPages = 2 # supposedly

    # display users text sample
    print(sample)

    # retrieve time at start (seconds since 1 Jan 1970)
    start = time.time()

    # give dummy value so can be changed later
    end = 3.0

    # wait for user to press key
    keypress = input()

    if keypress == "s": # if user enters s 
        end = time.time() # retrieve seconds at emd
        
        lapsed = end - start # take difference

        lapsed = round(lapsed) # round and print result
        minsPerPage = lapsed/ numOfPages
        print(minsPerPage)

        print("You read", numOfPages, "pages in" ,lapsed, "minutes, therefore it takes", minsPerPage ,"mins to read each page")

        # could use a command like fillTextBox rather than print if using flask

if __name__ == "__main__":
    main()