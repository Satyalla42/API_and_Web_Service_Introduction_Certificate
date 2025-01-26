import tweepy

consumer_key = 'rKWYccMhW70w6XGIBWeyJJVeA'
consumer_secret = 'gxumWlK2UoKUNeVRXrefpLN8TLBPHS4Z2wpw6fUBrRv5cpD6jq'
access_token = '1883243213915602944-D03o5F1gLIjiZFkHpjUpliL74q30lG'
access_token_secret = 'fHjX8lM0CZ4x3leXrO15ttavyIzxG8WNBENtjJ9nReqyK'

auth = tweepy.OAuth1UserHandler(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

api = tweepy.API(auth)

tweet_id = "1883640665588015432"

try:
    api.destroy_status(tweet_id)
    print(f"Tweet {tweet_id} has been deleted.")
except tweepy.TweepyException as e:
    print(f"Failed to delete tweet: {e}")