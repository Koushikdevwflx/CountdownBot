import tweepy
import os
from datetime import date, timedelta
from json import dumps

# Print statements for debugging
print("TWITTER_API_KEY:", os.environ.get("TWITTER_API_KEY"))
print("TWITTER_API_SECRET_KEY:", os.environ.get("TWITTER_API_SECRET_KEY"))
print("TWITTER_ACCESS_TOKEN:", os.environ.get("TWITTER_ACCESS_TOKEN"))
print("TWITTER_ACCESS_TOKEN_SECRET:", os.environ.get("TWITTER_ACCESS_TOKEN_SECRET"))

# Initialize Twitter client
consumer_key = os.environ['TWITTER_API_KEY']
consumer_secret = os.environ['TWITTER_API_SECRET_KEY']
access_token = os.environ['TWITTER_ACCESS_TOKEN']
access_token_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']
client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

# Calculate countdown
days = date(2024, 11, 27) - date.today() - timedelta(days=1)
cd = dumps(days.days, default=str)
print("Days countdown:", cd)  # Debug print statement

# Create tweet
response = client.create_tweet(text=cd)
print("Tweet response:", response)  # Debug print statement
