#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Geoedge v1.0 
#codificada por arthas1000 para sl4a 
#shiftshell@gmail.com
#basado en el script de cmartorella@edge-security.com geoedge v0.1
#AGREGADO SOPORTE PARA PLATAFORMA ANDROID 
#AGREGADO SISTEMA DE VOZ 
#implementado  gmaps

import sys
import re
import httplib
import os
 
 
        
#if len(sys.argv) < 2:
#	sys.exit()

#webi=sys.argv[1]
#cmd=sys.argv[1]


pagina = open('direccion.txt','r')
direccion = pagina.read()
webi = direccion
body= "ips="+ webi
print "Buscando en  Geoiptool....\n"
try:

	h = httplib.HTTP("www.geoiptool.com")
	h.putrequest('GET',"/es/?IP="+ webi )
	h.putheader('Host', 'www.geoiptool.com')
	h.putheader('User-agent', 'Internet Explorer 6.0 ')
	h.endheaders()
	returncode, returnmsg, headers = h.getreply()
	response=h.file.read()
	
	res=re.compile("<td align=\"left\" class=\"arial_bold\">.*</td>")
	results=res.findall(response)
	res=[]
	for x in results:
		x=x.replace("<td align=\"left\" class=\"arial_bold\">","")
		x=x.replace("</td>","")
		res.append(x)

	print "Informacion de  Geoiptool"
	print "========================\n"
	print "IP/Host: "+res[0]
	country=re.sub("<.*nk\">","",res[1])
	country=country.replace("</a>","")
	country=re.sub("<.*middle\" >","",country)
	print "Pais: " + country + ","+ res[2]
	city=re.sub("<.*nk\">","",res[3])
	city=city.replace("</a>","")
	print "Ciudad: " + city + ","+ res[4]
	print "Coordenadas: " + res[8] + ","+res[7]
	print "\n"

except:
	print "Error de conexion..\n"



