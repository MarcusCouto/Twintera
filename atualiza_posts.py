# -*- coding: utf-8 -*-

import sys
import time
import twitter
import os
import MySQLdb
from math import ceil
from exceptions import Exception
from datetime import datetime, timedelta
from function import *


mydb = MySQLdb.connect(host="localhost", user="root", passwd="server@bd", db="mydb") 
cursor = mydb.cursor() 


consumer_key = "eSWSQWbtOxtj5DJYz9I7dQ"
consumer_secret = "B3SPTXqFrgW4c4SsqrQlyyXuvQWTzdxyD6S8nI"

statement = """SELECT COUNT(*) FROM last_posts """
cursor.execute(statement)
list_posts = cursor.fetchone()	

statement = """SELECT access_token, secret_token, id_twitter FROM clients """
cursor.execute(statement)
lista_clients = cursor.fetchall()	

token_aouth=[]	
for clients in lista_clients:
	try:
		twitter_access = twitter.Twitter(domain='api.twitter.com', api_version='1', auth=twitter.oauth.OAuth(clients[0], clients[1], consumer_key, consumer_secret))
		credentials = twitter_access.account.verify_credentials()			
		token_aouth.append([clients[0],clients[1]])						
	except:
	
		escreveLog(" - id_twitter Desconhecido - "+ str(clients[2]))


total_clients = len(token_aouth)
modulo = list_posts[0] % total_clients
valor = list_posts[0]/total_clients
offset = int(valor) + modulo

count = 1
for token in token_aouth:
	statement = """SELECT id_twitter as post_id, users_id FROM last_posts LIMIT %i OFFSET %i ;"""%(offset, int((count-1)*offset))
	print statement
	cursor.execute(statement)
	lista_usuarios = cursor.fetchall()
	
	for friends in lista_usuarios:			
		
		try:
			twitter_access = twitter.Twitter(domain='api.twitter.com', api_version='1', auth=twitter.oauth.OAuth(token[0], token[1], consumer_key, consumer_secret))
			resultado_posts_ids = twitter_access.statuses.user_timeline(user_id=friends[1],since_id =friends[0],  count=200,encoding='utf-8')
			
			file = open("/var/www/posts/"+str(friends[0])+".xml",'w')  
			file.write(resultado_posts_ids)
			file.close()
			
			#statement = """UPDATE users  SET status = 1 WHERE  id_twitter = %i"""%( friends[0])
			#cursor.execute(statement)	 
			#mydb.commit()
		
		except:
			escreveLog(" - id_twitter Desconhecido - "+ str(friends[0]))
			
			
		
	count = count + 1	
	
mydb.close()

#cmd = '''python insert_posts.py'''
#os.system(cmd)	
