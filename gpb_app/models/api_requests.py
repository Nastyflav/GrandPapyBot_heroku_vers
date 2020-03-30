#! /usr/bin/env python3
# coding: UTF-8

import requests as rq
import json


class GoogleMapsRequest:
    """Class to load Google Maps datas and map from a user query"""
    def __init__(self):
        self.data_list = []

    def location_datas(self, query):
        """Make a request to the API, and sort datas"""
        payload = {'input': query, 'inputtype': 'textquery','fields': 'formatted_address,name,geometry',\
                        'key': 'AIzaSyCH_uGge9XRsTK22BY6zDrR2OgpqOZK204', 'language': 'fr'}
        request = rq.get(url='https://maps.googleapis.com/maps/api/place/findplacefromtext/json?', params=payload)
        data = request.json()
        self.data_list.append(data)
        print(self.data_list)


class WikiRequest:
    """Class to load Wikipedia datas from the GPS coordonates of the location"""
    def __init__(self):
        pass


def main():
    
    gm = GoogleMapsRequest()
    gm.location_datas('Nantes')

if __name__ == "__main__":
    main()
        