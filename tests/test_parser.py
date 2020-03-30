#! /usr/bin/env python3
# coding: UTF-8

import gpb_app.models.parser as script
import pytest

# Parser
#   - Récupérer une question posée
#   - Récupérer un lieu dans une phrase
#   - Enlever les symboles typographiques
#   - Enlever les stop words d'une phrase