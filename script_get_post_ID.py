from enum import auto
import tweepy
ak = "000"

aks = "000"


at = '000'

ats = '000'

Oauth = OAuth()
apicall = tweepy.API(Oauth)


tweets = api.user_timeline(count=5) 
for tweet in tweets:
    print(f"Tweet ID: {tweet.id} - Text: {tweet.text}")