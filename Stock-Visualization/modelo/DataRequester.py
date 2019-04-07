import requests
import json
from vista.vista import Vista

SYMBOLS_URL = "https://api.iextrading.com/1.0/ref-data/symbols"
GENERAL_URL = "https://api.iextrading.com/1.0"

class DataRequester:
    def __init__(self):
        pass

    def getSymbols(self):
        response = requests.get(SYMBOLS_URL)
        data_list = response.json()

        return [data['symbol']  for data in data_list]

    def getSymbolInfo(self, symbol, range):
        data_request = "/stock/" + symbol + "/chart/" + range
        data_url = GENERAL_URL + data_request

        response = requests.get(data_url)
        data = response.json()

        return data

    def existSymbol(self, symbol):
        symbols = self.getSymbols()

        if symbol in symbols:
            return True
        else:
            return False

    def check_if_exists_symbol(self, symbol):
        if not self.existSymbol(symbol):
            return False
        else:
            return True