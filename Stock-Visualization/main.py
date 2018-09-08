from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt


ts = TimeSeries(key='LH3WNUH2LPYLE6R9', output_format='pandas')

data, meta_data = ts.get_intraday(symbol='TSLA',interval='1min', outputsize='full')
data['4. close'].plot()
plt.title('Intraday Times Series for the MSFT stock (1 min)')
plt.show()