#! /usr/bin/env python3
# coding: UTF-8

import gpb_app.models.api_requests as script
import pytest 


class TestGoogleMapRequest:

    results = {'candidates': [{'formatted_address': 'Nantes, France', \
                            'geometry': {'location': {'lat': 47.218371, 'lng': -1.553621}, \
                            'viewport': {'northeast': {'lat': 47.29582689999999, 'lng': -1.4783261}, 'southwest': {'lat': 47.1806171, 'lng': -1.6417861}}}, \
                            'name': 'Nantes'}], 'status': 'OK'}

    def setup_method(self):
        self.gm_api = script.GoogleMapsRequest()

#   - Recevoir des données non valides ou manquantes
#   - Récupérer un nom
#   - Récupérer une adresse
#   - Récupérer une latitude
#   - Récupérer une longitude 
#   - Récupérer une carte


class TestWikiRequest:

    def setup_method(self):
        self.wiki_api = script.WikiRequest()
# API Wiki Media
#   - Vérifier qu'il existe une page Wikipédia
#   - Récupérer l'extrait d'une histoire
#   - Récupérer un lien
#   - Récupérer une erreur