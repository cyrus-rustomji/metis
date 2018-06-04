# Platinum or Bust

## Author

* Cyrus Rustomji

## Summary

The problem that each hip-hop/R&B artist has is determing if their new album will go platinum or not. To solve this classification problem, I used Spotify's API to all collect all my data points and features which are shown below. The goal of this prolem was to predict whether a new album will go platinum or not. The soltuion for this problem came to feature importance, using a Multinomial Naive Bayes model. I was able to determine the number of followers an artist has is heavily dependent if an artist will go platinum or not. This is shown through the flask app I created along with a precision score of **0.86**.

## Files

* spotify test.py
	* tests to see if I can pull data from Spotify's API
* spotify artist search.py
	* Looks up artist info for the artist inputted
* find all hip hop albums.py
	* Looks ups album, song, genres, and more
* 1 Data Cleaning.ipynb
	* combined all pkl files into a data frame
* 3 Pipeline.ipynb
	* EDA, Train/test split, Elastic Net, and Poly Fitting
* Pkl files
	* Used to compress files
* GDP_pop.csv
	* Data pulled from online sources and pasted into a csv
* Presentation

## Modeling

### Features

* Spotify Popularity Index
* Artist's Spotify followers
* Number of Genres
* Genres used as dummies
* Platinum album(s) (Y/N)?

### Tools Used

* Linear Regression
* OLS Testing
* Train/test split
* Elastic Net
* Logistic Regression
* Gradient Descent
* K Nearest Neighbors
* Classification Errors
* SVMs
* Decision Trees

## Packages 

* pandas
* numpy
* matplotlib
* seaborn
* sklearn
* patsy
* statsmodels
* scipy


