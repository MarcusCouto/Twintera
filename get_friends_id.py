# -*- coding: utf-8 -*-

import sys
import time
import twitter
import json
import MySQLdb

mydb = MySQLdb.connect(host="localhost", user="root", passwd="dbserver", db="mydb") 
cursor = mydb.cursor() 

OAUTH_TOKEN = sys.argv[1]
OAUTH_TOKEN_SECRET = sys.argv[2]
TWITTER_ID = sys.argv[3]

consumer_key = "eSWSQWbtOxtj5DJYz9I7dQ"
consumer_secret = "B3SPTXqFrgW4c4SsqrQlyyXuvQWTzdxyD6S8nI"

inicio = time.time()

twitter_access = twitter.Twitter(domain='api.twitter.com', api_version='1', auth=twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, consumer_key, consumer_secret))
resultado_friends_ids = twitter_access.friends.ids(user_id=TWITTER_ID, rpp=2, encoding='utf-8' )

json.dumps(resultado_friends_ids, sort_keys=True, indent=4)

for i in range(len(resultado_friends_ids)-1):
	statement = """INSERT INTO clients_users(clients_id, users_id, friend, follower)VALUES( %i, %i, %i, %i);"""%( int(TWITTER_ID), resultado_friends_ids[i],1,0)
	cursor.execute(statement)	 
	mydb.commit()

twitter_access = twitter.Twitter(domain='api.twitter.com', api_version='1', auth=twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, consumer_key, consumer_secret))
resultado_followers_ids = twitter_access.followers.ids(user_id=TWITTER_ID, rpp=2, encoding='utf-8' )

json.dumps(resultado_followers_ids, sort_keys=True, indent=4)

for i in range(len(resultado_followers_ids)-1):
	statement = """INSERT INTO clients_users(clients_id, users_id, friend, follower) VALUES( %i, %i, %i, %i);"""%( int(TWITTER_ID), resultado_followers_ids[i],0,1)
	cursor.execute(statement)	 
	mydb.commit()			

fim = time.time()
print fim - inicio
