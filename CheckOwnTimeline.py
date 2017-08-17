# coding : utf-8
# python3.6.2
# 直近の10ツイートからエアコンを制御

import TwitterAPI
import tweepy
import datetime
import re

MAX_COUNT = 10

CK = TwitterAPI.CK
CS = TwitterAPI.CS
AT = TwitterAPI.AT
ATS = TwitterAPI.ATS

auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, ATS)
api = tweepy.API(auth)

# cronで1分ごとに直近20ツイート取得
tweet_data = api.user_timeline(count = MAX_COUNT)

#内容確認
for tweet in tweet_data:
    print (str(tweet.created_at) + tweet.text)


# 取得したツイートを正規表現でチェック
signal = True
signalFlag = False

onPattern = "eakon on!"
offPattern = "eakon off!"


for data in tweet_data:
    if signalFlag == False:
        onMatchOb = re.search(data, onPattern)

        if onMatchOb:
            signal = True
            signalFlag = True

        offMatchOb = re.search(data, offPattern)
        if offMatchOb:
            signal = False
            signalFlag = True

# signalでonかoffのすくスクリプト実行
if signal:
    print ("-*-*- Putting On My Home AirConditioner... -*-*-")
else:
    print ("-*-*- Putting Off My Home AirConditioner... -*-*-")
