# Will a Hip-Hop and R&B album go Platinum or not?

## Author

* Cyrus Rustomji

# Executive Summary

> The most important feature in this model was the amount of spotify followers an artist has. The greater the number of spotify followers, the higher likelihood their album will go platinum. The number of genres was the least important feature in this model.

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


