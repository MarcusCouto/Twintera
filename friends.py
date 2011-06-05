
import twitter
import json

perfil_aberto = twitter.Twitter(domain='api.twitter.com', api_version='1')
resultado_perfil_aberto = perfil_aberto.users.show(screen_name='bueno_julio', encoding='utf-8')

json.dumps(resultado_perfil_aberto, sort_keys=True, indent=4)

friends_ids = twitter.Twitter(domain='api.twitter.com', api_version='1')
resultado_friends_ids = friends_ids.friends.ids(user_id=resultado_perfil_aberto["id"], rpp=2, encoding='utf-8' )



json.dumps(resultado_friends_ids, sort_keys=True, indent=4)

# print resultado_friends_ids
print len(resultado_friends_ids)
for i in range(len(resultado_friends_ids)-2):
# for i in range(2):
	public_timeline = twitter.Twitter(domain='api.twitter.com', api_version='1')
	resultado_public_timeline = public_timeline.statuses.user_timeline(user_id=resultado_friends_ids[i], rpp=2, encoding='utf-8')
	json.dumps(resultado_public_timeline, sort_keys=True, indent=4)
	# print i
	# print resultado_public_timeline[i]
	# print resultado_public_timeline[i]['user']['screen_name']
	print resultado_public_timeline[10]
	
	

	#print resultado_perfil_aberto["id"]user_id