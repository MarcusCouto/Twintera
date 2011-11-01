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
	
	dataPostagem  = corrigeDataPost(resultado_busca_alternativa["results"][i]["created_at"])
			
	statement = """INSERT INTO busca_externa(id, id_twitter, username, profile_image_url, text, data_criacao, word)VALUES(DEFAULT, %i, '%s', '%s', '%s', '%s','%s');"""%( 
			int(resultado_busca_alternativa["results"][i]["from_user_id"]),
			resultado_busca_alternativa["results"][i]["from_user"],
			resultado_busca_alternativa["results"][i]["profile_image_url"],
			post,
			dataPostagem,
			WORD)
	print statement
	try:
		cursor.execute(statement)
		mydb.commit()
	except:		
		 escreveLog(" - Error ao inserir no banco.")		
mydb.close()
