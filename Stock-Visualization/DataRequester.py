import requests

SYMBOLS_URL = "https://api.iextrading.com/1.0/ref-data/symbols"

class DataRequester:
    def __init__(self):
        pass

    def getSymbols(self):
        response = requests.get(SYMBOLS_URL)
        data_list = response.json()

        return [data['symbol'] for data in data_list]

