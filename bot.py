import tweepy
from secrets import *
from weather import Weather, Unit
# Twitter authentication
def auth():
	auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
	auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
	api = tweepy.API(auth)
	return api

def get_weather(location):
	weather = Weather(unit=Unit.CELSIUS)
	location = weather.lookup_by_location(location)
	condition = location.condition
	return condition

if __name__ == "__main__":
	api = auth()
	user = api.me()
	#print (user.name)
	place = input("What place do you want the weather of?\n")
	cur_weather = get_weather(place)
	#or x in cur_weather:
	#	print(x)
	try:
		api.update_status("Currently, " + place + " is "+cur_weather.text +" with a temperature of "+cur_weather.temp + u"\u00b0" +" C")
	except tweepy.error.TweepError as e:
		print("oops")

