# -*- coding: utf-8 -*-

import sys
import time
import twitter
import json
import MySQLdb
import os

mydb = MySQLdb.connect(host="localhost", user="root", passwd="server@bd", db="mydb") 
cursor = mydb.cursor() 

OAUTH_TOKEN = sys.argv[1]
OAUTH_TOKEN_SECRET = sys.argv[2]
TWITTER_ID = sys.argv[3]
RANGE = sys.argv[4]
OFFSET = sys.argv[5]


print '''======================================'''



consumer_key = "eSWSQWbtOxtj5DJYz9I7dQ"
consumer_secret = "B3SPTXqFrgW4c4SsqrQlyyXuvQWTzdxyD6S8nI"

inicio = time.time()

statement = """SELECT c.users_id FROM clients_users c INNER JOIN users u ON c.users_id = u.id_twitter WHERE c.clients_id = %i AND u.protected = 'False' GROUP BY c.users_id LIMIT %i OFFSET %i;"""%( int(TWITTER_ID), int(RANGE), int(OFFSET))
# print statement
cursor.execute(statement)
results = cursor.fetchall()
for dados in results:
	twitter_access = twitter.Twitter(domain='api.twitter.com', api_version='1', auth=twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, consumer_key, consumer_secret))
	resultado_user_timeline = twitter_access.statuses.user_timeline(user_id=dados[0], count=2, encoding='utf-8')
	arquivo = "./arquivo-" + OFFSET + ".txt"
	# print len(resultado_user_timeline)
	# file = open(arquivo,'w')
	for i in range(len(resultado_user_timeline)-1):
		print resultado_user_timeline[i]['id']
		print resultado_user_timeline[i]['text']
		print resultado_user_timeline[i]['created_at']
		print resultado_user_timeline[i]['user']['id']
		
		# file.write(resultado_user_timeline[i]['id'])
		# file.write(resultado_user_timeline[i]['text'])
		# file.write(resultado_user_timeline[i]['created_at'])
		# file.write(resultado_user_timeline[i]['user']['id'])
		# file.write(result)		
	
	
	# file.write(json.dumps(resultado_user_timeline, sort_keys=True, indent=4))
	# file.close()
	# print json.dumps(resultado_user_timeline, sort_keys=True, indent=4)
	# print resultado_user_timeline




# statement = """SELECT COUNT(*) FROM clients"""
# cursor.execute(statement)
# resultados = cursor.fetchone()
# total_usuarios = resultados[0]
# print total_usuarios

# limite_registros = total_dados/total_usuarios 
# print limite_registros

# if(total_dados % total_usuarios) == 0:
	# limite_registros = limite_registros
# else:
	# limite_registros = limite_registros + 1
	
# print numero_registros

# statement = """SELECT access_token, secret_token FROM clients"""
# cursor.execute(statement)
# resultados = cursor.fetchall()

# qtd_registros = 0	
# for dados in resultados:
	# OAUTH_TOKEN = dados[0]
	# OAUTH_TOKEN_SECRET = dados[1]
	# OFFSET = limite_registros*(qtd_registros)
	
	# cmd = '''python popula_posts.py'''   + str(OAUTH_TOKEN) + ''' ''' + str(OAUTH_TOKEN_SECRET) + ''' ''' + str(TWITTER_ID) + ''' ''' + str(limite_registros) + ''' ''' + str(OFFSET)
	# print cmd
	# os.system(cmd)
	# qtd_registros = qtd_registros+1
	


# statement = """SELECT DISTINCT id_twitter FROM users u INNER JOIN clients_users c ON u.id_twitter = c.users_id  WHERE  clients_id = %i GROUP BY u.id_twitter;"""%( int(TWITTER_ID))
# cursor.execute(statement)
# results = cursor.fetchall()

# for i in range(1,numero_registros):
	
		
	

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
		
# fim = time.time()
# print fim - inicio	

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

fim = time.time()
print fim - inicio

