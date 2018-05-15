import flask
from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import patsy
import statsmodels.api as sm
from statsmodels.formula.api import ols


#---------- MODEL IN MEMORY ----------------#

# Read the scientific data on breast cancer survival,
# Build a LogisticRegression predictor on it
# patients = pd.read_csv("haberman.data", header=None)
# patients.columns=['age','year','nodes','survived']

patients = pd.read_csv("first_album.csv")
patients.columns=['plat','followers','popularity']

# patients=patients.replace(2,0)  # The value 2 means death in 5 years, update to more common 0
# X = patients[['age','year','nodes']]
# Y = patients['survived']


X = patients[['followers','popularity']]
y = patients['plat']
PREDICTOR = LogisticRegression().fit(X,y)


# y, X = patsy.dmatrices('plat ~ popularity + followers', data=patients, return_type="dataframe")
# model_1 = sm.OLS(y,X)
# PREDICTOR = model_1.fit()

# PREDICTOR2 = LinearRegression()
# PREDICTOR = PREDICTOR2.fit(X,y)



#---------- URLS AND WEB PAGES -------------#

# Initialize the app
app = flask.Flask(__name__)

# Homepage
@app.route("/")
def viz_page():
    """
    Homepage: serve our visualization page, awesome.html
    """
    with open("music.html", 'r') as viz_file:
        return viz_file.read()

# Get an example and return it's score from the predictor model
@app.route("/score", methods=["POST"])
def score():
    """
    When A POST request with json data is made to this uri,
    Read the example from the json, predict probability and
    send it with a response
    """
    # Get decision score for our example that came with the request
    data = flask.request.json
    x = np.matrix(data["example"])
    score = PREDICTOR.predict_proba(x)
    # Put the result in a nice dict so we can send it as json
    results = {"score": score[0,1]}
    return flask.jsonify(results)

#--------- RUN WEB APP SERVER ------------#

# Start the app server on port 80
# (The default website port)
app.run(host='0.0.0.0')
app.run(debug=True)
