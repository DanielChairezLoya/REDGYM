from PyQt6 import QtWidgets, uic
from conexion import Conexion
class AddTrainerController:
    def __init__(self, window, model):
        self.window = window
        self.model = model
        self.conexion=Conexion()
        self.conexion.conectar()
        self.window.btn_add.clicked.connect(self.add_member)
        
    def add_member(self):
        name = self.window.txtNombre.text()
        last = self.window.txtApellido.text()
        number = str(self.window.txtNumber.text())
        email=str(self.window.txtEmail.text())
        experience=str(self.window.txtExperience.text())
        
        
        if name.strip() == "" or last.strip() == "" or number.strip() == "":
            QtWidgets.QMessageBox.warning(self.window, "Favor de llenar todos los campos")   
        else:
            sql= "INSERT INTO trainers values (%s,%s,%s,%s,%s,%s,%s,%s)"
            valores = (0,'img/default.png',name,last,number,email,experience,"0 Star")
            print(sql,valores)
            self.conexion.insertar(sql,valores)
            QtWidgets.QMessageBox.information(self.window,"registro insertado","")