from PyQt6 import QtWidgets, uic

class ReportController:
    def __init__(self, window, model):
        self.window = window
        self.model = model
        self.window.btn_back.clicked.connect(self.menu_back)
        self.window.btn_addm.clicked.connect(self.add_M)
            
    def menu_back(self):
        self.window.back_menu.emit()
        
    def add_M(self):
        self.window.add_m.emit()