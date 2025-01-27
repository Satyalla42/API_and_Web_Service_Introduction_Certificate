import tweepy
ak = "000"

aks = "000"


at = '000'

ats = '000'

def OAuth():
    try:
        auth = tweepy.OAuthHandler(ak, aks)
        auth.set_access_token(at, ats)
        return auth
    except Exception as e:
        return None
 
Oauth = OAuth()
apicall = tweepy.API(Oauth)

apicall.update_status('Here is a sample sweet from the API call program.')
print('Tweet created')