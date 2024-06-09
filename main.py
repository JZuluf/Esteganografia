import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from insertarusuarios import *
from basededatos import BaseDeDatos
from usuarios import Usuario
from leer import *
from ocultar import *
from consulta import *


class App:
    def __init__(self):
        self.app = QtWidgets.QApplication([])

        # Cargar la interfaz de usuario
        self.login = uic.loadUi("ventanas_interfaz/ventana1.ui")
        self.entrar_admin = uic.loadUi("ventanas_interfaz/decifrarimagenadmin.ui")
        self.entrar_user = uic.loadUi("ventanas_interfaz/decifrarimagenusu.ui")
        self.error = uic.loadUi("ventanas_interfaz/ventana3.ui")
        self.cerrar_sesion = uic.loadUi("ventanas_interfaz/cerrarsesion.ui")
        self.cifrarusu = uic.loadUi("ventanas_interfaz/cifrarimagenusu.ui")
        self.cerrarsesioncifrausu = uic.loadUi("ventanas_interfaz/cerrarsesion.ui")
        self.informacionusu = uic.loadUi("ventanas_interfaz/informacion_usuario.ui")
        self.cerrarsesioninfousu = uic.loadUi("ventanas_interfaz/cerrarsesion.ui")
        self.informacionadmin = uic.loadUi("ventanas_interfaz/informacion_usuarioadmin.ui")
        self.cifraradmin = uic.loadUi("ventanas_interfaz/cifrarimagenadm.ui")
        self.cerrarsesioninfoadmin = uic.loadUi("ventanas_interfaz/cerrarsesion.ui")
        self.cerrarsesiondecifraradmin = uic.loadUi("ventanas_interfaz/cerrarsesion.ui")
        self.crearusuarios = uic.loadUi("ventanas_interfaz/crearusuarios.ui")
        self.cerrarsesioncifraradmin = uic.loadUi("ventanas_interfaz/cerrarsesion.ui")
        self.cerrarsesioncrearusuario = uic.loadUi("ventanas_interfaz/cerrarsesion.ui")
        self.cerrarsesionresumenusu = uic.loadUi("ventanas_interfaz/cerrarsesion.ui")
        self.resumenusuarios = uic.loadUi("ventanas_interfaz/resumenusuarios.ui")

        self.conexionExitosa = None

        # Conectar señales y slots
        self.login.ingresar.clicked.connect(self.gui_login)
        self.login.pushButton_2.clicked.connect(self.salir)

        self.error.regresar.clicked.connect(self.regresar_error)
        self.error.pushButton_2.clicked.connect(self.salir)

        self.cerrar_sesion.cerrrar.clicked.connect(self.salir)
        self.cerrar_sesion.cancelar.clicked.connect(self.gui_cerrarsesion2)
        self.cerrarsesioncifrausu.cerrrar.clicked.connect(self.salir)
        self.cerrarsesioncifrausu.cancelar.clicked.connect(self.gui_cerrarsesion4)
        self.cerrarsesioninfousu.cerrrar.clicked.connect(self.salir)
        self.cerrarsesioninfousu.cancelar.clicked.connect(self.gui_cerrarsesion6)
        self.cerrarsesioninfoadmin.cerrrar.clicked.connect(self.salir)
        self.cerrarsesioninfoadmin.cancelar.clicked.connect(self.gui_cerrarsesion8)
        self.cerrarsesiondecifraradmin.cerrrar.clicked.connect(self.salir)
        self.cerrarsesiondecifraradmin.cancelar.clicked.connect(self.gui_cerrarsesion10)
        self.cerrarsesioncifraradmin.cerrrar.clicked.connect(self.salir)
        self.cerrarsesioncifraradmin.cancelar.clicked.connect(self.gui_cerrarsesion12)
        self.cerrarsesioncrearusuario.cerrrar.clicked.connect(self.salir)
        self.cerrarsesioncrearusuario.cancelar.clicked.connect(self.gui_cerrarsesion14)
        self.cerrarsesionresumenusu.cerrrar.clicked.connect(self.salir)
        self.cerrarsesionresumenusu.cancelar.clicked.connect(self.gui_cerrarsesion16)

        self.entrar_admin.guardartextodecifrados.clicked.connect(self.guardar_texto_en_archivo2)
        self.entrar_admin.infousuario.clicked.connect(self.gui_infousuarioadmin)
        self.entrar_admin.cifraradmin.clicked.connect(self.gui_cifrarimagenadmin)
        self.entrar_admin.cerrarsesion.clicked.connect(self.gui_cerrarsesion9)
        self.entrar_admin.crearusuarios.clicked.connect(self.gui_crearusuarios)
        self.entrar_admin.resumen.clicked.connect(self.gui_resumendeusuario)

        self.cifraradmin.decifrarimagen.clicked.connect(self.gui_cifrarDecifraradmin)
        self.cifraradmin.infousuario.clicked.connect(self.gui_cifrarInfousuario)
        self.cifraradmin.crearusuario.clicked.connect(self.gui_cifrarCrearusuario)
        self.cifraradmin.cerrarsesion.clicked.connect(self.gui_cerrarsesion11)
        self.cifraradmin.resumenusuario.clicked.connect(self.gui_cifrarResumen)

        self.entrar_user.cerrarsesion.clicked.connect(self.gui_cerrarsesion1)
        self.entrar_user.guardartextodecifrado.clicked.connect(self.guardar_texto_en_archivo)
        self.entrar_user.cifrarimagen.clicked.connect(self.gui_cifrarimagenusu)
        self.entrar_user.infousuario.clicked.connect(self.gui_infousuario)

        self.cifrarusu.cerrarsesion.clicked.connect(self.gui_cerrarsesion3)
        self.cifrarusu.decifrarimagenusuario.clicked.connect(self.gui_entrar_user2)
        self.cifrarusu.infousuario.clicked.connect(self.gui_infousuario2)

        self.informacionusu.cifrarusuario.clicked.connect(self.gui_cifrarusuario)
        self.informacionusu.decifrarusuario.clicked.connect(self.gui_decifrarusuario)
        self.informacionusu.cerrarsesion.clicked.connect(self.gui_cerrarsesion5)

        self.informacionadmin.cifrarusuario.clicked.connect(self.gui_cifraradmin)
        self.informacionadmin.decifrarusuario.clicked.connect(self.gui_decifraradmin)
        self.informacionadmin.crearusuario.clicked.connect(self.gui_infousuarioCrearusuario)
        self.informacionadmin.cerrarsesion.clicked.connect(self.gui_cerrarsesion7)
        self.informacionadmin.resumenusuario.clicked.connect(self.gui_informacionResumenusuario)

        self.crearusuarios.infousuario.clicked.connect(self.gui_crearusuarioInfousuario)
        self.crearusuarios.decifraradmin.clicked.connect(self.gui_crearusuarioDecifraradmin)
        self.crearusuarios.cifraradmin.clicked.connect(self.gui_crearusuarioCifraradmin)
        self.crearusuarios.cerrarsesion.clicked.connect(self.gui_cerrarsesion13)
        self.crearusuarios.resumenusuario.clicked.connect(self.gui_crearResumen)

        self.resumenusuarios.crearusuario.clicked.connect(self.gui_resumenCrearusuario)
        self.resumenusuarios.decifrar.clicked.connect(self.gui_resumenDecifrar)
        self.resumenusuarios.cifrar.clicked.connect(self.gui_resumenCifrar)
        self.resumenusuarios.infousuario.clicked.connect(self.gui_resumeninfousuario)
        self.resumenusuarios.cerrarsesion.clicked.connect(self.gui_cerrarsesion15)

        # Intentar conectar a la base de datos automáticamente
        self.conectarBD()

        # Mostrar la ventana principal
        self.login.show()

        # Ejecutar la aplicación
        sys.exit(self.app.exec_())

    def conectarBD(self):
        self.conexionExitosa = BaseDeDatos("bubble.db.elephantsql.com", 5432, "cnxcvolt",
                                           "3O13Dp1JaQF05JXHwl7FivVk-jwwxyVZ", "cnxcvolt").conectar()
        if self.conexionExitosa:
            print("Conexión establecida exitosamente")
        else:
            print("No se pudo establecer la conexión con la base de datos")
            self.login.label_4.setText("Error de conexión con la base de datos")

    def gui_login(self):
        if self.conexionExitosa is None:
            print("Conexión no establecida")
            self.login.label_4.setText("Error de conexión con la base de datos")
            return

        email = self.login.line_email.text().strip()
        contrasena = self.login.line_contrasena.text()

        if len(email) == 0 or len(contrasena) == 0:
            self.login.label_4.setText("Ingrese todos los datos")
            return

        usuario = Usuario()
        try:
            if usuario.verificar_credenciales(self.conexionExitosa, email, contrasena):
                rol = usuario.obtener_rol(self.conexionExitosa, email)
                if rol == "admin":
                    self.gui_entrar_admin()
                elif rol == "user":
                    self.gui_entrar_user()
                else:
                    self.gui_error()
            else:
                self.gui_error()

        except AttributeError as ex:
            print("Error de atributo:", ex)
        except ValueError as ex:
            print("Error de valor:", ex)
        except Exception as ex:
            print("Otro tipo de error:", ex)


    "manejo de interfaces del usuario"

    def gui_entrar_user(self):
        self.login.hide()
        self.entrar_user.show()
        self.buscar_archivo_gui = buscarArchivo(self.entrar_user)

    def gui_entrar_user2(self):
        self.cifrarusu.hide()
        self.entrar_user.show()
        self.buscar_archivo_gui = buscarArchivo(self.entrar_user)

    def gui_infousuario(self):
        self.entrar_user.hide()
        self.informacionusu.show()

    def gui_infousuario2(self):
        self.cifrarusu.hide()
        self.informacionusu.show()

    def gui_cifrarusuario(self):
        self.informacionusu.hide()
        self.cifrarusu.show()

    def gui_cifrarimagenusu(self):
        self.entrar_user.hide()
        self.cifrarusu.show()
        self.ocultarMensaje_gui = OcultarMensaje(self.cifrarusu)

    def gui_decifrarusuario(self):
        self.informacionusu.hide()
        self.entrar_user.show()

    "Manejo de interfaces administrador"

    def gui_infousuarioadmin(self):
        self.entrar_admin.hide()
        self.informacionadmin.show()

    def gui_infousuarioCrearusuario(self):
        self.informacionadmin.hide()
        self.crearusuarios.show()


    def gui_entrar_admin(self):
        self.login.hide()
        self.entrar_admin.show()
        self.buscar_archivo_gui = buscarArchivo(self.entrar_admin)
    def gui_cifraradmin(self):
        self.informacionadmin.hide()
        self.cifraradmin.show()

    def gui_cifrarimagenadmin(self):
        self.entrar_admin.hide()
        self.cifraradmin.show()
        self.ocultarMensajeadmin_gui = OcultarMensaje(self.cifraradmin)

    def gui_resumendeusuario(self):
        self.entrar_admin.hide()
        self.resumenusuarios.show()
        self.resumen_gui = consultarusuaariosgenerales(self.resumenusuarios)

    def gui_crearResumen(self):
        self.crearusuarios.hide()
        self.resumenusuarios.show()

    def gui_cifrarDecifraradmin(self):
        self.cifraradmin.hide()
        self.entrar_admin.show()

    def gui_cifrarInfousuario(self):
        self.cifraradmin.hide()
        self.informacionadmin.show()

    def gui_informacionResumenusuario(self):
        self.informacionadmin.hide()
        self.resumenusuarios.show()

    def gui_cifrarCrearusuario(self):
        self.cifraradmin.hide()
        self.crearusuarios.show()

    def gui_cifrarResumen(self):
        self.cifraradmin.hide()
        self.resumenusuarios.show()

    def gui_crearusuarioInfousuario(self):
        self.crearusuarios.hide()
        self.informacionadmin.show()

    def gui_crearusuarioDecifraradmin(self):
        self.crearusuarios.hide()
        self.entrar_admin.show()

    def gui_crearusuarioCifraradmin(self):
        self.crearusuarios.hide()
        self.cifraradmin.show()

    def gui_decifraradmin(self):
        self.informacionadmin.hide()
        self.entrar_admin.show()

    def gui_crearusuarios(self):
        self.entrar_admin.hide()
        self.crearusuarios.show()
        self.crearusuarios_gui = insertar(self.crearusuarios)

    def gui_resumenCrearusuario(self):
        self.resumenusuarios.hide()
        self.crearusuarios.show()

    def gui_resumenDecifrar(self):
        self.resumenusuarios.hide()
        self.entrar_admin.show()

    def gui_resumenCifrar(self):
        self.resumenusuarios.hide()
        self.cifraradmin.show()

    def gui_resumeninfousuario(self):
        self.resumenusuarios.hide()
        self.informacionadmin.show()

    "guardar texto"

    def guardar_texto_en_archivo(self):
        # Obtener el mensaje decodificado del atributo de la interfaz de usuario
        mensaje = getattr(self.entrar_user, 'mensaje_decodificado', '')

        if not mensaje:
            QMessageBox.warning(self.entrar_user, "Advertencia", "No hay mensaje decodificado para guardar.")
            print("No hay mensaje decodificado para guardar.")
            return

        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(None, "Guardar archivo de texto", "", "Archivos de texto (*.txt)",
                                                   options=options)
        if file_name:
            with open(file_name, 'w') as archivo:
                archivo.write(mensaje)
            print("Texto guardado correctamente en:", file_name)

    def guardar_texto_en_archivo2(self):
        # Obtener el mensaje decodificado del atributo de la interfaz de usuario
        mensaje = getattr(self.entrar_admin, 'mensaje_decodificado', '')

        if not mensaje:
            QMessageBox.warning(self.entrar_admin, "Advertencia", "No hay mensaje decodificado para guardar.")
            print("No hay mensaje decodificado para guardar.")
            return

        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(None, "Guardar archivo de texto", "", "Archivos de texto (*.txt)",
                                                   options=options)
        if file_name:
            with open(file_name, 'w') as archivo:
                archivo.write(mensaje)
            print("Texto guardado correctamente en:", file_name)

    "cerar sesiones"
    def gui_cerrarsesion1(self):
        self.entrar_user.hide()
        self.cerrar_sesion.show()

    def gui_cerrarsesion2(self):
        self.cerrar_sesion.hide()
        self.entrar_user.show()

    def gui_cerrarsesion3(self):
        self.cifrarusu.hide()
        self.cerrarsesioncifrausu.show()

    def gui_cerrarsesion4(self):
        self.cerrarsesioncifrausu.hide()
        self.cifrarusu.show()

    def gui_cerrarsesion5(self):
        self.informacionusu.hide()
        self.cerrarsesioninfousu.show()

    def gui_cerrarsesion6(self):
        self.cerrarsesioninfousu.hide()
        self.informacionusu.show()

    def gui_cerrarsesion7(self):
        self.informacionadmin.hide()
        self.cerrarsesioninfoadmin.show()

    def gui_cerrarsesion8(self):
        self.cerrarsesioninfoadmin.hide()
        self.informacionadmin.show()

    def gui_cerrarsesion9(self):
        self.entrar_admin.hide()
        self.cerrarsesiondecifraradmin.show()

    def gui_cerrarsesion10(self):
        self.cerrarsesiondecifraradmin.hide()
        self.entrar_admin.show()

    def gui_cerrarsesion11(self):
        self.cifraradmin.hide()
        self.cerrarsesioncifraradmin.show()

    def gui_cerrarsesion12(self):
        self.cerrarsesioncifraradmin.hide()
        self.cifraradmin.show()

    def gui_cerrarsesion13(self):
        self.crearusuarios.hide()
        self.cerrarsesioncrearusuario.show()

    def gui_cerrarsesion14(self):
        self.cerrarsesioncrearusuario.hide()
        self.crearusuarios.show()

    def gui_cerrarsesion15(self):
        self.resumenusuarios.hide()
        self.cerrarsesionresumenusu.show()

    def gui_cerrarsesion16(self):
        self.cerrarsesionresumenusu.hide()
        self.resumenusuarios.show()

    "errores del login y salir de interfaces"

    def gui_error(self):
        self.login.hide()
        self.error.show()

    def regresar_error(self):
        self.error.hide()
        self.login.label_4.setText("")
        self.login.show()

    def salir(self):
        self.app.exit()


if __name__ == "__main__":
    App()
