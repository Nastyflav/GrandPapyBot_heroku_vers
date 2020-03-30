#! /usr/bin/env python3
# coding: UTF-8

import requests as rq
import json
import config as cf


class GoogleMapsRequest:
    """Class to load Google Maps datas and map from a user query"""
    def __init__(self):
        self.data_list = []

    def location_datas(self, query):
        """Make a request to the API, and sort datas"""
        payload = {'input': query, 'inputtype': cf.GOOGLE_INPUTTYPE,'fields': cf.GOOGLE_FIELDS,\
                        'key': cf.GOOGLE_KEY, 'language': cf.GOOGLE_LANGUAGE}
        request = rq.get(url=cf.GOOGLE_URL, params=payload)
        data = request.json()
        self.data_list.append(data)
        print(self.data_list)
        