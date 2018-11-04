import tweepy
from secrets import *
from weather import Weather, Unit
# Twitter authentication
def auth():
	auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
	auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
	api = tweepy.API(auth)
	return api


if __name__ == "__main__":
	api = auth()
	user = api.me()
	print (user.name)
