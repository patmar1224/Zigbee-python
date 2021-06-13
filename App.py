import sys
from PyQt5 import uic #Carga la aplicación del Qt designer
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QMessageBox, QTableWidgetItem #Para cargar la aplicación
from PyQt5.QtGui import QCursor
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QTimer
from App_GUI import Ui_MainWindow
from PyQt5 import QtGui, QtCore, QtWidgets
import matplotlib.pyplot as plt
from deconz_aqara_multisensor import *
from bombilla_ikea import *
from datetime import datetime
import datetime
import matplotlib.dates as mdates
import numpy as np
from nube_cayenne import *
#import qtawesome as qta


class ejemplo_GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        #uic.loadUi ("App_GUI.ui", self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.stackedWidget.setCurrentWidget(self.ui.sensor)
        self.ui.stackedWidget.setCurrentWidget(self.ui.bombilla)
        self.ui.stackedWidget.setCurrentWidget(self.ui.home)
        
        self.ui.boton_sensor.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.sensor))
        self.ui.boton_luz.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.bombilla))
        self.ui.boton_atras_sensor.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.home))
        self.ui.boton_atras_luz.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.home))
        self.ui.boton_actualizar_datos_sensor.clicked.connect(self.env_datos_sensor)
        self.ui.boton_actualizar_datos_sensor_auto.clicked.connect(self.refresco_auto)
        self.ui.boton_borrar_sensor.clicked.connect(self.borrar_sensor)
        self.ui.boton_anadir_sensor.clicked.connect(self.conectar)
        self.ui.boton_borrar_bomb.clicked.connect(self.borrar_bombilla)
        self.ui.boton_anadir_bomb.clicked.connect(self.conectar_bomb)
        self.ui.boton_borrar_tabla.clicked.connect(self.borrar_tabla)
        self.ui.boton_bomb_on.clicked.connect(self.encender_bombilla)
        self.ui.boton_bomb_off.clicked.connect(self.apagar_bombilla)
        self.ui.checkBox_escena.stateChanged.connect(self.funcion_ModoAuto)
        self.ui.Spinbox_escena.editingFinished.connect(self.funcion_ModoAuto)
        self.ui.pantalla_conectar = Pantalla_conectar()
        self.ui.bombilla_conectar = Bombilla_conectar()
        
        #slider
        m = getModelo_bombilla()
        if m == "IKEA of Sweden":
            (satur, bril, col, ct, mod, on_bomb) = getEnvSensorValues_bombilla()
            if mod == "ct":
                brillo(bril)
                temperatura(ct)
            else:
                saturacion(satur)
                hue(col)
                brillo(bril)
        
        #Valor de la barra del brillo en modo color
        self.ui.brillo_slider.setMinimum(0)
        self.ui.brillo_slider.setMaximum(255)
        self.ui.brillo_slider.setSingleStep(1)
        self.ui.brillo_slider.setValue(0)
        self.ui.brillo_slider.valueChanged.connect(self.valor_brillo)
        
        #Valor de la barra del brillo en modo blanco
        self.ui.brillo_blanco_slider.setMinimum(0)
        self.ui.brillo_blanco_slider.setMaximum(255)
        self.ui.brillo_blanco_slider.setSingleStep(1)
        self.ui.brillo_blanco_slider.setValue(0)
        self.ui.brillo_blanco_slider.valueChanged.connect(self.valor_brillo_blanco)
        
        #Valor de la barra de temperatura
        self.ui.temp_slider.setMinimum(1000)
        self.ui.temp_slider.setMaximum(5000)
        self.ui.temp_slider.setSingleStep(1)
        self.ui.temp_slider.setValue(1000)
        self.ui.temp_slider.valueChanged.connect(self.valor_temp)
        
        #Valor de la barra de saturación
        self.ui.satur_slider.setMinimum(0)
        self.ui.satur_slider.setMaximum(255)
        self.ui.satur_slider.setSingleStep(1)
        self.ui.satur_slider.setValue(255)
        self.ui.satur_slider.valueChanged.connect(self.valor_satur)
        
        #Valor de la barra de color
        self.ui.color_slider.setMinimum(0)
        self.ui.color_slider.setMaximum(65535)
        self.ui.color_slider.setSingleStep(1)
        self.ui.color_slider.setValue(0)
        self.ui.color_slider.valueChanged.connect(self.valor_color)
        
        #Valor de la barra de brillo en la escena 
        self.ui.brillo_blanco_slider_escena.setMinimum(0)
        self.ui.brillo_blanco_slider_escena.setMaximum(255)
        self.ui.brillo_blanco_slider_escena.setSingleStep(1)
        self.ui.brillo_blanco_slider_escena.setValue(0)
        self.ui.brillo_blanco_slider_escena.valueChanged.connect(self.valor_blanco_escena)
        
        #Valor de la barra de temperatura 
        self.ui.temp_slider_escena.setMinimum(1000)
        self.ui.temp_slider_escena.setMaximum(5000)
        self.ui.temp_slider_escena.setSingleStep(1)
        self.ui.temp_slider_escena.setValue(1000)
        self.ui.temp_slider_escena.valueChanged.connect(self.valor_blanco_escena)
        
        #Timer refresco automatico 
        self.ui.timer=QTimer()
        self.ui.timer.timeout.connect(self.env_datos_sensor)
        
        #Pintar ejes de la grafica
        self.figura = self.ui.grafica.canvas.fig
        
        #Valores del eje X en horas
        x = ["00:00", "02:00", "04:00", "06:00", "08:00", "10:00", "12:00","14:00", "16:00", "18:00", "20:00", "22:00", "23:59"]
        dates_graf = [datetime.datetime.strptime(h, "%H:%M") for h in x]
        
        #Añadir las graficas que quiero
        self.ejes=self.figura.add_subplot(312)
        self.ejes2=self.figura.add_subplot(311)
        self.ejes3=self.figura.add_subplot(313)
        
        #Formato del eje X en horas
        #Gráfica humedad
        xformater = mdates.DateFormatter('%H:%M')
        self.ejes.xaxis.set_major_formatter(xformater)
        self.ejes.set_xlim((min(dates_graf) - datetime.timedelta(hours=1),max(dates_graf) + datetime.timedelta(hours=1)))
        self.ejes.set_ylim([0, 100])
        self.ejes.set(ylabel='Humedad(%)')
        self.ejes.grid()
        
        #Gráfica de temperatura
        self.ejes2.xaxis.set_major_formatter(xformater)
        self.ejes2.set_xlim((min(dates_graf) - datetime.timedelta(hours=1),max(dates_graf) + datetime.timedelta(hours=1)))
        self.ejes2.set_ylim([-20,50])
        self.ejes2.set(title='Datos del sensor')
        self.ejes2.set(ylabel='Temperatura(°C)')
        self.ejes2.grid()
        
        #Gráfica de presión
        self.ejes3.xaxis.set_major_formatter(xformater)
        self.ejes3.set_xlim((min(dates_graf) - datetime.timedelta(hours=1),max(dates_graf) + datetime.timedelta(hours=1)))
        self.ejes3.set_ylim([30,110])
        self.ejes3.set(ylabel='Presión (kPa)')
        self.ejes3.set(xlabel='Hora')
        self.ejes3.grid()
        
    def funcion_ModoAuto(self):
        global MedidaAutomatica
        
        if self.ui.checkBox_escena.isChecked()==True:
            MedidaAutomatica=True
            
        else:
            MedidaAutomatica=False
                
        
    def valor_blanco_escena(self):
        value = self.ui.brillo_blanco_slider_escena.value()
        self.ui.valor_brillo_blanco_escena.setText(str(value))
        
        value2 = self.ui.temp_slider_escena.value()
        self.ui.valor_temp_brillo_escena.setText(str(value2))
        
        return value, value2
    
    def encender_bombilla(self):
        encender()
        
    def apagar_bombilla(self):
        apagar()
        
    def valor_temp(self):
        value = self.ui.temp_slider.value()
        self.ui.valor_temp_blanco.setText(str(value))
        
        if getModelo_bombilla() == "IKEA of Sweden":
            temperatura(int(value))
        
    def valor_brillo(self):
        value = self.ui.brillo_slider.value()
        self.ui.valor_brillo.setText(str(value))
        m = getModelo_bombilla()
        if m == "IKEA of Sweden":
            brillo(int(value))
        
    def valor_brillo_blanco(self):
        value = self.ui.brillo_blanco_slider.value()
        self.ui.valor_brillo_blanco.setText(str(value))
        m = getModelo_bombilla()
        if m == "IKEA of Sweden":
            brillo(int(value))
    
    def valor_color(self):
        value = self.ui.color_slider.value()
        self.ui.valor_color.setText(str(value))
        m = getModelo_bombilla()
        if m == "IKEA of Sweden":
            hue(int(value))
    
    def valor_satur(self):
        value = self.ui.satur_slider.value()
        self.ui.valor_satur.setText(str(value))
        m = getModelo_bombilla()
        if m == "IKEA of Sweden":
            saturacion(int(value))
        
    def borrar_tabla(self):
        self.ui.tabla_sensor_datos.clearContents()
        fila=self.ui.tabla_sensor_datos.rowCount()
        for fila in range (-1, self.ui.tabla_sensor_datos.rowCount()):
            self.ui.tabla_sensor_datos.removeRow(fila)
            self.ui.tabla_sensor_datos.removeRow(0)
            fila-=1
    
    def env_datos_sensor(self):
        print("Envio datos")
        model = getModelo()
        print(model)
        
        if model == "LUMI":
            (t, h, p, b) = getEnvSensorValues()
            
            #Mostrar datos
            self.ui.etiqueta_conexion.setText("El sensor esta conectado")
            self.ui.texto_temperatura_dato.setText(str(t))
            self.ui.texto_humedad_dato.setText(str(h))
            self.ui.texto_presion_dato.setText(str(p))
            self.ui.texto_bateria_dato.setText(str(b))
            
            #Valores de la nube
            valor_nube(t,h,p,b)
            
            #Escena
            if MedidaAutomatica == True:
                if self.ui.Spinbox_escena.value() == t:
                    encender()
                    #Poner los valores que se han establecido
                    (bri_esc,temp_esc) = self.valor_blanco_escena()
                    brillo(bri_esc)
                    temperatura(temp_esc)
