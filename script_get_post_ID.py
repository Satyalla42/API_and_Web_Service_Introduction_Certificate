from enum import auto
import tweepy
ak = "rKWYccMhW70w6XGIBWeyJJVeA"

aks = "gxumWlK2UoKUNeVRXrefpLN8TLBPHS4Z2wpw6fUBrRv5cpD6jq"


at = '1883243213915602944-D03o5F1gLIjiZFkHpjUpliL74q30lG'

ats = 'fHjX8lM0CZ4x3leXrO15ttavyIzxG8WNBENtjJ9nReqyK'

Oauth = OAuth()
apicall = tweepy.API(Oauth)

# Get recent tweets from your timeline
tweets = api.user_timeline(count=5)  # Fetch the 5 most recent tweets
for tweet in tweets:
    print(f"Tweet ID: {tweet.id} - Text: {tweet.text}")