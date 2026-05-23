from PyQt6 import QtWidgets, uic
import sys
from conexion import Conexion
from controllers.login_controller import LoginController
from controllers.menu_controller import MenuController
from controllers.trainers_controller import TrainerController
from controllers.report_controller import ReportController
from controllers.addM_controller import AddMemberController
from controllers.addT_controller import AddTrainerController
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QPalette
from PyQt6.QtWidgets import QTableWidgetItem

class Login(QtWidgets.QMainWindow):
    login_succesfull=pyqtSignal()
    
    def __init__(self):
        super().__init__()
        uic.loadUi("./views/login.ui",self)
        self.controller = LoginController(self,self)
        
class Menu(QtWidgets.QMainWindow):
    trainers=pyqtSignal()
    reportar=pyqtSignal()
    
    def __init__(self):
        super().__init__()
        uic.loadUi("./views/menu.ui",self)
        self.controller = MenuController(self, self) 
        
class Trainer(QtWidgets.QMainWindow):
    back_menu=pyqtSignal()
    add_t=pyqtSignal()
    def __init__(self):
        super().__init__()
        uic.loadUi("./views/trainers.ui",self)
        self.controller = TrainerController(self, self) 
 
class Reports(QtWidgets.QMainWindow):
    back_menu=pyqtSignal()
    add_m=pyqtSignal()
    def __init__(self):
        super().__init__()
        uic.loadUi("./views/report.ui",self)
        self.controller = ReportController(self, self)              

class add_Member(QtWidgets.QMainWindow):
   
    def __init__(self):
        super().__init__()
        uic.loadUi("./views/addMembers.ui",self)
        self.controller = AddMemberController(self,self)
        
class add_Trainer(QtWidgets.QMainWindow):
    
    def __init__(self):
        super().__init__()
        uic.loadUi("./views/addTrainers.ui",self)
        self.controller = AddTrainerController(self,self)
                
class AppManager:
    def __init__(self):
        self.login_window=Login()
        self.menu_window=Menu()
        self.trainer_window=Trainer()
        self.report_window=Reports()
        self.addT_window=add_Trainer()
        self.addM_window=add_Member()
        self.login_window.login_succesfull.connect(self.show_main_window)

        self.menu_window.trainers.connect(self.show_trainer_window)
        self.menu_window.reportar.connect(self.show_report_window)
        
        self.trainer_window.back_menu.connect(self.back_trainer_window)
        self.report_window.back_menu.connect(self.back_report_window)
        
        self.report_window.add_m.connect(self.show_addM_window)
        self.trainer_window.add_t.connect(self.show_addT_window)
        
        self.login_window.show()
        
        
                
    def llenar_tablaT(self):
        self.conexion=Conexion()
        self.conexion.conectar()
        self.report_window.tableT.setRowCount(0) 
        
        resultados=self.conexion.seleccionar("SELECT * FROM trainers;")
        
        for fila_numero, fila_datos in enumerate(resultados):

            self.tableWidget.insertRow(fila_numero)

            for columna_numero, dato in enumerate(fila_datos):

                self.report_window.tableR.setItem(
                    fila_numero,
                    columna_numero,
                    QTableWidgetItem(str(dato))
                )
        
        
    def back_report_window(self):
        self.menu_window.show()
        self.report_window.close()
        
    def back_trainer_window(self):
        self.menu_window.show()
        self.trainer_window.close()    
    
    def show_trainer_window(self):
        self.trainer_window.show()
        self.menu_window.close()
        
    def show_report_window(self):
        self.report_window.show()
        self.menu_window.close()
            
    def show_main_window(self):
        self.menu_window.show()
        self.login_window.close()
        
    def show_addM_window(self):
        self.addM_window.show()
        
    def show_addT_window(self):
        self.addT_window.show()
            
        
app = QtWidgets.QApplication(sys.argv)
manager = AppManager()
sys.exit(app.exec())