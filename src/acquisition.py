import requests
import urllib.parse
import pandas as pd
from io import StringIO

print('\nLoading...\n')
with open('keys/api_key.txt', 'r') as file:
    usda_nass_key = file.read()
print('Access key loaded.')

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

months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
state_numbers = [11, 12, 13, 21, 23, 25]

years = list(range(1895, 2025))*6
years.sort()
list_temp = list(range(0, 6))*130
df_empty = pd.DataFrame({'year':years, 'state':list_temp})
df_empty['state'] = df_empty['state'].replace({i: states[i] for i in range(len(states))})

weather_raw = df_empty.copy()

for s, state_number in enumerate(state_numbers):
    for variable in ['tavg', 'tmax', 'tmin', 'pcp', 'pdsi']:
        for m, month in enumerate(months):

            state = states[s]

            skiprows = 3 if variable == 'pdsi' else 4

            link = f'https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/statewide/time-series/{state_number}/{variable}/12/{m+1}/1895-2024.csv?base_prd=true&begbaseyear=1895&endbaseyear=2000'

            temp = pd.read_csv(link, skiprows=skiprows)

            temp['Date'] = temp['Date'].apply(lambda x: int(str(x)[:4]))

            temp.rename(columns={'Date':'year'}, inplace=True)

            temp.rename(columns={'Value':f'{month}_{variable}'}, inplace=True)

            weather_raw.loc[weather_raw['state'] == state, f'{month}_{variable}'] = weather_raw.loc[weather_raw['state'] == state, 'year'].map(temp.set_index('year')[f'{month}_{variable}'])

weather_raw.to_csv('data/raw/weather_raw.csv', index=False)
print('Data saved as weather_raw.csv')