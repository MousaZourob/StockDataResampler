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
![d1](https://user-images.githubusercontent.com/66835262/92043460-0fffb300-ed4a-11ea-9a87-a4c523a119b8.png)
![d2](https://user-images.githubusercontent.com/66835262/92043481-1beb7500-ed4a-11ea-8d66-a477d3f00710.png)


### Packages used:
* **Pandas:** https://github.com/pandas-dev/pandas
* **Alpha Vantage API:** https://github.com/RomelTorres/alpha_vantage
* **Numpy:** https://github.com/numpy/numpy
