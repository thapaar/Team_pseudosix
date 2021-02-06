import time
# retrieve time at start (seconds since 1 Jan 1970)
start = time.time()

# give dummy value so can be changed later
end = 3.0

# display users text sample
print("Paragraph of text goes here \nplease press s when done")

wordCount = 10 # for arguements sake  

# wait for user to press key
keypress = input()

if keypress == "s": # if user enters s 
    end = time.time() # retrieve seconds at emd
    lapsed = end - start # take difference
    lapsed = round(lapsed) # round and print result
    wordsPerMin = wordCount/ lapsed
    print(wordsPerMin)

    # could use a command like fillTextBox rather than print if using flask
