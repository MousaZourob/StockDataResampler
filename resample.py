# Download the alpha-vantage API (pip install alpha-vantage), pandas (pip install pandas), and numpy (pip install numpy) packages
from alpha_vantage.timeseries import TimeSeries
import time, os
import pandas as pd
import numpy as np

# Get your alpha vantage API key from Alpha Vantage website then click get free API key
api_key = 'YOUR API KEY'

# Change to whatever ticker you want
ticker = "MSFT"

ts = TimeSeries(key=api_key, output_format="pandas")
data, meta_data = ts.get_intraday(symbol=ticker, interval="1min", outputsize='full')
print(data)

# Stores data in csv
data.to_csv("output.csv")

# Changes csv format
df = pd.read_csv("output.csv", parse_dates=["date"], index_col="date")

# Resamples data, changes interval specified to whatever time period you want (for example, 3 minutes is 3T, 30 seconds is 30S, 1 hour is 1H)
# Gaps in data are due to Alpha Vantage API missing some values
resample_interval = "3T"

# Resamples data
df = df.resample(resample_interval).agg({'1. open': 'first', '2. high': np.max, '3. low': np.min, '4. close': 'last', '5. volume': np.sum}).dropna(how='any')

# Stores data in csv
df.to_csv("resampled.csv")
