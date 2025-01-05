import requests
import urllib.parse
import pandas as pd
from io import StringIO

print('\nLoading...\n')
with open('keys/api_key.txt', 'r') as file:
    usda_nass_key = file.read()

states = ['ILLINOIS', 'INDIANA', 'IOWA', 'MINNESOTA', 'MISSOURI', 'NEBRASKA']
parameters = {
    'key': usda_nass_key,
    'source_desc': 'SURVEY',
    'sector_desc': 'CROPS',
    'group_desc': 'FIELD CROPS',
    'commodity_desc': 'CORN',
    'statisticcat_desc': 'YIELD',
    'agg_level_desc': 'STATE',
    'format': 'csv'
}

encoded_parameters = urllib.parse.urlencode(parameters)
base_url = 'https://quickstats.nass.usda.gov/api/api_GET/'
query = base_url+'?'+encoded_parameters
response = requests.get(query)

if response.status_code == 200:
    data = StringIO(response.text)
    yield_raw = pd.read_csv(data)
    yield_raw = yield_raw[['year', 'util_practice_desc', 'state_name', 'reference_period_desc', 'Value']]
    yield_raw = yield_raw[yield_raw['reference_period_desc'] == 'YEAR']
    yield_raw.to_csv('data/raw/yield_raw.csv', index=False)
    print('Data saved as yield_raw.csv')
else:
    print(f'Request failed with status code {response.status_code}')

print('\nLoading...\n')
for i, state in enumerate(states):
    parameters = {
        'key': usda_nass_key,
        'source_desc': 'SURVEY',
        'sector_desc': 'CROPS',
        'group_desc': 'FIELD CROPS',
        'commodity_desc': 'CORN',
        'statisticcat_desc': 'PRICE RECEIVED',
        'agg_level_desc': 'STATE',
        'state_name':state,
        'format': 'csv'
    }
    encoded_parameters = urllib.parse.urlencode(parameters)
    base_url = 'https://quickstats.nass.usda.gov/api/api_GET/'
    query = base_url+'?'+encoded_parameters
    response = requests.get(query)
    if response.status_code == 200:
        if i == 0:
            data = StringIO(response.text)
            price_received_raw = pd.read_csv(data)
            price_received_raw = price_received_raw[['year', 'state_name', 'reference_period_desc', 'Value']]
        else:
            data = StringIO(response.text)
            temp_df = pd.read_csv(data)
            temp_df = temp_df[['year', 'state_name', 'reference_period_desc', 'Value']]
            price_received_raw = pd.concat([price_received_raw, temp_df])
    else:
        print(f'Request failed for {state} with status code {response.status_code}')

price_received_raw.to_csv('data/raw/price_received_raw.csv', index=False)
print('Data saved as price_received_raw.csv')

print('\nLoading...\n')
months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'semptember', 'october', 'november', 'december']
state_numbers = [11, 12, 13, 21, 23, 25]
count1 = 0
count2 = 0

for state_number in state_numbers:
    for variable in ['tavg', 'tmax', 'tmin', 'pcp', 'pdsi']:
        for month_number in range(4, 12):
            skiprows = 3 if variable == 'pdsi' else 4
            link = f'https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/statewide/time-series/{state_number}/{variable}/12/{month_number}/1895-2024.csv?base_prd=true&begbaseyear=1895&endbaseyear=2000'
            if count1 == 0:
                state_weather = pd.read_csv(link, skiprows=skiprows)
                state_weather.drop(
                    columns=state_weather.columns[2:],
                    inplace=True
                )
                state_weather.rename(
                    columns={state_weather.columns[1]:f'{months[month_number]}_{variable}'},
                    inplace=True
                )
                state_weather['Date'] = state_weather['Date'].apply(lambda x: int(str(x)[:4]))
                count1 += 1
            else:
                temp = pd.read_csv(link, skiprows=skiprows)
                temp.drop(
                    columns=temp.columns[2:],
                    inplace=True
                )
                temp.rename(
                    columns={temp.columns[1]:f'{months[month_number]}_{variable}'},
                    inplace=True
                )
                temp['Date'] = temp['Date'].apply(lambda x: int(str(x)[:4]))
                state_weather = state_weather.merge(
                    temp,
                    on='Date',
                    how='outer'
                )
                count1 += 1
    state_weather['state'] = states[state_numbers.index(state_number)]
    if count2 == 0:
        weather_raw = state_weather.copy()
        count2 += 1
        count1 = 0
    else:
        weather_raw = pd.concat([weather_raw, weather_raw])
        count2 += 1
        count1 = 0

weather_raw.to_csv('data/raw/weather_raw.csv', index=False)
print('Data saved as weather_raw.csv')