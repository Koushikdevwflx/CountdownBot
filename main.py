import tweepy
import os
from datetime import date, timedelta
from json import dumps

# Load Twitter API credentials from environment variables
consumer_key = os.environ['TWITTER_API_KEY']
consumer_secret = os.environ['TWITTER_API_SECRET_KEY']
access_token = os.environ['TWITTER_ACCESS_TOKEN']
access_token_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']

# Authenticate with Twitter
client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

# Calculate the countdown in days
target_date = date(2024, 11, 4)
days_left = (target_date - date.today()).days

# Convert to JSON format to include in the tweet text
countdown_text = f"Days until September 27, 2024: {days_left} days!"
response = client.create_tweet(text=countdown_text)

print(f"Tweet sent: {countdown_text}")
