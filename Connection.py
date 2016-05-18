import tweepy

from bottle import route, run

@route('/hello')
def hello():
 consumer_key = "your consumer key here"
 consumer_secret = "your consumer secret here"
 access_token = "your access token here"
 access_token_secret = "your access token secret here"

 auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
 auth.set_access_token(access_token, access_token_secret)

 api = tweepy.API(auth)

 public_tweets = api.home_timeline()
 my_tweets = api.user_timeline()
 #for tweet in my_tweets:
 #    print(tweet.text)

 #for tweet in public_tweets:
 #    print(tweet.text)

 return public_tweets[0].text

run(host='localhost', port=8088, debug=True)

