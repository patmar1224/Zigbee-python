#from json import loads
#import urllib.request
#from urllib import parse
#from urllib import request
import json
import requests 
from pytz import timezone
import os

#libreruas para los hilos
import threading
import time


"""
Query deCONZ Zigbee Gateway specificly for AQARA Multi Sensor, which provides
temperature, humidity and pressure data.

Query via deCONZ REST API

"""

___version___ = 0.3

# General Configuration
deconzServerIPandPort = '192.168.1.109:80'
deconzAPIKey = 'CC95679D0E' 

# Static Sensor Information
bombillaIdentifier = "IKEA of Sweden"
bombillaModelID = "TRADFRI bulb E14 CWS 470lm"
bombillaType = "Extended color light"


# API URL
url = 'http://' + deconzServerIPandPort + '/api/' + deconzAPIKey + '/lights/'
#url_state = url + '68:0a:e2:ff:fe:59:86:ac-01/state'

def conectar_bombilla():
    
    res = requests.post(url).json()
    print(res)
    #print(getEnvSensors)

def getAPIResult_bombilla():

    """Function to get the REST API result needed from 'url'"""

    # Get data from REST API
    restApiUrlOpen = requests.get(url, timeout=5).json()
    return restApiUrlOpen

def getModelo_bombilla():
    
    contents = getAPIResult_bombilla()
    
    for key, value in contents.items():

        # Convert Key values (based on REST API return of "url")
        contentsBombillaIdentifier = contents[key]['manufacturername']
        contentsBombillaModelID = contents[key]['modelid']
        

        if contentsBombillaIdentifier == bombillaIdentifier and contentsBombillaModelID == bombillaModelID:
            modelo = str(contentsBombillaIdentifier)
            
        else:
            modelo = 0
  
    print(modelo)
    return modelo
            
    
def getEnvSensors_bombilla():

    contents = getAPIResult_bombilla()

    EnvSensorNames_bombilla = []
    for key, value in contents.items():

        # Convert Key values (based on REST API return of "url")
        contentsBombillaIdentifier = contents[key]['manufacturername']
        contentsBombillaModelID = contents[key]['modelid']
        contentsBombillaName = contents[key]['name']
        contentsBombillaType = contents[key]['type']
        

        if contentsBombillaIdentifier == bombillaIdentifier and contentsBombillaModelID == bombillaModelID:

            if contentsBombillaType == bombillaType:

                # Append Sensor name to List
                EnvSensorNames_bombilla.append(contentsBombillaName)
                id_bombilla = contents[key]['uniqueid']
                
    # Convert to uniqe entries only
    EnvSensorNames_bombilla = list(set(EnvSensorNames_bombilla))
    
    #print("El nombre de la bombilla es:" + str(EnvSensorNames_bombilla) + "el id de la bombilla es:" + str(id_bombilla) )
    
    return EnvSensorNames_bombilla, id_bombilla


def getEnvSensorValues_bombilla():
   
    data = getAPIResult_bombilla()
            
    for key, value in data.items():

        dataBombilla = data[key]['name']
        dataBombillaType = data[key]['type']
        
        #version = data[key]['swversion']
        (bombillaName, id_b) = getEnvSensors_bombilla()
            
            
        for i in range(len(bombillaName)):
                
            if dataBombilla == bombillaName[i] and dataBombillaType == bombillaType:
                bri = (data[key]['state']['bri'])
                sat = (data[key]['state']['sat'])
                col = (data[key]['state']['hue'])
                ct = (data[key]['state']['ct'])
                mode = (data[key]['state']['colormode'])
                on_off = (data[key]['state']['on'])
    
    return int(sat), int(bri), int(col), int(ct), str(mode), bool(on_off)
                
                
                
def url_state():
    (m,i) = getEnvSensors_bombilla()
    url_id = url + i +'/state'
    
    return url_id
#Establecer estados de luz
#put
def saturacion(n):

    datos = {"sat":n}
    requests.put(url_state(), json = datos).json()

def cambiar_color(x, y):

    data = {"xy":[x,y]}
    requests.put(url_state(), json = data)

def brillo(n):
    
    data = {"bri":n}
    requests.put(url_state(), json = data)

def efecto(n):
    
    data = {"effect":"colorloop","colorloopspeed":n}
    requests.put(url_state(), json = data)

def temperatura(n):
    #ctmin = 0 y ctmax = 65279
    data = {"ct":1000000/n}
    requests.put(url_state(), json = data)
    
def hue(n):
    #max 65535
    data = {"hue":n}
    requests.put(url_state(), json = data)
    
def apagar():

    data = {"on":False}
    requests.put(url_state(), json = data)
    
def encender():

    data = {"on":True}
    requests.put(url_state(), json = data)
    
def delete_bombilla():
    
    data_delete = getAPIResult_bombilla()
    model = getModelo_bombilla()
    
    if model == "IKEA of Sweden":
        (m,i) = getEnvSensors_bombilla()
          
        url_delete = url + i
        d1 = requests.delete(url_delete)


#getModelo_bombilla()
#getEnvSensors_bombilla()
#saturacion(0)

#cambiar_color(1,1)

#temperatura(3000)
#getEnvSensors_bombilla()
#hue(50000)
#brillo(0)
#apagar()

#delete_bombilla()
#conectar_bombilla()
#getModelo_bombilla()