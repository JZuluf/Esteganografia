# leer.py
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog, QInputDialog, QMessageBox, QLineEdit
from cryptography.fernet import Fernet
from PIL import Image
import base64
import hashlib

caracter_terminacion = "11111111"

def obtener_lsb(byte):
    return byte[-1]

def obtener_representacion_binaria(numero):
    return bin(numero)[2:].zfill(8)

def binario_a_decimal(binario):
    return int(binario, 2)

def caracter_desde_codigo_ascii(numero):
    return chr(numero)

def leer(ruta_imagen, contrasena):
    imagen = Image.open(ruta_imagen)
    pixeles = imagen.load()

    tamaño = imagen.size
    anchura = tamaño[0]
    altura = tamaño[1]

    byte = ""
    mensaje_encriptado = ""

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
                mensaje_encriptado += caracter_desde_codigo_ascii(binario_a_decimal(byte))
                byte = ""

            byte += obtener_lsb(obtener_representacion_binaria(verde))
            if len(byte) >= 8:
                if byte == caracter_terminacion:
                    break
                mensaje_encriptado += caracter_desde_codigo_ascii(binario_a_decimal(byte))
                byte = ""

            byte += obtener_lsb(obtener_representacion_binaria(azul))
            if len(byte) >= 8:
                if byte == caracter_terminacion:
                    break
                mensaje_encriptado += caracter_desde_codigo_ascii(binario_a_decimal(byte))
                byte = ""

        else:
            continue
        break

    # Generar una clave Fernet a partir de la contraseña
    key = base64.urlsafe_b64encode(hashlib.sha256(contrasena.encode()).digest())

    # Desencriptar el mensaje con la contraseña
    fernet = Fernet(key)
    try:
        mensaje = fernet.decrypt(mensaje_encriptado.encode()).decode()
    except Exception as e:
        QMessageBox.warning(None, "Error", "La contraseña es incorrecta o el mensaje no puede ser descifrado.")
        return ""

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
            contrasena, ok = QInputDialog.getText(None, "Contraseña", "Ingrese la contraseña:", QLineEdit.Password)
            if not ok:
                return

            imagen = Image.open(imagepath)
            if imagen.size != (1024, 768):
                QMessageBox.warning(None, "Advertencia", "La imagen debe ser de 1024 x 768 píxeles.")
                return

            mensaje = leer(imagepath, contrasena)
            print("El mensaje oculto es:")
            print(mensaje)
            pixmap = QPixmap(imagepath)
            self.ui.imagen.setPixmap(QPixmap(pixmap))
            self.ui.texto.setText(str(mensaje))
            self.ui.resize(pixmap.width(), pixmap.height())

            # Guardar el mensaje en un atributo del objeto ui
            self.ui.mensaje_decodificado = mensaje
