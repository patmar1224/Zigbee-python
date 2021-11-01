#Prueba de la nube -> myDevices.com
#Librerias
import paho.mqtt.client as mqtt
#import time
from bombilla_ikea import *

#Información sacada diredctamente de la plataforma myDevices
user = '507bf1f0-c86e-11eb-a2e4-b32ea624e442'
password = 'bd1072f590c780114182b3c91868ed6c21488f5f'
client_id = '6a5cd660-ca22-11eb-8779-7d56e82df461'
server = 'mqtt.mydevices.com'
port = 1883

publish_0 = 'v1/' + user + '/things/' + client_id + '/data/0' #Valor temperatura
publish_1 = 'v1/' + user + '/things/' + client_id + '/data/1' #Valor humedad
publish_2 = 'v1/' + user + '/things/' + client_id + '/data/3' #Valor presion
publish_3 = 'v1/' + user + '/things/' + client_id + '/data/4' #Valor bateria

publish_boton = 'v1/' + user + '/things/' + client_id + '/data/2' #ON/OFF bombilla 
subscribe_boton = 'v1/' + user + '/things/' + client_id + '/cmd/2'

publish_slider = 'v1/' + user + '/things/' + client_id + '/data/5' #Barra brillo
subscribe_slider = 'v1/' + user + '/things/' + client_id + '/cmd/5'

publish_sat = 'v1/' + user + '/things/' + client_id + '/data/6' #Barra saturación
subscribe_sat = 'v1/' + user + '/things/' + client_id + '/cmd/6'

publish_temp = 'v1/' + user + '/things/' + client_id + '/data/7' #Barra temperatura
subscribe_temp = 'v1/' + user + '/things/' + client_id + '/cmd/7'

publish_color = 'v1/' + user + '/things/' + client_id + '/data/8' #Barra color
subscribe_color = 'v1/' + user + '/things/' + client_id + '/cmd/8'


def valor_nube(t,h,p,b):
    client.publish(publish_0,t)
    client.publish(publish_1,h)
    client.publish(publish_2,p)
    client.publish(publish_3,(b))

def mensagens(client, userdata, msg):
    #client.publish(publish_boton,1)
    m = msg.topic.split('/')
    p = msg.payload.decode().split(',')

    channel = m[5]
    
    print(p[1])
    print(channel)
    
    if channel == '5':
        brillo(int(p[1]))
        
    elif channel == '2':
        print('hola')
        if p[1] == '1':
            encender()
            thingspeak_datos(0,0,0,True,0)
        else:
            apagar()
            thingspeak_datos(0,0,0,False,0)
            
    elif channel == '6':
        saturacion(int(p[1]))
        print(p[1])
    
    elif channel == '7':
        temperatura(int(p[1]))
        
    elif channel == '8':
        hue(int(p[1]))
        
#     p[1]=1
     
#     print(p[1])
    #client.subscribe(subscribe_boton)
    
    
client = mqtt.Client(client_id)
client.username_pw_set(user, password)
client.connect(server, port)

client.on_message = mensagens

client.subscribe(subscribe_slider)
client.subscribe(subscribe_boton)
client.subscribe(subscribe_color)
client.subscribe(subscribe_temp)
client.subscribe(subscribe_sat)

client.loop_start()

# for i in range(1, 10):
#     client.publish(publish_0,i)
#     client.publish(publish_1,i*2.1)
#     time.sleep(2)

