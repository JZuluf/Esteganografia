import psycopg2

class BaseDeDatos():
    url = ""
    port = 5432
    user = ""
    password = ""
    database = ""

    def __init__ (self, url, port, user, password, database):
        self.url = url
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    def conectar(self):
        try:
            credenciales = {
                "dbname": self.database,
                "user" : self.user,
                "password": self.password,
                "host": self.url,
                "port": self.port
            }
            conexion = psycopg2.connect(**credenciales)
            if conexion:
                print("conexión Exitosa")
            return conexion
        except psycopg2.Error as e:
            print("Ocurrio un error al conectar a postgreSQL: ", e)
