# -*- coding: utf-8 -*-

import twitter
import json

#Realiza as buscas no twitter...
busca_aberta = twitter.Twitter(domain='search.twitter.com')

resultado_busca_aberta = busca_aberta.search(q="aqui", rpp=10, page=1, encoding='utf-8')

#transforma o resultado da busca do twitter em um objeto louco...
json.dumps(resultado_busca_aberta, sort_keys=True, indent=4)

#vamos iterar dentro desse objeto da seguinte forma:
#	{,,,,} são acessadas pela String que nomeia essa hash
#	[,,,,] são acessadas como um Array ou vetor em C por exemplo.
for i in range(len(resultado_busca_aberta["results"])):
	#printamos a hash id que está dentro do vetor posição i que esta dentro do result
	print "_______________________________________________________________________________"
	print resultado_busca_aberta["results"][i]["created_at"]
	print 
	print resultado_busca_aberta["results"][i]["text"]
	print 
	print resultado_busca_aberta["results"][i]["from_user_id"]
	

perfil_aberto = twitter.Twitter(domain='api.twitter.com', api_version='1')
resultado_perfil_aberto = perfil_aberto.statuses.public_timeline(screen_name='bueno_julio', encoding='utf-8')

print json.dumps(resultado_perfil_aberto, sort_keys=True, indent=4)
