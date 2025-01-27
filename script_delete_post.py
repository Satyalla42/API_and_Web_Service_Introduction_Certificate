import tweepy

consumer_key = '000'
consumer_secret = '000'
access_token = '000'
access_token_secret = '000'

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