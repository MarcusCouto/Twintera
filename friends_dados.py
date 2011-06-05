# -*- coding: utf-8 -*-

import sys
import time
import twitter
import json
import os
import MySQLdb

mydb = MySQLdb.connect(host="localhost", user="root", passwd="dbserver", db="mydb") 
cursor = mydb.cursor() 

OAUTH_TOKEN = sys.argv[1]
OAUTH_TOKEN_SECRET = sys.argv[2]
TWITTER_ID = sys.argv[3]

consumer_key = "eSWSQWbtOxtj5DJYz9I7dQ"
consumer_secret = "B3SPTXqFrgW4c4SsqrQlyyXuvQWTzdxyD6S8nI"

inicio = time.time()

statement = """SELECT users_id FROM clients_users WHERE clients_id = %i GROUP BY users_id;"""%( int(TWITTER_ID))
cursor.execute(statement)
results = cursor.fetchall()
for result in results:
	twitter_access = twitter.Twitter(domain='api.twitter.com', api_version='1', auth=twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, consumer_key, consumer_secret))
	resultado_posts_ids = twitter_access.users.show(user_id=result[0],encoding='utf-8' )
	json.dumps(resultado_posts_ids, sort_keys=True, indent=4)
	
	id = resultado_posts_ids['id']
	profile_image_url = resultado_posts_ids['profile_image_url']
	location = resultado_posts_ids['location']
	screen_name = resultado_posts_ids['screen_name']
	protected = resultado_posts_ids['protected']
	friends_count = resultado_posts_ids['friends_count']
	followers_count = resultado_posts_ids['followers_count']
		
	statement = """INSERT INTO users(id, id_twitter, profile_image_url, location, username, protected, friends_count, follower_count) VALUES(DEFAULT, %i,'%s','%s','%s','%s', %i, %i);"""%( id, profile_image_url,location, screen_name, protected,friends_count,followers_count)
	cursor.execute(statement)
	mydb.commit()	
	
	# print resultado_posts_ids['id']
	# print resultado_posts_ids['profile_image_url']
	# print resultado_posts_ids['location']
	# print resultado_posts_ids['screen_name']
	# print resultado_posts_ids['protected']
	# print resultado_posts_ids['friends_count']
	# print resultado_posts_ids['followers_count']
	
	
	
	#cmd = "python insert_friends.py " + str(resultado_posts_ids['id']) + " " + resultado_posts_ids['profile_image_url'] + " " + resultado_posts_ids['location'] + " " + resultado_posts_ids['screen_name'] + " " + resultado_posts_ids['protected'] + " " + resultado_posts_ids['friends_count'] + " " + resultado_posts_ids['followers_count']
	#print cmd
	#os.system(cmd) 
		
fim = time.time()
#print fim - inicio	

