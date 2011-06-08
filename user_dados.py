# -*- coding: utf-8 -*-
import sys
import twitter
import json

import MySQLdb

mydb = MySQLdb.connect(host="localhost", user="root", passwd="server@bd", db="mydb") 
cursor = mydb.cursor() 

OAUTH_TOKEN = sys.argv[1]
OAUTH_TOKEN_SECRET = sys.argv[2]
SENHA = sys.argv[3]

consumer_key = "eSWSQWbtOxtj5DJYz9I7dQ"
consumer_secret = "B3SPTXqFrgW4c4SsqrQlyyXuvQWTzdxyD6S8nI"

twitter_access = twitter.Twitter(domain='api.twitter.com', api_version='1', auth=twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, consumer_key, consumer_secret))
perfil_usuario = twitter_access.account.verify_credentials(encoding='utf-8')
json.dumps(perfil_usuario, sort_keys=True, indent=4)

statement = """
			INSERT INTO clients( id, username, senha, inscricao_data, access_token, secret_token, 
								 id_twitter, friends_count, followers_count, profile_image_url, location, screen_name, created_at) 
			VALUES(DEFAULT, '%s', sha1('%s'), now(), '%s', '%s', %i, %i, %i, '%s', '%s','%s','%s');"""%( 
			perfil_usuario['screen_name'],
			SENHA,
			OAUTH_TOKEN,
			OAUTH_TOKEN_SECRET,
			perfil_usuario['id'],
			perfil_usuario['friends_count'],
			perfil_usuario['followers_count'],
			perfil_usuario['profile_image_url'],
			perfil_usuario['location'], 
			perfil_usuario['screen_name'],
			perfil_usuario['created_at'])
			
cursor.execute(statement)	 
mydb.commit()	
