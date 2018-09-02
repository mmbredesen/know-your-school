#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys
import json, urllib2
from algoliasearch import algoliasearch

client = algoliasearch.Client('E3Z5BWU5LE', 'f6f8da14853c3bdfa71fa1491c4ca78e')
index = client.init_index('know-your-school')

def extract():
    """
    Extracts data from a URL. Returns the data extracted as a dictionary.
    """
    URL = 'https://data.cityofnewyork.us/resource/sm8b-9vim.json'

    # Get JSON data from the URL
    response = urllib2.urlopen(URL)
    extracted_data  = json.load(response)

    return extracted_data

data = extract()

res = index.add_objects(data)