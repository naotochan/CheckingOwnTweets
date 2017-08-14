# coding : utf-8
# python3.6.2
# 1分以内のツイートからエアコンを制御する

import TwitterAPI
# import json
import tweepy
import csv
import datetime
import re

CK = TwitterAPI.CK
CS = TwitterAPI.CS
AT = TwitterAPI.AT
ATS = TwitterAPI.ATS

auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, ATS)
api = tweepy.API(auth)

tweet_data = []

# cronで1分ごとに1分以内のツイートツイート取得
for tweet in tweepy.Cursor(api.user_timeline,screen_name = "ChanmansCompany",exclude_replies = None).items():
    # 1分以内のツイートだけ取得
    print (tweet.created_at)
    tweetTime = datetime.datetime.strptime(tweet.created_at, '%Y/%m/%d %H:%M:%S')
    tweetTime += datetime.datetime.timedelta(mins = 1)
    now = datetime.datetime.now()

    if tweetTime > now:
        tweet_data.append(tweet.text.replace('\n',''))

for x in tweet:
    print (x)

# 取得したツイートを正規表現でチェック
# signal = TRUE
#
# for data in tweet_data:
#     patternOn = regex.compile("eakon on!")
#     compileOn = patternOn.compile(data)
#     if compileOn.find():
#         signal = TRUE
#
#     patternOff = regex.compile("eakon off!")
#     compileOff = patternOff.compile(data)
#     if compileOff.find():
#         signal = FALSE
#
# # signalでonかoffのすくスクリプト実行
# if signal = TRUE:
#     print ("-*-*- Putting On My Home AirConditioner... -*-*-")
# else:
#     print ("-*-*- Putting Off My Home AirConditioner... -*-*-")

#csv出力
with open('OwnTimeline.csv', 'w',newline='',encoding='utf-8') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(["id","created_at","text","fav","RT"])
    writer.writerows(tweet_data)
pass
# api.update_status(status='Test tweet via tweepy')
