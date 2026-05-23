import sys
from datetime import date
from dateutil.relativedelta import relativedelta
from PyQt6 import QtWidgets, uic
from conexion import Conexion
class AddMemberController:
    def __init__(self, window, model):
        self.window = window
        self.model = model
        self.conexion=Conexion()
        self.conexion.conectar()
        
        self.window.btn_addm.clicked.connect(self.add_member)
        
    def add_member(self):
        name = self.window.txtNombre.text()
        last = self.window.txtApellido.text()
        number = str(self.window.txtNumber.text())
        fecha_actual=date.today()
        fecha_exp=fecha_actual+relativedelta(months=1)
        cobro="$350"
        status=True
        trainer=self.conexion.seleccionar("SELECT trainer_id FROM trainers WHERE trainer_id=1 limit 1")
        trainer_id=trainer[0][0]
        print(trainer_id)
        if name.strip() == "" or last.strip() == "" or number.strip() == "":
            QtWidgets.QMessageBox.warning(self.window, "Favor de llenar todos los campos")   
        else:
            sql= "INSERT INTO reports values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            valores = ('img/default.png',0,name,last,number,trainer_id,fecha_actual,fecha_exp,'$350','$0',status)
            self.conexion.insertar(sql,valores)
            QtWidgets.QMessageBox.information(self.window,"registro insertado","")
                
    