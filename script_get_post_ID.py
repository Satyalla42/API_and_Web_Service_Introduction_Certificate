from enum import auto
import tweepy
ak = "000"

aks = "000"


at = '000'

ats = '000'

Oauth = OAuth()
apicall = tweepy.API(Oauth)

# Get recent tweets from your timeline
tweets = api.user_timeline(count=5)  # Fetch the 5 most recent tweets
for tweet in tweets:
    print(f"Tweet ID: {tweet.id} - Text: {tweet.text}")