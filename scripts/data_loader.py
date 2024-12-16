import pandas as pd

def load_stock_news(filepath):
    # Import Stock News data from the filepath directory 
    df = pd.read_csv(filepath)
    return df

def load_stock_data(filepath):
    # Import Stock data from the filepath directory 
    df = pd.read_csv(filepath)
    return df

 