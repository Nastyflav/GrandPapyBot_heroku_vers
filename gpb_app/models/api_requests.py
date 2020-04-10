#! /usr/bin/env python3
# coding: UTF-8

import requests as rq
import json
import urllib.parse as ur
from random import choice
import config as cf


class APIRequests:
    """Class to load Google Maps datas, a map and Wikipedia datas from a user query"""
    def __init__(self, query):
        self.query = str(query)

    def location_datas(self):
        """Make a request to the Google Maps API, and sort datas"""
        payload = {'input': self.query, 'inputtype': cf.GOOGLE_INPUTTYPE,'fields': cf.GOOGLE_FIELDS,\
                        'key': cf.GOOGLE_KEY, 'language': cf.GOOGLE_LANGUAGE}
        response = rq.get(url=cf.GOOGLE_URL, params=payload)
        self.data = response.json()
        
        if self.data.get("status") == "OK":
            self.latitude = self.data['candidates'][0]['geometry']['location']['lat']
            self.longitude = self.data['candidates'][0]['geometry']['location']['lng']
            self.name = self.data['candidates'][0]['name']
            self.address = self.data['candidates'][0]['formatted_address']

            return {'message_address': choice(cf.ANSWERS_ADRESS_OK), 'name': self.name, 'address': self.address,
                    'latitude': self.latitude, 'longitude': self.longitude}
        
        else:
            return {'message_address': choice(cf.ANSWERS_ADRESS_FAIL), 'name': False}

    def get_place_by_gps(self):
        """Make a request to MediaWiki Geosearch API, to get an amount of places around the GPS coordonnates"""
        try:
            payload = {'format': 'json', 'action': 'query', 'list': 'geosearch', 'gsradius': 10000, \
                    'gscoord': f'{self.latitude}|{self.longitude}'}
            response = rq.get(url =cf.WIKI_URL, params=payload)

            if response.status_code == 200:
                self.geosearch_data = response.json()
                return self.geosearch_data['query']['geosearch'][0]['pageid']
            else:
                return False
        except:
            return False

    def location_focus(self):
        """Make a request to the MediaWiki Extracts API, based on a Wiki page matching with the nearest place from the user query"""
        try:
            self.page_id = self.get_place_by_gps()
            payload = {'format': 'json', 'action': 'query', 'prop': 'extracts|info', \
                    'inprop': 'url', 'exsentences': 3, 'explaintext': 1, 'pageids': self.page_id}

            response = rq.get(cf.WIKI_URL, params=payload)
        
            if response.status_code == 200:
                self.wiki_data = response.json()
                self.wiki_data['status'] = True
                self.extract = self.wiki_data['query']['pages'][str(self.page_id)]['extract']
                self.url = self.wiki_data['query']['pages'][str(self.page_id)]['fullurl']

                return {'message_story': choice(cf.ANSWERS_STORY_OK), 'extract': self.extract, 'url': self.url}
            else:
                return {'message_story': choice(cf.ANSWERS_STORY_FAIL), 'extract': False, 'url': False}
        except:
            return {'message_story': choice(cf.ANSWERS_STORY_FAIL), 'extract': False, 'url': False}
