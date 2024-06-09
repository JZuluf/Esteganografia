import sys
import ast
from typing import Any
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5 import QtWidgets
from basededatos import *
from usuarios import *


class consultarusuaariosgenerales(QMainWindow):
    conexionExitosa: Any = None  # Cambié el valor predeterminado a None

    def __init__(self, ui):
        super().__init__()
        self.ui = ui
        self.conectarBD()  # Establecer la conexión en la inicialización
        self.ui.consultarTodos.clicked.connect(self.consultarTodosBD)
        self.ui.consultarNombre.clicked.connect(self.consultarNombreBD)
        self.ui.consultarApellido.clicked.connect(self.consultarApellidoBD)

        self.nombre = self.ui.nombre
        self.apellido = self.ui.apellido
        "self.cedula = self.ui.cedula"


    # Conectar la base de datos
    def conectarBD(self):
        if self.conexionExitosa is None:  # Asegurar que la conexión no se establezca si ya está establecida
            conexion = BaseDeDatos("bubble.db.elephantsql.com", 5432, "cnxcvolt", "3O13Dp1JaQF05JXHwl7FivVk-jwwxyVZ",
                                   "cnxcvolt")
            self.conexionExitosa = conexion.conectar()

    # Desconectar la base de datos
    def desconectarBD(self):
        try:
            if self.conexionExitosa:  # Verificar si hay una conexión establecida antes de intentar cerrarla
                self.conexionExitosa.close()
                print("Conexión terminada")
                self.conexionExitosa = None  # Establecer la conexión a None después de cerrarla
            else:
                print("No hay conexión establecida para cerrar")
        except Exception as ex:
            print("Error al cerrar la conexión:", type(ex))

    # Consultar todos los registros en la base de datos
    def consultarTodosBD(self):
        usuario = Usuario()
        self.eliminarFila()
        try:
            data = usuario.consultarUsuarios(self.conexionExitosa)
            for row in data:
                self.adicionarFila(self.convert(row))  # Llamada a convert aquí

        except Exception as ex:
            print("Error de conexión", type(ex))

    # Adicionar una fila a la tabla
    def adicionarFila(self, columns):
        fila = self.ui.tablaBD.rowCount()  # Nota: cambié self.tablaBD a self.ui.tablaBD
        self.ui.tablaBD.insertRow(fila)  # insert new row
        for i, column in enumerate(columns):
            self.ui.tablaBD.setItem(fila, i, QtWidgets.QTableWidgetItem(str(column)))

    # Eliminar una fila de la tabla
    def eliminarFila(self):
        filas = self.ui.tablaBD.rowCount()  # Nota: cambié self.tablaBD a self.ui.tablaBD
        for i in range(filas):
            self.ui.tablaBD.removeRow(0)   # Siempre se borra la fila 0 y en cada ciclo se va subiendo la fila hasta
                                            # terminar todo

    # Consultar un registro por nombre
    def consultarNombreBD(self):
        nombre = self.nombre.text()
        usuario = Usuario()
        try:
            resultados = usuario.consultarNombre(self.conexionExitosa, nombre)
            if resultados:
                print("Resultados de la consulta por nombre:", resultados)
                QMessageBox.information(self, "Resultados", f"Resultados: {resultados}")
            else:
                print("No se encontraron resultados")
                QMessageBox.information(self, "Resultados", "No se encontraron resultados")
        except Exception as ex:
            print("Error de conexión", type(ex), ex)
            QMessageBox.critical(self, "Error", f"Error de conexión: {str(ex)}")
            if self.conexionExitosa:
                self.conexionExitosa.rollback()

    def consultarApellidoBD(self):
        apellido = self.apellido.text()
        usuario = Usuario()
        try:
            resultados = usuario.consultarApellido(self.conexionExitosa, apellido)
            if resultados:
                print("Resultados de la consulta por apellido:", resultados)
                QMessageBox.information(self, "Resultados", f"Resultados: {resultados}")
            else:
                print("No se encontraron resultados")
                QMessageBox.information(self, "Resultados", "No se encontraron resultados")
        except Exception as ex:
            print("Error de conexión", type(ex), ex)
            QMessageBox.critical(self, "Error", f"Error de conexión: {str(ex)}")
            if self.conexionExitosa:
                self.conexionExitosa.rollback()

    def consultarCedulaBD(self):
        cedula = self.cedula.text()
        usuario = Usuario()
        try:
            resultados = usuario.consultarCedula(self.conexionExitosa, cedula)  # Añadir método en la clase Usuario
            if resultados:
                print("Resultados de la consulta por cédula:", resultados)
                QMessageBox.information(self, "Resultados", f"Resultados: {resultados}")
            else:
                print("No se encontraron resultados")
                QMessageBox.information(self, "Resultados", "No se encontraron resultados")
        except Exception as ex:
            print("Error de conexión", type(ex), ex)
            QMessageBox.critical(self, "Error", f"Error de conexión: {str(ex)}")
            if self.conexionExitosa:
                self.conexionExitosa.rollback()

    # La función convert integrada en la clase
    def convert(self, in_data):
        def cvt(data):
            try:
                return ast.literal_eval(data)
            except Exception:
                return str(data)
        return tuple(map(cvt, in_data))



