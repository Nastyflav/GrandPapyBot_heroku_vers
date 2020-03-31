#! /usr/bin/env python3
# coding: UTF-8

import config as cf
import requests as rq
import json


class GoogleMapsRequest:
    """Class to load Google Maps datas and map from a user query"""
    def __init__(self, query):
        self.query = str(query)

    def location_datas(self):
        """Make a request to the API, and sort datas"""
        payload = {'input': self.query, 'inputtype': 'textquery','fields': 'formatted_address,name,geometry',\
                        'key': 'AIzaSyCH_uGge9XRsTK22BY6zDrR2OgpqOZK204', 'language': 'fr'}
        request = rq.get(url=cf.GOOGLE_URL, params=payload)
        datas = request.json()
        print(datas)


class WikiRequest:
    """Class to load Wikipedia datas from the GPS coordonates of the location"""
    def __init__(self):
        pass


def main():
    
    gm = GoogleMapsRequest('Nantes')
    gm.location_datas()

if __name__ == "__main__":
    main()
        