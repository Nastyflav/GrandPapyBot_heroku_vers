#! /usr/bin/env python3
# coding: UTF-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-04-20
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

import requests as rq
from random import choice
import config as cf


class APIRequests:
    """
    Class to load Google Maps datas.

    Also load Wikipedia datas from a user query

    """
    
    def __init__(self, query):
        """Init method"""
        self.query = str(query)

    def location_datas(self):
        """Make a request to the Google Maps API, and sort datas"""
        payload = {'address': self.query, 'key': cf.GOOGLE_KEY,
                   'language': cf.GOOGLE_LANGUAGE}
        response = rq.get(url=cf.GOOGLE_URL, params=payload)
        self.data = response.json()

        if self.data.get("status") == "OK":
            for data in self.data['results'][0]['address_components']:
                self.latitude = self.data['results'][0]['geometry']\
                ['location']['lat']
                self.longitude = self.data['results'][0]['geometry']\
                ['location']['lng']
                self.address = self.data['results'][0]['formatted_address']

            return {'message_address': choice(cf.ANSWERS_ADRESS_OK),
                    'address': self.address, 'latitude': self.latitude,
                    'longitude': self.longitude}

        else:
            return {'message_address': choice(cf.ANSWERS_ADRESS_FAIL),
                    'address': False}

    def get_place_by_gps(self):
        """
        Make a request to MediaWiki Geosearch API
        To get an amount of places around the GPS coordonnates
        
        """
        try:
            payload = {'format': 'json', 'action': 'query', 'list':
                       'geosearch', 'gsradius': 10000,
                       'gscoord': f'{self.latitude}|{self.longitude}'}
            response = rq.get(url=cf.WIKI_URL, params=payload)

            if response.status_code == 200:
                self.geosearch_data = response.json()
                return self.geosearch_data['query']['geosearch'][0]['pageid']
            else:
                return False
        except KeyError:
            return False

    def location_focus(self):
        """
        Make a request to the MediaWiki Extracts API
        Based on a Wiki page matching with the nearest place
        from the user query
        
        """
        try:
            self.page_id = self.get_place_by_gps()
            payload = {'format': 'json', 'action': 'query',
                       'prop': 'extracts|info', 'inprop': 'url',
                       'exsentences': 3, 'explaintext': 1,
                       'pageids': self.page_id}

            response = rq.get(cf.WIKI_URL, params=payload)

            if response.status_code == 200:
                self.wiki_data = response.json()
                self.wiki_data['status'] = True
                self.extract = self.wiki_data['query']['pages']\
                [str(self.page_id)]['extract']
                self.url = self.wiki_data['query']['pages']\
                [str(self.page_id)]['fullurl']

                return {'message_story': choice(cf.ANSWERS_STORY_OK),
                        'extract': self.extract, 'url': self.url}
            else:
                return {'message_story': choice(cf.ANSWERS_STORY_FAIL),
                        'extract': False}
        except KeyError:
            return {'message_story': choice(cf.ANSWERS_STORY_FAIL),
                    'extract': False}
