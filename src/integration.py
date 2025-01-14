import pandas as pd

states = ['ILLINOIS', 'INDIANA', 'IOWA', 'MINNESOTA', 'MISSOURI', 'NEBRASKA']

yield_raw = pd.read_csv('data/raw/yield_raw.csv')
price_received_raw = pd.read_csv('data/raw/price_received_raw.csv')
weather_raw = pd.read_csv('data/raw/weather_raw.csv')

yield_raw = yield_raw[(yield_raw['state_name'].isin(states)) & (yield_raw['reference_period_desc'] == 'YEAR')]\
    .drop_duplicates(subset=['year', 'state_name', 'util_practice_desc'])

yield_raw = yield_raw.pivot(
    index=['year', 'state_name'],
    columns='util_practice_desc',
    values='Value'
).reset_index()

price_received_raw = price_received_raw.pivot(
    index=['year', 'state_name'],
    columns='reference_period_desc',
    values='Value'
).reset_index()

weather_raw = weather_raw.rename(columns={'Date':'year', 'state':'state_name'})

temp = yield_raw.merge(price_received_raw, on=['year', 'state_name'], how='outer')

integrated = temp.merge(
    weather_raw,
    on=['year', 'state_name'],
    how='outer'
)

for x in integrated.columns:
    integrated.rename(columns={x:x.lower()}, inplace=True)

integrated.to_csv('data/raw/integrated.csv', index=False)