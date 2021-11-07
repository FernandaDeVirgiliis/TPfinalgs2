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
    def actualizar(self):
        '''Ésta función sirve para actualizar a un empleado existente'''
        try:
            self.tree.item(self.tree.selection())['text']
        except IndexError: 
            messagebox.showwarning(message="Selecciona un empleado", title="Aviso")
            return
        
        nombreupdate = self.tree.item(self.tree.selection())['text']
        queryupdate='UPDATE empleados SET Legajo = ?, Nombre = ?, Puesto = ?, Sucursal = ?'
        self.run_query(queryupdate, (nombreupdate, ))
        messagebox.showinfo(message="Empleado actualizado", title="Actualizar")

        	
        self.get_empleados()
        
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
        
