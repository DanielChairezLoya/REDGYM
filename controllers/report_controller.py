from PyQt6 import QtWidgets, uic
from conexion import Conexion
from PyQt6.QtWidgets import QTableWidgetItem
class ReportController:
    def __init__(self, window, model):
        self.window = window
        self.model = model
        self.window.btn_back.clicked.connect(self.menu_back)
        self.window.btn_addm.clicked.connect(self.add_M)
        self.window.btn_refresh.clicked.connect(self.llenar_tablaR)
        self.window.btn_delete.clicked.connect(self.delete)
        self.window.btn_desactivar.clicked.connect(self.Desactivar)
        self.window.btn_activar.clicked.connect(self.Activar)
        
        self.llenar_tablaR()
    
            
    def menu_back(self):
        self.window.back_menu.emit()
        
    def add_M(self):
        self.window.add_m.emit()
        
    def llenar_tablaR(self):
        self.conexion=Conexion()
        self.conexion.conectar()
        self.window.tableR.setRowCount(0) 
        
        resultados=self.conexion.seleccionar("SELECT * FROM reports;")
        
        for fila_numero, fila_datos in enumerate(resultados):

            self.window.tableR.insertRow(fila_numero)

            for columna_numero, dato in enumerate(fila_datos):

                self.window.tableR.setItem(
                    fila_numero,
                    columna_numero,
                    QTableWidgetItem(str(dato))
                )
                
    def delete(self):
        
        fila = self.window.tableR.currentRow()

        
        # Obtener el id_member (columna 0)
        id_member = self.window.tableR.item(fila, 1).text()
        sql = (f"DELETE FROM reports WHERE id_member = {id_member}")
        self.conexion.borrar(sql)
        self.window.tableR.removeRow(fila)
        
    def Desactivar(self):
        fila=self.window.tableR.currentRow()
        
        id_member = self.window.tableR.item(fila, 1).text()
        sql = (f"UPDATE reports  SET status = FALSE WHERE id_member={id_member}")
        self.conexion.desactivar_activar(sql)
        
    def Activar(self):
        fila=self.window.tableR.currentRow()
        
        id_member = self.window.tableR.item(fila, 1).text()
        sql = (f"UPDATE reports  SET status = TRUE WHERE id_member={id_member}")
        self.conexion.desactivar_activar(sql)