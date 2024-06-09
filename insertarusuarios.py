import sys
from basededatos import *
from usuarios import *
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from typing import Any


class insertar:
    conexionExitosa: Any = None

    def __init__(self, ui):
        super().__init__()
        self.ui = ui
        self.conectarBD()
        self.ui.conectar.clicked.connect(self.conectarBD)
        self.ui.guardar.clicked.connect(self.insertarBD)
        self.nombre = self.ui.nombre
        self.apellido = self.ui.apellido
        self.cedula = self.ui.cedula
        self.contrasena = self.ui.contrasena
        self.email = self.ui.email
        self.rol = self.ui.rol
        self.resultado = self.ui.resultado

    def conectarBD(self):
        if self.conexionExitosa is None:  # Asegurar que la conexión no se establezca si ya está establecida
            conexion = BaseDeDatos("bubble.db.elephantsql.com", 5432, "cnxcvolt", "3O13Dp1JaQF05JXHwl7FivVk-jwwxyVZ",
                                   "cnxcvolt")
            self.conexionExitosa = conexion.conectar()

    def insertarBD(self):
        nombre = self.nombre.text()
        apellido = self.apellido.text()
        cedula = self.cedula.text()
        contrasena = self.contrasena.text()
        email = self.email.text()
        rol = self.rol.text()

        # Verificar si el email contiene '@'
        if '@' not in email:
            QMessageBox.warning(self.ui, 'Error', 'El email debe contener el carácter @')
            return

        # Verificar si el rol es 'admin' o 'user'
        if rol not in ['admin', 'user']:
            QMessageBox.warning(self.ui, 'Error', 'El rol debe ser "admin" o "user"')
            return

        self.resultado.setText(nombre + " " + apellido + " " + cedula + " " + contrasena + " " + email + " " + rol)
        usuario = Usuario()
        try:
            if usuario.insertar(self.conexionExitosa, nombre, apellido, cedula, contrasena, email, rol):
                print("Usuario ingresado correctamente")
            else:
                print("Error en la creación del usuario")
        except Exception as ex:
            print("Error en la conexión", type(ex))

