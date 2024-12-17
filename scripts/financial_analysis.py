import talib as ta
import pandas as pd
import plotly.express as px


class FinancialAnalyzer:
    def __init__(self, ticker, start_date, end_date, data_dir):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        self.data_dir = data_dir

    def retrieve_stock_data(self):
        """
        Load stock data from local CSV file instead of downloading.
        """
        file_path = f"{self.data_dir}/{self.ticker}.csv"
        data = pd.read_csv(file_path, index_col='Date', parse_dates=True)
        data = data.loc[self.start_date:self.end_date]
        data.dropna(inplace=True)
        return data

    def calculate_moving_average(self, data, window_size):
        return ta.SMA(data, timeperiod=window_size)

    def calculate_technical_indicators(self, data):
        """
        Calculate various technical indicators such as SMA, EMA, RSI, MACD, and Bollinger Bands.
        """
        data['SMA'] = self.calculate_moving_average(data['Close'], 20)
        data['RSI'] = ta.RSI(data['Close'], timeperiod=14)
        data['EMA'] = ta.EMA(data['Close'], timeperiod=20)
        
        macd, macd_signal, _ = ta.MACD(data['Close'])
        data['MACD'] = macd
        data['MACD_Signal'] = macd_signal
        
        # Bollinger Bands
        upperband, middleband, lowerband = ta.BBANDS(data['Close'], timeperiod=20)
        data['Upper_BB'] = upperband
        data['Lower_BB'] = lowerband

        return data

    def visualize_data(self, data):
        """
        Generate visualizations to explore stock data and indicators.
        """
        # Close Price and Moving Average
        fig = px.line(data, x=data.index, y=['Close', 'SMA'], title='Stock Price with Simple Moving Average')
        fig.show()

        # RSI Visualization
        fig = px.line(data, x=data.index, y='RSI', title='Relative Strength Index (RSI)')
        fig.show()

        # EMA Visualization
        fig = px.line(data, x=data.index, y=['Close', 'EMA'], title='Stock Price with Exponential Moving Average')
        fig.show()

        # MACD Visualization
        fig = px.line(data, x=data.index, y=['MACD', 'MACD_Signal'], title='MACD and Signal Line')
        fig.show()

        # Bollinger Bands
        fig = px.line(data, x=data.index, y=['Close', 'Upper_BB', 'Lower_BB'], 
                      title='Bollinger Bands with Stock Price')
        fig.show()

    def calculate_portfolio_weights(self, tickers, data_path):
        """
        Optimize portfolio weights using PyPortfolioOpt with local data.
        """
        all_data = {}
        for ticker in tickers:
            file_path = f"{data_path}/{ticker}.csv"
            stock_data = pd.read_csv(file_path, parse_dates=['Date'], index_col='Date')
            all_data[ticker] = stock_data['Close']

        # Combine close prices into a single DataFrame
        data = pd.DataFrame(all_data)

        # Portfolio Optimization
        mu = expected_returns.mean_historical_return(data)
        cov = risk_models.sample_cov(data)
        ef = EfficientFrontier(mu, cov)
        weights = ef.max_sharpe()
        return ef.clean_weights(), ef.portfolio_performance()
    

