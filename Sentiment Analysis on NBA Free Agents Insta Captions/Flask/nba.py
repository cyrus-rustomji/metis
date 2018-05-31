import pandas as pd
import gensim
import os
import collections
import smart_open
import random
import flask
from surprise import SVDpp,SVD
from surprise import Dataset
from surprise import Reader
import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
#import urllib2

app = flask.Flask(__name__)

#pulling in dataset, item list
with open('/Users/deven/Documents/pickleddata/projectfletcher/newdatalist.pkl', 'rb') as picklefile:
    itemdf = pickle.load(picklefile)
with open('surprise_data.pkl', 'rb') as picklefile:
    surprisedf = pickle.load(picklefile)


@app.route("/score", methods=["POST"])
def score():
    """
    When A POST request with json data is made to this uri,
    Read the example from the json, predict probability and
    send it with a response
    """
    # Get decision score for our example that came with the request
    data = flask.request.json
    color='#00dbfb'
    x = data["example"]
    rec1,rec2,rec3 = get_top_n(x[0],x[2])
    bookrec= getBookrec(x[0])
    print(score)
    list1=[]
    for i in score[0]:
        list1.append(i)
    index, value = max(enumerate(list1), key=operator.itemgetter(1))
    print(index)
    clas = ['F23-', 'F24-26','F27-28','F29-32', 'F33-42', 'F43+', 'M22-', 'M23-26', 'M27-28', 'M29-31', 'M32-38', 'M39+']
    label = clas[index]
    if index <= 5:
        color ='#FF75A3'
    else:
        color ='#00dbfb'
    print(label)
    print(color)
    # Put the result in a nice dict so we can send it as json
    results = {"tearec1":rec1,"tearec2":rec2,"tearec3":rec3,"bookrec":bookrec}
    return flask.jsonify(results)

#--------- RUN WEB APP SERVER ------------#

# Start the app server on port 80
# (The default website port)
#app.run(host='0.0.0.0')
# app.run(debug=True)