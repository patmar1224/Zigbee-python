import requests 
import time

APIKey_read = 'YJ51881ROCGYVH92'
APIKey_write = 'D60K51CD04ZGH3HY'

url_write = 'https://api.thingspeak.com/update?api_key=' + APIKey_write


def thingspeak_datos(temperatura,humedad,presion):
    env_datos = url_write+ '&field1=' + str(temperatura) + '&field2=' + str(humedad) + '&field3=' + str(presion) 
    requests.get(env_datos)
