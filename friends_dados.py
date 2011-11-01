# -*- coding: utf-8 -*-
import sys
import time
import twitter
import os
import MySQLdb
from exceptions import Exception
from math import ceil

mydb = MySQLdb.connect(host="localhost", user="root", passwd="server@bd", db="mydb") 
cursor = mydb.cursor() 

consumer_key = "eSWSQWbtOxtj5DJYz9I7dQ"
consumer_secret = "B3SPTXqFrgW4c4SsqrQlyyXuvQWTzdxyD6S8nI"


statement = """SELECT COUNT(*) FROM clients_users WHERE status = 0;"""
cursor.execute(statement)
total_usuarios = cursor.fetchone()

print "entrou no friends dados"

if total_usuarios[0] > 0:

	statement = """SELECT COUNT(*) FROM clients"""
	cursor.execute(statement)
	total_clients = cursor.fetchone()
	

	valor = total_usuarios[0]/total_clients[0]
	offset = round(valor)

	statement = """SELECT access_token, secret_token FROM clients """
	cursor.execute(statement)
	lista_clients = cursor.fetchall()
	count = 1
	for clients in lista_clients:
		statement = """SELECT users_id FROM clients_users WHERE status = 0 LIMIT %i OFFSET %i ;"""%(offset, int((count-1)*offset))
		cursor.execute(statement)
		lista_usuarios = cursor.fetchall()
		
		for friends in lista_usuarios:
			
			try:
				
				twitter_access = twitter.Twitter(domain='api.twitter.com', api_version='1', auth=twitter.oauth.OAuth(clients[0], clients[1], consumer_key, consumer_secret))
				resultado_posts_ids = twitter_access.users.show(user_id=friends[0],encoding='utf-8' )	
				
				nome_arquivo = "/var/www/profile/" + str(friends[0]) + ".xml"
						
				file = open(nome_arquivo,'w')  
				file.write(resultado_posts_ids)
				file.close()
				
				statement = """UPDATE clients_users  SET status = 1 WHERE  users_id = '%s'"""%(friends[0])
				cursor.execute(statement)	 
				mydb.commit()
				
			except:
				print statement
				print "erro ao acessar dados do usuario " + str(friends[0])
				

		count = count + 1		
		

	cmd = '''python insert_friends.py'''
	os.system(cmd)
	
mydb.close()
	
