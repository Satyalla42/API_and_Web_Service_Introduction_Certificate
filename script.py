import tweepy
ak = "rKWYccMhW70w6XGIBWeyJJVeA"

aks = "gxumWlK2UoKUNeVRXrefpLN8TLBPHS4Z2wpw6fUBrRv5cpD6jq"


at = '1883243213915602944-D03o5F1gLIjiZFkHpjUpliL74q30lG'

ats = 'fHjX8lM0CZ4x3leXrO15ttavyIzxG8WNBENtjJ9nReqyK'

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