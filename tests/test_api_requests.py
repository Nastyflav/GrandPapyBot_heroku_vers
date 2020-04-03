#! /usr/bin/env python3
# coding: UTF-8

import gpb_app.models.api_requests as script
import pytest 
import json
import os
import requests
import urllib.parse as ur


class TestApiRequests:

    user_input = 'Nantes'
    place = script.APIRequests(user_input)
    results = {'candidates': [{'formatted_address': 'Nantes, France', \
                            'geometry': {'location': {'lat': 47.218371, 'lng': -1.553621}, \
                            'viewport': {'northeast': {'lat': 47.29582689999999, 'lng': -1.4783261}, 'southwest': {'lat': 47.1806171, 'lng': -1.6417861}}}, \
                            'name': 'Nantes'}], 'status': 'OK'}
            
    def test_location_datas(self, monkeypatch):

        def mock_json_example(*param):
            with open("tests/mock_requests/nantes.json", "r") as json_file:
                return json.loads(json_file.read())

        self.place.query = self.user_input
        monkeypatch.setattr('gpb_app.models.api_requests.APIRequests.location_datas', mock_json_example)
        self.place.location_datas()
        assert self.place.data == self.results

    def test_get_map(self):
        self.place.data['location'] = {'lat': '47.1806171', 'lng': '-1.6417861'}

        # Testing response URL without API key
        url = self.place.get_map()

        if 'key=' in url:
            old_parts = ur.urlparse(url)
            padic = ur.parse_qs(old_parts.query)
            del(padic['key'])
            query = ur.urlencode(padic, doseq=True)
            parts = (old_parts.scheme, old_parts.netloc, old_parts.path, '', query, '')
            url = ur.urlunparse(parts)

        assert url == "https://maps.googleapis.com/maps/api/staticmap?key=AIzaSyCH_uGge9XRsTK22BY6zDrR2OgpqOZK204&center=47.218371%2C-1.553621&markers=47.218371%2C-1.553621&size=500x400"
#   - Recevoir des données non valides ou manquantes 


# API Wiki Media
#   - Vérifier qu'il existe une page Wikipédia
#   - Récupérer l'extrait d'une histoire
#   - Récupérer un lien
#   - Récupérer une erreur