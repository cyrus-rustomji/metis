# Sentiment Analysis on 2018 NBA Free Agents

## Author

* Cyrus Rustomji

## Summary

The problem I am trying to solve is how a NBA General Manager (GM) can retain their top free agents and/or acquire other top free agents. I scraped Instagram using Selenium and Beautiful Soup to capture a sentiment analysis on their captions. The goal of this project is try to predict if a player is happy or sad on their respective teams. After doing LDA on the whole dataset, I realized it is more beneficial to do LDA on a player by player basis as GM's already know which ~10 players they will target and built a flask app showing each player sentiment throughout this past basketball year vs. their whole Instagram history.


## Modeling


### Tools Used

* LSA
* LDA
* NMF
* K - Means
* Topic Modeling
* LDAvis
* Word2Vec

## Packages 

* pandas
* nltk
* selenium
* Beautiful Soup
* numpy
* matplotlib
* sklearn
* textblob
* pyLDAvis


