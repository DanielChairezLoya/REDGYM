from PyQt6 import QtWidgets, uic

class MenuController:
    def __init__(self, window, model):
        self.window = window
        self.model = model
        self.window.btn_coach.clicked.connect(self.menu_actionT)
        self.window.btn_reporte.clicked.connect(self.menu_actionR)
        
    def menu_actionT(self):
        self.window.trainers.emit()
        
    def menu_actionR(self):
        self.window.reportar.emit()