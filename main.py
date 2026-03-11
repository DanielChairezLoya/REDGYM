from PyQt6 import QtWidgets, uic
import sys
#from controllers.login_controller import LoginController
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QPalette

class Login(QtWidgets.QMainWindow):
    #login_succesfull=pyqtSignal()
    
    def __init__(self):
        super().__init__()
        uic.loadUi("./views/login.ui",self)
        
        
        
class AppManager:
    def __init__(self):
        self.login_window=Login()
        
        self.login_window.show()
        
app = QtWidgets.QApplication(sys.argv)
manager = AppManager()
sys.exit(app.exec())