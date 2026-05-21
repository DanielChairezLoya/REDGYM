import sys
from PyQt6 import QtWidgets, uic
from conexion import Conexion
class AddMemberController:
    def __init__(self, window, model):
        self.window = window
        self.model = model
        #self.conexion=Conexion()
        #self.conexion.conectar()
        self.btn_add.clicked.connect(self.add_member)
        
    def add_member(self):
        name = self.txtName.text()
        last = self.txtApellido.text()
        email = self.txtNumber.text()
        
        if name.strip() == "" or last.strip() == "" or email.strip() == "":
            QtWidgets.QMessageBox.warning(self, "Favor de llenar todos los campos")   
        else:
            sql= "INSERT INTO users values (%s,%s,%s,%s,%s,%s)"
            valores = (0,name,last,email,'default.png')
            self.conexion.insertar(sql,valores)
            QtWidgets.QMessageBox.information(self,"registro insertado")    
    