# Sentiment Analysis on 2018 NBA Free Agents

## Author

* Cyrus Rustomji

# Summary

> The problem I am trying to solve is how a NBA GM can retain their top free agents and/or acquire other top free agents. I scraped Instagram using Selenium and Beautiful Soup to capture a sentiment analysis on their captions. The goal of this project is try to predict if a player is happy or sad on their respective teams.

## Files

* full model.ipynb
	* Includes all NLP modeling
* all captions in one scrape
	* Final scrape of instagram captions
* flask.py, index.html, and dropdown.js
	* All relate to the flask app

## Modeling

### Features

* Spotify Popularity Index
* Artist's Spotify followers
* Number of Genres
* Genres used as dummies
* Platinum album(s) (Y/N)?

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


