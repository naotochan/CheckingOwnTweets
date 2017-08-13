# coding : utf-8
# python3.6.2

import TwitterAPI
import json
import tweepy

CK = TwitterAPI.CK
CS = TwitterAPI.CS
AT = TwitterAPI.AT
ATS = TwitterAPI.ATS

auth = tweepy.OAuthHandler(CA, CS)
auth.set_access_token(AT, ATS)

api = tweepy.API(auth)

print (api.me().name)

api.update_status(status='Test tweet via tweepy')
