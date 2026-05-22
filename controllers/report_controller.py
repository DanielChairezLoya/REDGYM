from PyQt6 import QtWidgets, uic

class ReportController:
    def __init__(self, window, model):
        self.window = window
        self.model = model
        self.window.btn_back.clicked.connect(self.menu_back)
        self.window.btn_addm.clicked.connect(self.add_M)
        
    #def llenar_tabla(self):
        #row_position= self.report_window.tableR.rowCount()
        #self.window.table.insertRow(row_position)
        
        #self.window.table.setItem(row_position, 0, QtWidgets.QTableWidgetItem('default.png'))
        #self.window.table.setItem(row_position, 1, QtWidgets.QTableWidgetItem())
        #self.window.table.setItem(row_position, 2, QtWidgets.QTableWidgetItem('default.png'))
        #self.window.table.setItem(row_position, 3, QtWidgets.QTableWidgetItem('default.png'))
        #self.window.table.setItem(row_position, 4, QtWidgets.QTableWidgetItem('default.png'))
        #self.window.table.setItem(row_position, 5, QtWidgets.QTableWidgetItem('default.png'))
        #self.window.table.setItem(row_position, 6, QtWidgets.QTableWidgetItem('default.png'))
        #self.window.table.setItem(row_position, 7, QtWidgets.QTableWidgetItem('default.png'))
        #self.window.table.setItem(row_position, 8, QtWidgets.QTableWidgetItem('default.png'))
        #self.window.table.setItem(row_position, 9, QtWidgets.QTableWidgetItem('default.png'))
        #self.window.table.setItem(row_position, 10, QtWidgets.QTableWidgetItem('default.png'))
            
    def menu_back(self):
        self.window.back_menu.emit()
        
    def add_M(self):
        self.window.add_m.emit()