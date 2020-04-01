#! /usr/bin/env python3
# coding: UTF-8

import gpb_app.models.parser as script
import pytest


class TestUserQuery:

    USER_QUERY = script.Parser('Bonjour GrandPy ! Tu peux me donner l\'adresse du Louvre s\'il te plait ?')

    def test_get_textinput(self):
        """We get an input in lower cases"""
        assert self.USER_QUERY.textinput == 'bonjour grandpy ! tu peux me donner l\'adresse du louvre s\'il te plait ?'

    def test_get_rid_of_symbols(self):
        assert self.USER_QUERY.final_query_in_string == 'bonjour grandpy  tu peux me donner l adresse du louvre s il te plait  '

    def test_textinput_type(self):
        """Check the type of the returned input"""
        assert isinstance(self.USER_QUERY.textinput, str)
#   - Récupérer un lieu dans une phrase
#   - Enlever les stop words d'une phrase