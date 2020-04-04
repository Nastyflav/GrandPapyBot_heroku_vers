#! /usr/bin/env python3
# coding: UTF-8

import gpb_app.models.api_requests as script
import pytest 
import json
import os
import urllib.request
import urllib.parse as ur


class TestApiRequests:

    user_input = 'Nantes'
    place = script.APIRequests(user_input)
            
    def test_location_datas(self, monkeypatch):
        """Test if the Google API returns us the right informations"""
        self.results = {'candidates': [{'formatted_address': 'Nantes, France', \
                            'geometry': {'location': {'lat': 47.218371, 'lng': -1.553621}, \
                            'viewport': {'northeast': {'lat': 47.29582689999999, 'lng': -1.4783261}, 'southwest': {'lat': 47.1806171, 'lng': -1.6417861}}}, \
                            'name': 'Nantes'}], 'status': 'OK'}

        def mock_json_location(requests):
            return self.results

        self.place.query = self.user_input
        monkeypatch.setattr(urllib.request, 'urlopen', mock_json_location)
        self.place.location_datas()
        assert self.place.data == self.results

    def test_get_coordinates(self, monkeypatch):
        """Check if the GPS coordinates are the right ones"""
        self.wiki_latitude = 47.2183475
        self.wiki_longitude = -1.5533048

        def mock_place_coord(requests):
            return self.wiki_coord

        self.place.query = self.user_input
        monkeypatch.setattr(urllib.request, 'urlopen', mock_place_coord)
        self.place.get_place_by_gps()
        assert self.place.geosearch_data['query']['geosearch'][0]['lat'] == self.wiki_latitude
        assert self.place.geosearch_data['query']['geosearch'][0]['lon'] == self.wiki_longitude

    def test_get_place_url(self, monkeypatch):
        """Check if twe can get an url for the Wiki page"""
        self.wiki_url = 'https://fr.wikipedia.org/wiki/Rue_de_la_Commune_(Nantes)'

        def mock_place_url(requests):
            return self.wiki_url

        self.place.query = self.user_input
        monkeypatch.setattr(urllib.request, 'urlopen', mock_place_url)
        self.place.location_focus()
        assert self.place.wiki_data['query']['pages']['7148944']['fullurl'] == self.wiki_url

    def test_get_place_extract(self, monkeypatch):
        """Check if twe can get the extract for the Wiki page"""
        self.wiki_extract = "La rue de la Commune est une voie située dans le centre-ville de Nantes, en France.\n\n\n== Description ==\nLa rue de la Commune est une voie bitumée et ouverte à la circulation automobile. Elle va de la place Saint-Jean à la place de l'Hôtel-de-Ville.\n\n\n== Dénomination ==\nCe nom lui a été attribué en 1793, la rue s'appelait auparavant « rue de Verdun ».\n\n\n== Historique ==\nLa rue était naguère plus longue qu'elle ne l'est aujourd'hui. En effet, avant l'aménagement de la place de l'Hôtel-de-ville, elle englobait également la partie septentrionale de la rue du Moulin, jusqu'au niveau de la rue Fénelon (voire jusqu'à l'actuelle rue de la Marne selon Ange Guépin).\n\n\n== Références ==\n\n\n== Voir aussi ==\n\n\n=== Bibliographie ===\nÉdouard Pied, Notices sur les rues de Nantes, A. Dugas, 1906, 331 p., p. 75.\n\n\n=== Articles connexes ===\nListe des voies de Nantes Portail de l’architecture et de l’urbanisme   Portail de Nantes…"

        def mock_place_extract(requests):
            return self.wiki_extract

        self.place.query = self.user_input
        monkeypatch.setattr(urllib.request, 'urlopen', mock_place_extract)
        self.place.location_focus()
        assert self.place.wiki_data['query']['pages']['7148944']['extract'] == self.wiki_extract

    def test_get_map(self):
        """Test the returned map static url by the get_map() method, but without the Google API Key"""
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

        assert url == "https://maps.googleapis.com/maps/api/staticmap?center=47.218371%2C-1.553621&markers=47.218371%2C-1.553621&size=500x400"