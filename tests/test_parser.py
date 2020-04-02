#! /usr/bin/env python3
# coding: UTF-8

import gpb_app.models.parser as script
import pytest


class TestUserQuery:

    USER_QUERY = script.Parser('Bonjour GrandPy ! Tu peux me donner l\'adresse du Louvre s\'il te plait ?')

    def test_get_textinput(self):
        """We get an input in lower cases"""
        assert self.USER_QUERY.textinput == 'bonjour grandpy ! tu peux me donner l\'adresse du louvre s\'il te plait ?'

    def test_clean_input_of_symbols(self):
        """Test the method that delete all the alphanum symbols"""
        self.USER_QUERY.clean_input_of_symbols()
        assert self.USER_QUERY.textinput == 'bonjour grandpy   tu peux me donner l adresse du louvre s il te plait  '

    def test_clean_input_of_stopwords(self):
        """Test the method that removes all the stopwords from"""
        self.USER_QUERY.clean_input_of_stopwords()
        assert self.USER_QUERY.final_query_in_string == 'louvre'

    def test_textinput_type(self):
        """Check the type of the returned input"""
        assert isinstance(self.USER_QUERY.textinput, str)
