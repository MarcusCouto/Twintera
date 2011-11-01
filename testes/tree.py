from xml.etree.ElementTree import ElementTree
# import MySQLdb
import os, glob, re
import sys 
from string import maketrans 

	
class Dir:
  def read(self, dir, extension, files=[]):
    for f in glob.glob( os.path.join(dir, "*") ):

      if os.path.isdir( f ):
        files = self.read( f, extension, files )
      else:
        if f.endswith(".%s" % extension):
          files.append( f )

    return files

# mydb = MySQLdb.connect(host="localhost", user="root", passwd="server@bd", db="mydb") 
# cursor = mydb.cursor() 


arquivos = Dir().read("./arquivos", "xml")

for arquivo in arquivos:


	tree = ElementTree(file="./arquivos/" + arquivo[11:])
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
		post_texto = post_texto.replace("0x2026", "...")
		# post_texto = post_texto.translate(charmap)
		# post_texto = post_texto.encode("iso-8859-11", "replace")
		print post_texto
		# statement = """INSERT INTO posts(id, criacao_data, id_twitter, text, users_id) VALUES(DEFAULT, '%s', '%s', '%s', %i);"""%( created_at.text, id.text, post_texto, int(user_id.text))
		# print statement
		# cursor.execute(statement)
		# smydb.commit()	
		
	# os.remove("./arquivos/" + arquivo[11:])
	
	