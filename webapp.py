from flask import Flask, request
from flask import render_template, flash, Markup

import os
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/showFact')
def search_by_county():
    state = request.args.get('state')
    county = county_most_under_18(state)
    fact = "In " + state + ", the county with the highest percentage of under 18 year olds is " + county + "."
    return render_template('home.html', funFact=fact)

def county_most_under_18(state):
    """Return the name of a county in the given state with the highest percent of under 18 year olds."""
    with open('demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    highest=0
    county = ""
    for c in counties:
        if c["State"] == state:
            if c["Age"]["Percent Under 18 Years"] > highest:
                highest = c["Age"]["Percent Under 18 Years"]
                county = c["County"]
    return county

def is_localhost():
    """ Determines if app is running on localhost or not
    Adapted from: https://stackoverflow.com/questions/17077863/how-to-see-if-a-flask-app-is-being-run-on-localhost
    """
    root_url = request.url_root
    developer_url = 'http://127.0.0.1:5000/'
    return root_url == developer_url


if __name__ == '__main__':
    app.run(debug=True) # change to False when running in production