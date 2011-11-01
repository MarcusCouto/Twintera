from xml.etree.ElementTree import ElementTree
import search_twitter
import twitter
import json
import sys
import MySQLdb
import os, glob, re
from function import *

	
class Dir:
  def read(self, dir, extension, files=[]):
    for f in glob.glob( os.path.join(dir, "*") ):

      if os.path.isdir( f ):
        files = self.read( f, extension, files )
      else:
        if f.endswith(".%s" % extension):
          files.append( f )

    return files


mydb = MySQLdb.connect(host="localhost", user="root", passwd="server@bd", db="mydb") 
cursor = mydb.cursor() 

consumer_key = "eSWSQWbtOxtj5DJYz9I7dQ"
consumer_secret = "B3SPTXqFrgW4c4SsqrQlyyXuvQWTzdxyD6S8nI"

WORD = sys.argv[1]

#Realiza as buscas no twitter...
twitter_access = search_twitter.Twitter(domain='search.twitter.com')
resultado_busca_alternativa = twitter_access.search(q=WORD,locale="br", rpp=100,)
texto = json.dumps(resultado_busca_alternativa,indent=4)

file = open("./buscas/"+WORD+".json",'w')  
file.write(texto)
file.close()


for i in range(len(resultado_busca_alternativa["results"])):
	
	post = removeMarcacaoEncode(resultado_busca_alternativa["results"][i]["text"])
	post = trataCodigosHTML(resultado_busca_alternativa["results"][i]["text"])
	
	if '"' in post:
		post = post.replace('"','')
	if "'" in post:
		post = post.replace("'","")	
		
			
	statement = """	INSERT INTO temp_search(id, id_twitter, text, username, data_criacao, word)
			VALUES(DEFAULT, %i, '%s', '%s', now(),'%s');"""%( 
			resultado_busca_alternativa["results"][i]["from_user_id"],
			post,
			resultado_busca_alternativa["results"][i]["from_user"],
			#resultado_busca_alternativa["results"][i]["created_at"],
			WORD)
	try:
		cursor.execute(statement)
		mydb.commit()
	except:		
		print " - Error ao inserir no banco."
		# escreveLog(" - Error ao inserir no banco.")
		
statement = """SELECT access_token ,secret_token FROM clients ORDER BY rand() LIMIT 1"""
# print statement
cursor.execute(statement)
tokens = cursor.fetchone()

statement = """SELECT id_twitter, COUNT(username) as qtd, username, word FROM temp_search WHERE word= '%s' GROUP BY username ORDER BY qtd DESC LIMIT 25"""%(WORD)
# print statement
cursor.execute(statement)
lista_usuarios = cursor.fetchall()

for users in lista_usuarios:
		
	try:
		twitter_access = twitter.Twitter(domain='api.twitter.com', api_version='1', auth=twitter.oauth.OAuth(tokens[0], tokens[1], consumer_key, consumer_secret))
		resultado_posts_ids = twitter_access.users.show(user_id=users[0],encoding='utf-8' )
	
		file = open("./profile/"+str(users[0])+".xml",'w')  
		file.write(resultado_posts_ids)
		file.close()	
	except:		
		print " - Error ao inserir no banco."
		# escreveLog(" - Error ao inserir no banco.")
	
	
arquivos = Dir().read("./profile", "xml")

for arquivo in arquivos:
	
	# print arquivo[10:]
	tree = ElementTree(file="./profile/" + arquivo[10:])
	root = tree.getroot()
	
	id = root.find('id')
	profile_image_url = root.find('profile_image_url')
	location = root.find('location')
	screen_name = root.find('screen_name')
	protected = root.find('protected')
	friends_count = root.find('friends_count')
	followers_count = root.find('followers_count')
	description = root.find('description')
	statuses_count = root.find('statuses_count')
	lang = root.find('lang')
	url = root.find('url')
	
	descricao = description.text
	descricao = trataPalavra(descricao)
	# descricao = trataCodigosHTML(descricao)
		
	statement = """INSERT INTO users(id, id_twitter, profile_image_url, location, username, protected, friends_count, follower_count, status, description, statuses_count, lang, url, search) VALUES(DEFAULT, %i,'%s','%s','%s','%s', %i, %i, 0, '%s', %i, '%s', '%s', 1);"""%( int(id.text), 
	profile_image_url.text, location.text, screen_name.text, protected.text, int(friends_count.text),int(followers_count.text), descricao, int(statuses_count.text), lang.text, url.text)
	
	# print statement
	
	try:
		cursor.execute(statement)
		mydb.commit()	
	except:		
		print " - Error ao inserir no banco."
		# escreveLog(" - Error ao inserir no banco.")
		
mydb.close()
