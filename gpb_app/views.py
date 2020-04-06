#! /usr/bin/env python3
# coding: utf-8

import random
from flask import Flask, render_template, request, jsonify

from .models.api_requests import APIRequests
from .models.parser import Parser
import config as cf

app = Flask(__name__)
app.config.from_object('config')

@app.route('/chatbox', methods=['POST'])

def chatbox():
    """Route to connect Python backend and JS frontend"""
    query = request.form['userinput']

    if len(query) <= 1:         #if the user doesn't write a single character
        empty_error = cf.EMPTY_QUERY_ANSWER
        return jsonify({'error': empty_error})

    parser = Parser(query)      #parse the user input
    parser.clean_input_of_symbols()
    parser.clean_input_of_stopwords()

    try:
        place = APIRequests(parser.final_query_in_string)     #call the API to search the place contained in the user query
    except:
        return jsonify({'error': "Ton Internet déraille complètement..."})

    if place.location_datas is False:       #if there's no such place existing
        error_list = cf.ANSWERS_ADRESS_FAIL
        random_index = random.randint(0, 3)
        missing_place_answer = error_list[random_index]
        return jsonify({'error': missing_place_answer})
    else:
        answers_list = cf.ANSWERS_ADRESS_OK
        random_index = random.randint(0, 3)
        text_location = answers_list[random_index]
        
        location_geo_datas = place.location_datas()
        name = location_geo_datas.get('name')     #if there's a place, gets its name and adress
        adress = location_geo_datas('adress')

    map_url = place.get_map()       #get the map url from a method

    if place.get_place_by_gps is False:
        return jsonify({'error': "Ton Internet déraille complètement..."})

    if place.location_focus is False:       #if the Wikipedia page is missing or empty
        error_list = cf.ANSWERS_STORY_FAIL
        random_index = random.randint(0, 3)
        missing_story_answer = error_list[random_index]
        return jsonify({'error': missing_story_answer})
    else:
        answers_list = cf.ANSWERS_STORY_OK
        random_index = random.randint(0, 3)
        text_story = answers_list[random_index]

        location_datas = place.location_focus()
        extract = location_datas.get('extract')       #gets the infos we need
        url = location_datas.get('url')

    return jsonify({'name': name, 'adress': adress, 'map': map_url, 'location': text_location, 'story': text_story,
                    'extract': extract, 'url': url})

@app.route('/')
@app.route('/index/')
def index():
    """Display the web page with html and css code"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run()