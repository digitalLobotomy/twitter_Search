"""
Created on Sun Apr 30 09:44:40 2017

@author: Kevin McGrath
Purpose: Search twitter using TwitterSearch for given search term(s)
"""

from TwitterSearch import *

searchTerms = ['[search terms]']
tso = TwitterSearchOrder()
tso.set_keywords(searchTerms)
tso.set_language('en')
tso.set_include_entities(False)

userTweets = {}


ts = TwitterSearch(consumer_key = '[your consumer key]',\
                 consumer_secret = '[your consumer secret]',\
                 access_token = '[access token]',\
                 access_token_secret = '[access token secret]'\
        )

outfile = open('tweetfile.txt', 'w')
outfile.write('User\t\t\Tweets')
outfile.write('\n.........................................................')

for tweet in  ts.search_tweets_iterable(tso):
    username = tweet['user']['name'] + '(@' + tweet['user']['screen_name'] + ')'
    if username in userTweets.keys():
        tweetlist = userTweets[username]
        tweetlist.append(tweet['text'].encode('utf8'))
        userTweets[username] = tweetlist
    else:
        userTweets[username] = [tweet['text'].encode('utf8')]

for usrNm, tweets in userTweets.iteritems():
    for tweet in tweets:
        outfile.write("\n" + usrNm.encode('utf8') + "\t\t" + tweet + "\n")

outfile.close()

