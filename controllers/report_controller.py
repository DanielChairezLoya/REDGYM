from PyQt6 import QtWidgets, uic

class ReportController:
    def __init__(self, window, model):
        self.window = window
        self.model = model
        self.window.btn_back.clicked.connect(self.menu_back)
        
    def menu_back(self):
        self.window.back_menu.emit()