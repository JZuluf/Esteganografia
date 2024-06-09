from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog

from PIL import Image

caracter_terminacion = "11111111"

class OcultarMensaje:
    def __init__(self, ui):
        self.ui = ui
        self.ui.anadirarchivo.clicked.connect(self.tomar_imagen)
        self.ui.anadirarchivo_2.clicked.connect(self.buscar_ruta_de_salida)
        self.ui.ocultarmensaje.clicked.connect(self.ocultar_mensaje)

    def obtener_lsb(byte):
        return byte[-1]

    @staticmethod
    def obtener_representacion_binaria(numero):
        return bin(numero)[2:].zfill(8)

    @staticmethod
    def binario_a_decimal(binario):
        return int(binario, 2)

    @staticmethod
    def caracter_desde_codigo_ascii(numero):
        return chr(numero)

    @staticmethod
    def cifrar(mensaje, ruta_imagen_original, ruta_imagen_salida):

        imagen = Image.open(ruta_imagen_original)
        pixeles = imagen.load()

        tamaño = imagen.size
        anchura = tamaño[0]
        altura = tamaño[1]

        lista_bits_mensaje = OcultarMensaje.obtener_lista_de_bits(mensaje)

        contador = 0
        longitud = len(lista_bits_mensaje)

        for x in range(anchura):
            for y in range(altura):
                if contador < longitud:
                    pixel = pixeles[x, y]

                    rojo = pixel[0]
                    verde = pixel[1]
                    azul = pixel[2]

                    if contador < longitud:
                        rojo_modificado = OcultarMensaje.modificar_color(rojo, lista_bits_mensaje[contador])
                        contador += 1
                    else:
                        rojo_modificado = rojo

                    if contador < longitud:
                        verde_modificado = OcultarMensaje.modificar_color(verde, lista_bits_mensaje[contador])
                        contador += 1
                    else:
                        verde_modificado = verde

                    if contador < longitud:
                        azul_modificado = OcultarMensaje.modificar_color(azul, lista_bits_mensaje[contador])
                        contador += 1
                    else:
                        azul_modificado = azul

                    pixeles[x, y] = (rojo_modificado, verde_modificado, azul_modificado)
                else:
                    break
            else:
                continue
            break

        try:
            imagen.save(ruta_imagen_salida)
            print("Mensaje cifrado y guardado en", ruta_imagen_salida)
        except Exception as e:
            print(f"Error al guardar la imagen cifrada: {e}")
        print("cifrado completado")
    @staticmethod
    def obtener_lista_de_bits(texto):
        lista = []
        for letra in texto:
            representacion_ascii = ord(letra)
            representacion_binaria = OcultarMensaje.obtener_representacion_binaria(representacion_ascii)
            for bit in representacion_binaria:
                lista.append(bit)
        for bit in caracter_terminacion:
            lista.append(bit)
        return lista

    @staticmethod
    def modificar_color(color_original, bit):
        color_binario = OcultarMensaje.obtener_representacion_binaria(color_original)
        color_modificado = color_binario[:-1] + str(bit)
        return OcultarMensaje.binario_a_decimal(color_modificado)

    def tomar_imagen(self):
        options = QFileDialog.Options()
        imagepath, _ = QFileDialog.getOpenFileName(None, "Seleccionar Imagen", "",
                                                   "Imágenes (*.png *.jpg *.bmp);;Todos los archivos (*)",
                                                   options=options)
        if imagepath:
            self.ui.texto.setText(imagepath)
            pixmap = QPixmap(imagepath)
            self.ui.imagen.setPixmap(QPixmap(pixmap))
            self.ui.resize(pixmap.width(), pixmap.height())

    def buscar_ruta_de_salida(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(None, "Guardar Imagen como", "",
                                                   "Imágenes (*.png *.jpg *.bmp);;Todos los archivos (*)",
                                                   options=options)
        if file_name:
            self.ui.ruta_salida.setText(file_name)

    def ocultar_mensaje(self):
        mensaje = self.ui.mensaje.toPlainText()  # Obtener el texto del QTextEdit

        if not mensaje:
            QtWidgets.QMessageBox.warning(self.ui, "Advertencia", "Debe ingresar un mensaje para cifrar.")
            return

        ruta_imagen_original = self.ui.texto.toPlainText().strip()
        ruta_imagen_salida = self.ui.ruta_salida.toPlainText().strip()

        if not ruta_imagen_original:
            QtWidgets.QMessageBox.warning(self.ui, "Advertencia", "Debe seleccionar una imagen de entrada.")
            return

        if not ruta_imagen_salida:
            QtWidgets.QMessageBox.warning(self.ui, "Advertencia", "Debe seleccionar una ruta y nombre de salida.")
            return

        OcultarMensaje.cifrar(mensaje, ruta_imagen_original, ruta_imagen_salida)

