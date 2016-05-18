import tweepy

from bottle import route, run

api = None

@route('/auth/<ckey>/<csecret>/<atoken>/<atokensecret>')
def authentication():
 consumer_key = ckey
 consumer_secret = csecret
 access_token = atoken
 access_token_secret = atokensecret

 auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
 auth.set_access_token(access_token, access_token_secret)

 api = tweepy.API(auth)
 mytweets = my_tweets()
 myfirsttweet = my_first_tweet()
 print("Tweet One: {myfirsttweet}")
 print("All Tweets: {mytweets}")


def my_tweets():  
 my_tweets = api.user_timeline()

 return my_tweets


def my_first_tweet():
 my_tweets = api.user_timeline()

 return my_tweets[0].text

def my_public_tweets():
 public_tweets = api.home_timeline()

 return public_tweets

def my_first_public_tweet():
 public_tweets = api.home_timeline()

 return public_tweets[0].text

run(host='localhost', port=8088, debug=True)

