import flask
from flask import request
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask import render_template

#---------- URLS AND WEB PAGES -------------#

# Initialize the app
app = flask.Flask(__name__)
# app.config['SECRET_KEY'] = 'hard to guess string'

# bootstrap = Bootstrap(app)
# moment = Moment(app)

# class NameForm(FlaskForm):
#     name = StringField('What is your name?', validators=[DataRequired()])
#     submit = SubmitField('Submit')

@app.route('/', methods=["GET","POST"])
def viz_page():
    """
    Homepage: serve our visualization page, awesome.html
    """
    with open("index.html", 'r') as viz_file:
        return viz_file.read()
def score():
    print('hi)')
    if request.method=="GET":
        # print('i am here')
        # if request.form['recipes'] == 'Do Something':
            # print('here')
            # return render_template('music.html')
        return render_template('music.html')
    elif request.method=='POST':
        print('below get')
        return render_template('index.html')
    else:
        print('good')
        # return("ok")
        return render_template('music.html')

# def contact():
#     if request.method == 'POST':
#         if request.form['submit'] == 'Do Something':
#             pass # do something
#         elif request.form['submit'] == 'Do Something Else':
#             pass # do something else
#         else:
#             pass # unknown
#     elif request.method == 'GET':
#         return render_template('contact.html', form=form)

#--------- RUN WEB APP SERVER ------------#

# Start the app server on port 80
# (The default website port)
app.run(host='0.0.0.0')
app.run(debug=True)


# def score():
#     if request.method=="GET":
#         return '<form action="/score" method="post"><input type="submit" value="Send" /></form>'

#     elif request.method=='POST':
#         return render_template('music.html', form=form)
#     else:
#         return("ok")