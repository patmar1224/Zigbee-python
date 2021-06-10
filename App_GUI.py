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
        MainWindow.resize(741, 489)
        MainWindow.setStyleSheet("background-color: rgb(93, 107, 171);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(170, 170, 255);\n"
"background-color: rgb(48, 48, 48);")
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, -10, 741, 501))
        self.stackedWidget.setStyleSheet("background-color: rgb(93, 107, 171);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.home = QtWidgets.QWidget()
        self.home.setObjectName("home")
        self.boton_luz = QtWidgets.QPushButton(self.home)
        self.boton_luz.setGeometry(QtCore.QRect(430, 160, 191, 81))
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
        self.boton_luz.setObjectName("boton_luz")
        self.boton_sensor = QtWidgets.QPushButton(self.home)
        self.boton_sensor.setGeometry(QtCore.QRect(170, 160, 191, 81))
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
        self.boton_sensor.setObjectName("boton_sensor")
        self.stackedWidget.addWidget(self.home)
        self.sensor = QtWidgets.QWidget()
        self.sensor.setObjectName("sensor")
        self.tabWidget = QtWidgets.QTabWidget(self.sensor)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(240, 20, 491, 461))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("background-color: rgb(153, 153, 230);")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.datos_sensor = QtWidgets.QWidget()
        self.datos_sensor.setObjectName("datos_sensor")
        self.texto_actualizar_auto = QtWidgets.QLabel(self.datos_sensor)
        self.texto_actualizar_auto.setGeometry(QtCore.QRect(10, 320, 231, 22))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.texto_actualizar_auto.setFont(font)
        self.texto_actualizar_auto.setObjectName("texto_actualizar_auto")
        self.texto_presion = QtWidgets.QLabel(self.datos_sensor)
        self.texto_presion.setGeometry(QtCore.QRect(10, 160, 291, 22))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.texto_presion.setFont(font)
        self.texto_presion.setObjectName("texto_presion")
        self.texto_humedad = QtWidgets.QLabel(self.datos_sensor)
        self.texto_humedad.setGeometry(QtCore.QRect(10, 120, 231, 22))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.texto_humedad.setFont(font)
        self.texto_humedad.setObjectName("texto_humedad")
        self.texto_humedad_dato = QtWidgets.QLabel(self.datos_sensor)
        self.texto_humedad_dato.setGeometry(QtCore.QRect(320, 120, 141, 22))
        self.texto_humedad_dato.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.texto_humedad_dato.setStyleSheet("font: 57 16pt \"Monoscape\";")
        self.texto_humedad_dato.setObjectName("texto_humedad_dato")
        self.texto_bateria_dato = QtWidgets.QLabel(self.datos_sensor)
        self.texto_bateria_dato.setGeometry(QtCore.QRect(320, 200, 141, 22))
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
        self.texto_presion_dato.setGeometry(QtCore.QRect(320, 160, 141, 22))
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
        self.texto_bateria.setGeometry(QtCore.QRect(10, 200, 231, 22))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.texto_bateria.setFont(font)
        self.texto_bateria.setObjectName("texto_bateria")
        self.texto_temperatura_dato = QtWidgets.QLabel(self.datos_sensor)
        self.texto_temperatura_dato.setGeometry(QtCore.QRect(320, 80, 141, 22))
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
        self.texto_temperatura.setGeometry(QtCore.QRect(10, 80, 231, 22))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(14)
        self.texto_temperatura.setFont(font)
        self.texto_temperatura.setObjectName("texto_temperatura")
        self.tiempo_actualizacion_sensor = QtWidgets.QTextEdit(self.datos_sensor)
        self.tiempo_actualizacion_sensor.setGeometry(QtCore.QRect(253, 310, 121, 41))
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
        self.etiqueta_conexion.setGeometry(QtCore.QRect(200, 30, 261, 22))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.etiqueta_conexion.setFont(font)
        self.etiqueta_conexion.setText("")
        self.etiqueta_conexion.setObjectName("etiqueta_conexion")
        self.boton_actualizar_datos_sensor = QtWidgets.QPushButton(self.datos_sensor)
        self.boton_actualizar_datos_sensor.setGeometry(QtCore.QRect(298, 260, 171, 30))
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
        self.boton_actualizar_datos_sensor.setObjectName("boton_actualizar_datos_sensor")
        self.boton_actualizar_datos_sensor_auto = QtWidgets.QPushButton(self.datos_sensor)
        self.boton_actualizar_datos_sensor_auto.setGeometry(QtCore.QRect(390, 310, 81, 41))
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
        self.texto_valido.setGeometry(QtCore.QRect(260, 360, 111, 21))
        self.texto_valido.setText("")
        self.texto_valido.setObjectName("texto_valido")
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
        self.tabWidget.addTab(self.datos_sensor, "")
        self.grafica_sensor = QtWidgets.QWidget()
        self.grafica_sensor.setObjectName("grafica_sensor")
        self.grafica = Grafica(self.grafica_sensor)
        self.grafica.setGeometry(QtCore.QRect(0, -30, 511, 471))
        self.grafica.setObjectName("grafica")
        self.tabWidget.addTab(self.grafica_sensor, "")
        self.tabla_sensor = QtWidgets.QWidget()
        self.tabla_sensor.setMouseTracking(False)
        self.tabla_sensor.setObjectName("tabla_sensor")
        self.boton_borrar_tabla = QtWidgets.QPushButton(self.tabla_sensor)
        self.boton_borrar_tabla.setGeometry(QtCore.QRect(370, 390, 99, 30))
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
        self.boton_borrar_tabla.setObjectName("boton_borrar_tabla")
        self.tabla_sensor_datos = QtWidgets.QTableWidget(self.tabla_sensor)
        self.tabla_sensor_datos.setGeometry(QtCore.QRect(0, 1, 491, 381))
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
        self.tabWidget.addTab(self.tabla_sensor, "")
        self.config_sensor = QtWidgets.QWidget()
        self.config_sensor.setObjectName("config_sensor")
        self.boton_anadir_sensor = QtWidgets.QPushButton(self.config_sensor)
        self.boton_anadir_sensor.setGeometry(QtCore.QRect(170, 90, 141, 71))
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
        self.boton_anadir_sensor.setObjectName("boton_anadir_sensor")
        self.boton_borrar_sensor = QtWidgets.QPushButton(self.config_sensor)
        self.boton_borrar_sensor.setGeometry(QtCore.QRect(170, 200, 141, 71))
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
        self.boton_borrar_sensor.setObjectName("boton_borrar_sensor")
        self.tabWidget.addTab(self.config_sensor, "")
        self.boton_atras_sensor = QtWidgets.QPushButton(self.sensor)
        self.boton_atras_sensor.setGeometry(QtCore.QRect(20, 20, 99, 30))
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
        self.boton_atras_sensor.setObjectName("boton_atras_sensor")
        self.boton_atras_sensor.raise_()
        self.tabWidget.raise_()
        self.stackedWidget.addWidget(self.sensor)
        self.bombilla = QtWidgets.QWidget()
        self.bombilla.setObjectName("bombilla")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.bombilla)
        self.tabWidget_2.setGeometry(QtCore.QRect(240, 10, 491, 471))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.tabWidget_2.setFont(font)
        self.tabWidget_2.setStyleSheet("background-color: rgb(153, 153, 230);")
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.datos_luz = QtWidgets.QWidget()
        self.datos_luz.setObjectName("datos_luz")
        self.brillo_slider = QtWidgets.QSlider(self.datos_luz)
        self.brillo_slider.setGeometry(QtCore.QRect(70, 90, 26, 281))
        self.brillo_slider.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.brillo_slider.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:0.55 rgba(210, 210, 210, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        self.brillo_slider.setOrientation(QtCore.Qt.Vertical)
        self.brillo_slider.setObjectName("brillo_slider")
        self.color_slider = QtWidgets.QSlider(self.datos_luz)
        self.color_slider.setGeometry(QtCore.QRect(190, 90, 26, 281))
        self.color_slider.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.color_slider.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255));")
        self.color_slider.setOrientation(QtCore.Qt.Vertical)
        self.color_slider.setObjectName("color_slider")
        self.satur_slider = QtWidgets.QSlider(self.datos_luz)
        self.satur_slider.setGeometry(QtCore.QRect(300, 90, 26, 281))
        self.satur_slider.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.satur_slider.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.55 rgba(210, 210, 210, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        self.satur_slider.setOrientation(QtCore.Qt.Vertical)
        self.satur_slider.setObjectName("satur_slider")
        self.etiqueta_brillo = QtWidgets.QLabel(self.datos_luz)
        self.etiqueta_brillo.setGeometry(QtCore.QRect(50, 40, 81, 22))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.etiqueta_brillo.setFont(font)
        self.etiqueta_brillo.setObjectName("etiqueta_brillo")
        self.etiqueta_color = QtWidgets.QLabel(self.datos_luz)
        self.etiqueta_color.setGeometry(QtCore.QRect(180, 40, 68, 22))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setBold(True)
        font.setWeight(75)
        self.etiqueta_color.setFont(font)
        self.etiqueta_color.setObjectName("etiqueta_color")
        self.etiqueta_satur = QtWidgets.QLabel(self.datos_luz)
        self.etiqueta_satur.setGeometry(QtCore.QRect(270, 40, 101, 22))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setBold(True)
        font.setWeight(75)
        self.etiqueta_satur.setFont(font)
        self.etiqueta_satur.setObjectName("etiqueta_satur")
        self.valor_brillo = QtWidgets.QLabel(self.datos_luz)
        self.valor_brillo.setGeometry(QtCore.QRect(60, 380, 41, 22))
        self.valor_brillo.setText("")
        self.valor_brillo.setObjectName("valor_brillo")
        self.valor_color = QtWidgets.QLabel(self.datos_luz)
        self.valor_color.setGeometry(QtCore.QRect(180, 380, 51, 22))
        self.valor_color.setText("")
        self.valor_color.setObjectName("valor_color")
        self.valor_satur = QtWidgets.QLabel(self.datos_luz)
        self.valor_satur.setGeometry(QtCore.QRect(300, 380, 41, 22))
        self.valor_satur.setText("")
        self.valor_satur.setObjectName("valor_satur")
        self.tabWidget_2.addTab(self.datos_luz, "")
        self.blanca_luz = QtWidgets.QWidget()
        self.blanca_luz.setObjectName("blanca_luz")
        self.brillo_blanco_slider = QtWidgets.QSlider(self.blanca_luz)
        self.brillo_blanco_slider.setGeometry(QtCore.QRect(80, 90, 26, 281))
        self.brillo_blanco_slider.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.brillo_blanco_slider.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:0.55 rgba(210, 210, 210, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        self.brillo_blanco_slider.setOrientation(QtCore.Qt.Vertical)
        self.brillo_blanco_slider.setObjectName("brillo_blanco_slider")
        self.temp_slider = QtWidgets.QSlider(self.blanca_luz)
        self.temp_slider.setGeometry(QtCore.QRect(190, 90, 26, 281))
        self.temp_slider.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.temp_slider.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(255, 255, 71, 255), stop:0.55 rgba(217, 209, 255, 255), stop:0.98 rgba(0, 0, 225, 255), stop:1 rgba(0, 0, 0, 0));")
        self.temp_slider.setOrientation(QtCore.Qt.Vertical)
        self.temp_slider.setObjectName("temp_slider")
        self.etiqueta_brillo_blanco = QtWidgets.QLabel(self.blanca_luz)
        self.etiqueta_brillo_blanco.setGeometry(QtCore.QRect(60, 40, 81, 22))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.etiqueta_brillo_blanco.setFont(font)
        self.etiqueta_brillo_blanco.setObjectName("etiqueta_brillo_blanco")
        self.etiqueta_temp_blanco = QtWidgets.QLabel(self.blanca_luz)
        self.etiqueta_temp_blanco.setGeometry(QtCore.QRect(150, 40, 111, 22))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.etiqueta_temp_blanco.setFont(font)
        self.etiqueta_temp_blanco.setObjectName("etiqueta_temp_blanco")
        self.valor_brillo_blanco = QtWidgets.QLabel(self.blanca_luz)
        self.valor_brillo_blanco.setGeometry(QtCore.QRect(70, 380, 41, 22))
        self.valor_brillo_blanco.setText("")
        self.valor_brillo_blanco.setObjectName("valor_brillo_blanco")
        self.valor_temp_blanco = QtWidgets.QLabel(self.blanca_luz)
        self.valor_temp_blanco.setGeometry(QtCore.QRect(180, 380, 41, 22))
        self.valor_temp_blanco.setText("")
        self.valor_temp_blanco.setObjectName("valor_temp_blanco")
        self.tabWidget_2.addTab(self.blanca_luz, "")
        self.config_luz = QtWidgets.QWidget()
        self.config_luz.setObjectName("config_luz")
        self.boton_borrar_bomb = QtWidgets.QPushButton(self.config_luz)
        self.boton_borrar_bomb.setGeometry(QtCore.QRect(170, 220, 141, 71))
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
        self.boton_borrar_bomb.setObjectName("boton_borrar_bomb")
        self.boton_anadir_bomb = QtWidgets.QPushButton(self.config_luz)
        self.boton_anadir_bomb.setGeometry(QtCore.QRect(170, 110, 141, 71))
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
        self.boton_anadir_bomb.setObjectName("boton_anadir_bomb")
        self.tabWidget_2.addTab(self.config_luz, "")
        self.boton_atras_luz = QtWidgets.QPushButton(self.bombilla)
        self.boton_atras_luz.setGeometry(QtCore.QRect(30, 20, 99, 30))
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
        self.boton_atras_luz.setObjectName("boton_atras_luz")
        self.boton_bomb_on = QtWidgets.QPushButton(self.bombilla)
        self.boton_bomb_on.setGeometry(QtCore.QRect(20, 419, 51, 41))
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
        self.boton_bomb_on.setObjectName("boton_bomb_on")
        self.boton_bomb_off = QtWidgets.QPushButton(self.bombilla)
        self.boton_bomb_off.setGeometry(QtCore.QRect(100, 420, 51, 41))
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
        self.boton_bomb_off.setObjectName("boton_bomb_off")
        self.stackedWidget.addWidget(self.bombilla)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.boton_luz.setText(_translate("MainWindow", "BOMBILLA"))
        self.boton_sensor.setText(_translate("MainWindow", "SENSOR"))
        self.texto_actualizar_auto.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Tiempo actualización (s)</span></p></body></html>"))
        self.texto_presion.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">PRESIÓN ATMOSFÉRICA (kPa)</span></p></body></html>"))
        self.texto_humedad.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">HUMEDAD (%)</span></p></body></html>"))
        self.texto_humedad_dato.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><br/></p></body></html>"))
        self.texto_bateria_dato.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><br/></p></body></html>"))
        self.texto_presion_dato.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><br/></p></body></html>"))
        self.texto_bateria.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">BATERIA (%)</span></p></body></html>"))
        self.texto_temperatura_dato.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><br/></p></body></html>"))
        self.texto_temperatura.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">TEMPERATURA (°C)</span></p></body></html>"))
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
        self.boton_anadir_sensor.setText(_translate("MainWindow", "CONECTAR"))
        self.boton_borrar_sensor.setText(_translate("MainWindow", "BORRAR"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.config_sensor), _translate("MainWindow", "Configuración"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.config_sensor), _translate("MainWindow", "Ver configuración"))
        self.boton_atras_sensor.setText(_translate("MainWindow", "ATRÁS"))
        self.etiqueta_brillo.setText(_translate("MainWindow", "BRILLO"))
        self.etiqueta_color.setText(_translate("MainWindow", "COLOR"))
        self.etiqueta_satur.setText(_translate("MainWindow", "SATURACIÓN"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.datos_luz), _translate("MainWindow", "Color"))
        self.tabWidget_2.setTabToolTip(self.tabWidget_2.indexOf(self.datos_luz), _translate("MainWindow", "Ver color"))
        self.etiqueta_brillo_blanco.setText(_translate("MainWindow", "BRILLO"))
        self.etiqueta_temp_blanco.setText(_translate("MainWindow", "TEMPERATURA"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.blanca_luz), _translate("MainWindow", "Blanca"))
        self.tabWidget_2.setTabToolTip(self.tabWidget_2.indexOf(self.blanca_luz), _translate("MainWindow", "Ver blanca"))
        self.boton_borrar_bomb.setText(_translate("MainWindow", "BORRAR"))
        self.boton_anadir_bomb.setText(_translate("MainWindow", "CONECTAR"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.config_luz), _translate("MainWindow", "Configuración"))
        self.tabWidget_2.setTabToolTip(self.tabWidget_2.indexOf(self.config_luz), _translate("MainWindow", "Ver configuración"))
        self.boton_atras_luz.setText(_translate("MainWindow", "ATRÁS"))
        self.boton_bomb_on.setText(_translate("MainWindow", "ON"))
        self.boton_bomb_off.setText(_translate("MainWindow", "OFF"))

from grafica import Grafica
