from PyQt6 import QtWidgets, uic

class TrainerController:
    def __init__(self, window, model):
        self.window = window
        self.model = model
        self.window.btn_back.clicked.connect(self.menu_back)
        self.window.btn_addT.clicked.connect(self.add_T)
        
    def menu_back(self):
        self.window.back_menu.emit()
        
    def add_T(self):
        self.window.add_t.emit()
        