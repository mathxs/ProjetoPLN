# -*- coding: utf-8 -*-
import tweepy

auth = tweepy.OAuthHandler("x5u9rCVgbFHZllSqSAuJgNuTv", "q6mYHBSROEpQdHaeFayOpp2Nf9Y2MwvIjXWabKo8UOMAUx36vq")
auth.set_access_token("1156898520030470144-dnFJuLoY5bk6xGQBwH9behG2QoRUnu", "zDVR3WOKfFWeBR2bFPbM989OGPevyywHGmJRquKg9MnfB")

# Calling api 
api = tweepy.API(auth) 

api.search

user = api.me()

print('Name: ' + user.name)
print('Location: ' + user.location)
print('Friends: ' + str(user.friends_count))