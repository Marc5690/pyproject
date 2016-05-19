import tweepy

from recommender import Recommender

from bottle import route, run, template

#Use the following url to use my (Marc's) details to login with all the keys/tokens and get back my first tweet:
#localhost:8088/auth/oj8A0mh2hMMLZBAYr9hrsyGXK/vEbApM5duqpSj3fu0oYDmuIMSDlcefk5wToHwmt5DByrqpTR3x/3088841945-9TzefMYW385iw5jsPSo7NeujLn6OigE3ZBC86hu/bve9QIWzyFUlMn4BOVZemcnZ8e3GjhwmuVViz8QhwoRse

@route('/auth/<ckey>/<csecret>/<atoken>/<atokensecret>')
def authentication(ckey, csecret, atoken, atokensecret):
 consumer_key = ckey
 consumer_secret = csecret
 access_token = atoken
 access_token_secret = atokensecret

 auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
 auth.set_access_token(access_token, access_token_secret)

 api = tweepy.API(auth)
 my_tweets = api.user_timeline()
 my_first_tweet = my_tweets[0].text
 following = api.followers()

 recommenderObj = Recommender()
 generatedTweet = recommenderObj.generate(my_tweets, 1, following, 2)

 return template('My first Tweet was: {{my_first_tweet_here}}, my generated text is {{generatedTweetHere}}', my_first_tweet_here = my_first_tweet, generatedTweetHere =generatedTweet)

run(host='localhost', port=8088, debug=True)