# -*- coding: utf-8 -*-

import sys
import time
import twitter
import os
import glob
import MySQLdb
from xml.etree.ElementTree import ElementTree
from string import maketrans 
from math import ceil
from exceptions import Exception
from datetime import datetime, timedelta
from function import *

mydb = MySQLdb.connect(host="localhost", user="root", passwd="server@bd", db="mydb") 
cursor = mydb.cursor() 

statement = """SELECT id_twitter FROM clients;"""
cursor.execute(statement)
clients_id = cursor.fetchall()

consumer_key = "eSWSQWbtOxtj5DJYz9I7dQ"
consumer_secret = "B3SPTXqFrgW4c4SsqrQlyyXuvQWTzdxyD6S8nI"

for id in clients_id:

	statement = """SELECT access_token, secret_token FROM clients WHERE id_twitter = %i;"""%(id)
	cursor.execute(statement)	 
	tokens = cursor.fetchone()

	twitter_access = twitter.Twitter(domain='api.twitter.com', api_version='1', auth=twitter.oauth.OAuth(tokens[0], tokens[1], consumer_key, consumer_secret))
	resultado_friends_ids = twitter_access.friends.ids(user_id=id[0], cursor=-1, encoding='utf-8' )
	
	file = open("/var/www/friends/friends_"+str(id[0])+".xml",'w')  
	file.write(resultado_friends_ids)
	file.close()

	tree = ElementTree(file="/var/www/friends/friends_"+str(id[0])+".xml")
	root = tree.getroot()
	ids = root.find('ids')
	list_friends_id	= ids.findall('id')
	
	list_friends = [] 
	for friends_id in list_friends_id:
		list_friends.append(friends_id.text) 
	
	twitter_access = twitter.Twitter(domain='api.twitter.com', api_version='1', auth=twitter.oauth.OAuth(tokens[0], tokens[1], consumer_key, consumer_secret))
	resultado_followers_ids = twitter_access.followers.ids(user_id=id[0], cursor=-1, encoding='utf-8' )
	
	file = open("/var/www/friends/followers_"+str(id[0])+".xml",'w')  
	file.write(resultado_followers_ids)
	file.close()

	tree = ElementTree(file="/var/www/friends/followers_"+str(id[0])+".xml")
	root = tree.getroot()
	ids = root.find('ids')
	list_followers_id = ids.findall('id')
	
	list_followers = [] 
	for followers_id in list_followers_id:
		list_followers.append(followers_id.text)	
		
		
	statement = """SELECT users_id FROM clients_users WHERE clients_id = %i  AND friend = 1 GROUP BY users_id;"""%(id)
	cursor.execute(statement)	 
	lista_atual = cursor.fetchall()
	
	#monto minha rede de amigos
	minha_rede_amigos= []
	for item in lista_atual:
		minha_rede_amigos.append(str(item[0]))			
	
	#comparo minha rede de amigos com a nova rede
	for id_friend in  minha_rede_amigos:
				
		if id_friend in list_friends:
			list_friends.remove(id_friend)			
	
	
	for friends_id in list_friends:
		statement = """INSERT INTO clients_users(clients_id, users_id, friend, follower, status)VALUES( '%s', '%s', %i, %i, %i);"""%( str(id[0]), str(friends_id),1,0,0)
		print statement
		cursor.execute(statement)	 
		mydb.commit()
		
	statement = """SELECT users_id FROM clients_users WHERE clients_id = %i  AND follower = 1 GROUP BY users_id;"""%(id)
	cursor.execute(statement)	 
	lista_atual = cursor.fetchall()
	
	#monto minha rede de seguidores
	minha_rede_seguidores= []
	for item in lista_atual:
		minha_rede_seguidores.append(str(item[0]))			
	
	#comparo minha rede de seguidores com a nova rede
	for id_friend in  minha_rede_seguidores:
				
		if id_friend in list_followers:
			list_followers.remove(id_friend)		
	
	for followers_id in list_followers:
		statement = """INSERT INTO clients_users(clients_id, users_id, friend, follower, status) VALUES( '%s', '%s', %i, %i, %i);"""%( str(id[0]), str(followers_id), 0,1,0)
		print statement
		cursor.execute(statement)	 
		mydb.commit()	
	
