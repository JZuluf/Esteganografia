import psycopg2

class Usuario():
    id = ""
    nombre = ""
    apellido = ""
    cedula = ""
    contrasena = ""
    email = ""
    rol = ""

    def insertar(self, conexion, nombre, apellido, cedula, contrasena, email, rol):
        try:
            with conexion.cursor() as cursor:
                consulta = "INSERT INTO usuario(nombre, apellido, cedula, contraseña, email, rol) VALUES (%s, %s, %s, %s, %s, %s);"
                cursor.execute(consulta, (nombre, apellido, cedula, contrasena, email, rol))
            conexion.commit()
            print("usuario agregado correctamente")
            return True
        except psycopg2.Error as e:
            print("Ocurrio un error al crear el usuario: ", e)
            return False

    def consultarUsuarios(self, conexion):
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT id_usuario,nombre,apellido,cedula,email,rol FROM usuario;")
                usuarios = cursor.fetchall()
                return usuarios
                """for usuario in usuario:
                    print(usuario)"""
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar: ", e)

    def consultarNombre(self, conexion, nombre):
        cursor = conexion.cursor()
        query = "SELECT * FROM usuario WHERE nombre = %s"
        cursor.execute(query, (nombre,))
        resultados = cursor.fetchall()
        cursor.close()
        return resultados

    def consultarApellido(self, conexion, apellido):
        cursor = conexion.cursor()
        query = "SELECT * FROM usuario WHERE apellido = %s"
        cursor.execute(query, (apellido,))
        resultados = cursor.fetchall()
        cursor.close()
        return resultados

    def verificar_credenciales(self, conexion, email, contrasena):
        try:
            with conexion.cursor() as cursor:
                consulta = "SELECT * FROM usuario WHERE email = %s AND contraseña = %s;"
                cursor.execute(consulta, (email, contrasena))
                usuario = cursor.fetchone()
                if usuario:
                    print("Credenciales válidas")
                    return True
                else:
                    print("Credenciales inválidas")
                    return False
        except psycopg2.Error as e:
            print("Ocurrió un error al verificar las credenciales: ", e)
            return False

    def obtener_rol(self, conexion, email):
        try:
            with conexion.cursor() as cursor:
                consulta = "SELECT rol FROM usuario WHERE email = %s;"
                cursor.execute(consulta, (email,))
                rol = cursor.fetchone()
                if rol:
                    return rol[0]  # Devuelve el primer valor de la tupla (el rol)
                else:
                    print("El usuario no existe")
                    return None
        except psycopg2.Error as e:
            print("Ocurrió un error al obtener el rol: ", e)
            return None
