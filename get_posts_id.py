# -*- coding: utf-8 -*-

import sys
import time
import twitter
import json
import MySQLdb

mydb = MySQLdb.connect(host="localhost", user="root", passwd="dbserver", db="mydb") 
cursor = mydb.cursor() 

#OAUTH_TOKEN = sys.argv[1]
#OAUTH_TOKEN_SECRET = sys.argv[2]
#TWITTER_ID = sys.argv[3]

TWITTER_ID = sys.argv[1]

consumer_key = "eSWSQWbtOxtj5DJYz9I7dQ"
consumer_secret = "B3SPTXqFrgW4c4SsqrQlyyXuvQWTzdxyD6S8nI"

inicio = time.time()

statement = """SELECT DISTINCT id_twitter FROM users u INNER JOIN clients_users c ON u.id_twitter = c.users_id  WHERE  clients_id = %i GROUP BY u.id_twitter;"""%( int(TWITTER_ID))
cursor.execute(statement)
results = cursor.fetchall()
print len(results)

statement = """SELECT COUNT(*) FROM clients GROUP BY id_twitter"""
cursor.execute(statement)
user_system = cursor.fetchone()

print user_system[0]
#for result in results:
	#twitter_access = twitter.Twitter(domain='api.twitter.com', api_version='1', auth=twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, consumer_key, consumer_secret))
	#resultado_posts_ids = twitter_access.statuses.user_timeline(user_id=result[0],encoding='utf-8' )
	#json.dumps(resultado_posts_ids, sort_keys=True, indent=4)
	#for i in range(len(resultado_posts_ids)-1):
		#print resultado_posts_ids[i]['id']
		# print resultado_posts_ids[i]['text']
		#print resultado_posts_ids[i]['created_at']
		#print resultado_posts_ids[i]['user']['id']
		#print result		
		
		# statement = """INSERT INTO posts(id, criacao_data, id_twitter, text, users_id) VALUES(DEFAULT, '%s', %i, '%s', %i);"""%( resultado_posts_ids[i]['created_at'], resultado_posts_ids[i]['id'],resultado_posts_ids[i]['text'], resultado_posts_ids[i]['user']['id'])
		# print statement
		# cursor.execute(statement)
		# mydb.commit()	
		
fim = time.time()
print fim - inicio	

# twitter_access = twitter.Twitter(domain='api.twitter.com', api_version='1', auth=twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, consumer_key, consumer_secret))
# resultado_posts_ids = twitter_access.statuses.user_timeline(user_id=15576145,encoding='utf-8' )
# json.dumps(resultado_posts_ids, sort_keys=True, indent=4)
# for i in range(len(resultado_posts_ids)-1):
	# print resultado_posts_ids[i]['id']
	# print resultado_posts_ids[i]['text']
	# print resultado_posts_ids[i]['created_at']
	# print resultado_posts_ids[i]['entities']['hashtags']
	# for j in range(len(resultado_posts_ids[i]['entities']['hashtags'])-1):
		# print resultado_posts_ids[i]['entities']['hashtags'][j]



	# statement = """SELECT users_id FROM clients_users WHERE clients_id = %i GROUP BY users_id;"""%( int(TWITTER_ID))
	# print statement
	# busca = cursor.execute(statement)
	# results = busca.fetchall() 	
	# print results
# mydb.commit()

# twitter_access = twitter.Twitter(domain='api.twitter.com', api_version='1', auth=twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, consumer_key, consumer_secret))
# resultado_friends_ids = twitter_access.friends.ids(user_id=TWITTER_ID, rpp=2, encoding='utf-8' )

# json.dumps(resultado_friends_ids, sort_keys=True, indent=4)

# for i in range(len(resultado_friends_ids)-1):
	# statement = """INSERT INTO clients_users(clients_id, users_id, friend, follower)VALUES( %i, %i, %i, %i);"""%( int(TWITTER_ID), resultado_friends_ids[i],1,0)
	# cursor.execute(statement)	 
	# mydb.commit()

# twitter_access = twitter.Twitter(domain='api.twitter.com', api_version='1', auth=twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, consumer_key, consumer_secret))
# resultado_followers_ids = twitter_access.followers.ids(user_id=TWITTER_ID, rpp=2, encoding='utf-8' )

# json.dumps(resultado_followers_ids, sort_keys=True, indent=4)

# for i in range(len(resultado_followers_ids)-1):
	# statement = """INSERT INTO clients_users(clients_id, users_id, friend, follower) VALUES( %i, %i, %i, %i);"""%( int(TWITTER_ID), resultado_followers_ids[i],0,1)
	# cursor.execute(statement)	 
	# mydb.commit()			

# fim = time.time()
# print fim - inicio
