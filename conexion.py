import mysql.connector
from mysql.connector import Error
import mariadb
class Conexion:
    def __init__(self):
        self.config = {
            "host":'localhost',
            "user":'root',
            "password":"",
            "database":"redgym"
        }
        
        
        self.conexion = None
        self.cursor = None
    def conectar(self):
        try:
            self.conexion = mariadb.connect(**self.config)
            print("Conexión exitosa")   
            self.cursor = self.conexion.cursor()
        except Exception as e:
            print(f"ERROR: {e}")
            
    def insertar(self, sql, valores):
        self.cursor.execute(sql, valores)
        self.conexion.commit()
        #sirve para seleccionar bonito
    def seleccionar (self,sql):
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def borrar(self,sql):
        self.cursor.execute(sql)
        self.conexion.commit()