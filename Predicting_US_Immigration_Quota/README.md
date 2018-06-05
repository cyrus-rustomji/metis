# Predicting the US Immigration Quota

## Author

* Cyrus Rustomji

## Summary

The problem that each potential US immigrant has is wondering what the US population will be the next 5-10 years. This number is dependent on if they and/or their family will gain citizenship or not. The goal of this project was to see what feature(s) are most important in determining this number. To solve this problem, I used regularization methods to determine where the feature importance lies in the data. I used Elastic Net and saw that the US and Global Population were eliminated; however, the US GDP has the highest feature importance as with a coefficient of **+7.4e+4**.


## Modeling

### Features Used

* US Population
* Global Population
* US GDP
* Global GDP
* Foreign Policy Indicator

### Tools Used

* Linear Regression
* OLS Testing
* Train/test split
* Lasso, Ridge, and Elastic Net

## Packages 

* pandas
* numpy
* matplotlib
* seaborn
* sklearn
* patsy
* statsmodels
* scipy