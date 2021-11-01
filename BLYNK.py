import blynklib
from deconz_aqara_multisensor import *
from bombilla_ikea import *
from thingspeak import *
from nube_cayenne import *

# global blynk
# global BLYNK_AUTH
BLYNK_AUTH = 'Urq9JqZLJxaBKpjRXo1j6E8Va83bG0ec' # insert your Auth Token here

# initialize Blynk

blynk = blynklib.Blynk(BLYNK_AUTH)
#blynk.connect()


READ_PRINT_MSG = "[READ_VIRTUAL_PIN_EVENT] Pin: V{}"
WRITE_EVENT_PRINT_MSG = "[WRITE_VIRTUAL_PIN_EVENT] Pin: V{} Value: '{}'"

T_PIN = 1
H_PIN = 3
G_T_PIN = 2
G_H_PIN = 6
G_P_PIN = 7
B_PIN = 0
P_PIN = 5
C_PIN = 10
i=0
# register handler for virtual pin V11 reading
@blynk.handle_event('read V1')
def read_virtual_pin_handler_1(pin):
    print(READ_PRINT_MSG.format(pin))
    model = getModelo()
    
    if model == "LUMI":
        blynk.virtual_write(C_PIN, 1)
        (t,h,p,b) = getEnvSensorValues()
        blynk.virtual_write(pin, t)
        blynk.virtual_write(H_PIN, h)
        blynk.virtual_write(G_T_PIN, t)
        blynk.virtual_write(G_H_PIN, h)
        blynk.virtual_write(G_P_PIN, p)
        blynk.virtual_write(P_PIN, p)
        
    else:
        blynk.virtual_write(C_PIN, 1)
        blynk.virtual_write(pin, 0)
        blynk.virtual_write(H_PIN, 0)
        blynk.virtual_write(P_PIN, 10)
# @blynk.handle_event('write V4')
# def write_virtual_pin_handler_4(pin, value):
#     print(WRITE_EVENT_PRINT_MSG.format(pin, value))

@blynk.handle_event('write V0')
def write_virtual_pin_handler_0(pin, value):
    print(WRITE_EVENT_PRINT_MSG.format(pin, value))
    if value == ['1']:
        (t,h,p,b) = getEnvSensorValues()
        valor_nube(t,h,p,b)
        thingspeak_datos(t,h,p,0,1)
        blynk.virtual_write(T_PIN, t)
        blynk.virtual_write(H_PIN, h)
        blynk.virtual_write(G_T_PIN, t)
        blynk.virtual_write(G_H_PIN, h)
        blynk.virtual_write(G_P_PIN, p)
        blynk.virtual_write(P_PIN, p)
    
    
@blynk.handle_event('write V10')
def write_virtual_pin_handler_10(pin, value):
    print(WRITE_EVENT_PRINT_MSG.format(pin, value))
    print(value)
    if value == ['0']:
        #borro
        delete_sensor()
    else:
        conectar_sensor()
        
@blynk.handle_event('write V11')
def write_virtual_pin_handler_11(pin, value):
    print(WRITE_EVENT_PRINT_MSG.format(pin, value))
        
    if value == ['0']:
        #encender
        encender()
        thingspeak_datos(0,0,0,True,0)
    else:
        #apagar
        apagar()
        thingspeak_datos(0,0,0,False,0)
        
@blynk.handle_event('write V12')
def write_virtual_pin_handler_12(pin, value):
    print(WRITE_EVENT_PRINT_MSG.format(pin, value))
    brillo(int(value[0]))

    
@blynk.handle_event('write V13')
def write_virtual_pin_handler_13(pin, value):
    print(WRITE_EVENT_PRINT_MSG.format(pin, value))
    hue(int(value[0])*10)
    
@blynk.handle_event('write V14')
def write_virtual_pin_handler_14(pin, value):
    print(WRITE_EVENT_PRINT_MSG.format(pin, value))
    
    saturacion(int(value[0]))
    
@blynk.handle_event('write V15')
def write_virtual_pin_handler_15(pin, value):
    print(WRITE_EVENT_PRINT_MSG.format(pin, value))
    temperatura(int(value[0]))
    
###########################################################
# infinite loop that waits for event
###########################################################
def conect_blynk():
    while True:
        blynk.run()
