import networkx as nx
import matplotlib.pyplot as plt
from exceptions import Exception
from function import *
import MySQLdb
import os
import sys

try:
	PALAVRA = sys.argv[1]
except:
	print "Erro: Nao foi passado nenhum argumento"
	exit(1)
	
mydb = MySQLdb.connect(host="localhost", user="root", passwd="server@bd", db="mydb") 
cursor = mydb.cursor() 
G=nx.Graph()

try:
	statement = """SELECT u.id_twitter, u.username FROM users u INNER JOIN (SELECT COUNT(*) as qtd , id_twitter FROM users_token WHERE id_token = (SELECT id FROM token  WHERE  token = '%s') GROUP BY id_twitter ORDER BY qtd DESC)x ON u.id_twitter = x.id_twitter;"""%(PALAVRA)
	#print statement
	cursor.execute(statement)
	mydb.commit()
	
except:	
	print "Erro ao selecionar usuario id_twitter"
	exit(1)

total_resultados = cursor.fetchall()

for resultado in total_resultados:
	G.add_node(resultado[1])
	
	statement = """SELECT u.username FROM clients_users c INNER JOIN users u ON c.users_id = u.id_twitter WHERE c.clients_id = %i GROUP BY c.users_id"""%(resultado[0])
	cursor.execute(statement)
	mydb.commit()
	total_amigos = cursor.fetchall()
	for amigos in total_amigos:
		G.add_edge(amigos[0],resultado[1])

#G.add_edge(1,2)
#nx.draw(G)
nx.draw(G,node_color='#A0CBE2',width=2,edge_cmap=plt.cm.Blues)
plt.savefig("path.png")
#plt.show()
