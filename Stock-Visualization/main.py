from alpha_vantage.timeseries import TimeSeries


ts = TimeSeries(key='LH3WNUH2LPYLE6R9', output_format='pandas')

data, meta_data = ts.get_intraday(symbol='TSLA',interval='1min', outputsize='compact')
print(data.head())
