#! /usr/bin/env python3
# coding: utf-8

from flask import Flask, render_template, request, jsonify

from .models.api_requests import APIRequests
from .models.parser import Parser
import config as cf

app = Flask(__name__)
app.config.from_object('config')

@app.route('/chatbox', methods=['POST'])

def chatbox():
    """Route to connect Python backend and JS frontend"""

    if "input" in request.form:        #if the user actually writes a single character

        response = {'userquestion': request.form['input']}
        query = request.form['input']
        parser = Parser(query)      #parse the user input
        parser.clean_input_of_symbols()
        parser.clean_input_of_stopwords()

        place = APIRequests(parser.final_query_in_string)     #call the API to search the place contained in the user query



    return jsonify(response)

@app.route('/')
@app.route('/index/')
def index():
    """Display the web page with html and css code"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run()