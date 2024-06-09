# leer.py
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPixmap
from PIL import Image
from PyQt5.QtWidgets import QFileDialog

caracter_terminacion = "11111111"

def obtener_lsb(byte):
    return byte[-1]

def obtener_representacion_binaria(numero):
    return bin(numero)[2:].zfill(8)

def binario_a_decimal(binario):
    return int(binario, 2)

def caracter_desde_codigo_ascii(numero):
    return chr(numero)

def leer(ruta_imagen):
    imagen = Image.open(ruta_imagen)
    pixeles = imagen.load()

    tamaño = imagen.size
    anchura = tamaño[0]
    altura = tamaño[1]

    byte = ""
    mensaje = ""

    for x in range(anchura):
        for y in range(altura):
            pixel = pixeles[x, y]

            rojo = pixel[0]
            verde = pixel[1]
            azul = pixel[2]

            byte += obtener_lsb(obtener_representacion_binaria(rojo))
            if len(byte) >= 8:
                if byte == caracter_terminacion:
                    break
                mensaje += caracter_desde_codigo_ascii(binario_a_decimal(byte))
                byte = ""

            byte += obtener_lsb(obtener_representacion_binaria(verde))
            if len(byte) >= 8:
                if byte == caracter_terminacion:
                    break
                mensaje += caracter_desde_codigo_ascii(binario_a_decimal(byte))
                byte = ""

            byte += obtener_lsb(obtener_representacion_binaria(azul))
            if len(byte) >= 8:
                if byte == caracter_terminacion:
                    break
                mensaje += caracter_desde_codigo_ascii(binario_a_decimal(byte))
                byte = ""

        else:
            continue
        break
    return mensaje

class buscarArchivo:
    def __init__(self, ui):
        self.ui = ui
        self.ui.anadirarchivo.clicked.connect(self.tomarImagen)
        self.ui.anadirarchivo_2.clicked.connect(self.tomarImagen)

    def buscar(self):
        options = QtWidgets.QFileDialog.Options()
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, options=options)

        if fileName:
            print(fileName)
            self.ui.texto.setText(str(fileName))
            archivo = open(fileName)
            texto = archivo.read()
            print(texto)
            self.ui.texto.setText(texto)

    def tomarImagen(self):
        options = QtWidgets.QFileDialog.Options()
        imagepath, _ = QtWidgets.QFileDialog.getOpenFileName(None, options=options)
        if imagepath:
            mensaje = leer(imagepath)
            print("El mensaje oculto es:")
            print(mensaje)
            pixmap = QPixmap(imagepath)
            self.ui.imagen.setPixmap(QPixmap(pixmap))
            archivo = open(imagepath, "rb")
            texto = archivo.read()
            self.ui.texto.setText(str(mensaje))
            self.ui.resize(pixmap.width(), pixmap.height())

            # Guardar el mensaje en un atributo del objeto ui
            self.ui.mensaje_decodificado = mensaje


