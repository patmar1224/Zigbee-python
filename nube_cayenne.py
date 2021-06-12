#Prueba de la nube -> myDevices.com
#Librerias
import paho.mqtt.client as mqtt
import time
#Información sacada diredctamente de la plataforma myDevices
user = '507bf1f0-c86e-11eb-a2e4-b32ea624e442'
password = 'bd1072f590c780114182b3c91868ed6c21488f5f'
client_id = '6a5cd660-ca22-11eb-8779-7d56e82df461'
server = 'mqtt.mydevices.com'
port = 1883

publish_0 = 'v1/' + user + '/things/' + client_id + '/data/0' #Valor temperatura
publish_1 = 'v1/' + user + '/things/' + client_id + '/data/1' #Valor humedad
publish_2 = 'v1/' + user + '/things/' + client_id + '/data/3' #Valor presion
publish_3 = 'v1/' + user + '/things/' + client_id + '/data/4' #Valor presion

publish_boton = 'v1/' + user + '/things/' + client_id + '/data/2'
subscribe_boton = 'v1/' + user + '/things/' + client_id + '/cmd/2'

def valor_nube(t,h,p,b):
    client.publish(publish_0,t)
    client.publish(publish_1,h)
    client.publish(publish_2,p)
    client.publish(publish_3,b)

def mensagens(client, userdata, msg): 
    m = msg.topic.split('/')
    p = msg.payload.decode().split(',')
    print(m)
    print(p)
    client.publish(publish_boton, p[1])
    print(p[1])
    
client = mqtt.Client(client_id)
client.username_pw_set(user, password)
client.connect(server, port)

client.on_message = mensagens
client.subscribe(subscribe_boton)

client.loop_start()

# for i in range(1, 10):
#     client.publish(publish_0,i)
#     client.publish(publish_1,i*2.1)
#     time.sleep(2)

