# -*- coding: utf-8 -*-
from xml.etree.ElementTree import ElementTree
import sys
import twitter
import MySQLdb
import os
import subprocess

mydb = MySQLdb.connect(host="localhost", user="root", passwd="server@bd", db="mydb") 
cursor = mydb.cursor() 

print "entrou no get_friends_id"

TWITTER_ID = sys.argv[1]

statement = """SELECT access_token, secret_token FROM clients WHERE id_twitter = %i  """%(int(TWITTER_ID))
cursor.execute(statement)
tokens = cursor.fetchone()

OAUTH_TOKEN = tokens[0]
OAUTH_TOKEN_SECRET = tokens[1]

consumer_key = "eSWSQWbtOxtj5DJYz9I7dQ"
consumer_secret = "B3SPTXqFrgW4c4SsqrQlyyXuvQWTzdxyD6S8nI"

twitter_access = twitter.Twitter(domain='api.twitter.com', api_version='1', auth=twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, consumer_key, consumer_secret))
resultado_friends_ids = twitter_access.friends.ids(user_id=TWITTER_ID, cursor=-1, encoding='utf-8' )

file = open("/var/www/friends/friends_"+TWITTER_ID+".xml",'w')  
file.write(resultado_friends_ids)
file.close()

tree = ElementTree(file="/var/www/friends/friends_"+TWITTER_ID+".xml")
root = tree.getroot()
ids = root.find('ids')
list_friends_id	= ids.findall('id')

for friends_id in list_friends_id:
	statement = """INSERT INTO clients_users(clients_id, users_id, friend, follower, status)VALUES( '%s', '%s', %i, %i, %i);"""%( TWITTER_ID, friends_id.text,1,0,0)
	cursor.execute(statement)	 
	mydb.commit()

twitter_access = twitter.Twitter(domain='api.twitter.com', api_version='1', auth=twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, consumer_key, consumer_secret))
resultado_followers_ids = twitter_access.followers.ids(user_id=TWITTER_ID, cursor=-1, encoding='utf-8' )

file = open("/var/www/friends/followers_"+TWITTER_ID+".xml",'w')  
file.write(resultado_followers_ids)
file.close()

tree = ElementTree(file="/var/www/friends/followers_"+TWITTER_ID+".xml")
root = tree.getroot()
ids = root.find('ids')
list_followers_id = ids.findall('id')

for followers_id in list_followers_id:
	statement = """INSERT INTO clients_users(clients_id, users_id, friend, follower, status) VALUES( '%s', '%s', %i, %i, %i);"""%( TWITTER_ID, followers_id.text,0,1,0)
	cursor.execute(statement)	 
	mydb.commit()	
	
os.remove("/var/www/friends/friends_"+TWITTER_ID+".xml")
os.remove("/var/www/friends/followers_"+TWITTER_ID+".xml")

mydb.close()
