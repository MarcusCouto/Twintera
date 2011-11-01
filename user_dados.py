# -*- coding: utf-8 -*-
from xml.etree.ElementTree import ElementTree
import sys
import twitter
import os, glob, re
import MySQLdb
from exceptions import Exception
from function import *
from time import sleep


mydb = MySQLdb.connect(host="localhost", user="root", passwd="server@bd", db="mydb") 
cursor = mydb.cursor() 

OAUTH_TOKEN = sys.argv[1]
OAUTH_TOKEN_SECRET = sys.argv[2]
#SENHA = sys.argv[3]

print "entrou no user dados"

consumer_key = "eSWSQWbtOxtj5DJYz9I7dQ"
consumer_secret = "B3SPTXqFrgW4c4SsqrQlyyXuvQWTzdxyD6S8nI"

twitter_access = twitter.Twitter(domain='api.twitter.com', api_version='1', auth=twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, consumer_key, consumer_secret))
perfil_usuario = twitter_access.account.verify_credentials(encoding='utf-8')

file = open("./profile_users/"+OAUTH_TOKEN_SECRET+".xml",'w')  
file.write(perfil_usuario)
file.close()

tree = ElementTree(file="./profile_users/"+OAUTH_TOKEN_SECRET+".xml")
root = tree.getroot()
id	= root.find('id')
friends_count	= root.find('friends_count')
followers_count	= root.find('followers_count')
profile_image_url	= root.find('profile_image_url')
location	= root.find('location')
screen_name	= root.find('screen_name')
created_at	= root.find('created_at')
data_criacao = corrigeData(created_at.text)

statement = """UPDATE  clients SET 
			friends_count = %i, followers_count = %i, profile_image_url = '%s', location = '%s',	screen_name = '%s',
			created_at = '%s' ;"""%( int(friends_count.text),	int(followers_count.text), profile_image_url.text,	location.text, screen_name.text, data_criacao)
			
cursor.execute(statement)	 
mydb.commit()	

os.remove("./profile_users/"+OAUTH_TOKEN_SECRET+".xml")

statement = """SELECT id_twitter FROM clients WHERE access_token = '%s' AND secret_token = '%s'  """%(	OAUTH_TOKEN,	OAUTH_TOKEN_SECRET)
cursor.execute(statement)
id_twitter = cursor.fetchone()

try:
	twitter_access = twitter.Twitter(domain='api.twitter.com', api_version='1', auth=twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, consumer_key, consumer_secret))
	resultado_friends_ids = twitter_access.friends.ids(user_id=id_twitter[0], cursor=-1, encoding='utf-8' )
							
except:
	escreveLog("- Erro ao pegar a lista de friends do id  - "+ str(id_twitter[0]))

twitter_access = twitter.Twitter(domain='api.twitter.com', api_version='1', auth=twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, consumer_key, consumer_secret))
resultado_friends_ids = twitter_access.friends.ids(user_id=id_twitter[0], cursor=-1)

file = open("/var/www/friends/friends_"+str(id_twitter[0])+".xml",'w')  
file.write(resultado_friends_ids)
file.close()

tree = ElementTree(file="/var/www/friends/friends_"+str(id_twitter[0])+".xml")
root = tree.getroot()
ids = root.find('ids')
list_friends_id	= ids.findall('id')

for friends_id in list_friends_id:
	statement = """INSERT INTO clients_users(clients_id, users_id, friend, follower, status)VALUES( '%s', '%s', %i, %i, %i);"""%( id_twitter[0], friends_id.text,1,0,0)
	cursor.execute(statement)	 
	mydb.commit()

try:
	twitter_access = twitter.Twitter(domain='api.twitter.com', api_version='1', auth=twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, consumer_key, consumer_secret))
	resultado_followers_ids = twitter_access.followers.ids(user_id=id_twitter[0], cursor=-1)
							
except:
	escreveLog("- Erro ao pegar a lista de followers do id  - "+ str(id_twitter[0]))	
	
file = open("/var/www/friends/followers_"+str(id_twitter[0])+".xml",'w')  
file.write(resultado_followers_ids)
file.close()

tree = ElementTree(file="/var/www/friends/followers_"+str(id_twitter[0])+".xml")
root = tree.getroot()
ids = root.find('ids')
list_followers_id = ids.findall('id')

for followers_id in list_followers_id:
	statement = """INSERT INTO clients_users(clients_id, users_id, friend, follower, status) VALUES( '%s', '%s', %i, %i, %i);"""%( id_twitter[0], followers_id.text,0,1,0)
	cursor.execute(statement)	 
	mydb.commit()
	
os.remove("/var/www/friends/friends_"+str(id_twitter[0])+".xml")
os.remove("/var/www/friends/followers_"+str(id_twitter[0])+".xml")
