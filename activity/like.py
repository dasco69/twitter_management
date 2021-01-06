import api.auth
import tweepy
import time

user = api.auth.api.me()
#search = 'Javascript'
#nrTweets = 500


def like(search,nrTweets): 
    for tweet in tweepy.Cursor(api.auth.api.search, search).items(nrTweets):
        try:
            print('Tweet liked')
            tweet.favorite()
            time.sleep(20)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break