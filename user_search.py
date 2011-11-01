from xml.etree.ElementTree import ElementTree
import sys

#import search_twitter
import twitter

import os, glob, re
import MySQLdb
import subprocess


mydb = MySQLdb.connect(host="localhost", user="root", passwd="server@bd", db="mydb") 
cursor = mydb.cursor() 

OAUTH_TOKEN = sys.argv[1]
OAUTH_TOKEN_SECRET = sys.argv[2]

consumer_key = "eSWSQWbtOxtj5DJYz9I7dQ"
consumer_secret = "B3SPTXqFrgW4c4SsqrQlyyXuvQWTzdxyD6S8nI"

# twitter_access = search_twitter.Twitter(domain='api.twitter.com', api_version='1', auth=search_twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, consumer_key, consumer_secret))
# perfil_usuario = twitter_access.users.search(q="marcuscouto",encoding='utf-8')

# file = open("./buscas/teste.txt",'w')  
# file.write(str(perfil_usuario))
# file.close()
query = "marcuscouto"
twitter_access = twitter.Twitter(domain='api.twitter.com', api_version='1', auth=twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, consumer_key, consumer_secret))
perfil_usuario = twitter_access.users.search(q=query, per_page=20, encoding='utf-8')

file = open("./buscas/"+query+".xml",'w')  
file.write(perfil_usuario)
file.close()


topo_site = ''' <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"> 
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="pt-br"> 
	<head> 
		<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" /> 
		<link rel="stylesheet" href="./estilo/estilo.css" type="text/css" /> 
		<link rel="stylesheet" href="./estilo/tabelas.css" type="text/css" /> 
		<title>#twintera!</title> 
	</head> 
	<body> 
	<div id="container">
		<div id="site_corpo">
			<div id="corpo">
				<br /><br />
				<img src="./estilo/images/logo-twintera.jpg" alt="twintera" class="logoGPMH"/>
				<hr/>				
'''



tree = ElementTree(file="./buscas/"+query+".xml")
root = tree.getroot()

users = root.findall('user')

meio_site = []

for user in users:

	name = user.find('name')
	screen_name = user.find('screen_name')
	file_image_url = user.find('profile_image_url')
	location = user.find('location')
	description = user.find('description')
	friends_count = user.find('friends_count')
	followers_count = user.find('followers_count')
	statuses_count = user.find('statuses_count')
		
	meio_site.append("<ul><li>"+str(name.text.decode('utf8', 'replace'))+"</li><li>"+str(screen_name.text.decode('utf8', 'replace'))+"</li><li>"+str(file_image_url.text)+"</li><li>"+str(location.text.decode('utf8', 'replace'))+"</li><li>"+str(description.text.decode('utf8', 'replace'))+"</li><li>"+str(friends_count.text)+"</li><li>"+str(followers_count.text)+"</li><li>"+str(statuses_count.text)+"</li></ul>")
	print meio_site
	
	# print name.text
	# print screen_name.text
	# print file_image_url.text
	# print location.text
	# print description.text
	# print friends_count.text
	# print followers_count.text
	# print statuses_count.text
	


rodape_site = '''
			</div>
		</div>	
	</div>	
	</body> 
</html>
'''
mydb.close()

file = open("resultado.html",'w')  
file.write(topo_site+str(meio_site)+rodape_site)
file.close()


# http://api.twitter.com/1/users/search.json?q=Twitter%20API
# tree = ElementTree(file="./profile_users/"+OAUTH_TOKEN_SECRET+".xml")
# root = tree.getroot()
# id	= root.find('id')
# friends_count	= root.find('friends_count')
# followers_count	= root.find('followers_count')
# profile_image_url	= root.find('profile_image_url')
# location	= root.find('location')
# screen_name	= root.find('screen_name')
# created_at	= root.find('created_at')

# statement = """	INSERT INTO clients( id, username, senha, inscricao_data, access_token, secret_token, 
								 # id_twitter, friends_count, followers_count, profile_image_url, location, screen_name, created_at) 
			# VALUES(DEFAULT, '%s', sha1('%s'), now(), '%s', '%s', %i, %i, %i, '%s', '%s','%s','%s');"""%( 
			# screen_name.text,
			# SENHA,
			# OAUTH_TOKEN,
			# OAUTH_TOKEN_SECRET,
			# int(id.text),
			# int(friends_count.text),
			# int(followers_count.text),
			# profile_image_url.text,
			# location.text,
			# screen_name.text,
			# str(created_at.text))
			
			
# cursor.execute(statement)	 
# mydb.commit()	

# os.remove("./profile_users/"+OAUTH_TOKEN_SECRET+".xml",)
# p = subprocess.Popen([sys.executable, './friends_dados.py'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	
	





