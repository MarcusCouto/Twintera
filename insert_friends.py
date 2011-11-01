from xml.etree.ElementTree import ElementTree
import MySQLdb
import os, glob, re
import sys 
from string import maketrans 
from exceptions import Exception
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

print "entrou no insert friends"

arquivos = Dir().read("/var/www/profile", "xml")

for arquivo in arquivos:
	
	tree = ElementTree(file="/var/www/profile/" + arquivo[17:])
	root = tree.getroot()
	id = root.find('id')
	
	
	statement = """SELECT COUNT(*) FROM users WHERE id_twitter = %i"""%( int(id.text))
	cursor.execute(statement)
	result = cursor.fetchone()

	if result[0] == 0:
		created_at = root.find('created_at')
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
		
		try:
			descricao = str(description.text)	
			
			if "'" in descricao:
				descricao = descricao.replace("'", " ")
			if '"' in descricao:
				descricao = descricao.replace('"', ' ')
				
			descricao = removeMarcacaoEncode(descricao)
			descricao = trataCodigosHTML(descricao)					
			
		except:
				descricao = "None"
				
		try:
			local = location.text
			
			if "'" in local:
				local = local.replace("'", " ")
			if '"' in local:
				local = local.replace('"', ' ')			
			
		except:
				descricao = "None"
			
		data_criacao = created_at.text
		data_criacao = corrigeData(data_criacao)
			
		try:
			statement = """INSERT INTO users(id, id_twitter, profile_image_url, location, username, protected, friends_count, follower_count, status, description, statuses_count, lang, url, data_criacao) VALUES(DEFAULT, %i,'%s','%s','%s','%s', %i, %i, 0, '%s', %i, '%s', '%s','%s');"""%( int(id.text), 
			profile_image_url.text, local, screen_name.text, protected.text, int(friends_count.text),int(followers_count.text), descricao, int(statuses_count.text), lang.text, url.text, data_criacao)

			#print statement
			cursor.execute(statement)
			mydb.commit()	
		except:	
			escreveLog("Erro o perfil do usuario id_twitter - "+ id.text)
		
		os.remove("/var/www/profile/" + arquivo[17:])	
	
	else:
		escreveLog(" usuario ja inserido no sistema. Duplicacao de perfil - "+ str(id.text))			
	
	
mydb.close()
