from xml.etree.ElementTree import ElementTree
import MySQLdb
import os, glob, re
import sys 
from string import maketrans 
from function import *
from exceptions import Exception
	
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

arquivos = Dir().read("/var/www/posts", "xml")

for arquivo in arquivos:
	print  arquivo[15:]
	tree = ElementTree(file="/var/www/posts/" + arquivo[15:])
	root = tree.getroot()
	status	= root.findall('status')
	for tag in status:
		created_at =tag.find('created_at')
		id = tag.find('id')
		text = tag.find('text')
		user = tag.find('user')
		user_id = user.find('id')	
		
		post_texto = text.text
		post_texto = post_texto.replace("'", "")
		post_texto = post_texto.replace("\"", "")
		post_texto = removeMarcacaoEncode(post_texto)
		post_texto = trataCodigosHTML(post_texto)
	
		#post_texto = post_texto.encode("iso-8859-1", "replace")		
		data_criacao = corrigeData(created_at.text)
		
		statement = """INSERT INTO posts(id, criacao_data, id_twitter, text, users_id) VALUES(DEFAULT, '%s', '%s', '%s', %i);"""%(data_criacao, id.text, post_texto, int(user_id.text))
		print statement
		try:
			cursor.execute(statement)
			mydb.commit()
		except:		
			escreveLog(" - Error ao inserir no banco.")
			
	os.remove("/var/www/posts/" + arquivo[15:])
	
mydb.close()
