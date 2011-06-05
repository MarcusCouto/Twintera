# -*- coding: utf-8 -*-

import sys
import time
import twitter
import json
import MySQLdb

mydb = MySQLdb.connect(host="localhost", user="root", passwd="dbserver", db="mydb") 
cursor = mydb.cursor() 

id = sys.argv[1]
profile_image_url = sys.argv[2]
location = sys.argv[3]
screen_name = sys.argv[4]
protected = sys.argv[5]
friends_count = sys.argv[6]
followers_count = sys.argv[7]


statement = """INSERT INTO users(id, id_twitter, profile_image_url, location, username, protected, friends_count, follower_count) VALUES(DEFAULT, %i,'%s','%s','%s','%s', %i, %i);"""%( id, rprofile_image_url,location, screen_name, protected,friends_count,followers_count)
cursor.execute(statement)
mydb.commit()	
