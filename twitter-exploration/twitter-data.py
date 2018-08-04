import json
from textblob import TextBlob

import matplotlib.pyplot as plt


# gets json data (open, load close)
file = open("tweets.json", "r")
tweetData = json.load(file)
file.close()

#sentiment = polarity
#sentiment list

polarityList = []

#get sentiment data

#for loop

#use textblob here

for tweets in tweetData:
    textBlob = TextBlob(tweets["text"])
    polarityList.append(textBlob.polarity)

# print(polarityList)

#createhistogram, polarity, and BioInsights

plt.hist(polarityList, bins = [-1.0, -.75, -.5, -.25, 0, .25, .5, .75, 1.0])

#set x and y labelmars
plt.xlabel("Polarities")
plt.ylabel("Number of tweets")

#give it a title
plt.title("Histogram of Tweet Polarity")

#set the axis to fit data range
plt.axis([-1.0, 1.0, 0, 100])
plt.grid(True)
#Shows
plt.show()




# for tweets in range(len(tweetData)):
#     print("Tweet Text: ", tweetData[tweets]["text"], "\n")
#
# for tweets in range(len(tweetData)):
#     print("Tweet id: ", tweetData[tweets]["id"], "\n")
