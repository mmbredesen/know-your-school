from datetime import datetime
from pprint import pprint
import pandas as pd
import numpy as np
import urllib2
import json

DATA_FILE_PATH = 'data/debug.json'

def extract():
    """
    Extracts data from a URL. Returns the data extracted as a dictionary.
    """
    URL = 'http://data.cityofnewyork.us/resource/pivb-ninm.json'

    # Get JSON data from the URL
    response = urllib2.urlopen(URL)
    extracted_data  = json.load(response)

    return extracted_data

def transform(data):
    types = {}
    costs = {}

    for datum in data:
        bor = datum["borough"]
        total = int(datum["total"])
        des = datum["description"]

        if bor not in costs:
            costs[bor] = total
        else:
            costs[bor] = costs[bor] + total
        key = bor + ":" + des
        if  key not in types:
            types[key] = 1
        else:
            types[key] = types[key] + 1

    for key in types:
        print("%s: %d\n" % (key, types[key]))

    for key in costs:
        print("%s: %d\n" % (key, costs[key]))

data = extract()
transform(data)
