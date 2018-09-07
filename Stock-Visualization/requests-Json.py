import requests

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
    print(data)

