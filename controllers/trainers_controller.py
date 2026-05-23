from PyQt6 import QtWidgets, uic
from conexion import Conexion
from PyQt6.QtWidgets import QTableWidgetItem

class TrainerController:
    def __init__(self, window, model):
        self.window = window
        self.model = model
        self.window.btn_back.clicked.connect(self.menu_back)
        self.window.btn_addT.clicked.connect(self.add_T)
        self.window.btn_refresh.clicked.connect(self.llenar_tablaT)
        self.window.btn_delete.clicked.connect(self.delete)
        self.llenar_tablaT()
        
    def menu_back(self):
        self.window.back_menu.emit()
        
    def add_T(self):
        self.window.add_t.emit()
        
    def llenar_tablaT(self):
        self.conexion=Conexion()
        self.conexion.conectar()
        self.window.tableT.setRowCount(0) 
        
        resultados=self.conexion.seleccionar("SELECT * FROM trainers;")
        
        for fila_numero, fila_datos in enumerate(resultados):

            self.window.tableT.insertRow(fila_numero)

            for columna_numero, dato in enumerate(fila_datos):

                self.window.tableT.setItem(
                    fila_numero,
                    columna_numero,
                    QTableWidgetItem(str(dato))
                )
    def delete(self):
        
        fila = self.window.tableT.currentRow()

        
        # Obtener el id_member (columna 0)
        id_member = self.window.tableT.item(fila, 0).text()
        sql = (f"DELETE FROM trainers WHERE id_trainer = {id_member}")
        self.conexion.borrar(sql)
        self.window.tableT.removeRow(fila)