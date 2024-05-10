from PyQt5 import QtWidgets, uic

app = QtWidgets.QApplication([])

login= uic.loadUi("ventana1.ui")
entrar= uic.loadUi("ventana2.ui")
error= uic.loadUi("ventana3.ui")

def gui_login():
    name = login.lineEdit.text()
    password = login.lineEdit_2.text()
    if len(name)==0 or len(password)==0:
        login.label_4.setText("ingrese todos los datos")

    elif name== "yered" and password == "12345":
        gui_entrar()
    else:
        gui_error()

def gui_entrar():
    login.hide()
    entrar.show()

def gui_error():
    login.hide()
    error.show()

def regresar_entrar():
    entrar.hide()
    login.label_4.setText("")
    login.show()

def regresar_error():
    error.hide()
    login.label_4.setText("")
    login.show()

def salir():
    app.exit()

login.pushButton.clicked.connect(gui_login)
login.pushButton_2.clicked.connect(salir)

entrar.pushButton.clicked.connect(regresar_entrar)
error.pushButton.clicked.connect(regresar_entrar)
error.pushButton_2.clicked.connect(salir)
entrar.pushButton_2.clicked.connect(salir)

login.show()
app.exec()


