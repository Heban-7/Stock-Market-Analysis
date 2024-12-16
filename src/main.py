def main():
    tickers = ['AAPL', 'AMZN', 'GOOG', 'MSFT', 'META', 'NVDA', 'TSLA']
    start_date = '2015-01-01'
    end_date = '2023-12-31'
    data_dir = 'path/to/your/data'  # Adjust this to the path where your CSV files are stored

    # Instantiate Analyzer
    analyzer = FinancialAnalyzer(ticker='AAPL', start_date=start_date, end_date=end_date, data_dir=data_dir)

    # Retrieve and prepare data
    stock_data = analyzer.retrieve_stock_data()

    # Calculate technical indicators
    stock_data = analyzer.calculate_technical_indicators(stock_data)

    # Visualize data
    analyzer.visualize_data(stock_data)

    # Portfolio Analysis
    portfolio_weights = analyzer.calculate_portfolio_weights(tickers, start_date, end_date)
    portfolio_perf = analyzer.calculate_portfolio_performance(tickers, start_date, end_date)

    print("Optimized Portfolio Weights:", portfolio_weights)
    print("Portfolio Performance (Return, Volatility, Sharpe Ratio):", portfolio_perf)

if __name__ == "__main__":
    main()