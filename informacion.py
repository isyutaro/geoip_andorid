#!/usr/bin/env python
#BUSCARIN  v1.0 
#codificada por arthas1000 para sl4a 
#shiftshell@gmail.com
#basado en el script de cmartorella@edge-security.com geoedge v0.2
#disponible  aqui : http://www.edge-security.com/soft/geoedge.py 
#AGREGADO SOPORTE PARA PLATAFORMA ANDROID 
#AGREGADO SISTEMA DE VOZ 

# -*- coding: utf-8 -*-

#LA LIBRERIA STRING ES PARA MANEJO DE TIEMPO 
#PERMITE MANTENER LA PANTALLA X SEGUNDOS
#USANDO EL COMANDO sleep(argumento)
import sys
import re
import httplib
import android
import string
import time

#nuestra hermosa ayuda 
def manifesto():
  arriba = 'geolocalizador'
  ayudita = 'con grandes poderes vienen grandes responsabilidades'
  droid.dialogCreateAlert(arriba , ayudita)
  droid.dialogSetPositiveButtonText('Acepto')
  droid.dialogShow()
  response = droid.dialogGetResponse().result

#solicitamos la pagina web 
def solicitud ():
  paginaweb = droid.dialogGetInput('DATOS', 'Escriba la direccion web:', None).result
  #guarda nuestra pagina web 
  direccion = open('direccion.txt','wt+')
  direccion.write(paginaweb)
  direccion.close()
  #vibra al terminar 
  result = droid.vibrate()
 
def buscando():
  #creamos titulosapantalladores
  title1 = 'Buscando'
  message1 = 'geolocalizando'
  #un spinner para dar emocion 
  droid.dialogCreateSpinnerProgress(title1,message1)
  droid.dialogShow()
  #quedure unos dos segundos
  time.sleep(1)
  droid.dialogDismiss()
	
  #he aqui el pex  jean  no quiero que use el sys.argv   de  informacion2.py 
def informacion():
  host2 =open('direccion.txt','r')
  host = host2.read()
  print host 
  body="ips="+host
  print "Buscando en  Geoiptool....\n"
  try:
    h = httplib.HTTP("www.geoiptool.com")
    h.putrequest('GET',"/es/?IP="+ host )
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
    arriba3 = ' :( '
    ayudita3 = 'Error de conexion '
    droid.dialogCreateAlert(arriba3 , ayudita3)
    droid.dialogSetPositiveButtonText('KO')
    droid.dialogShow()
    response = droid.dialogGetResponse().result		

if __name__ == '__main__':
  droid = android.Android()
  manifesto()
  solicitud()
  buscando()
  informacion()