#                 else:
#                     apagar()
            
            #Listar datos en la tabla 
            self.ui.array=[]
            self.ui.array.append((datetime.datetime.now().strftime("%d-%m-%Y"),datetime.datetime.now().strftime("%H:%M:%S"), str(t), str(h), str(p), str(b)))
            
            fila=0
            for registro in self.ui.array:
                columna=0
                self.ui.tabla_sensor_datos.insertRow(fila)
                for elemento in registro:               
                    celda=QTableWidgetItem(elemento)
                    self.ui.tabla_sensor_datos.setItem(fila,columna,celda)
                    columna+=1
                fila+=1
                
            #Graficar datos
            pr = [(datetime.datetime.now().strftime("%H:%M"))]
            print(pr)
            x = [datetime.datetime.strptime(h, "%H:%M") for h in pr]
            
            self.ejes.scatter(x,h, c='blue', marker="X")
            self.ejes2.scatter(x,t, c='red', marker="D")
            self.ejes3.scatter(x,p, c='grey', marker="^")
            
            self.ui.grafica.canvas.draw()
          
        else:
            self.ui.etiqueta_conexion.setText("El sensor no esta conectado")
            self.ui.timer.stop()
            self.ui.texto_temperatura_dato.setText("--")
            self.ui.texto_humedad_dato.setText("--")
            self.ui.texto_presion_dato.setText("--")
            self.ui.texto_bateria_dato.setText("--")
        
            
    def refresco_auto(self):
        if not self.ui.tiempo_actualizacion_sensor.toPlainText() or self.ui.tiempo_actualizacion_sensor.toPlainText().isdigit() == False or float(self.ui.tiempo_actualizacion_sensor.toPlainText()) == True:
            print("No se ha metido ningun valor")
            self.ui.texto_valido.setText("Valor inválido")
            
        else:
            val_ref=int(self.ui.tiempo_actualizacion_sensor.toPlainText())
            print(val_ref)
            
            if val_ref>0:
                self.ui.texto_valido.setText("Número válido")
                self.ui.timer.start(val_ref*1000)
            else:
                self.ui.texto_valido.setText("Número inválido")

            
    def borrar_sensor(self):
        delete_sensor()
        self.ui.timer.stop()
        self.ui.etiqueta_conexion.setText("El sensor no esta conectado")
        self.ui.texto_temperatura_dato.setText("--")
        self.ui.texto_humedad_dato.setText("--")
        self.ui.texto_presion_dato.setText("--")
        self.ui.texto_bateria_dato.setText("--")
            
    def conectar(self):
        conectar_sensor()
        self.ui.pantalla_conectar.empezar_timer()
        self.ui.pantalla_conectar.exec_()
        
    def conectar_bomb(self):
        conectar_bombilla()
        self.ui.bombilla_conectar.empezar_timer_bombilla()
        self.ui.bombilla_conectar.exec_()
        
    def borrar_bombilla(self):
        delete_bombilla()

