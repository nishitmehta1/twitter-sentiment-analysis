import tweepy
from textblob import TextBlob

import sys
import csv

if len(sys.argv) >= 2:
    topic = sys.argv[1]
else:
    print("By default topic is Trump.")
    topic = "Trump"

consumer_key = 'tVkD4eg1gcMNyRQTcnB2rtC0z'
consumer_secret = 'rdUvDluqCXfXwf3u50I0PRXDEjxamFtQ9qjsSWaAEQfRzrezd7'

access_token = '923922799919616000-yhpVboR412PZep2o2pN3T2GInlLSOOa'
access_token_secret = 'oF8sibIMzgN0IHLHGALzhQISrqcnOenpiFndYgALM2Eqy'

authenticate = tweepy.OAuthHandler(consumer_key, consumer_secret)
authenticate.set_access_token(access_token, access_token_secret)

api = tweepy.API(authenticate)

tweets = api.search('Trump')

with open('sentiment.csv', 'w', newline='\n') as  f:
    writer = csv.DictWriter(f, fieldnames=['Tweet', 'Sentiment'])
    writer.writeheader()
    for tweet in tweets:
        text = tweet.text
        # Cleaning tweet
        cleanedtext = ' '.join( [word for word in text.split(' ') if len(word) > 0 and word[0] != '@' and word[0] != '.' and word[0] != '#' and 'http' not in word and word != 'RT'] )

        analysis = TextBlob(cleanedtext)

        sentiment = analysis.sentiment.polarity
        if sentiment >= 0:
            polarity = 'Positive'
        else:
            polarity = 'Negative'

        # print(cleanedtext, polarity)

        writer.writerow({'Tweet': text, 'Sentiment': polarity})