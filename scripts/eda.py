import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def data_summary(data):
    print("Head of Stock market data")
    print(data.head())

    print("\n\nShape of the Data")
    print(data.shape)

    print("\n\nData Information")
    print(data.info())

    print("\n\nData Discription")
    print(data.describe())

    print("\n\nMissing value in Data")
    print(data.isnull().sum())

def summary_statistics(data, column_names):
    """
    Generate summary statistics and distribution plots for selected columns.
    """
    print(data[column_names].describe())
    sns.histplot(data[column_names], kde=True, palette="viridis")
    plt.title(f"Distribution of {column_names}")
    plt.show()

def value_count(data, column_name):
    # Count every unique value in a given column of data
    count = data[column_name].value_counts()
    print("Top 10 ", column_name)
    print(count.head())

    # Visualize top 10 publisher
    top = count.head(10)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top.values, y=top.index, palette="viridis")
    plt.title("Top 10 ", column_name)
    plt.xlabel("Frequency")
    plt.ylabel(column_name)
    plt.tight_layout()
    plt.show()




