import requests 
from datetime import datetime
import os
import time


"""
Query deCONZ Zigbee Gateway specificly for AQARA Multi Sensor, which provides
temperature, humidity and pressure data.

Query via deCONZ REST API

"""

___version___ = 0.3

# General Configuration
deconzServerIPandPort = '192.168.1.110:80'
deconzAPIKey = 'CC95679D0E' 

# Static Sensor Information
aqaraSesnorIdentifier = "LUMI"
aqaraSensorModelID = "lumi.weather"
aqaraSensorTypeTemperature = "ZHATemperature"
aqaraSensorTypeHumidty = "ZHAHumidity"
aqaraSensorTypePressure = "ZHAPressure"

# API URL
url = 'http://' + deconzServerIPandPort + '/api/' + deconzAPIKey + '/sensors/'

def conectar_sensor():
    
    res = requests.post(url).json()
    print(res)
    #print(getEnvSensors)

def getAPIResult():

    """Function to get the REST API result needed from 'url'"""

    # Get data from REST API
    restApiUrlOpen = requests.get(url, timeout=10).json()
    return restApiUrlOpen

def getModelo():
    contents = getAPIResult()
    for key, value in contents.items():

        # Convert Key values (based on REST API return of "url")
        contentsSensorIdentifier = contents[key]['manufacturername']
        contentsSensorModelID = contents[key]['modelid']
        contentsSensorName = contents[key]['name']
        contentsSensorType = contents[key]['type']
        

        if contentsSensorIdentifier == aqaraSesnorIdentifier and contentsSensorModelID == aqaraSensorModelID:
            modelo = str(contentsSensorIdentifier)
            
        else:
            modelo = 0
        
#         print(modelo)
    return modelo
            
    
def getEnvSensors():

    """Function to get a List - EnvSensorNames with all enviroment sensors names from the AQARA Sensor"""

    contents = getAPIResult()

    EnvSensorNames = []
    for key, value in contents.items():

        # Convert Key values (based on REST API return of "url")
        contentsSensorIdentifier = contents[key]['manufacturername']
        contentsSensorModelID = contents[key]['modelid']
        contentsSensorName = contents[key]['name']
        contentsSensorType = contents[key]['type']
        

        if contentsSensorIdentifier == aqaraSesnorIdentifier and contentsSensorModelID == aqaraSensorModelID:

            if contentsSensorType == aqaraSensorTypeTemperature or contentsSensorType == aqaraSensorTypeHumidty or contentsSensorType == aqaraSensorTypePressure:

                # Append Sensor name to List
                EnvSensorNames.append(contentsSensorName)
 
    # Convert to uniqe entries only
    EnvSensorNames = list(set(EnvSensorNames))
    
    return EnvSensorNames


def getEnvSensorValues():
   
    hora = datetime.now()
    

    data = getAPIResult()
            
    for key, value in data.items():

        dataSensor = data[key]['name']
        dataSensorType = data[key]['type']
        
        #version = data[key]['swversion']
        sensorName = getEnvSensors()
            
            
        for i in range(len(getEnvSensors())):
                
            if dataSensor == sensorName[i] and dataSensorType == aqaraSensorTypeTemperature:
                temperatura = (data[key]['state']['temperature'])/100
                bateria = (data[key]['config']['battery'])

            elif dataSensor == sensorName[i] and dataSensorType == aqaraSensorTypeHumidty:
                humedad = (data[key]['state']['humidity'])/100
                    
            elif dataSensor == sensorName[i] and dataSensorType == aqaraSensorTypePressure:
                presion = (data[key]['state']['pressure'])/10
    
        
    hora_app = hora.strftime("%M.%S")
    global nombre_arc
    nombre_arc= hora.strftime("%d-%m-%Y_%H:%M:%S")
    segundos = hora.strftime("%S")
    global datos_arc
    datos_arc = "Datos del sensor " + str(dataSensor) + hora.strftime(" el día %d/%m/%Y a las %H:%M:%S")
    global temp_arc
    temp_arc = "TEMPERATURA " + str(temperatura) + "°C"
    global humed_arc
    humed_arc = "HUMEDAD " + str(humedad) + "%"
    global presion_arc
    presion_arc = "PRESIÓN ATMOSFÉRICA " + str(presion) + "kPa"
    global bat_arc
    bat_arc = "BATERIA " + str(bateria) + "%"
    
    print(datos_arc)
    print(temp_arc)
    print(humed_arc)
    print(presion_arc)
    print(bat_arc)
    
    return temperatura, humedad, presion, bateria

def delete_sensor():
    
    data_delete = getAPIResult()

    for key, value in data_delete.items():

        dataSensor = data_delete[key]['name']
        dataSensorType = data_delete[key]['type']
    
        #version = data[key]['swversion']
        sensorName = getEnvSensors()
        
        
        for i in range(len(getEnvSensors())):
            
            if dataSensor == sensorName[i] and dataSensorType == aqaraSensorTypeTemperature:
                id_temperatura = data_delete[key]['uniqueid']

            elif dataSensor == sensorName[i] and dataSensorType == aqaraSensorTypeHumidty:
                id_humedad = data_delete[key]['uniqueid']
                
            elif dataSensor == sensorName[i] and dataSensorType == aqaraSensorTypePressure:
                id_presion = data_delete[key]['uniqueid']
                
    url_delete = url + id_temperatura
    url_delete2 = url + id_humedad
    url_delete3 = url + id_presion
    d1 = requests.delete(url_delete)
    d2 = requests.delete(url_delete2)
    d3 = requests.delete(url_delete3)

def arc_nombre_sensores(datos):
    
    file = open("/home/pi/Desktop/Zigbee-python/lista_sensores.txt", "a")
    file.write(datos + os.linesep)
    #file.close()
    return

def listar_sensor():
    data_listar = getAPIResult()
    file = open("/home/pi/Desktop/Zigbee-python/lista_sensores.txt", "w").close()
    i=1
    for key, value in data_listar.items():
        sensor_names = data_listar[key]['name']
        sensor_id = data_listar[key]['manufacturername']
        sensor_model = data_listar[key]['modelid']
        #sensor_version = data_listar[key]['swversion']
        sensor_tipo = data_listar[key]['type']
        sens = "-Sensor "+str(i)+"\nNombre:" +sensor_names + "\nFabricante:" + sensor_id + "\nTipo:" + sensor_tipo +  "\nModelo:" + sensor_model + "\n"#+ "\nVersión:" + sensor_version
        #print(sens)
        i=i+1
        arc_nombre_sensores(sens)
        #leer_sensor()
    with open("/home/pi/Desktop/Zigbee-python/lista_sensores.txt",'r') as file:
        datos = file.read()
    
    return datos

def leer_sensor():
    with open("/home/pi/Desktop/Zigbee-python/lista_sensores.txt",'r') as file:
        datos = file.read()
    
    return datos
#listar_sensor()
#leer_sensor()
# print(getModelo())
# print(getEnvSensors())
#conectar_sensor()

#time.sleep(60)
#for a in range(121):
#    if a == 120:
#        print(getEnvSensors())
#print(getEnvSensors())
#getEnvSensorValues()
#delete_sensor()
#print(getEnvSensors())

