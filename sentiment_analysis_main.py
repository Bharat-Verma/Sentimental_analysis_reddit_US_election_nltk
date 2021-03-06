#!/usr/bin/python
"""
Created on Tue Mar 14 20:00:41 2017
@author: Bharat
"""
import pandas as pd

#importing the dataset
dataset = pd.read_csv("RS_abc.csv")

#Cleaning the texts
import re
#remove the non significant words which doesnt help us to 
#know whether the comment is good or bad (e.g. is, am, are etc)
#stopwords is the list of those words.
import nltk
#nltk.download()
nltk.download('stopwords')
from nltk.corpus import stopwords

#stemming the words will make sure to take the root words only
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

#corpus is list of all the words for each email
corpus = []
#pre processing the text of the comments by removing all the unwanted spaces,
#converting the words in lower case and 
#removing all the words that are in the stopwords list from the comments
#after this for loop each word in corpus is lower case and root word
for i in xrange(0,65280):
    review = re.sub('[^a-zA-Z]', ' ', dataset['title'][i])
    review = review.lower()
    review = review.split()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = " ".join(review)
    corpus.append(review)

    
from nltk.sentiment.vader import SentimentIntensityAnalyzer

polarity = []
sid = SentimentIntensityAnalyzer()
for sentence in corpus:
    print(sentence)
    ss = sid.polarity_scores(sentence)
    print (ss)
    print (ss['compound'])
    polarity.append(ss['compound'])
    #for k in sorted(ss):
    #    print('{0}: {1}, '.format(k, ss[k]))
    #print()
    
f = open("senti_stem_stop.csv", "w")

for i in xrange(0,65280):
    f.write("{},{},{}\n".format(corpus[i], dataset['created_utc'][i], polarity[i]))

f.close() 
    
    
    
