import tweepy
import requests

# Replace these with your own API keys
consumer_key = 'XXXXXXXXXXXXXXXXXXXXXXXXX'
consumer_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
access_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
access_token_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

# Set up the API client
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Get a random joke from the API
response = requests.get(
    'https://geek-jokes.sameerkumar.website/api?format=json')
joke = response.json()['joke']

# Post the joke to Twitter
api.update_status(joke)

print("Tweeted: " + joke)
