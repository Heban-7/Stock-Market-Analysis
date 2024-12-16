import seaborn as sns
import matplotlib.pyplot as plt

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer 
from wordcloud import WordCloud
nltk.download('vader_lexicon')

def sentiment_data_visualization(sentimental_data):
    # Plot sentiment distribution
    plt.figure(figsize=(8, 6))
    sns.countplot(data=sentimental_data, x='sentiment_category', palette='coolwarm')
    plt.title("Sentiment Distribution")
    plt.xlabel("Sentiment")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()


# Generate Word Cloud
def generate_wordcloud(df):
    """Generates a word cloud for the headlines."""
    text = ' '.join(df['headline'].dropna())
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title("Word Cloud of Headlines")
    plt.show()
