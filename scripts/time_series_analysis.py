import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def article_publication_time_anaysis(data):
    # Convert date to datetime
    data['date'] = pd.to_datetime(data['date'], errors='coerce', utc=True)

    # Extract time-based features
    data['hour'] = data['date'].dt.hour
    data['day'] = data['date'].dt.day
    data['weekday'] = data['date'].dt.day_name()
    data['month'] = data['date'].dt.month
    data['year'] = data['date'].dt.year

    # Grouping by time intervals
    daily_publication = data.groupby(data['date'].dt.date).size()
    hourly_publication = data.groupby(data['hour']).size()

    print("Daily Article Publication Trend")

    # Overall Trend: Daily publication count
    plt.figure(figsize=(12, 6))
    daily_publication.plot(title="Daily Article Publication Trend", color='blue')
    plt.xlabel('Date', fontsize=14)
    plt.ylabel('Number of Articles', fontsize=14)
    plt.grid()
    plt.tight_layout()
    plt.show()

    print("Hourly Article Distribution")

    # Hourly Distribution: When are most articles published?
    plt.figure(figsize=(12, 6))
    sns.barplot(x=hourly_publication.index, y=hourly_publication.values, palette="viridis")
    plt.title('Hourly Article Distribution', fontsize=16)
    plt.xlabel('Hour of the Day', fontsize=14)
    plt.ylabel('Number of Articles', fontsize=14)
    plt.grid()
    plt.tight_layout()
    plt.show()

    print("Weekly Article Distribution")

    # Weekly Patterns: Day of the week
    weekly_publication = data.groupby('weekday').size()
    plt.figure(figsize=(12, 6))
    sns.barplot(x=weekly_publication.index, y=weekly_publication.values, order=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], palette="coolwarm")
    plt.title('Weekly Article Distribution', fontsize=16)
    plt.xlabel('Day of the Week', fontsize=14)
    plt.ylabel('Number of Articles', fontsize=14)
    plt.grid()
    plt.tight_layout()
    plt.show()
