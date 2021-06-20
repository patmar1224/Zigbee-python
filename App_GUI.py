# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'App_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1154, 749)
        MainWindow.setStyleSheet("background-color: rgb(93, 107, 171);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(170, 170, 255);\n"
"background-color: rgb(48, 48, 48);")
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, -10, 1161, 761))
        self.stackedWidget.setStyleSheet("background-color: rgb(93, 107, 171);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.home = QtWidgets.QWidget()
        self.home.setObjectName("home")
        self.boton_luz = QtWidgets.QPushButton(self.home)
        self.boton_luz.setGeometry(QtCore.QRect(720, 430, 191, 81))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans Mono")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.boton_luz.setFont(font)
        self.boton_luz.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_luz.setStyleSheet("QPushButton{\n"
"    background-color: rgb(170, 170, 255);\n"
"    border:none;\n"
"    padding-top: 3px;\n"
"    border-left: 3px solid rgb(62, 72, 115);\n"
"    border-bottom: 4px solid rgb(62, 72, 115);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(139, 139, 209);\n"
"    border:none;\n"
"    border-left: 3px solid rgb(62, 72, 115);\n"
"    border-bottom: 6px solid rgb(62, 72, 115);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(139, 139, 209);\n"
"    border:none;\n"
"    border-left: 3px solid rgb(62, 72, 115);\n"
"    border-top: 4px solid rgb(62, 72, 115);\n"
"    padding-top: -3px;\n"
"    border-bottom: none;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/cct/business-and-money-icon-pack-91/iconmonstr-idea-2-240.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boton_luz.setIcon(icon)
        self.boton_luz.setObjectName("boton_luz")
        self.boton_sensor = QtWidgets.QPushButton(self.home)
        self.boton_sensor.setGeometry(QtCore.QRect(240, 430, 191, 81))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans Mono")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.boton_sensor.setFont(font)
        self.boton_sensor.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_sensor.setStyleSheet("QPushButton{\n"
"    background-color: rgb(170, 170, 255);\n"
"    border:none;\n"
"    padding-top: 3px;\n"
"    border-left: 3px solid rgb(62, 72, 115);\n"
"    border-bottom: 4px solid rgb(62, 72, 115);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(139, 139, 209);\n"
"    border:none;\n"
"    border-left: 3px solid rgb(62, 72, 115);\n"
"    border-bottom: 6px solid rgb(62, 72, 115);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(139, 139, 209);\n"
"    border:none;\n"
"    border-left: 3px solid rgb(62, 72, 115);\n"
"    border-top: 4px solid rgb(62, 72, 115);\n"
"    padding-top: -3px;\n"
"    border-bottom: none;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/cct/business-and-money-icon-pack-91/sensor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boton_sensor.setIcon(icon1)
        self.boton_sensor.setObjectName("boton_sensor")
        self.frame_14 = QtWidgets.QFrame(self.home)
        self.frame_14.setGeometry(QtCore.QRect(650, 30, 291, 381))
        self.frame_14.setStyleSheet("border-image: url(:/cct/business-and-money-icon-pack-91/bomb.png);")
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.frame_15 = QtWidgets.QFrame(self.home)
        self.frame_15.setGeometry(QtCore.QRect(160, 90, 341, 321))
        self.frame_15.setStyleSheet("border-image: url(:/cct/business-and-money-icon-pack-91/sensorMarina.png);")
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.boton_listar = QtWidgets.QPushButton(self.home)
        self.boton_listar.setGeometry(QtCore.QRect(720, 630, 341, 51))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans Mono")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.boton_listar.setFont(font)
        self.boton_listar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_listar.setStyleSheet("QPushButton{\n"
"    background-color: rgb(170, 170, 255);\n"
"    border:none;\n"
"    padding-top: 3px;\n"
"    border-left: 3px solid rgb(62, 72, 115);\n"
"    border-bottom: 4px solid rgb(62, 72, 115);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(139, 139, 209);\n"
"    border:none;\n"
"    border-left: 3px solid rgb(62, 72, 115);\n"
"    border-bottom: 6px solid rgb(62, 72, 115);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(139, 139, 209);\n"
"    border:none;\n"
"    border-left: 3px solid rgb(62, 72, 115);\n"
"    border-top: 4px solid rgb(62, 72, 115);\n"
"    padding-top: -3px;\n"
"    border-bottom: none;\n"
"}")
        self.boton_listar.setIcon(icon1)
        self.boton_listar.setObjectName("boton_listar")
        self.boton_luz.raise_()
        self.frame_14.raise_()
        self.frame_15.raise_()
        self.boton_sensor.raise_()
        self.boton_listar.raise_()
        self.stackedWidget.addWidget(self.home)
        self.sensor = QtWidgets.QWidget()
        self.sensor.setObjectName("sensor")
        self.tabWidget = QtWidgets.QTabWidget(self.sensor)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(280, 20, 831, 701))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("background-color: rgb(153, 153, 230);\n"
"")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.datos_sensor = QtWidgets.QWidget()
        self.datos_sensor.setObjectName("datos_sensor")
        self.texto_actualizar_auto = QtWidgets.QLabel(self.datos_sensor)
        self.texto_actualizar_auto.setGeometry(QtCore.QRect(150, 510, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.texto_actualizar_auto.setFont(font)
        self.texto_actualizar_auto.setObjectName("texto_actualizar_auto")
        self.texto_presion = QtWidgets.QLabel(self.datos_sensor)
        self.texto_presion.setGeometry(QtCore.QRect(150, 240, 331, 22))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.texto_presion.setFont(font)
        self.texto_presion.setObjectName("texto_presion")
        self.texto_humedad = QtWidgets.QLabel(self.datos_sensor)
        self.texto_humedad.setGeometry(QtCore.QRect(150, 200, 231, 22))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.texto_humedad.setFont(font)
        self.texto_humedad.setObjectName("texto_humedad")
        self.texto_humedad_dato = QtWidgets.QLabel(self.datos_sensor)
        self.texto_humedad_dato.setGeometry(QtCore.QRect(550, 190, 141, 22))
        self.texto_humedad_dato.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.texto_humedad_dato.setStyleSheet("font: 57 16pt \"Monoscape\";")
        self.texto_humedad_dato.setObjectName("texto_humedad_dato")
        self.texto_bateria_dato = QtWidgets.QLabel(self.datos_sensor)
        self.texto_bateria_dato.setGeometry(QtCore.QRect(550, 270, 141, 22))
        font = QtGui.QFont()
        font.setFamily("Monoscape")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.texto_bateria_dato.setFont(font)
        self.texto_bateria_dato.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.texto_bateria_dato.setStyleSheet("font: 57 16pt\"Monoscape\";")
        self.texto_bateria_dato.setObjectName("texto_bateria_dato")
        self.texto_presion_dato = QtWidgets.QLabel(self.datos_sensor)
        self.texto_presion_dato.setGeometry(QtCore.QRect(550, 230, 141, 22))
        font = QtGui.QFont()
        font.setFamily("Monoscape")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.texto_presion_dato.setFont(font)
        self.texto_presion_dato.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.texto_presion_dato.setStyleSheet("font: 57 16pt \"Monoscape\";")
        self.texto_presion_dato.setObjectName("texto_presion_dato")
        self.texto_bateria = QtWidgets.QLabel(self.datos_sensor)
        self.texto_bateria.setGeometry(QtCore.QRect(150, 280, 231, 22))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.texto_bateria.setFont(font)
        self.texto_bateria.setObjectName("texto_bateria")
        self.texto_temperatura_dato = QtWidgets.QLabel(self.datos_sensor)
        self.texto_temperatura_dato.setGeometry(QtCore.QRect(550, 150, 141, 22))
        font = QtGui.QFont()
        font.setFamily("Monoscape")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.texto_temperatura_dato.setFont(font)
        self.texto_temperatura_dato.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.texto_temperatura_dato.setStyleSheet("font: 57 16pt \"Monoscape\";")
        self.texto_temperatura_dato.setObjectName("texto_temperatura_dato")
        self.texto_temperatura = QtWidgets.QLabel(self.datos_sensor)
        self.texto_temperatura.setGeometry(QtCore.QRect(150, 160, 231, 22))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(14)
        self.texto_temperatura.setFont(font)
        self.texto_temperatura.setObjectName("texto_temperatura")
        self.tiempo_actualizacion_sensor = QtWidgets.QTextEdit(self.datos_sensor)
        self.tiempo_actualizacion_sensor.setGeometry(QtCore.QRect(460, 500, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Monoespace")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.tiempo_actualizacion_sensor.setFont(font)
        self.tiempo_actualizacion_sensor.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.tiempo_actualizacion_sensor.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 italic 14pt \"Monoespace\";")
        self.tiempo_actualizacion_sensor.setObjectName("tiempo_actualizacion_sensor")
        self.etiqueta_conexion = QtWidgets.QLabel(self.datos_sensor)
        self.etiqueta_conexion.setGeometry(QtCore.QRect(470, 90, 261, 22))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.etiqueta_conexion.setFont(font)
        self.etiqueta_conexion.setText("")
        self.etiqueta_conexion.setObjectName("etiqueta_conexion")
        self.boton_actualizar_datos_sensor = QtWidgets.QPushButton(self.datos_sensor)
        self.boton_actualizar_datos_sensor.setGeometry(QtCore.QRect(510, 350, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setBold(False)
        font.setWeight(50)
        self.boton_actualizar_datos_sensor.setFont(font)
        self.boton_actualizar_datos_sensor.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_actualizar_datos_sensor.setStyleSheet("QPushButton{\n"
"    background-color: rgb(170, 170, 255);\n"
"    border:none;\n"
"    padding-top: 3px;\n"
"    border-left: 3px solid rgb(62, 72, 115);\n"
"    border-bottom: 4px solid rgb(62, 72, 115);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(139, 139, 209);\n"
"    border:none;\n"
"    border-left: 3px solid rgb(62, 72, 115);\n"
"    border-bottom: 6px solid rgb(62, 72, 115);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(139, 139, 209);\n"
"    border:none;\n"
"    border-left: 3px solid rgb(62, 72, 115);\n"
"    border-top: 4px solid rgb(62, 72, 115);\n"
"    padding-top: -3px;\n"
"    border-bottom: none;\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/cct/business-and-money-icon-pack-91/iconmonstr-reload-thin-240.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boton_actualizar_datos_sensor.setIcon(icon2)
        self.boton_actualizar_datos_sensor.setObjectName("boton_actualizar_datos_sensor")
        self.boton_actualizar_datos_sensor_auto = QtWidgets.QPushButton(self.datos_sensor)
        self.boton_actualizar_datos_sensor_auto.setGeometry(QtCore.QRect(600, 500, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        self.boton_actualizar_datos_sensor_auto.setFont(font)
        self.boton_actualizar_datos_sensor_auto.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_actualizar_datos_sensor_auto.setStyleSheet("QPushButton{\n"
"    background-color: rgb(170, 170, 255);\n"
"    border:none;\n"
"    padding-top: 3px;\n"
"    border-left: 3px solid rgb(62, 72, 115);\n"
"    border-bottom: 4px solid rgb(62, 72, 115);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(139, 139, 209);\n"
"    border:none;\n"
"    border-left: 3px solid rgb(62, 72, 115);\n"
"    border-bottom: 6px solid rgb(62, 72, 115);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(139, 139, 209);\n"
"    border:none;\n"
"    border-left: 3px solid rgb(62, 72, 115);\n"
"    border-top: 4px solid rgb(62, 72, 115);\n"
"    padding-top: -3px;\n"
"    border-bottom: none;\n"
"}")
        self.boton_actualizar_datos_sensor_auto.setObjectName("boton_actualizar_datos_sensor_auto")
        self.texto_valido = QtWidgets.QLabel(self.datos_sensor)
        self.texto_valido.setGeometry(QtCore.QRect(470, 560, 111, 21))
        self.texto_valido.setText("")
        self.texto_valido.setObjectName("texto_valido")
        self.frame = QtWidgets.QFrame(self.datos_sensor)
        self.frame.setGeometry(QtCore.QRect(20, 20, 91, 81))
        self.frame.setStyleSheet("border-image: url(:/cct/business-and-money-icon-pack-91/contenido.png);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.texto_actualizar_auto.raise_()
        self.texto_presion.raise_()
        self.texto_humedad.raise_()
        self.texto_humedad_dato.raise_()
        self.texto_bateria_dato.raise_()
        self.texto_presion_dato.raise_()
        self.texto_bateria.raise_()
        self.texto_temperatura.raise_()
        self.tiempo_actualizacion_sensor.raise_()
        self.etiqueta_conexion.raise_()
        self.boton_actualizar_datos_sensor.raise_()
        self.boton_actualizar_datos_sensor_auto.raise_()
        self.texto_temperatura_dato.raise_()
        self.texto_valido.raise_()
        self.frame.raise_()
        self.tabWidget.addTab(self.datos_sensor, "")
        self.grafica_sensor = QtWidgets.QWidget()
        self.grafica_sensor.setObjectName("grafica_sensor")
        self.grafica = Grafica(self.grafica_sensor)
        self.grafica.setGeometry(QtCore.QRect(140, 10, 681, 651))
        self.grafica.setObjectName("grafica")
        self.frame_2 = QtWidgets.QFrame(self.grafica_sensor)
        self.frame_2.setGeometry(QtCore.QRect(10, 20, 120, 111))
        self.frame_2.setStyleSheet("border-image: url(:/cct/business-and-money-icon-pack-91/grafico-de-lineas.png);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.tabWidget.addTab(self.grafica_sensor, "")
        self.tabla_sensor = QtWidgets.QWidget()
        self.tabla_sensor.setMouseTracking(False)
        self.tabla_sensor.setObjectName("tabla_sensor")
        self.boton_borrar_tabla = QtWidgets.QPushButton(self.tabla_sensor)
        self.boton_borrar_tabla.setGeometry(QtCore.QRect(700, 610, 99, 41))
        self.boton_borrar_tabla.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_borrar_tabla.setStyleSheet("QPushButton{\n"
"    background-color: rgb(170, 170, 255);\n"
"    border:none;\n"
"    padding-top: 3px;\n"
"    border-left: 3px solid rgb(62, 72, 115);\n"
"    border-bottom: 4px solid rgb(62, 72, 115);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(139, 139, 209);\n"
"    border:none;\n"
"    border-left: 3px solid rgb(62, 72, 115);\n"
"    border-bottom: 6px solid rgb(62, 72, 115);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(139, 139, 209);\n"
"    border:none;\n"
"    border-left: 3px solid rgb(62, 72, 115);\n"
"    border-top: 4px solid rgb(62, 72, 115);\n"
"    padding-top: -3px;\n"
"    border-bottom: none;\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/cct/business-and-money-icon-pack-91/iconmonstr-trash-can-30-240.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boton_borrar_tabla.setIcon(icon3)
        self.boton_borrar_tabla.setObjectName("boton_borrar_tabla")
        self.tabla_sensor_datos = QtWidgets.QTableWidget(self.tabla_sensor)
        self.tabla_sensor_datos.setGeometry(QtCore.QRect(30, 110, 781, 491))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.tabla_sensor_datos.setFont(font)
        self.tabla_sensor_datos.setObjectName("tabla_sensor_datos")
        self.tabla_sensor_datos.setColumnCount(6)
        self.tabla_sensor_datos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_sensor_datos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_sensor_datos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_sensor_datos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_sensor_datos.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_sensor_datos.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_sensor_datos.setHorizontalHeaderItem(5, item)
        self.tabla_sensor_datos.horizontalHeader().setDefaultSectionSize(130)
        self.frame_3 = QtWidgets.QFrame(self.tabla_sensor)
        self.frame_3.setGeometry(QtCore.QRect(20, 0, 121, 101))
        self.frame_3.setStyleSheet("border-image: url(:/cct/business-and-money-icon-pack-91/celulas.png);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.tabWidget.addTab(self.tabla_sensor, "")
        self.escena_sensor = QtWidgets.QWidget()
        self.escena_sensor.setObjectName("escena_sensor")
        self.etiqueta_elegir = QtWidgets.QLabel(self.escena_sensor)
        self.etiqueta_elegir.setGeometry(QtCore.QRect(210, 120, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.etiqueta_elegir.setFont(font)
        self.etiqueta_elegir.setObjectName("etiqueta_elegir")
        self.etiqueta_temp_blanco_3 = QtWidgets.QLabel(self.escena_sensor)
        self.etiqueta_temp_blanco_3.setGeometry(QtCore.QRect(150, 480, 111, 22))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.etiqueta_temp_blanco_3.setFont(font)
        self.etiqueta_temp_blanco_3.setObjectName("etiqueta_temp_blanco_3")
        self.etiqueta_brillo_blanco_3 = QtWidgets.QLabel(self.escena_sensor)
        self.etiqueta_brillo_blanco_3.setGeometry(QtCore.QRect(170, 340, 81, 22))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.etiqueta_brillo_blanco_3.setFont(font)
        self.etiqueta_brillo_blanco_3.setObjectName("etiqueta_brillo_blanco_3")
        self.brillo_blanco_slider_escena = QtWidgets.QSlider(self.escena_sensor)
        self.brillo_blanco_slider_escena.setGeometry(QtCore.QRect(310, 340, 411, 26))
        self.brillo_blanco_slider_escena.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.544643 rgba(203, 203, 203, 255), stop:0.96875 rgba(255, 255, 255, 255));")
        self.brillo_blanco_slider_escena.setOrientation(QtCore.Qt.Horizontal)
        self.brillo_blanco_slider_escena.setObjectName("brillo_blanco_slider_escena")
        self.temp_slider_escena = QtWidgets.QSlider(self.escena_sensor)
        self.temp_slider_escena.setGeometry(QtCore.QRect(310, 480, 411, 26))
        self.temp_slider_escena.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 71, 255), stop:0.55 rgba(217, 209, 255, 255), stop:0.98 rgba(0, 0, 225, 255), stop:1 rgba(0, 0, 0, 0));")
        self.temp_slider_escena.setOrientation(QtCore.Qt.Horizontal)
        self.temp_slider_escena.setObjectName("temp_slider_escena")
        self.valor_brillo_blanco_escena = QtWidgets.QLabel(self.escena_sensor)
        self.valor_brillo_blanco_escena.setGeometry(QtCore.QRect(480, 310, 68, 22))
        self.valor_brillo_blanco_escena.setText("")
        self.valor_brillo_blanco_escena.setObjectName("valor_brillo_blanco_escena")
        self.valor_temp_brillo_escena = QtWidgets.QLabel(self.escena_sensor)
        self.valor_temp_brillo_escena.setGeometry(QtCore.QRect(470, 450, 81, 22))
        self.valor_temp_brillo_escena.setText("")
        self.valor_temp_brillo_escena.setObjectName("valor_temp_brillo_escena")
        self.Spinbox_escena = QtWidgets.QDoubleSpinBox(self.escena_sensor)
        self.Spinbox_escena.setGeometry(QtCore.QRect(550, 120, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(14)
        self.Spinbox_escena.setFont(font)
        self.Spinbox_escena.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Spinbox_escena.setMinimum(-20.0)
        self.Spinbox_escena.setMaximum(50.0)
        self.Spinbox_escena.setSingleStep(0.5)
        self.Spinbox_escena.setProperty("value", 25.0)
        self.Spinbox_escena.setObjectName("Spinbox_escena")
        self.checkBox_escena = QtWidgets.QCheckBox(self.escena_sensor)
        self.checkBox_escena.setGeometry(QtCore.QRect(540, 580, 111, 27))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_escena.setFont(font)
        self.checkBox_escena.setObjectName("checkBox_escena")
        self.frame_4 = QtWidgets.QFrame(self.escena_sensor)
        self.frame_4.setGeometry(QtCore.QRect(20, 10, 111, 91))
        self.frame_4.setStyleSheet("border-image: url(:/cct/business-and-money-icon-pack-91/galeria.png);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame_5 = QtWidgets.QFrame(self.escena_sensor)
        self.frame_5.setGeometry(QtCore.QRect(90, 320, 61, 51))
        self.frame_5.setStyleSheet("border-image: url(:/cct/business-and-money-icon-pack-91/iconmonstr-weather-2-240.png);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.frame_6 = QtWidgets.QFrame(self.escena_sensor)
        self.frame_6.setGeometry(QtCore.QRect(80, 460, 71, 61))
        self.frame_6.setStyleSheet("border-image: url(:/cct/business-and-money-icon-pack-91/herramienta-termometro.png);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.frame_7 = QtWidgets.QFrame(self.escena_sensor)
        self.frame_7.setGeometry(QtCore.QRect(300, 270, 51, 51))
        self.frame_7.setStyleSheet("border-image: url(:/cct/business-and-money-icon-pack-91/iconmonstr-idea-1-240.png);")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.frame_8 = QtWidgets.QFrame(self.escena_sensor)
        self.frame_8.setGeometry(QtCore.QRect(680, 270, 61, 51))
        self.frame_8.setStyleSheet("border-image: url(:/cct/business-and-money-icon-pack-91/iconmonstr-idea-2-240.png);")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.tabWidget.addTab(self.escena_sensor, "")
        self.boton_atras_sensor = QtWidgets.QPushButton(self.sensor)
        self.boton_atras_sensor.setGeometry(QtCore.QRect(20, 20, 99, 41))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans Mono")
        self.boton_atras_sensor.setFont(font)
        self.boton_atras_sensor.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_atras_sensor.setStyleSheet("QPushButton{\n"
"    background-color: rgb(170, 170, 255);\n"
"    border:none;\n"
"    padding-top: 3px;\n"
"    border-left: 3px solid rgb(62, 72, 115);\n"
"    border-bottom: 4px solid rgb(62, 72, 115);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(139, 139, 209);\n"
"    border:none;\n"
"    border-left: 3px solid rgb(62, 72, 115);\n"
"    border-bottom: 6px solid rgb(62, 72, 115);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(139, 139, 209);\n"
"    border:none;\n"
"    border-left: 3px solid rgb(62, 72, 115);\n"
"    border-top: 4px solid rgb(62, 72, 115);\n"
"    padding-top: -3px;\n"
"    border-bottom: none;\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/cct/business-and-money-icon-pack-91/iconmonstr-arrow-68-240.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boton_atras_sensor.setIcon(icon4)
        self.boton_atras_sensor.setObjectName("boton_atras_sensor")
        self.boton_anadir_sensor = QtWidgets.QPushButton(self.sensor)
        self.boton_anadir_sensor.setGeometry(QtCore.QRect(20, 470, 231, 71))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans Mono")
        font.setBold(True)
        font.setWeight(75)
        self.boton_anadir_sensor.setFont(font)
        self.boton_anadir_sensor.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_anadir_sensor.setStyleSheet("QPushButton{\n"
"    background-color: rgb(170, 170, 255);\n"
"    border:none;\n"
"    padding-top: 3px;\n"
"    border-left: 3px solid rgb(62, 72, 115);\n"
"    border-bottom: 4px solid rgb(62, 72, 115);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(139, 139, 209);\n"
"    border:none;\n"
"    border-left: 3px solid rgb(62, 72, 115);\n"
"    border-bottom: 6px solid rgb(62, 72, 115);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(139, 139, 209);\n"
"    border:none;\n"
"    border-left: 3px solid rgb(62, 72, 115);\n"
"    border-top: 4px solid rgb(62, 72, 115);\n"
"    padding-top: -3px;\n"
"    border-bottom: none;\n"
"}")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/cct/business-and-money-icon-pack-91/iconmonstr-radio-tower-12-240.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boton_anadir_sensor.setIcon(icon5)
        self.boton_anadir_sensor.setObjectName("boton_anadir_sensor")
        self.boton_borrar_sensor = QtWidgets.QPushButton(self.sensor)
        self.boton_borrar_sensor.setGeometry(QtCore.QRect(20, 570, 231, 71))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans Mono")
        font.setBold(True)
        font.setWeight(75)
        self.boton_borrar_sensor.setFont(font)
        self.boton_borrar_sensor.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_borrar_sensor.setStyleSheet("QPushButton{\n"
"    background-color: rgb(170, 170, 255);\n"
"    border:none;\n"
"    padding-top: 3px;\n"
"    border-left: 3px solid rgb(62, 72, 115);\n"
"    border-bottom: 4px solid rgb(62, 72, 115);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(139, 139, 209);\n"
"    border:none;\n"
"    border-left: 3px solid rgb(62, 72, 115);\n"
"    border-bottom: 6px solid rgb(62, 72, 115);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(139, 139, 209);\n"
"    border:none;\n"
"    border-left: 3px solid rgb(62, 72, 115);\n"
"    border-top: 4px solid rgb(62, 72, 115);\n"
"    padding-top: -3px;\n"
"    border-bottom: none;\n"
"}")
        self.boton_borrar_sensor.setIcon(icon3)
        self.boton_borrar_sensor.setObjectName("boton_borrar_sensor")
        self.frame_16 = QtWidgets.QFrame(self.sensor)
        self.frame_16.setGeometry(QtCore.QRect(10, 160, 241, 231))
        self.frame_16.setStyleSheet("border-image: url(:/cct/business-and-money-icon-pack-91/sensorMarina.png);")
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.boton_atras_sensor.raise_()
        self.tabWidget.raise_()
        self.boton_anadir_sensor.raise_()
        self.boton_borrar_sensor.raise_()
        self.frame_16.raise_()
        self.stackedWidget.addWidget(self.sensor)
        self.bombilla = QtWidgets.QWidget()
        self.bombilla.setObjectName("bombilla")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.bombilla)
        self.tabWidget_2.setGeometry(QtCore.QRect(280, 20, 841, 711))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.tabWidget_2.setFont(font)
        self.tabWidget_2.setStyleSheet("background-color: rgb(153, 153, 230);")
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.datos_luz = QtWidgets.QWidget()
        self.datos_luz.setObjectName("datos_luz")
        self.brillo_slider = QtWidgets.QSlider(self.datos_luz)
        self.brillo_slider.setGeometry(QtCore.QRect(170, 170, 26, 351))
        self.brillo_slider.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.brillo_slider.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:0.55 rgba(210, 210, 210, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        self.brillo_slider.setOrientation(QtCore.Qt.Vertical)
        self.brillo_slider.setObjectName("brillo_slider")
        self.color_slider = QtWidgets.QSlider(self.datos_luz)
        self.color_slider.setGeometry(QtCore.QRect(410, 170, 26, 351))
        self.color_slider.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.color_slider.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255));")
        self.color_slider.setOrientation(QtCore.Qt.Vertical)
        self.color_slider.setObjectName("color_slider")
        self.satur_slider = QtWidgets.QSlider(self.datos_luz)
        self.satur_slider.setGeometry(QtCore.QRect(650, 170, 26, 351))
        self.satur_slider.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.satur_slider.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.55 rgba(210, 210, 210, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        self.satur_slider.setOrientation(QtCore.Qt.Vertical)
        self.satur_slider.setObjectName("satur_slider")
        self.etiqueta_brillo = QtWidgets.QLabel(self.datos_luz)
        self.etiqueta_brillo.setGeometry(QtCore.QRect(160, 140, 81, 22))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.etiqueta_brillo.setFont(font)
        self.etiqueta_brillo.setObjectName("etiqueta_brillo")
        self.etiqueta_color = QtWidgets.QLabel(self.datos_luz)
        self.etiqueta_color.setGeometry(QtCore.QRect(400, 140, 68, 22))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setBold(True)
        font.setWeight(75)
        self.etiqueta_color.setFont(font)
        self.etiqueta_color.setObjectName("etiqueta_color")
        self.etiqueta_satur = QtWidgets.QLabel(self.datos_luz)
        self.etiqueta_satur.setGeometry(QtCore.QRect(610, 140, 101, 22))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setBold(True)
        font.setWeight(75)
        self.etiqueta_satur.setFont(font)
        self.etiqueta_satur.setObjectName("etiqueta_satur")
        self.valor_brillo = QtWidgets.QLabel(self.datos_luz)
        self.valor_brillo.setGeometry(QtCore.QRect(160, 550, 41, 22))
        self.valor_brillo.setText("")
        self.valor_brillo.setObjectName("valor_brillo")
        self.valor_color = QtWidgets.QLabel(self.datos_luz)
        self.valor_color.setGeometry(QtCore.QRect(400, 550, 51, 22))
        self.valor_color.setText("")
        self.valor_color.setObjectName("valor_color")
        self.valor_satur = QtWidgets.QLabel(self.datos_luz)
        self.valor_satur.setGeometry(QtCore.QRect(640, 550, 41, 22))
        self.valor_satur.setText("")
        self.valor_satur.setObjectName("valor_satur")
        self.frame_9 = QtWidgets.QFrame(self.datos_luz)
        self.frame_9.setGeometry(QtCore.QRect(150, 70, 71, 61))
        self.frame_9.setStyleSheet("border-image: url(:/cct/business-and-money-icon-pack-91/iconmonstr-weather-2-240.png);")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.frame_10 = QtWidgets.QFrame(self.datos_luz)
        self.frame_10.setGeometry(QtCore.QRect(380, 60, 91, 71))
        self.frame_10.setStyleSheet("border-image: url(:/cct/business-and-money-icon-pack-91/paleta-de-pintura.png);")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.frame_11 = QtWidgets.QFrame(self.datos_luz)
        self.frame_11.setGeometry(QtCore.QRect(610, 60, 101, 71))
        self.frame_11.setStyleSheet("border-image: url(:/cct/business-and-money-icon-pack-91/kisspng-computer-icons-saturation-clip-art-5b2d502837d132.0254893715296962962286.png);")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.tabWidget_2.addTab(self.datos_luz, "")
        self.blanca_luz = QtWidgets.QWidget()
        self.blanca_luz.setObjectName("blanca_luz")
        self.brillo_blanco_slider = QtWidgets.QSlider(self.blanca_luz)
        self.brillo_blanco_slider.setGeometry(QtCore.QRect(230, 180, 31, 351))
        self.brillo_blanco_slider.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.brillo_blanco_slider.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:0.55 rgba(210, 210, 210, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        self.brillo_blanco_slider.setOrientation(QtCore.Qt.Vertical)
        self.brillo_blanco_slider.setObjectName("brillo_blanco_slider")
        self.temp_slider = QtWidgets.QSlider(self.blanca_luz)
        self.temp_slider.setGeometry(QtCore.QRect(490, 180, 31, 351))
        self.temp_slider.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.temp_slider.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(255, 255, 71, 255), stop:0.55 rgba(217, 209, 255, 255), stop:0.98 rgba(0, 0, 225, 255), stop:1 rgba(0, 0, 0, 0));")
        self.temp_slider.setOrientation(QtCore.Qt.Vertical)
        self.temp_slider.setObjectName("temp_slider")
        self.etiqueta_brillo_blanco = QtWidgets.QLabel(self.blanca_luz)
        self.etiqueta_brillo_blanco.setGeometry(QtCore.QRect(220, 140, 81, 22))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.etiqueta_brillo_blanco.setFont(font)
        self.etiqueta_brillo_blanco.setObjectName("etiqueta_brillo_blanco")
        self.etiqueta_temp_blanco = QtWidgets.QLabel(self.blanca_luz)
        self.etiqueta_temp_blanco.setGeometry(QtCore.QRect(450, 140, 111, 22))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.etiqueta_temp_blanco.setFont(font)
        self.etiqueta_temp_blanco.setObjectName("etiqueta_temp_blanco")
        self.valor_brillo_blanco = QtWidgets.QLabel(self.blanca_luz)
        self.valor_brillo_blanco.setGeometry(QtCore.QRect(220, 550, 41, 22))
        self.valor_brillo_blanco.setText("")
        self.valor_brillo_blanco.setObjectName("valor_brillo_blanco")
        self.valor_temp_blanco = QtWidgets.QLabel(self.blanca_luz)
        self.valor_temp_blanco.setGeometry(QtCore.QRect(470, 550, 41, 22))
        self.valor_temp_blanco.setText("")
        self.valor_temp_blanco.setObjectName("valor_temp_blanco")
        self.frame_12 = QtWidgets.QFrame(self.blanca_luz)
        self.frame_12.setGeometry(QtCore.QRect(210, 70, 71, 61))
        self.frame_12.setStyleSheet("border-image: url(:/cct/business-and-money-icon-pack-91/iconmonstr-weather-2-240.png);")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.frame_13 = QtWidgets.QFrame(self.blanca_luz)
        self.frame_13.setGeometry(QtCore.QRect(460, 70, 81, 61))
        self.frame_13.setStyleSheet("border-image: url(:/cct/business-and-money-icon-pack-91/herramienta-termometro.png);")
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.tabWidget_2.addTab(self.blanca_luz, "")
        self.boton_atras_luz = QtWidgets.QPushButton(self.bombilla)
        self.boton_atras_luz.setGeometry(QtCore.QRect(30, 20, 99, 41))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans Mono")
        self.boton_atras_luz.setFont(font)
        self.boton_atras_luz.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_atras_luz.setStyleSheet("QPushButton{\n"
"    background-color: rgb(170, 170, 255);\n"
"    border:none;\n"
"    padding-top: 3px;\n"
"    border-left: 3px solid rgb(62, 72, 115);\n"
"    border-bottom: 4px solid rgb(62, 72, 115);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(139, 139, 209);\n"
"    border:none;\n"
"    border-left: 3px solid rgb(62, 72, 115);\n"
"    border-bottom: 6px solid rgb(62, 72, 115);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(139, 139, 209);\n"
"    border:none;\n"
"    border-left: 3px solid rgb(62, 72, 115);\n"
"    border-top: 4px solid rgb(62, 72, 115);\n"
"    padding-top: -3px;\n"
"    border-bottom: none;\n"
"}")
        self.boton_atras_luz.setIcon(icon2)
        self.boton_atras_luz.setObjectName("boton_atras_luz")
        self.boton_bomb_on = QtWidgets.QPushButton(self.bombilla)
        self.boton_bomb_on.setGeometry(QtCore.QRect(20, 360, 110, 51))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans Mono")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.boton_bomb_on.setFont(font)
        self.boton_bomb_on.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_bomb_on.setStyleSheet("QPushButton{\n"
"    background-color: rgb(170, 170, 255);\n"
"    border:none;\n"
"    padding-top: 3px;\n"
"    border-left: 3px solid rgb(62, 72, 115);\n"
"    border-bottom: 4px solid rgb(62, 72, 115);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(139, 139, 209);\n"
"    border:none;\n"
"    border-left: 3px solid rgb(62, 72, 115);\n"
"    border-bottom: 6px solid rgb(62, 72, 115);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(139, 139, 209);\n"
"    border:none;\n"
"    border-left: 3px solid rgb(62, 72, 115);\n"
"    border-top: 4px solid rgb(62, 72, 115);\n"
"    padding-top: -3px;\n"
"    border-bottom: none;\n"
"}")
        self.boton_bomb_on.setIcon(icon)
        self.boton_bomb_on.setObjectName("boton_bomb_on")
        self.boton_bomb_off = QtWidgets.QPushButton(self.bombilla)
        self.boton_bomb_off.setGeometry(QtCore.QRect(140, 360, 110, 51))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans Mono")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.boton_bomb_off.setFont(font)
        self.boton_bomb_off.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_bomb_off.setStyleSheet("QPushButton{\n"
"    background-color: rgb(170, 170, 255);\n"
"    border:none;\n"
"    padding-top: 3px;\n"
"    border-left: 3px solid rgb(62, 72, 115);\n"
"    border-bottom: 4px solid rgb(62, 72, 115);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(139, 139, 209);\n"
"    border:none;\n"
"    border-left: 3px solid rgb(62, 72, 115);\n"
"    border-bottom: 6px solid rgb(62, 72, 115);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(139, 139, 209);\n"
"    border:none;\n"
"    border-left: 3px solid rgb(62, 72, 115);\n"
"    border-top: 4px solid rgb(62, 72, 115);\n"
"    padding-top: -3px;\n"
"    border-bottom: none;\n"
"}")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/cct/business-and-money-icon-pack-91/iconmonstr-idea-1-240.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boton_bomb_off.setIcon(icon6)
        self.boton_bomb_off.setObjectName("boton_bomb_off")
        self.boton_anadir_bomb = QtWidgets.QPushButton(self.bombilla)
        self.boton_anadir_bomb.setGeometry(QtCore.QRect(20, 470, 231, 71))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans Mono")
        font.setBold(True)
        font.setWeight(75)
        self.boton_anadir_bomb.setFont(font)
        self.boton_anadir_bomb.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_anadir_bomb.setStyleSheet("QPushButton{\n"
"    background-color: rgb(170, 170, 255);\n"
"    border:none;\n"
"    padding-top: 3px;\n"
"    border-left: 3px solid rgb(62, 72, 115);\n"
"    border-bottom: 4px solid rgb(62, 72, 115);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(139, 139, 209);\n"
"    border:none;\n"
"    border-left: 3px solid rgb(62, 72, 115);\n"
"    border-bottom: 6px solid rgb(62, 72, 115);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(139, 139, 209);\n"
"    border:none;\n"
"    border-left: 3px solid rgb(62, 72, 115);\n"
"    border-top: 4px solid rgb(62, 72, 115);\n"
"    padding-top: -3px;\n"
"    border-bottom: none;\n"
"}")
        self.boton_anadir_bomb.setIcon(icon5)
        self.boton_anadir_bomb.setObjectName("boton_anadir_bomb")
        self.boton_borrar_bomb = QtWidgets.QPushButton(self.bombilla)
        self.boton_borrar_bomb.setGeometry(QtCore.QRect(20, 570, 231, 71))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.boton_borrar_bomb.setFont(font)
        self.boton_borrar_bomb.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_borrar_bomb.setStyleSheet("QPushButton{\n"
"    background-color: rgb(170, 170, 255);\n"
"    border:none;\n"
"    padding-top: 3px;\n"
"    border-left: 3px solid rgb(62, 72, 115);\n"
"    border-bottom: 4px solid rgb(62, 72, 115);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(139, 139, 209);\n"
"    border:none;\n"
"    border-left: 3px solid rgb(62, 72, 115);\n"
"    border-bottom: 6px solid rgb(62, 72, 115);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(139, 139, 209);\n"
"    border:none;\n"
"    border-left: 3px solid rgb(62, 72, 115);\n"
"    border-top: 4px solid rgb(62, 72, 115);\n"
"    padding-top: -3px;\n"
"    border-bottom: none;\n"
"}")
        self.boton_borrar_bomb.setIcon(icon3)
        self.boton_borrar_bomb.setObjectName("boton_borrar_bomb")
        self.frame_17 = QtWidgets.QFrame(self.bombilla)
        self.frame_17.setGeometry(QtCore.QRect(50, 90, 181, 221))
        self.frame_17.setStyleSheet("border-image: url(:/cct/business-and-money-icon-pack-91/bomb.png);")
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.stackedWidget.addWidget(self.bombilla)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.boton_luz.setText(_translate("MainWindow", "BOMBILLA"))
        self.boton_sensor.setText(_translate("MainWindow", "SENSOR"))
        self.boton_listar.setText(_translate("MainWindow", "LISTAR DISPOSITIVOS"))
        self.texto_actualizar_auto.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Tiempo actualización (s)</span></p></body></html>"))
        self.texto_presion.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">PRESIÓN ATMOSFÉRICA (kPa)</span></p></body></html>"))
        self.texto_humedad.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">HUMEDAD (%)</span></p></body></html>"))
        self.texto_humedad_dato.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><br/></p></body></html>"))
        self.texto_bateria_dato.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><br/></p></body></html>"))
        self.texto_presion_dato.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><br/></p></body></html>"))
        self.texto_bateria.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">BATERIA (%)</span></p></body></html>"))
        self.texto_temperatura_dato.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><br/></p></body></html>"))
        self.texto_temperatura.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">TEMPERATURA (°C)</span></p></body></html>"))
        self.boton_actualizar_datos_sensor.setText(_translate("MainWindow", "Actualizar datos"))
        self.boton_actualizar_datos_sensor_auto.setText(_translate("MainWindow", "OK"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.datos_sensor), _translate("MainWindow", "Datos"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.datos_sensor), _translate("MainWindow", "Ver datos"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.grafica_sensor), _translate("MainWindow", "Gráfica"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.grafica_sensor), _translate("MainWindow", "Ver gráfica"))
        self.boton_borrar_tabla.setText(_translate("MainWindow", "Borrar"))
        item = self.tabla_sensor_datos.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Fecha"))
        item = self.tabla_sensor_datos.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Hora"))
        item = self.tabla_sensor_datos.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Temperatura(°C)"))
        item = self.tabla_sensor_datos.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Humedad(%)"))
        item = self.tabla_sensor_datos.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Presión(kPa)"))
        item = self.tabla_sensor_datos.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Batería(%)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabla_sensor), _translate("MainWindow", "Tabla"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tabla_sensor), _translate("MainWindow", "Ver tabla"))
        self.etiqueta_elegir.setText(_translate("MainWindow", "ELEGIR VALOR TEMPERATURA:"))
        self.etiqueta_temp_blanco_3.setText(_translate("MainWindow", "TEMPERATURA"))
        self.etiqueta_brillo_blanco_3.setText(_translate("MainWindow", "BRILLO"))
        self.checkBox_escena.setText(_translate("MainWindow", "ESCENA"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.escena_sensor), _translate("MainWindow", "Escena"))
        self.boton_atras_sensor.setText(_translate("MainWindow", "ATRÁS"))
        self.boton_anadir_sensor.setText(_translate("MainWindow", "CONECTAR"))
        self.boton_borrar_sensor.setText(_translate("MainWindow", "BORRAR"))
        self.etiqueta_brillo.setText(_translate("MainWindow", "BRILLO"))
        self.etiqueta_color.setText(_translate("MainWindow", "COLOR"))
        self.etiqueta_satur.setText(_translate("MainWindow", "SATURACIÓN"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.datos_luz), _translate("MainWindow", "Color"))
        self.tabWidget_2.setTabToolTip(self.tabWidget_2.indexOf(self.datos_luz), _translate("MainWindow", "Ver color"))
        self.etiqueta_brillo_blanco.setText(_translate("MainWindow", "BRILLO"))
        self.etiqueta_temp_blanco.setText(_translate("MainWindow", "TEMPERATURA"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.blanca_luz), _translate("MainWindow", "Blanca"))
        self.tabWidget_2.setTabToolTip(self.tabWidget_2.indexOf(self.blanca_luz), _translate("MainWindow", "Ver blanca"))
        self.boton_atras_luz.setText(_translate("MainWindow", "ATRÁS"))
        self.boton_bomb_on.setText(_translate("MainWindow", "ON"))
        self.boton_bomb_off.setText(_translate("MainWindow", "OFF"))
        self.boton_anadir_bomb.setText(_translate("MainWindow", "CONECTAR"))
        self.boton_borrar_bomb.setText(_translate("MainWindow", "BORRAR"))

from grafica import Grafica
import logo
