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

# cronで1分ごとに直近10ツイート取得
tweet_data = api.user_timeline(count = MAX_COUNT)

#内容確認
for tweet in tweet_data:
    print (str(tweet.created_at) + tweet.text)

# 取得したツイートを正規表現でチェック
signal = 0
signalFlag = False

onPattern = "eakon on!"
offPattern = "eakon off!"

now = datetime.date.today()
now -= datetime.timedelta(minutes = 60)
print ("now : " + str(now))

for tweet in tweet_data:
    if tweet.created_at > now():
        if signalFlag == False:
            onMatchOb = re.search(tweet.text, onPattern)

            if onMatchOb:
                signal = 1
                signalFlag = True

            offMatchOb = re.search(tweet.text, offPattern)
            if offMatchOb:
                signal = -1
                signalFlag = True
    else:
        print ("nothing tweet in recently")

# signalでonかoffのすくスクリプト実行
if signal == 1:
    print ("-*-*- Putting On My Home AirConditioner... -*-*-")
elif signal == -1:
    print ("-*-*- Putting Off My Home AirConditioner... -*-*-")
else :
    print ("-*-*- do nothing -*-*-")
