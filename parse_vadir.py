from datetime import datetime
from pprint import pprint
import pandas as pd
import numpy as np
import urllib2
import json
import matplotlib.pyplot as plt
import seaborn as sns


COUNTY_FILE_PATH = 'data/sex_crimes_county.json'

def extract():
    """
    Extracts data from a URL. Returns the data extracted as a dictionary.
    """
    URL = 'http://data.cityofnewyork.us/resource/myab-vkpf.json'

    # Get JSON data from the URL
    response = urllib2.urlopen(URL)
    extracted_data  = json.load(response)

    return extracted_data

agg_function_sum = {'forcible_sex_offenses_with_weapon_s': ['sum'],
'other_sex_offenses_without_weapon_s': ['sum'],
'other_sex_offenses_with_weapon_s': ['sum'],
'forcible_sex_offenses_without_weapon_s': ['sum']}

def group_county(df):

    df = df.groupby(["county"]).agg(agg_function_sum)
    df.reset_index(inplace=True)
    return df.T.to_dict().values()

def group_type(df):
    df = df.groupby(["school_type"]).agg(agg_function_sum)

    df.reset_index(inplace=True)
    return df.T.to_dict().values()

def transform(data):
    school_data_set = []
    sex_crimes = []

    for datum in data: #sex crimes
        county = datum["county"]
        school_name = datum["school_name"]
        forcible_sex_offenses_with_weapon_s = int(datum["forcible_sex_offenses_with_weapon_s"])
        other_sex_offenses_without_weapon_s = int(datum["other_sex_offenses_without_weapon_s"])
        other_sex_offenses_with_weapon_s = int(datum["other_sex_offenses_with_weapon_s"])
        forcible_sex_offenses_without_weapon_s = int(datum["forcible_sex_offenses_without_weapon_s"])
        school_type = datum["school_type"]
        school_datum = {
            "county": county,
            "school_name" : school_name,
            "forcible_sex_offenses_with_weapon_s": forcible_sex_offenses_with_weapon_s,
            "other_sex_offenses_without_weapon_s": other_sex_offenses_without_weapon_s,
            "other_sex_offenses_with_weapon_s": other_sex_offenses_with_weapon_s,
            "forcible_sex_offenses_without_weapon_s": forcible_sex_offenses_without_weapon_s,
            "school_type": school_type,
        }
        sex_crimes.append(school_datum)



    sex_crimes_df = pd.DataFrame.from_dict(sex_crimes)
    return sex_crimes_df

data = extract()
data_points = transform(data)
by_county = group_county(data_points)
pprint(by_county)

x=['forcible sex\noffenses\nwith weapons', 'forcible sex\noffenses\nwithout weapons', 'other sex\noffenses\nwith weapons', 'other sex\noffenses\nwithout weapons']
values=[0, 0, 0, 2]
y_pos = np.arange(len(x))

plt.title('Nassau Sex Offenses in Public Schools 2014-2015')
plt.xlabel('Count')
plt.ylabel('Type')

plt.barh(y_pos, values)
plt.yticks(y_pos, x)
plt.show()