class Pantalla_conectar(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi ("Conexion_sensor.ui", self)
        self.boton_comp_conexion.clicked.connect(self.comprobar)
        #Timer detectar sensor cuando lo conecto
        self.timer_sensor=QTimer()
        self.timer_sensor.timeout.connect(self.comprobar)
        
    def empezar_timer(self):
        self.timer_sensor.start(10000)
        print("Ha empezado el timer del sensor para ver si se conecta")
        
    def comprobar(self):
        m = getModelo()
        if m == "LUMI":
            QMessageBox.information(self, "Conexión correcta", "CONEXIÓN CON EL SENSOR REALIZADA")
            self.timer_sensor.stop()
                
class Bombilla_conectar(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi ("Conexion_bombilla.ui", self)
        self.boton_comp_conexion_bomb.clicked.connect(self.comprobar_bomb)
          
        self.timer_bombilla=QTimer()
        self.timer_bombilla.timeout.connect(self.comprobar_bomb)
    
    def empezar_timer_bombilla(self):
        self.timer_bombilla.start(10000)
        print("Ha empezado el timer de la bombilla para ver si se conecta")
          
    def comprobar_bomb(self):
        m = getModelo_bombilla()
        if m == "IKEA of Sweden":
            QMessageBox.information(self, "Conexión correcta", "CONEXIÓN CON LA BOMBILLA REALIZADA")                       
            self.timer_bombilla.stop()
            (satur, bril, col, ct, mod, on_bomb) = getEnvSensorValues_bombilla()
            print(on_bomb)
            encender()
            
if __name__ == '__main__':
    app=QApplication(sys.argv) #Para abrir la aplicación
    App_prueba = ejemplo_GUI()
    pantalla_conectar = Pantalla_conectar()
    bombilla_conectar = Bombilla_conectar()
    MedidaAutomatica = False
    App_prueba.show()
    sys.exit(app.exec_())
