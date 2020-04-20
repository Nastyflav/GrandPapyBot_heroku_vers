#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-04-20
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from flask import Flask, render_template, request, jsonify

from .models.api_requests import APIRequests
from .models.parser import Parser

app = Flask(__name__)
app.config.from_object('config')


@app.route('/chatbox', methods=['POST'])
def chatbox():
    """Route to connect Python backend and JS frontend"""
    if "input" in request.form:
        response = {'userquestion': request.form['input']}
        query = request.form['input']
        parser = Parser(query)
        parser.clean_input_of_symbols()
        parser.clean_input_of_stopwords()

        place = APIRequests(parser.final_query_in_string)
        response.update(place.location_datas())
        response.update(place.location_focus())

    return jsonify(response)


@app.route('/')
@app.route('/index/')
def index():
    """Display the web page with html and css code"""
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
