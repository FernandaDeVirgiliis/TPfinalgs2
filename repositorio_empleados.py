from empleado import Empleados
import sqlite3

class RepositorioEmpleados:

    def __init__(self):
        self.bd = sqlite3.connect("bd.db")
        self.cursor = self.bd.cursor()
    
    def registrar(self, Empleados):
        try:
            #Ejecuto la query	
            query = 'INSERT INTO empleados VALUES(?,?,?,?)'
            execute = self.cursor.execute(query,[Empleados.legajo,Empleados.nombre,Empleados.puesto,Empleados.sucursal])
            self.bd.commit()
            return 1
        except:
            self.bd.rollback()
            return 0

    #Funcion actualizar
    def actualizar(self, Empleados):
        '''Ésta función sirve para actualizar a un empleado existente'''
        try:
        #Ejecuto la query	
            query = 'UPDATE empleados SET Nombre = ?, Puesto = ?, Sucursal = ? WHERE Legajo = ?'
            execute = self.cursor.execute(query,[Empleados.nombre,Empleados.puesto,Empleados.sucursal,Empleados.legajo])
            self.bd.commit()
            return 1
        except:
            self.bd.rollback()
            return 0
        
    #Funcion eliminar
    def eliminar(self, Empleados):
        '''Ésta función sirve para eliminar a un empleado existente'''
        try:
            query = 'DELETE FROM empleados WHERE Legajo = ?'
            execute = self.cursor.execute(query,[Empleados.legajo])
            self.bd.commit()
            return 1
        except:
            self.bd.rollback()
            return 0
        
