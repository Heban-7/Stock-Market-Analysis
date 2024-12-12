import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from nltk.sentiment import SentimentIntensityAnalyzer
from wordcloud import WordCloud
import nltk

# Load Data
def load_data(filepath):
    df = pd.read_cv(filepath)
    return df

def info(data):
    df = data.info()
    return df

