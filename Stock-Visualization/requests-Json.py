import requests
import pandas as pd
from pandas.io.json import json_normalize

url = 'https://www.alphavantage.co/query'

params = dict(
    function='TIME_SERIES_INTRADAY',
    symbol='TSLA',
    interval='1min',
    apikey='LH3WNUH2LPYLE6R9',
)

def getData():

    resp = requests.get(url, params)

    data = resp.json()

    return data


json_str = getData()

df = pd.DataFrame.from_dict(json_normalize(json_str), orient='columns')
print(df)

