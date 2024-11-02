
import tweepy
import os
from datetime import date, timedelta
from json import dumps

# Set up Twitter API credentials from environment variables
consumer_key = os.environ['TWITTER_API_KEY']
consumer_secret = os.environ['TWITTER_API_SECRET_KEY']
access_token = os.environ['TWITTER_ACCESS_TOKEN']
access_token_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']

# Authenticate using the Tweepy Client for v2 API
client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

# Set target date and calculate days remaining
target_date = date(2024, 11, 27)
today = date.today()
days_remaining = (target_date - today).days  # Countdown days

# Format countdown text for tweet
countdown_text = f"Only {days_remaining} days left until September 27, 2024! 🎉"

# Create tweet with the countdown text
response = client.create_tweet(text=countdown_text)

# Print response for confirmation (optional)
print("Tweet sent:", countdown_text)
print("Response:", response)
