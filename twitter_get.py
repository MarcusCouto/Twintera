# _*_econding:utf8_*_
import urllib2
import json
import time

'''headers = { 'Host':'search.twitter.com','User-Agent':'Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0','Accept':'application/xml;q=0.9,*/*;q=0.8','Accept-Language':'pt-br,pt;q=0.5','Accept-Charset':'utf-8;q=0.7,*;q=0.7'}
'''


init = time.time()
headers={}

req = urllib2.Request('http://search.twitter.com/search.json?q=%23microblogging&result_type=mixed&rpp=200', None, headers)



text = urllib2.urlopen(req).read()
print json.dumps(text, sort_keys=True, indent=4)

# print x

file = open("arquivo.txt",'w')  
file.write(x)
file.close()
fim = time.time()

print "TEMPO TOTAL: "+str(fim-init)
