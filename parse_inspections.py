from datetime import datetime
from pprint import pprint
import pandas as pd
import numpy as np
import urllib2
import json
import matplotlib.pyplot as plt
import seaborn as sns

DATA_FILE_PATH = 'data/debug.json'

def extract():
    """
    Extracts data from a URL. Returns the data extracted as a dictionary.
    """
    URL = 'http://data.cityofnewyork.us/resource/p4ef-99fx.json'

    # Get JSON data from the URL
    response = urllib2.urlopen(URL)
    extracted_data  = json.load(response)

    return extracted_data

def transform(data):
    safety = {}

    for datum in data:
        bor = datum["borough_name"]
        category = datum["inspection_category"]
        obs = datum["observation_description"]

        if bor == "QUEENS" and obs == "Deficiency":
            if category not in safety:
                safety[category] = 1
            else:
                safety[category] = safety[category] + 1

    for key in safety:
        print("%s: %d\n" % (key, safety[key]))


data = extract()
transform(data)

x=['Roofing', 'Architectural', 'Boiler', 'Window', 'Safety', 'Plumbing', 'Construction', 'Sprinklers and Pipe', 'Masonry', 'Power and Lighting', 'HVAC', 'Low Voltage', 'Fuel Storage Burner']
values=[9, 11, 1, 0, 44, 6, 11, 0, 9, 3, 5, 2, 1]
y_pos = np.arange(len(x))

plt.title('Queens School Inspections Labeled Deficient 2018')
plt.xlabel('Count')
plt.ylabel('Type')

plt.barh(y_pos, values)
plt.yticks(y_pos, x)
plt.show()
