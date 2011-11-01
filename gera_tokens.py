# !/usr/bin/python
# -*- coding: utf-8 -*-

import nltk
from nltk.stem import SnowballStemmer
import MySQLdb
import re
import sys
from function import *

stopwords = nltk.corpus.stopwords.words('portuguese')
palavras_excluidas = ['caralho','porra', 'puta','pariu', 'cu','cacete', 'buseta','sexo','xereca','fuder','fudido','!','#','$','%','&','*','(',')','.','<','>',':',';','.',',','~','{','}','[',']','/','http',	'^','-','_','+','=','`','0','1','2','3','4','5','6','7','8','9','?','@','RT','pq','vc','so','!']

mydb = MySQLdb.connect(host="localhost", user="root", passwd="server@bd", db="mydb") 
cursor = mydb.cursor() 

statement = """TRUNCATE  last_posts; """
cursor.execute(statement)

statement = """SELECT users_id, id_twitter, criacao_data, text  FROM (SELECT * FROM  posts ORDER BY criacao_data DESC)x GROUP BY users_id;"""
cursor.execute(statement)
post_id = cursor.fetchall()

for bck_post in post_id:
	statement = """INSERT INTO last_posts(users_id, id_twitter, criacao_data, post)VALUES(%i, %i, '%s', '%s');"""%(bck_post[0], int(bck_post[1]), bck_post[2], bck_post[3])
	cursor.execute(statement)
	mydb.commit()	


statement = """SELECT u.id_twitter, u.username, p.criacao_data, p.text, p.id  FROM users u INNER JOIN posts p ON u.id_twitter = p.users_id WHERE p.status = 0  LIMIT 2000;"""
cursor.execute(statement)
results = cursor.fetchall()

palavras = []
lixo=[]

for resultado in results:

	tokens = resultado[3].split()
	list_tokens = [variavel for variavel in tokens if variavel not in palavras_excluidas]	
	list_tokens = [variavel for variavel in list_tokens if variavel not in stopwords]		
	
	for word in list_tokens:
	
		word = word.lower()	
		
				
		if word[:7] == "http://":
			statement = """INSERT INTO temp_links(id, token, id_twitter, data_criacao)VALUES(DEFAULT, '%s', %i, '%s');"""%( word, resultado[0],resultado[2])
			cursor.execute(statement)
			mydb.commit()	
			
		elif word[:1] == "@":
			word = trataPalavra(word)
			statement = """INSERT INTO temp_mention(id, token, id_twitter, data_criacao)VALUES(DEFAULT, '%s', %i, '%s');"""%( word, resultado[0], resultado[2])
			cursor.execute(statement)
			mydb.commit()	
		
		elif word[:1] == "#":
			word = trataPalavra(word)
			statement = """INSERT INTO temp_hashtag(id, token, id_twitter, data_criacao)VALUES(DEFAULT, '%s', %i, '%s');"""%( word, resultado[0], resultado[2])
			cursor.execute(statement)
			mydb.commit()	
			
		elif re.search('[0-9]+',word,re.IGNORECASE):
			lixo.append(word)				
			
		else:
			word = trataPalavra(word)		
			statement = """SELECT COUNT(*), id from token WHERE token= '%s';"""%(word)
			cursor.execute(statement)
			dicionario = cursor.fetchone()
		
			#verifico se palavra existe no dicionario
			if dicionario[0] > 0:
				
				statement = """SELECT COUNT(quantidade), quantidade FROM users_token WHERE id_token = %i AND id_twitter = %i;"""%(dicionario[1], resultado[0])	
				cursor.execute(statement)
				palavraUsuario = cursor.fetchone()
				
				#verifico se usuario ja falou essa palavra				
				if  palavraUsuario[0]  != 0:
				
					novo_valor = palavraUsuario[1] + 1
					statement = """UPDATE users_token SET  data_criacao = '%s' AND quantidade = %i WHERE id_token = %i AND id_twitter = %i;"""%(resultado[2], novo_valor, dicionario[1], resultado[0])
					cursor.execute(statement)
					mydb.commit()
									
				else:										
					
					statement = """INSERT INTO users_token(id_token, id_twitter, data_criacao, quantidade)VALUES( %i, %i, '%s', 1);"""%(dicionario[1], resultado[0],resultado[2])
					cursor.execute(statement)
					mydb.commit()
								
			else:
				
				statement = """INSERT INTO token (token, id)VALUES('%s', DEFAULT);"""%(word)
				cursor.execute(statement)
				mydb.commit()	
				word_id = mydb.insert_id()
				
				statement = """INSERT INTO users_token(id_token, id_twitter, data_criacao, quantidade)VALUES( %i, %i, '%s', 1);"""%(word_id, resultado[0],resultado[2])
				cursor.execute(statement)
				mydb.commit()							
		
		statement = """DELETE FROM posts WHERE id = %i;"""%(int(resultado[4]))
		cursor.execute(statement)
		mydb.commit()		
		
mydb.close()	
