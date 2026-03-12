from PyQt6 import QtWidgets, uic
import sys
from controllers.login_controller import LoginController
from controllers.menu_controller import MenuController
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QPalette

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
    def __init__(self):
        super().__init__()
        uic.loadUi("./views/trainers.ui",self)       
        
class AppManager:
    def __init__(self):
        self.login_window=Login()
        self.menu_window=Menu()
        self.trainer_window=Trainer()
        self.login_window.login_succesfull.connect(self.show_main_window)
        
        self.menu_window.trainers.connect(self.show_trainer_window)
        
        self.login_window.show()
    
    def show_trainer_window(self):
        self.trainer_window.show()
        self.menu_window.close()
            
    def show_main_window(self):
        self.menu_window.show()
        self.login_window.close()    
        
app = QtWidgets.QApplication(sys.argv)
manager = AppManager()
sys.exit(app.exec())