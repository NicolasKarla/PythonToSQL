import mysql.connector

def menu_opciones():
    answer = int(input("Ingresa la opcion de lo que deseas hacer: \n 1-Ingresar Nuevo Usuario\n 2-ver tabla"))
    if answer == 1:
        IngresoUsuario()
    elif answer == 2:
        imprimir_tabla()
    else:
        print("el valor ingresado es erroneo")
def IngresoUsuario():
    AnswerId = input("Ingrese Id del usuario")
    AnswerName = input("Ingrese nombre del usuario")
    mi_bd.insertar_evento(AnswerId,AnswerName)
    print(f"el usuario{AnswerName} ha sido ingresado")

class MiBaseDeDatos:
    def __init__(self):
        self.conexion = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="admin1234",
            database="FirstData"
        )
        self.cursor = self.conexion.cursor()
    def insertar_evento(self, id, name):
        insert_query = "INSERT INTO user (id, name) VALUES (%s, %s)"
        datos = (id, name)
        self.cursor.execute(insert_query, datos)
        self.conexion.commit()
        print("Registro insertado correctamente.")
    def obtener_registros(self):
        select_query = "SELECT * FROM user"
        self.cursor.execute(select_query)
        return self.cursor.fetchall()
    
    def cerrar_conexion(self):
        self.cursor.close()
        self.conexion.close()
def imprimir_tabla():
        mi_bd = MiBaseDeDatos()
        registros = mi_bd.obtener_registros()
        mi_bd.cerrar_conexion()
        print("Tabla 'user':")
        print("ID\tNombre")
        print("-" * 20)
        for registro in registros:
            id, name = registro
            print(f"{id}\t{name}")
# Ejemplo de uso

if __name__ == "__main__":
    mi_bd = MiBaseDeDatos()
    menu_opciones()
    mi_bd.cerrar_conexion()

