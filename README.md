# StockDataResampler

### Overview:
Stock Data Resampler is a **Python** program that resamples an instruments minute by minute candle stick data (opening, closing price, ) to whatever interval you want, creating new candlesticks for those intervals using the prior data. It recieves a stocks data using the **Alpha Vantage API**, and resamples data using the **Pandas** and **Numpy** packages for Python.

### Features:
* Free and efficient pulling of stock data from **Alpha Vantage**, which is then outputted to a CSV file
* Ability to specify from thousands of stocks to gather data from
* Resampling of data to whatever time interval you want using **Pandas**
* Correctly sorted candle sticks using **Numpy** showing proper closing, opening, high, low, and volume values

### Demo:
**Minute by minute data resampled to 3 minute candle sticks**
![d1](https://user-images.githubusercontent.com/66835262/92043675-7c7ab200-ed4a-11ea-98af-79d5ea7dd8af.png)
![d2](https://user-images.githubusercontent.com/66835262/92043721-97e5bd00-ed4a-11ea-93d3-77ef8fd044aa.png)

### Packages used:
* **Pandas:** https://github.com/pandas-dev/pandas
* **Alpha Vantage API:** https://github.com/RomelTorres/alpha_vantage
* **Numpy:** https://github.com/numpy/numpy
