#Importaciones
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

import sqlite3
from repositorio_empleados import repositorio_empleados

class programa:

    #Defino el nombre de la base de datos
    base_nombre='bd.db'

    def __init__(self,window):
        '''Objeto constructor'''
        self.wind = window
        self.wind.geometry("850x300")
        self.wind.title("Programa CRUD")


        #Frames
        frame=LabelFrame(self.wind,text='Registro de empleados')
        frame.grid(row=0,column=0,columnspan=5,pady=30)

        Label(frame,text="Legajo: ").grid(row=2,column=0)
        self.legajo=Entry(frame)
        self.legajo.grid(row=2,column=1)

        Label(frame,text="Nombre y Apellido: ").grid(row=2,column=3)
        self.nombre=Entry(frame)
        self.nombre.grid(row=2,column=4)
        

        Label(frame,text="Puesto: ").grid(row=3,column=0)
        self.puesto=ttk.Combobox(frame,width=17)
        self.puesto.grid(row=3,column=1)
        opciones=["Operativo","Administrativo","Gerencial"]
        self.puesto['values']=opciones
        
        

        Label(frame,text="Sucursal: ").grid(row=3,column=3)
        self.sucursal=Entry(frame)
        self.sucursal.grid(row=3,column=4)

        

        #botones
        ttk.Button(frame,text="Registrar",command=self.registrar).grid(row=5,column=0)
        ttk.Button(frame,text="Modificar",command=self.actualizar).grid(row=5,column=3)
        ttk.Button(frame,text="Eliminar",command=self.eliminar).grid(row=5,column=6)
        

        #Creacion de tablas
        self.tree=ttk.Treeview(height=10, columns=('#1','#2','#3'))
        self.tree.place(x=0, y=250)
        self.tree.heading('#0', text="Legajo", anchor=CENTER)
        self.tree.heading('#1', text="Nombre", anchor=CENTER)
        self.tree.heading('#2', text="Puesto", anchor=CENTER)
        self.tree.heading('#3', text="Sucursal", anchor=CENTER)

        self.get_empleados()

    def get_seleccion(self):
        # Limpio la tabla antes de arrancar la query
        print (self.opcion.get())

    def run_query(self,query,parameters=()):
        '''Esta funcion realiza una conexión y consulta con la BBDD'''
        with sqlite3.connect(self.base_nombre) as conn:
                cursor=conn.cursor()
                result=cursor.execute(query,parameters)
                conn.commit()
        return result

    def get_empleados(self):
        # Limpio la tabla antes de arrancar la query
        elementos = self.tree.get_children()
        for element in elementos:
            self.tree.delete(element)
        
        #consulta de datos
        query = 'SELECT * FROM empleados'
        db_rows=self.run_query(query)
        # Insertar la consulta dentro de la tabla
        for row in db_rows:
            self.tree.insert('', 0, text = (row[0]), values = (row[1],row[2], row[3]))
                
    
if __name__ == '__main__':
    window = Tk()
    Aplicacion = programa(window)
    window.mainloop()
        
