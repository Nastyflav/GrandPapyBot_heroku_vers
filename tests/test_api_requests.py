#! /usr/bin/env python3
# coding: UTF-8

import gpb_app.models.api_requests as script
import pytest 
import json
import os
import requests

class TestApiRequests:

    user_input = 'Nantes'
    place = script.APIRequests(user_input)
    results = {'candidates': [{'formatted_address': 'Nantes, France', \
                            'geometry': {'location': {'lat': 47.218371, 'lng': -1.553621}, \
                            'viewport': {'northeast': {'lat': 47.29582689999999, 'lng': -1.4783261}, 'southwest': {'lat': 47.1806171, 'lng': -1.6417861}}}, \
                            'name': 'Nantes'}], 'status': 'OK'}
            
    def test_location_datas(self, monkeypatch):

        def mock_json_oc(*args, **kwargs):
            with open("tests/mock_requests/nantes.json", "r") as json_file:
                return json.loads(json_file.read())

        self.place.query = self.user_input
        monkeypatch.setattr('gpb_app.models.api_requests.GoogleMapsRequest.location_datas', mock_json_oc)
        self.place.location_datas()
        assert self.place.location_datas == self.results
#   - Recevoir des données non valides ou manquantes
#   - Récupérer un nom
#   - Récupérer une adresse
#   - Récupérer une latitude
#   - Récupérer une longitude 
#   - Récupérer une carte


# API Wiki Media
#   - Vérifier qu'il existe une page Wikipédia
#   - Récupérer l'extrait d'une histoire
#   - Récupérer un lien
#   - Récupérer une erreur