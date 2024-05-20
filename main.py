import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog

from basededatos import BaseDeDatos
from usuarios import Usuario
from leer import *

app = QtWidgets.QApplication([])


# Cargar la interfaz de usuario
login = uic.loadUi("ventana1.ui")
entrar_admin = uic.loadUi("decifrarimagenadmin.ui")
entrar_user = uic.loadUi("decifrarimagenusu.ui")
error = uic.loadUi("ventana3.ui")
cerrar_sesion = uic.loadUi("cerrarsesion.ui")

# Inicializar la variable de conexión
conexionExitosa = None

def conectarBD():
    global conexionExitosa
    conexion = BaseDeDatos("bubble.db.elephantsql.com", 5432, "cnxcvolt", "3O13Dp1JaQF05JXHwl7FivVk-jwwxyVZ", "cnxcvolt")
    conexionExitosa = conexion.conectar()

def gui_login():
    global conexionExitosa

    if conexionExitosa is None:
        print("Conexión no establecida")
        return

    email = login.line_email.text()
    contraseña = login.line_contrasena.text()
    rol = login.line_rol.text()

    if len(email) == 0 or len(contraseña) == 0 or len(rol) == 0:
        login.label_4.setText("Ingrese todos los datos")
        return

    else:
        usuario = Usuario()
        try:
            if usuario.verificar_credenciales(conexionExitosa, email, contraseña, rol):
                rol = usuario.obtener_rol(conexionExitosa, email)
                if rol == "admin":
                    gui_entrar_admin()
                elif rol == "user":
                    gui_entrar_user()
                else:
                    gui_error()
            else:
                gui_error()

        except AttributeError as ex:
            print("Error de atributo:", ex)

        except ValueError as ex:
            print("Error de valor:", ex)

        except Exception as ex:
            print("Otro tipo de error:", ex)

def gui_entrar_admin():
    login.hide()
    entrar_admin.show()

def gui_entrar_user():
    login.hide()
    entrar_user.show()

    global buscar_archivo_gui
    buscar_archivo_gui = buscarArchivo(entrar_user)



def guardar_texto_en_archivo(mensaje):
    print(mensaje)
    options = QFileDialog.Options()
    file_name, _ = QFileDialog.getSaveFileName(None, "Guardar archivo de texto", "", "Archivos de texto (*.txt)", options=options)
    if file_name:
        with open(file_name, 'w') as archivo:
            archivo.write(mensaje)
        print("Texto guardado correctamente en:", file_name)

def gui_error():
    login.hide()
    error.show()

def gui_cerrarsesion1():
    entrar_user.hide()
    cerrar_sesion.show()

def regresar_entrar():
    entrar_admin.hide()
    login.label_4.setText("")
    login.show()

def regresar_error():
    error.hide()
    login.label_4.setText("")
    login.show()

def salir():
    app.exit()

# Conectar señales y ranuras
login.conectar.clicked.connect(conectarBD)
login.ingresar.clicked.connect(gui_login)
login.pushButton_2.clicked.connect(salir)

error.regresar.clicked.connect(login.show)
error.regresar.clicked.connect(error.hide)
error.pushButton_2.clicked.connect(salir)

entrar_user.cerrarsesion.clicked.connect(cerrar_sesion.show)
cerrar_sesion.cerrrar.clicked.connect(salir)


entrar_user.guardartextodecifrado.clicked.connect(guardar_texto_en_archivo("hola"))


# Mostrar la ventana principal
login.show()

# Ejecutar la aplicación
sys.exit(app.exec_())
