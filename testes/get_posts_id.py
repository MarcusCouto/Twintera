# -*- coding: utf-8 -*-
import sys
import json
import MySQLdb
import os
import time
import threading

# class MyThread(threading.Thread):
	# def __init__(self, oauth_token, oauth_token_secret,twitter_id,limite_registros, offset):
		# threading.Thread.__init__(self)
		# self.oauth_token = oauth_token
		# self.oauth_token_secret = oauth_token_secret
		# self.twitter_id = twitter_id
		# self.limite_registros = limite_registros
		# self.offset = offset	
	# def run(self):
		# mydb = MySQLdb.connect(host="localhost", user="root", passwd="server@bd", db="mydb") 
		# cursor = mydb.cursor() 
		# consumer_key = "eSWSQWbtOxtj5DJYz9I7dQ"
		# consumer_secret = "B3SPTXqFrgW4c4SsqrQlyyXuvQWTzdxyD6S8nI"

		# print '''======================================'''
		# inicio = time.time()

		# statement = """SELECT c.users_id FROM clients_users c INNER JOIN users u ON c.users_id = u.id_twitter WHERE c.clients_id = %i AND u.protected = 'False' GROUP BY c.users_id LIMIT %i OFFSET %i;"""%( int(TWITTER_ID), int(limite_registros), int(offset))
		# print statement
		# cursor.execute(statement)
		# results = cursor.fetchall()
		# for dados in results:
			# twitter_access = twitter.Twitter(domain='api.twitter.com', api_version='1', auth=twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, consumer_key, consumer_secret))
			# resultado_user_timeline = twitter_access.statuses.user_timeline(user_id=dados[0], encoding='utf-8')
	
		# fim = time.time()
		# print fim - inicio
	



mydb = MySQLdb.connect(host="localhost", user="root", passwd="", db="mydb") 
cursor = mydb.cursor() 


TWITTER_ID = sys.argv[1]

statement = """SELECT COUNT(*) FROM (SELECT * FROM clients_users c INNER JOIN users u ON c.users_id = u.id_twitter WHERE c.clients_id = %i AND u.protected = 'False' GROUP BY c.users_id) x;"""%( int(TWITTER_ID))
cursor.execute(statement)
results = cursor.fetchone()
total_dados = results[0]

statement = """SELECT COUNT(*) FROM clients"""
cursor.execute(statement)
resultados = cursor.fetchone()
total_usuarios = resultados[0]

limite_registros = total_dados/total_usuarios 

if(total_dados % total_usuarios) == 0:
	limite_registros = limite_registros
else:
	limite_registros = limite_registros + 1

statement = """SELECT access_token, secret_token FROM clients"""
cursor.execute(statement)
resultados = cursor.fetchall()

qtd_registros = 0	
for dados in resultados:
	oauth_token = dados[0]
	oautho_token_secret = dados[1]
	offset = limite_registros*(qtd_registros)
	
	# mt = MyThread(oauth_token, oautho_token_secret, TWITTER_ID, limite_registros, offset)
	# qtd_registros = qtd_registros+1	
	# mt.start()
	
	cmd = '''python popula_posts.py '''  + str(oauth_token) + ''' ''' + str(oautho_token_secret) + ''' ''' + str(TWITTER_ID) + ''' ''' + str(limite_registros) + ''' ''' + str(offset)
	print cmd
	os.system(cmd)
	qtd_registros = qtd_registros+1	
